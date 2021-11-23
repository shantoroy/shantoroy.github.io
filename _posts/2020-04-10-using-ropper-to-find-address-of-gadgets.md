---
layout: single
title: "Using Ropper to find ROP Gadgets"
header:
  image: "https://live.staticflickr.com/65535/49852909896_7baa2438ae_z.jpg"
  teaser: "https://live.staticflickr.com/65535/49852909896_7baa2438ae_z.jpg"
categories:
  - Security
tags:
  - Exploitation
  - Tutorial
  - ARM
  - Buffer Overflow
  - Shellcode
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

To exploit using `ret-to-libc` or `ROP`, we need approprate gadgets and their addresses. In this post, we will learn how to use it to extract these gadget information.

## Install Prerequisites
Let's first install the Ropper by installing particular frameworks using following commands:

```bash
pi@raspberrypi:~$ sudo pip install capstone
pi@raspberrypi:~$ sudo pip install filebytes
pi@raspberrypi:~$ sudo pip install keystone-engine
```

## Install Ropper
Now, let's install Ropper:
```bash
pi@raspberrypi:~$ git clone https://github.com/sashs/Ropper.git
pi@raspberrypi:~$ cd Ropper
pi@raspberrypi:~$ python setup.py install
pi@raspberrypi:~$ ropper
```

We can also use the `Ropper.py` file directly. 

## Usage and Examples
### Usage
Here is the usage of `Ropper` from the official repository.
```
usage: Ropper.py [-h] [-v] [--console] [-f <file>] [-r] [-a <arch>]
                 [--section <section>] [--string [<string>]] [--hex]
                 [--asm <asm> [H|S|R] [<asm> [H|S|R] ...]] [--disasm <opcode>]
                 [--disassemble-address <address:length>] [-i] [-e]
                 [--imagebase] [-c] [-s] [-S] [--imports] [--symbols]
                 [--set <option>] [--unset <option>] [-I <imagebase>] [-p]
                 [-j <reg>] [--stack-pivot] [--inst-count <n bytes>]
                 [--search <regex>] [--quality <quality>] [--opcode <opcode>]
                 [--instructions <instructions>] [--type <type>] [--detailed]
                 [--all] [--cfg-only] [--chain <generator>] [-b <badbytes>]
                 [--nocolor] [--clear-cache]
```

### `<search>` Examples
Suppose, we are looking for a gadget **`pop {r0, r4, pc}`** that is within the **`libc.so.6`**. Now, let's find the gadget address using the following command:
```bash
pi@raspberrypi:~$ ./Ropper.py --file /lib/arm-linux-gnueabihf/libc.so.6 --search "pop {r0, r4, pc}"

    [INFO] Load gadgets for section: LOAD
    [LOAD] loading... 100%
    [LOAD] removing double gadgets... 100%
    [INFO] Searching for gadgets: pop {r0, r4, pc}
    
    [INFO] File: /lib/arm-linux-gnueabihf/libc.so.6
    0x000791fc: pop {r0, r4, pc};
```
So, we find the offset address of the gadget that is $0x000791fc$.

Here's another example useing `ropper` command if installed...
```bash
pi@raspberrypi:~$ ropper --file /lib/arm-linux-gnueabihf/libc.so.6 --search "pop {r4, pc}"
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: pop {r4, pc}

[INFO] File: /lib/arm-linux-gnueabihf/libc.so.6
0x00018164: pop {r4, pc}; 
0x000c4308: pop {r4, pc}; cmp r1, #2; strls r1, [r0, #0x10c]; movls r0, #0; movhi r0, #0x16; bx lr; 
0x0010d30c: pop {r4, pc}; cmp r2, #0; bne #0x10d320; mov r0, #1; bx lr; 
0x00114a90: pop {r4, pc}; ldr r3, [pc, #0x24]; add r3, pc, r3; ldr r3, [r3]; ldr r3, [r3]; blx r3; 
0x00114b5c: pop {r4, pc}; ldr r3, [pc, #0x28]; add r3, pc, r3; ldr r3, [r3]; ldr r3, [r3, #4]; blx r3; 
0x000c42d0: pop {r4, pc}; ldr r3, [r0, #0x10c]; mov r0, #0; str r3, [r1]; bx lr; 
0x000c3a80: pop {r4, pc}; ldrsh r3, [r0]; mov r0, #0; strh r3, [r1]; bx lr; 
0x000c3a40: pop {r4, pc}; mov r0, #0; bx lr; 
0x00114798: pop {r4, pc}; mov r0, #0; pop {r4, pc}; mov r0, #0; bx lr; 
0x000d16b4: pop {r4, pc}; mov r0, #1; bx lr; 
0x0008065c: pop {r4, pc}; mov r0, ip; bx lr; 
0x00077960: pop {r4, pc}; mov r0, r1; bx lr; 
0x00073904: pop {r4, pc}; mov r1, lr; bx r3; 
0x000f4d00: pop {r4, pc}; mvn r0, #0; bx lr; 
0x000f57f8: pop {r4, pc}; mvn r0, #0; pop {r4, pc}; mvn r0, #0; bx lr;
```

Here, we find all patterns that contain **`pop {r4, pc}`**. 

**Note:** if you do not use space as shown, it will return nothing. Also, these should be in small case letters.

We can also search for instructions within system commands-
```bash
pi@raspberrypi:~$ ropper --file /bin/ls --search "pop {r4, pc}"
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: pop {r4, pc}

[INFO] File: /bin/ls
0x00013c14: pop {r4, pc}; 
0x00024210: pop {r4, pc}; mov r0, r3; bx lr; 
0x0001b728: pop {r4, pc}; sub r0, r1, r0; clz r0, r0; lsr r0, r0, #5; bx lr;
```

or, you can search for all instructions that uses `pop`
```bash
pi@raspberrypi:~/exploitation/mprotect $ ropper --file /bin/ls --search "pop"
[INFO] Load gadgets for section: LOAD
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: pop

[INFO] File: /bin/ls
0x0001b1f8: pop {pc}; mov r0, r3; bx lr; 
0x00024d18: pop {r1, pc}; 
0x000245ec: pop {r1, r2, lr}; mul r3, r2, r0; sub r1, r1, r3; bx lr; 
0x00024c4c: pop {r2, r3}; bx lr; 
0x00024d04: pop {r2, r3}; bx lr; push {r1, lr}; mov r0, #8; bl #0x18b4; pop {r1, pc}; 
0x00024c9c: pop {r2, r3}; rsbs r0, r0, #0; sbc r1, r1, r1, lsl #1; bx lr; 
0x00024c70: pop {r2, r3}; rsbs r0, r0, #0; sbc r1, r1, r1, lsl #1; rsbs r2, r2, #0; sbc r3, r3, r3, lsl #1; bx lr; 
0x00024cc0: pop {r2, r3}; rsbs r2, r2, #0; sbc r3, r3, r3, lsl #1; bx lr; 
0x00011884: pop {r3, pc}; 
0x00013c14: pop {r4, pc}; 
0x00024210: pop {r4, pc}; mov r0, r3; bx lr; 
0x0001b728: pop {r4, pc}; sub r0, r1, r0; clz r0, r0; lsr r0, r0, #5; bx lr; 
0x0001b628: pop {r4, r5, pc}; 
0x00022128: pop {r4, r5, r6, lr}; add sp, sp, #4; bx lr; 
0x00019694: pop {r4, r5, r6, lr}; b #0x4878; mvn r0, #0; bx lr; 
0x000145bc: pop {r4, r5, r6, pc}; 
0x000239d8: pop {r4, r5, r6, pc}; ldr r3, [pc, #8]; ldr r3, [r3]; blx r3; 
0x0001a4f0: pop {r4, r5, r6, pc}; mov r0, #0; bx lr; 
0x00016a7c: pop {r4, r5, r6, r7, pc}; 
0x0001de98: pop {r4, r5, r6, r7, r8, sb, sl, fp, pc}; ldrd r6, r7, [r0]; mov r0, r6; mov r1, r7; blx r3; 
0x00024edc: pop {r4, r5, r6, r7, r8, sb, sl, pc}; andeq r5, r1, ip, asr r0; andeq r5, r1, r4, asr r0; bx lr; 
0x0001ba98: pop {r4, r5, r6, r7, r8, sb, sl, pc}; ldr r0, [r0, #8]; bx lr; 
0x0001bf00: pop {r4, r5, r6, r7, r8, sb, sl, pc}; mov r4, r8; b #0xbf10; ldr r0, [r4]; mov r1, r7; blx r6; 
0x000170a0: pop {r4, r5}; b #0x18d8; mov r0, #1; bx lr; 
0x00016ffc: pop {r4, r5}; b #0x4878; mov r0, #1; bx lr; 
0x00013c70: pop {r4, r5}; bx lr; 
0x00016f54: pop {r4, r5}; ldr r0, [ip]; b #0x18d8; mov r0, #1; bx lr; 
0x00017144: pop {r4, r5}; ldr r0, [ip]; b #0x4878; mov r0, #1; bx lr; 
0x00022254: popeq {r4, pc}; bl #0x12408; bl #0x1938; mov r0, #0; pop {r4, pc}; 
0x0001ac5c: popeq {r4, r5, r6, pc}; ldrb r1, [r3], #-1; cmp r1, #0x2f; beq #0xac54; pop {r4, r5, r6, pc}; 
0x00024ab0: poplo {r4, r5, pc}; and r5, r1, #0x80000000; orr r1, r5, #0x7f000000; orr r1, r1, #0xf00000; mov r0, #0; pop {r4, r5, pc}; 
0x00013c04: popne {r4, pc}; bl #0x3b90; mov r3, #1; strb r3, [r4]; pop {r4, pc}; 
0x0001be08: popne {r4, r5, r6, pc}; add r2, r2, #8; cmp r3, r2; bhi #0xbe00; mov r0, #0; pop {r4, r5, r6, pc};
```



## References:
1. [https://github.com/sashs/Ropper](https://github.com/sashs/Ropper)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg3NjU3OTkxOCwtMjk0MzgzMCwyNTgyMz
QzODFdfQ==
-->