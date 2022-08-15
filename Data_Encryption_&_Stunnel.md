# Encryption

## Install

```
python -m pip install cryptography
```

## Fernet Encryption

Fernet uses AES 128 encryption in CBC mode. See the cryptography docs for an example of using AES 256. Whatever you choose to do, use cryptography, not pycrypto (imported as Crypto), which is no longer actively maintained.

```python
import json
from cryptography.fernet import Fernet

cipher = Fernet( Fernet.generate_key() )
info = {
  "carnum": 2211849528391929,
  "exp": [2020, 9],
  "cv2": 842,
}

#Encoding data
data_encoded = cipher.encrypt( json.dumps(info).encode("utf-8") )

#Decoding data
data_decoded = cipher.decrypt( data_encoded )
```

# Hashing Information

```python
import hashlib

ID = "joss229"

msg_clear = "hola mundo"

md5 = hashlib.md5()
md5.update(msg_clear.encode('utf-8'))
print(md5.digest())

msg_clear = ID
sha256 = hashlib.sha256()
sha256.update(msg_clear.encode('utf-8'))
print(sha256.hexdigest())
#\xcf\xef\x88\x0b\x08\xfaYW\x8d\x80\xb0\xe0\xf6E\x0c\x0e\xe0\xb1\xdc\xb6SWg\xa2\xfb\x81\x0c\xd1\xd6\xa3

#104dd2dd06747463200199967ab72d81
#26cfef880b08fa59578d80b0e0f6450c0ee0b1dcb6535767a2fb810cd1d6a33d
```

# RSA Encryption

```python
# coding: utf-8
# pip install cryptography
# no pip install winrandom
# no pip install RSA
# https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/
# http://www.pythondiario.com/2018/09/cryptography-cifrado-simetrico.html
# Empezaremos generando la clave privada
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

class cypherRSA(object):
    def __init__(self):
        self.private_key=[]
        self.public_key=[]

    def genKeys(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()
        print("Public Key: " + str(self.public_key))
        print("Private Key: "+ str(self.private_key))

    def getPublicKey(self):
        return self.public_key

    def getPrivateKey(self):
        
        return self.public_key

    def encrypt(self,nameFile):
        print("Encriptar datos")

    def decrypt(self,nameFile):
        print("Desencriptar datos")


obj = cypherRSA()
obj.genKeys()
```

## Cesar Encryption

```python
# coding:utf-8
"""
@Autor Deiner Zapata Silva
@Link  https://programacionpython80889555.wordpress.com/2018/06/28/cifrado-cesar-en-python-ejercicio-basico/
"""

# Peticion de texto a cifrar
print("\n-----------------------------------------------------------------------------------------------------------")
txt_clr = input("Ingrese texto a cifrar:\n")
print("-----------------------------------------------------------------------------------------------------------")
# Creamos cadena de caracteres
if txt_clr == txt_clr.upper():
    abc = "ABCDEFGHIKLMNÑOPQRSTUVWXYZ"
else:
    abc = "abcdefghijklmnñopqrstuvwxyz"

# Definimos valor del desplazamiento
k = int(input("Valor de desplazamiento:"))

# Cadena cifrada
txt_enc = ""

# Realizamos cifrado
for c in txt_clr:
    if c in abc:
        txt_enc += abc[(abc.index(c)+k) % (len(abc))]
    else:
        txt_enc += c

# Visualizamos texto cifrado
print("-----------------------------------------------------------------------------------------------------------")
print("Texto cifrado:\n", txt_enc)
print("-----------------------------------------------------------------------------------------------------------")

```

# STUNNEL

Stunnel is a proxy designed to add TLS encryption functionality to existing clients and servers without any changes in the programs' code. Its architecture is optimized for security, portability, and scalability (including load-balancing), making it suitable for large deployments.

Stunnel uses the OpenSSL library for cryptography, so it supports whatever cryptographic algorithms are compiled into the library. It can benefit from the FIPS 140-2 validation of the OpenSSL FIPS Object Module, as long as the building process meets its Security Policy. A scanned FIPS 140-2 Validation Certificate document is available for download on the NIST web page. The OpenSSL FIPS 140-2 module is currently only available for OpenSSL 1.0.2. FIPS-enabled Windows installers of stunnel are available on request with our customer support plans.

Stunnel is a free software authored by Michał Trojnara. Although distributed under GNU GPL version 2 or later with OpenSSL exception, stunnel is not a community project. We retain the copyright of the source code. Please contact us for commercial support or non-GPL licenses. Free, community-based support is also available via stunnel-users mailing list.

* Download: https://www.stunnel.org/downloads.html 

### Configuration


- ``` touch /etc/stunnel/stunnel.conf``` 
- ``` chmod 775 /etc/stunnel/stunnel.conf``` 
- ``` nano /etc/stunnel/stunnel.conf``` 
- ``` systemctl restart stunnel4``` 
- ``` systemctl status stunnel4``` 


### Documentation about Fernet
- https://github.com/fernet/spec/blob/master/Spec.md#token-format
- 

