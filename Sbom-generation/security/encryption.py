import hmac
import hashlib
import json
from base64 import b64encode, b64decode

def encrypt_data(data, key):
    '''
    Encrypts the given data using the given key and returns the encrypted data.
    args:
        data: The data to encrypt.(json data no file input)
        key: The key to use for encryption.
    '''

    key_bytes = key.encode('utf-8')
    json_string = json.dumps(data, indent=2)
    hash_digest = hmac.new(key_bytes, json_string.encode('utf-8'), hashlib.sha256).digest()
    encrypted_data = b64encode(hash_digest + json_string.encode('utf-8')).decode('utf-8')
    return encrypted_data

def decrypt_data(encrypted_data, key):
    '''
    Decrypts the given data using the given key and returns the decrypted data.
    args:
        encrypted_data: The data to decrypt.
        key: The key to use for decryption.

    '''

    key_bytes = key.encode('utf-8')
    encrypted_bytes = b64decode(encrypted_data)

    # Extract the hash and the JSON string from the encrypted data
    received_hash_digest = encrypted_bytes[:32]
    json_string = encrypted_bytes[32:]

    # Verify the hash using HMAC-SHA256
    if hmac.compare_digest(received_hash_digest, hmac.new(key_bytes, json_string, hashlib.sha256).digest()):
        decrypted_data = json.loads(json_string.decode('utf-8'))
        return decrypted_data
    else:
        return None




