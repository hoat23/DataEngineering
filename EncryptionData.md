# Encryption

## Install

´´´
python -m pip install cryptography
´´´

## Fernet Encryption

´´´
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

´´´
