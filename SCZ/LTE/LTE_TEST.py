# pip install pycryptodomex
from typing import KeysView
from Cryptodome import Hash, Random, PublicKey, Protocol, IO, Cipher, Math, Signature, SelfTest, Util
from Cryptodome.PublicKey import RSA
from Cryptodome.Hash import MD5, SHA384
import numpy as np

class Redb(str):
    """
    Database
    """
    username = ['Alex','sero']
    message = ['Hello', 'hi']

    
def Decrypt(self, get_data, key):
    """
    Decrypt
    """
    Redb = b'ww'

    #def LTE_1(self, get_data, key):
    
    """
    LTE 1
    """
    code = 'nooneknows'
    key = RSA.generate(2048)
    encrypted_key = key.exportKey(
        passphrase=code, 
        pkcs=8, 
        protection="scryptAndAES128-CBC"
    )

    print(encrypted_key.hex())
    with open('LTE\key\LTE_private_rsa_key.bin', 'wb') as f:
        f.write(encrypted_key)
    
    with open('LTE\key\LTE_rsa_public.pem', 'wb') as f:
        f.write(key.publickey().exportKey())
    
    return key, send_data_end, self
    


with open('encrypted_data.bin', 'wb') as out_file:
    recipient_key = RSA.import_key(
        open('SCZ\\LTE\\key\\LTE_key_MD5_public\\LTE_1_MD5_rsa_public.pem').read()
    )
    
    session_key = Random.get_random_bytes(16)
    
    cipher_rsa = MD5.new(recipient_key)
    out_file.write(cipher_rsa.encrypt(session_key))
    
    cipher_aes = Cipher.AES.new(session_key, Cipher.AES.MODE_EAX)
    data = b'blah blah blah Python blah blah'
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    
    out_file.write(cipher_aes.nonce)
    out_file.write(tag)
    out_file.write(ciphertext)