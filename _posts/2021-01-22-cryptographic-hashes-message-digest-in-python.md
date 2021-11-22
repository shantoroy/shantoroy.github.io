---
layout: single
title: "Cryptographic Hashes and Message Digest in Python"
header:
  image: "https://live.staticflickr.com/65535/51697235355_8a0b24e338_o.png"
  teaser: "https://live.staticflickr.com/65535/51697235355_8a0b24e338_o.png"
categories:
  - Python
tags:
  - Python
  - Tutorial
  - hashlib
  - pycrypto
  - crypto
  - md5
  - sha256
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---



A hash function is a one-way function that takes a string as a input and creates a fixed-length output (hash value of the corresponding input). Because it is a one-way function, it is very difficult to guess the original input.

This is why the passwords stored in a computer are hashed before storing so that even if a hacker gets access to the password database, he cannot guess the original password. In practice, we actually add a `salt` to the password to make it more difficult to bruteforce. 

Here, in this post, we will find out how to generate the hash of a text using two popular python modules: `hashlib` and `Crypto`.

There are several hashing algorithms:
1. MD5
2. SHA1
3. SHA256
4. SHA512
5. HMAC

and some other variants of different output lengths. 

## Using `hashlib` module
We can use `hashlib` module in two ways to create object of a particular algorithm class.

The first way is pretty straightforward. Creating object by calling the algorithm class like this
```python
obj1 = hashlib.md5()
obj2 = hashlib.sha256()
```

then we update data using the `update()` method

```python
obj1.update("hello".encode())
```
or directly using the byte type data
```python
obj1.update(b"hello")
```

finally we can generate the digest using the `digest()` or `hexdigest()` methods.

Here is an elaborated example that contains generated hash digests using different algorithms.
```python
import hashlib

data = "This is a test"

hash_obj1 = hashlib.md5()
hash_obj1.update(data.encode())
print(f"Md5 Hash: {hash_obj1.hexdigest()}")

hash_obj2 = hashlib.sha1()
hash_obj2.update(data.encode())
print(f"SHA1 Hash: {hash_obj2.hexdigest()}")

hash_obj3 = hashlib.sha256()
hash_obj3.update(data.encode())
print(f"SHA256 Hash: {hash_obj3.hexdigest()}")

hash_obj4 = hashlib.sha512()
hash_obj4.update(data.encode())
print(f"SHA512 Hash: {hash_obj4.hexdigest()}")
```
Now, we can see the following output if run the program.
```
Md5 Hash: ce114e4501d2f4e2dcea3e17b546f339
SHA1 Hash: a54d88e06612d820bc3be72877c74f257b561b19
SHA256 Hash: c7be1ed902fb8dd4d48997c6452f5d7e509fbcdbe2808b16bcf4edce4c07d14e
SHA512 Hash: a028d4f74b602ba45eb0a93c9a4677240dcf281a1a9322f183bd32f0bed82ec72de9c3957b2f4c9a1ccf7ed14f85d73498df38017e703d47ebb9f0b3bf116f69
```

Another way to create object is using the `new()` method and passing the algorithm name as an argument.
```python
obj1 = hashlib.new("md5")
obj2 = hashlib.new("sha256")
```

The elaborated example and output are as follows:
```python
import hashlib

data = "This is a test"

hash_obj1 = hashlib.new("md5")
hash_obj1.update(data.encode())
print(f"Md5 Hash: {hash_obj1.hexdigest()}")

hash_obj2 = hashlib.new("sha1")
hash_obj2.update(data.encode())
print(f"SHA1 Hash: {hash_obj2.hexdigest()}")

hash_obj3 = hashlib.new("sha256")
hash_obj3.update(data.encode())
print(f"SHA256 Hash: {hash_obj3.hexdigest()}")

hash_obj4 = hashlib.new("sha512")
hash_obj4.update(data.encode())
print(f"SHA512 Hash: {hash_obj4.hexdigest()}")
```

We can make the whole code shorter by creating a function

```python
import hashlib

def hashing(hash_type, data):
    hash_obj = hashlib.new(hash_type)
    hash_obj.update(data.encode())
    print(f"{hash_type} Hash: {hash_obj.hexdigest()}")

if __name__=="__main__":
    data = "This is a test"
    hash_types = ["md5", "sha1", "sha256", "sha512"]
    _ = [hashing(hash_type,data) for hash_type in hash_types]
```

If we run the program, we will find out the same outputs we have seen earlier.


## Using `pycrypto` module
Another way to perform the same job is using the `pycrypto` module.

We can import all the necessary algorithm classes from `Crypto.Hash`.

An elaborated example is shown here:

```python
from Crypto.Hash import HMAC, MD5, SHA as SHA1, SHA256

data = "This is a test"

hash_obj1 = MD5.new()
hash_obj1.update(data.encode())
print(f"Md5 Hash: {hash_obj1.hexdigest()}")

secret = "hello"
hash_obj2 = HMAC.new(secret.encode())
hash_obj2.update(data.encode())
print(f"HMAC Hash: {hash_obj2.hexdigest()}")

hash_obj3 = SHA1.new()
hash_obj3.update(data.encode())
print(f"SHA1 Hash: {hash_obj3.hexdigest()}")

hash_obj4 = SHA256.new()
hash_obj4.update(data.encode())
print(f"SHA256 Hash: {hash_obj4.hexdigest()}")
```
And the output is exactly the same.
```
Md5 Hash: ce114e4501d2f4e2dcea3e17b546f339
HMAC Hash: 842dbe36d5adb49ae838f7d146496852
SHA1 Hash: a54d88e06612d820bc3be72877c74f257b561b19
SHA256 Hash: c7be1ed902fb8dd4d48997c6452f5d7e509fbcdbe2808b16bcf4edce4c07d14e
```

In this post, we learnt a few basic examples of performing hash operations in python. Hope, that helps.

Until another post, cheers!!! :sunglasses:

## References

1. [hashlib - Secure hashes and message digests](https://docs.python.org/3/library/hashlib.html)
2. [`Crypto.Hash` package](https://pycryptodome.readthedocs.io/en/latest/src/hash/hash.html)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk5MDcxODcwXX0=
-->