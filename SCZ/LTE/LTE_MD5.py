# pip install pycryptodomex
from typing import KeysView
from Cryptodome import Hash, Random, PublicKey, Protocol, IO, Cipher, Math, Signature, SelfTest, Util
from Cryptodome.PublicKey import RSA
from Cryptodome.Hash import MD5, SHA384
import numpy as np
from os import path 
class Redb(str):
    """
    Database
    """
    username = ['Alex','sero']
    message = ['Hello', 'hi']


class Encryption:
    """
    Encryption
    """

    #def setting_RSA():

    def LTE_1(self, get_data, key):
        """
        LTE 1
        """
    
        if False:
            code = 'nooneknows'
            key = RSA.generate(2048)
            encrypted_key = key.exportKey(
                passphrase=code, 
                pkcs=8, 
                protection="scryptAndAES128-CBC"
            )
            with open('SCZ\\LTE\\key\\LTE_key_MD5_private\\LTE_1_MD5_private_rsa_key.bin', 'wb') as f:
                f.write(encrypted_key)
        
            with open('SCZ\\LTE\\key\\LTE_key_MD5_public\\LTE_1_MD5_rsa_public.pem', 'wb') as f:
                f.write(key.publickey().exportKey())
   
#        with open('encrypted_data.bin', 'wb') as out_file:   
#            public_key = RSA.import_key(open('SCZ\\LTE\\key\\LTE_key_MD5_public\\LTE_1_MD5_rsa_public.pem').read())

        object_data = MD5.new(get_data)
        hexcode = object_data.hexdigest()
        send_data = hexcode.encode('utf-8')
        print(hexcode)
        return send_data

    def LTE_2(self, get_data, key,):

            """
            LTE 2
            """
            if False:    
                code = 'nooneknows'
                key = RSA.generate(2048)
                encrypted_key = key.exportKey(
                    passphrase=code, 
                    pkcs=8, 
                    protection="scryptAndAES128-CBC"
                )
                with open('SCZ\\LTE\\key\\LTE_key_MD5_private\\LTE_2_MD5_private_rsa_key.bin', 'wb') as f:
                    f.write(encrypted_key)
        
                with open('SCZ\\LTE\\key\\LTE_key_MD5_public\\LTE_2_MD5_rsa_public.pem', 'wb') as f:
                    f.write(key.publickey().exportKey())            

            object_data = MD5.new(get_data)
            hexcode = object_data.hexdigest()
            send_data = hexcode.encode('utf-8')
            print(hexcode)
            return send_data

    def LTE_3(self, get_data, key):
            """
            LTE 3
            """
            if False:    
                code = 'nooneknows'
                key = RSA.generate(2048)
                encrypted_key = key.exportKey(
                    passphrase=code, 
                    pkcs=8, 
                    protection="scryptAndAES128-CBC"
                )
                with open('SCZ\\LTE\\key\\LTE_key_MD5_private\\LTE_3_MD5_private_rsa_key.bin', 'wb') as f:
                    f.write(encrypted_key)
            
                with open('SCZ\\LTE\\key\\LTE_key_MD5_public\\LTE_3_MD5_rsa_public.pem', 'wb') as f:
                    f.write(key.publickey().exportKey())

            object_data = MD5.new(get_data)
            hexcode = object_data.hexdigest()
            send_data = hexcode.encode('utf-8')
            print(hexcode)
            return send_data

    def LTE_4(self, get_data, key):
            """
            LTE 4
            """
            if False:                    
                code = 'nooneknows'
                key = RSA.generate(2048)
                encrypted_key = key.exportKey(
                    passphrase=code, 
                    pkcs=8, 
                    protection="scryptAndAES128-CBC"
                )
                with open('SCZ\\LTE\\key\\LTE_key_MD5_private\\LTE_4_MD5_private_rsa_key.bin', 'wb') as f:
                    f.write(encrypted_key)
            
                with open('SCZ\\LTE\\key\\LTE_key_MD5_public\\LTE_4_MD5_rsa_public.pem', 'wb') as f:
                    f.write(key.publickey().exportKey())

            object_data = MD5.new(get_data)
            hexcode = object_data.hexdigest()
            send_data = hexcode.encode('utf-8')
            print(hexcode)
            return send_data

    def LTE_5(self, get_data, key):
            """
            LTE 5
            """
            if False:
                code = 'nooneknows'
                key = RSA.generate(2048)
                encrypted_key = key.exportKey(
                    passphrase=code, 
                    pkcs=8, 
                    protection="scryptAndAES128-CBC"
                )
                with open('SCZ\\LTE\\key\\LTE_key_MD5_private\\LTE_5_MD5_private_rsa_key.bin', 'wb') as f:
                    f.write(encrypted_key)
            
                with open('SCZ\\LTE\\key\\LTE_key_MD5_public\\LTE_5_MD5_rsa_public.pem', 'wb') as f:
                    f.write(key.publickey().exportKey())

            object_data = MD5.new(get_data)
            hexcode = object_data.hexdigest()
            send_data = hexcode.encode('utf-8')
            print(hexcode)
            return send_data
            
# Get Data
    def get_data(get_data):
            """
            Get Data
            """
            En_lte_1 = Encryption.LTE_1(self='', get_data = get_data, key='')
            En_lte_2 = Encryption.LTE_2(self='', get_data = En_lte_1, key='')
            En_lte_3 = Encryption.LTE_3(self='', get_data = En_lte_2, key='')
            En_lte_4 = Encryption.LTE_4(self='', get_data = En_lte_3, key='')
            En_lte_5 = Encryption.LTE_5(self='', get_data = En_lte_4, key='')

            #Encryption.LTE_1(self='' ,get_data = get_data, key='')
            return En_lte_1, En_lte_2, En_lte_3, En_lte_4, En_lte_5

# TEST Code 'ON = True' - 'OFF = False'
if True:
    print('Test code Encryption')
    Encryption.get_data(get_data=b'TEST')


class Decryption():
    """
    LTE Decryption
    """
    De_lte_1 = Encryption.LTE_1#(self='', get_data = None, key='')
    De_lte_2 = Encryption.LTE_2#(self='', get_data = '', key='')
    De_lte_3 = Encryption.LTE_3#(self='', get_data = '', key='')
    De_lte_4 = Encryption.LTE_4#(self='', get_data = '', key='')
#    print(De_lte_1)

    def Decryption_LTE_1():
        """
        Decryption LTE 1
	    """
        De_lte_5 = Encryption.get_data
        get_data = MD5.MD5Hash(De_lte_5)
        print(get_data)
		
        return 
#Decryption.Decryption_LTE_1()

         