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

```
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

### Documentation about Fernet
- https://github.com/fernet/spec/blob/master/Spec.md#token-format

