# HashCollisionProject
This repository includes a Python script created in CISC 410 (Advanced Security) as part of an assignment. 

The purpose of this program is to demonstrate a hash collision attack on a message. This is done by creating two messages, the original "good" message, and an altered "bad" message. Then these messages continue to be slightly altered and hashed until a collision occurs. This shows illustrates how a message can be altered but maintain the same signature which in turn sends the wrong message to the recipient. 

## Files Included
1. attack.py - This file contains the code that creates the different messages, hashes them, and tests for collision.
2. evil.txt - This file contains the version of the evil message that collides with an altered version of the original message.
3. harmless.txt - This file contains the version of the original message that collides with an altered version of the evil message.
   
## Installation
This program is to be ran on a virtual machine that has Python3 installed. 
Once these files are in a directory, this command can be run to execute the program:
```Python
Python3 attack.py
```
To view the content of each output file, run the following commands:
```python
less evil.txt
less harmless.txt
```

### Project instructions
***These instructions were provided by Dr. Yilek as an assignment in CISC 410***<br>
You are working as Alice’s personal assistant. She has dictated to you an email she wants to send to her close friend Bob:
```
Hello Bob
We should go out next week and meet for coffee
Let me know your thoughts
I hope you’re having a good day
Best,
Alice
```

She wants you to type up the email (adding your own formatting, punctuation, etc), give her the email text, and she will digitally sign it, give you the signature, and you can send the email and signature to Bob. She is using RSA signatures by first hashing the message with sha256to3bytes (a bad hash function that hashes with sha-256 and then just uses the first 3 bytes/6 hex characters), then padding it as explained in the crypto notes (with her 1024 bit RSA modulus, this will be a 00 byte, 01 byte, 122 FF bytes, a 00 byte, and then the 3 bytes of hash) before finally applying RSA. The included script generateMsg.py does this for you: if you pipe the message to be signed, it will output what bytes will actually be sent to RSA.


Your job on this problem is to come up with two messages:

In a file harmless.txt, the original message above with added punctuation and perhaps a few different but equivalent word choices.
In a file evil.txt, some version of the following message that expresses the opposite sentiment:
```
Hello Bob
We should not go out next week and meet for coffee
Don’t let me know your thoughts
I hope you’re having a bad day
Worst,
Alice
```
Again, feel free to swap out some words for synonyms and edit the punctuation and spacing. Both of these messages should result in the same output from generateMsg.py. Thus, if Alice signs your version of the original message (harmless.txt), this signature can also be used for your malicious message (evil.txt). Submit harmless.txt and evil.txt, and also attach any scripts you use.

## Limitations and possible improvements 
This project was made to meet assignment requirements, but could be altered to be used for other purposes/messages.
