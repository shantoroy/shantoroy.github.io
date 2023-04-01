---
layout: single
title: "Basic Cryptographic Operations (Encryption and Decryption) in Python"
excerpt:  
seo_title:  Your  meta  title  
seo_description:  Your  meta  description
header:
  image: "https://live.staticflickr.com/65535/51697584980_255eb49bb7_o.png"
  teaser: "https://live.staticflickr.com/65535/51697584980_255eb49bb7_o.png"
categories:
  - Python
tags:
  - Python
  - Tutorial
  - hashlib
  - pycrypto
  - crypto
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

In this post we will take a look at the basic operations on cryptography (encryption and decryption) in python. We have an excellent module `pycrypto` that offers different built-in symmetric and asymmetric key cryptosystems.

Symmetric key cryptosystems use the same key to encrypt and decrypt a data or file. For example, DES and AES. Now-a-days, AES is the most common symmetric key cryptosystem. 

Asymmetric key cryptosystems use two different mathematically related keys: one to encrypt and another to decrypt. For example, RSA and ECC.

Let's first install the module:
```bash
pip install pycrypto
```

## Symmetric Cryptography
### DES
In the following examples, we will encrypt and decrypt our data using DES.
```python
from Crypto.Cipher import DES

des = DES.new('eightchr', DES.MODE_ECB)
data = 'eightltr'
cipher_text = des.encrypt(data)
print(f"Encrypted Text: {cipher_text}")
print(f"Decrypted Text: {des.decrypt(cipher_text)}")
```
Here's our output after running the program:
```
Encrypted Text: b'<e\x1d\xf2\xb2a\xa9a'
Decrypted Text: b'eightltr'
```

In the CFB mode, the object keeps changing each step. That's why we will use seperate object to manage the key. 
```python
from Crypto.Cipher import DES
from Crypto import Random

iv = Random.get_random_bytes(8)
des_obj_1 = DES.new('eightchr', DES.MODE_CFB, iv)
des_obj_2 = DES.new('eightchr', DES.MODE_CFB, iv)
data = 'sixteencharacter'      # multiple of eight
cipher_text = des_obj_1.encrypt(data)
print(f"Encrypted Text: {cipher_text}")
print(f"Decrypted Text: {des_obj_2.decrypt(cipher_text)}")
```
Here is the program output:
```
Encrypted Text: b'\x92\x9ckk9{3\x0b3\xc8\xef\xb1_\xb0\xd0v'
Decrypted Text: b'sixteencharacter'
```

### AES
The following example offers encryption and decryption in python.
```python
from os import urandom
from Crypto.Cipher import AES

def AES_encrypt(secret,iv,mode,data):
    enc = AES.new(secret, mode, iv)
    return data, enc.encrypt(data)

def AES_decrypt(secret,iv,mode,data):
    dec = AES.new(secret, mode, iv)
    return dec.decrypt(data).decode('utf-8')

if __name__=="__main__":
    secret = urandom(16)
    iv = urandom(16)
    mode = AES.MODE_CBC
    
    msg, encrypted_msg = AES_encrypt(secret, iv, mode, "this is a crypto")
    print(encrypted_msg)
    print(AES_decrypt(secret, iv, mode, encrypted_msg))
```

## Asymmetric Cryptography
Let's create public-private key pair using RSA. Then we will encrypt the data using the public key. And then we will use the private key to decrypt the ciphertext (encrypted data).
```python
import Crypto.Random
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
import binascii

random = Crypto.Random.new().read
private_key = RSA.generate(1024, random)
public_key = private_key.publickey()

print("Private and Public Keys")
print(binascii.hexlify(private_key.exportKey(format='DER')).decode("ascii"))
print(binascii.hexlify(public_key.exportKey(format='DER')).decode("ascii"))

print("\n")
data = "this is a test"
cipher_text = public_key.encrypt(data.encode(), 32)
print(f"Encrypted Text: {cipher_text}")
print(f"Decrypted Text: {private_key.decrypt(cipher_text)}")
```

```
Private and Public Keys
3082025c02010002818100d622ee0ed403dda6a91f48426a80d16f76377c8fb1347f2e39a57d340fc807125a2c92eb6d22e4ef954a7c20f1d0ddcf9eb08d802e8324c71fbb46f683a3159aa87ebf8c1ca97f7824d7b5a8014541071f5a8c3b5ab3b4c3222be18ffdd1a5ecca9aa3114dc3a667e51f1588a486427a1625da4000b1d5d9a7d1181640b11b7b02030100010281805ac31f68059145e798137c4b3a5d33682d1143a89c11863e8f8c874f03c962c5f296a6074790dcbc77e8c4482a76bf2d7b3396265890998c14f50a14fea2a74ac94171dd4dd0062e107d140be363b9e2ba2c8db257c707f6b484b88f50d07ebf36fc0e115fe713a51131f0d9fc1ab2f2da73e6914e594ef4ae8bf538880570e1024100d8b65fc47166f312fe32555a33b8583dcba164f9905c2c97b472a719a324af8d16f594c47dd2211aac02ccff2220665d88101f2b7690397fccc7c6bd5a303a93024100fcf50179c7695db02025bfc5a233c7916c35171ef0cbe9bb5bc6b5e66cf636f17b52e0808cfeaab2d484c131574c444629462dc0898472e121ae06e5816c647902406604d4e8a18a197c2376867fc441502927277f658cf4177a0354c61d6793e9a0bde2367a99d0c60ccc5535341658b257eda9c942a8ba1497794bc2df7909a3490240296f3c89a5176648464bc8a8e7d3d179c99ebca5cdcda9008e9cf308c68a621f9612d2415c570ec0f23cb8a48b672bbbce60f777954f03be4ad505be2c400409024100d32b4ba44cd09ce69f101d8bab9bec67c60fff3c911b23b22f21a8ad8a969a31c8f643dda929b95cf40e3eb3b16dd1d06e3edcfe6b542cccfd034fbb9664bf5e
30819f300d06092a864886f70d010101050003818d0030818902818100d622ee0ed403dda6a91f48426a80d16f76377c8fb1347f2e39a57d340fc807125a2c92eb6d22e4ef954a7c20f1d0ddcf9eb08d802e8324c71fbb46f683a3159aa87ebf8c1ca97f7824d7b5a8014541071f5a8c3b5ab3b4c3222be18ffdd1a5ecca9aa3114dc3a667e51f1588a486427a1625da4000b1d5d9a7d1181640b11b7b0203010001

Encrypted Text: (b'\x97y\xdb\xd1\x16\x8b\xa7\xe4\xa4\xd7W\x11\x88.\xac\xa8\xa7j\xc3.y:\xde|\xd2\xcd\xafw;\x18\xe3\xbe\xe7\xf5\xed\n\xa1t\xd8\xfbVZ\x98\x18!F/\xec\xf3\t\xbdy\x1c\x06-\xe0 pN\xa7\x0e\xe8\xed\x18\xd3\x02\xc4\xa8&@\x04\x82\x050d\xa8\xb4V,\x12\x1b\xa0)\x1a\xaa\x1b\xfe6\x8fw\x1d=\xe5\xdd{L\xb0\x8c\xd7\x97\xa8\xc2M\x89s8S-\xe7\xc7<\xbb%\xd7\x05PH\xaf\xc5\x82\xc4\x06\x01\x1a\x180V\xf6',)
Decrypted Text: b'this is a test'
```


## References
1. [Python and cryptography with pycrypto](https://www.laurentluce.com/posts/python-and-cryptography-with-pycrypto/)
2. [Pycrypto Example: Encryption And Decryption In Python](https://appdividend.com/2020/06/16/pycrypto-example-encryption-and-decryption-in-python/)
3. [Python Encryption and Decryption with PyCryptodome](https://nitratine.net/blog/post/python-encryption-and-decryption-with-pycryptodome/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2NTQ1MjQzMTUsNTYwNTAyMDY2XX0=
-->