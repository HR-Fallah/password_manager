import os
import time
import base64
import platform
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def encrypt_AES(key, data):
    key = key.ljust(32, b'\0')[:32]
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    return base64.b64encode(iv + ciphertext).decode('utf-8')


def decrypt_AES(key, enc_data):
    key = key.ljust(32, b'\0')[:32]
    enc_data = base64.b64decode(enc_data)
    iv = enc_data[:16]
    ciphertext = enc_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode('utf-8')


def clear_terminal():
    if platform.system().lower() == "windows": os.system('cls')
    else: os.system('clear')

def print_delay(msg, delay):
    for c in msg:
        print(c, end='', flush=True)
        time.sleep(delay)
    print('', flush=True)


key = input("Enter Key: ").encode('utf-8')
clear_terminal()
print_delay('Key Recieved!', 0.1)
print('')

while True:
    print('1. Encrypt')
    print('2. Decrypt')
    print('0. Exit')
    operation_number = input('Enter Operation Number: ')

    if operation_number == "1":
        print('')
        message = input('Enter A Message: ')
        encrypted = encrypt_AES(key, message)
        print('')
        print(f"Encrypted Message: {encrypted}")
        print('')

    elif operation_number == "2":
        print('')
        encrypted = input('Enter An Encrypted Message: ')
        try:
            decrypted = decrypt_AES(key, encrypted)
        except:
            print('')
            print('Invalid Encrypted Message!')
            print('')
            continue
        
        print('')
        print(f"Decrypted: {decrypted}")
        print('')

    elif operation_number == "0":
        quit()

    else:
        print('Invalid Operation Number!')

