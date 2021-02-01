# Encryption

## Install

```
python -m pip install cryptography
```

## Fernet Encryption

Fernet uses AES 128 encryption in CBC mode. See the cryptography docs for an example of using AES 256. Whatever you choose to do, use cryptography, not pycrypto (imported as Crypto), which is no longer actively maintained.

```
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

### Documentation about Fernet
- https://github.com/fernet/spec/blob/master/Spec.md#token-format

