Steps to Run Assignment

In Command Prompt/ Terminal Type:


1. make setup       ##Installs Required python libraries

2. make run         ##Generates plaintexts, ciphertexts and decrypts given ciphertext to get our password


Python Script Description

1.plaingen.py : generates plaintexts required for breaking encryption and stores in plaintexts.txt

2.robot1.py : Establishes connection to game server and generates ciphertext corresponding to plaintext in plaintexts.txt and stores in ciphertext.txt and then processes it to get in desired format and stores this as ciphertexrts.txt

3.decrpyt.py : Uses plaintext-ciphertext pairs to figure out Linear Transformation Matrix A and Exponent Vector E and then performs reverse operation on given ciphertext from game to decrypt it to get level password.