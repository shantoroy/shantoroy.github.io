---
layout: single
title: "Symmetric and Asymmetric Key Cryptography Concept in Python"
header:
  image: "https://live.staticflickr.com/65535/52703382288_65d2aced51_o.png"
  teaser: "https://live.staticflickr.com/65535/52703382288_65d2aced51_o.png"
categories:
  - Security
tags:
  - Python
  - Tutorial
  - symmetric-key-crypto
  - asymmetric-key-crypto
  - public-key-crypto
  - AES
  - RSA
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


Cryptography provides privacy and security of data. It involves the use of mathematical algorithms to encrypt and decrypt data. The process is also called ciphering and deciphering.

In this blog post, we will differentiate symmetric and asymmetric key cryptography and provide one example for each in Python.

## Cryptography
Today, cryptography is used in a wide range of applications, including secure communication over the internet, data confidentiality, digital signature, secure computation.

Cryptography has been used since ancient times, with early examples including the use of substitution ciphers in ancient Egypt and the Caesar cipher used by the Roman Empire. 

The field of cryptography is constantly evolving, with new cryptographic algorithms and protocols being developed. However, there are a few popular ones being used now-a-days with increasing size of key as computation power increases day by day.

## Symmetric Key Cryptography
In symmetric key cryptography, the same key is used for both encryption and decryption. 

This means that both the sender and receiver have the same key. The key is either shared earlier between two parties or the sender can send the the key along with the message payload if encrypted with new keys for each new communication. 

The main advantage of symmetric key cryptography is its speed. It is much faster than asymmetric key cryptography because the algorithms used for encryption and decryption are relatively simple.

In this blog post, we will see the implementation of a widely used symmetric key cryptography algorithms named the Advanced Encryption Standard (AES). In Python, the `pycryptodome` library can be used to implement AES encryption and decryption.

### importing modules
```py
from Cryptodome.Cipher import AES
# from Crypto.Cipher import AES         # does not work
from Crypto.Random import get_random_bytes
```
Note that, in many example, you will find the second one `Crypto.Cipher` being used. However, it does not work for the `EAX` mode. So, you might want to import AES from `Cryptodome.Cipher`.

### Code

```py
# class for symmetric key crypto (AES)
class symmetricKeyCrypto:
    def encryption(self, plaintext, key):
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(plaintext)
        iv = cipher.nonce
        return (ciphertext, iv, tag)
    
    def decryption(self, ciphertext, key, iv, tag):
        cipher = AES.new(key, AES.MODE_EAX, nonce=iv)
        decrypted = cipher.decrypt_and_verify(ciphertext, tag)
        return decrypted
```

In this example, `AES.MODE_EAX` mode is used for encryption and decryption. Then the `encrypt_and_digest` method is used to encrypt the plaintext and generate a tag. 

We use the `nonce` attribute to get the IV, which we return along with the ciphertext and the tag. During decryption, `decrypt_and_verify` method is used to decrypt the ciphertext and verify the tag. Then the IV and the tag along with the key to the `AES.new` method are passed.

if you are perplexed by the terms, here's a mini description for each:

-   AES.MODE_EAX: A mode of operation for symmetric-key encryption that provides confidentiality, integrity, and authenticity of messages. There are other modes including ECB, CBC, CTR, OFB, etc. 
-   Nonce: A random number used only once in cryptographic communication. It helps to protect against replay attacks and ensures freshness of the data.
-   IV: Initialization Vector, a random value used in symmetric-key cryptography to ensure that the same plaintext message encrypts to a different ciphertext each time it is encrypted, adding randomness to the encryption process.

### Example Use Case
```py
if __name__ == "__main__":
    # Example usage of symmetric key cryptography
    key = get_random_bytes(16)
    plaintext = b'Hello World!'
    symm_crypto = symmetricKeyCrypto()

    ciphertext, iv, tag = symm_crypto.encryption(plaintext, key)
    decrypted = symm_crypto.decryption(ciphertext, key, iv, tag)

    print(f"\nSymmetric key encryption:\n")
    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted: {decrypted}")
```

Run the code and you will see the following output:
```
Symmetric key encryption:

Plaintext: b'Hello World!'
Ciphertext: b'\x84\n\x0fE\xb2\xb9\x04\xf1\x07\xc7N\x1a'
Decrypted: b'Hello World!'
```


## Asymmetric Key Cryptography
In asymmetric key cryptography, two different keys are used for encryption and decryption. The key used for encryption is called the public key, and the key used for decryption is called the private key. 

This is why it is called public-key cryptography as well. Many times you may have heard the later one.

The public key can be shared with anyone, but the private key must be kept secret. Asymmetric key cryptography is comparatively more expensive and consumes significantly more computational power than symmetric key cryptography. However, it provides better security in exchange for the cost.

One of the most commonly used asymmetric key cryptography algorithms is the RSA algorithm. In Python, the `cryptography` library can be used to generate RSA key pairs and encrypt/decrypt messages.

### import modules
```py
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
```

### Code
```py
# class for asymmetric key crypto (RSA)
class asymmetricKeyCrypto:
    def encryption(self, plaintext, public_key):
        ciphertext = public_key.encrypt(
            plaintext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext

    def decryption(self, ciphertext, private_key):
        decrypted = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted
```

Here, the `asymmetricKeyCrypto` class implements the RSA encryption and decryption algorithm using the `cryptography` library. 

The `encryption` method takes plaintext and the recipient's public key as input and returns the ciphertext. The `decryption` method takes the ciphertext and the recipient's private key as input and returns the original plaintext message.

### Example Use Case

```py
if __name__ == "__main__":
    # Example usage of asymmetric key cryptography
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    plaintext = b'Hello World!'
    asymm_crypto = asymmetricKeyCrypto()

    ciphertext = asymm_crypto.encryption(plaintext, public_key)
    decrypted = asymm_crypto.decryption(ciphertext, private_key)

    print(f"\nAsymmetric key encryption:\n")
    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted: {decrypted}")
```

Running the program will generate the following output:

```
Asymmetric key encryption:

Plaintext: b'Hello World!'
Ciphertext: b'I\xa5Ru\xedYE<\x9dK\xb0tf\x8a\xf3\xa7\xbb\xe0\t\xdf\xa6;\x80\xe4\x0bb\x92\xd5\xb8\xbd^\xec+\xd16\x94\x02A=\x82\xfc\xb6f`\x90s\xb8[\xd4h\xe5J\xab\x9a;I\xa2>c\xdcrE\xfbMY\xf4.E\x18K\x14"r\x94\xe3E\xfb\xcf\xdaZ\xfc\'\xb1\xcc\xb8P\xea\xa7A\xfddb\x1fA\x81\xcb?\xce\x9d\xac\xc9\x00\x89\x84\x8f\\\x03\xd8"\xf4\xa2b\xa9\xb6\x8e\xdc\n~Nbn\xda\x11\xf9\xbe\xfe-nu@\xa0\xd4(\xdf%AA@\xec}\xa4,\x94:e\xbf\\o\x1b\x93!\x97\xdch\xfb\x0bM>\x0f\xeaU\xa5u\xcb\xa8\x8d\xbe\x10i@B\x97W\x1f\x8b\x05\x10.\xb8\x1f*\x96\xda\xd5\xcc\xfe0-\t\xf2\x7f\x85\xbd \x1b\xdd\x07r]57\x05z\xe4\xebF\x08\x91>\xc4_\xf6\';\xe6}\xafv0\xdb\x96(\xe5HWH\x1f\xdb\xda\xc4k\x88\x13\xda\xe8\xab@m\xb1\x81\xc2\x8d\xcc(\xb8\xb3H86b\x1f\xc2\xa0!\xfe\x10'
Decrypted: b'Hello World!'
```


## Full Code
```py
from Cryptodome.Cipher import AES
# from Crypto.Cipher import AES         # does not work
from Crypto.Random import get_random_bytes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


# class for symmetric key crypto (AES)
class symmetricKeyCrypto:
    def encryption(self, plaintext, key):
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(plaintext)
        iv = cipher.nonce
        return (ciphertext, iv, tag)
    
    def decryption(self, ciphertext, key, iv, tag):
        cipher = AES.new(key, AES.MODE_EAX, nonce=iv)
        decrypted = cipher.decrypt_and_verify(ciphertext, tag)
        return decrypted


# class for asymmetric key crypto (RSA)
class asymmetricKeyCrypto:
    def encryption(self, plaintext, public_key):
        ciphertext = public_key.encrypt(
            plaintext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext

    def decryption(self, ciphertext, private_key):
        decrypted = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted

if __name__ == "__main__":
    # Example usage of symmetric key cryptography
    key = get_random_bytes(16)
    plaintext = b'Hello World!'
    symm_crypto = symmetricKeyCrypto()

    ciphertext, iv, tag = symm_crypto.encryption(plaintext, key)
    decrypted = symm_crypto.decryption(ciphertext, key, iv, tag)

    print(f"\nSymmetric key encryption:\n")
    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted: {decrypted}")
    

    # Example usage of asymmetric key cryptography
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    plaintext = b'Hello World!'
    asymm_crypto = asymmetricKeyCrypto()

    ciphertext = asymm_crypto.encryption(plaintext, public_key)
    decrypted = asymm_crypto.decryption(ciphertext, private_key)

    print(f"\nAsymmetric key encryption:\n")
    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted: {decrypted}")
```

That's all for today! Cheers!!! :sunglasses:

The code is available in [this Github repo](https://github.com/shantoroy/intro-2-cybersecurity-in-python). Feel free to give a star if you like it.

You can also read related blog posts:
1. [Password Cracking through Dictionary Attack in Python](https://shantoroy.com/security/password-cracking-through-dictionary-attack-in-python/) 
2. [A Basic Keylogger in Python](https://shantoroy.com/security/a-simple-keylogger-in-python/)
3. [Write a Simple Virus in Python](https://shantoroy.com/security/write-a-virus-in-python/)
4. [Write a Worm (Malware) in Python](https://shantoroy.com/security/write-a-worm-malware-in-python/)
5. [Write a Backdoor in Python](https://shantoroy.com/security/simple-backdoor-using-python/)
6. [I Exploited the Moral of ChatGPT by giving slightly Different Instructions to write Ransomware!](https://medium.com/@shantoroy/i-exploited-the-moral-of-chatgpt-by-giving-slightly-different-instructions-to-write-ransomware-c0bb9cad0a55)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTc0NTEyMTgyN119
-->