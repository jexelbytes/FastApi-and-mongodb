import hashlib

def hash_password(password: str) -> str:
    result = hashlib.md5(password.encode())
    arrb = result.hexdigest()
    return str(arrb)
