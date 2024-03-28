import hashlib

def hash_sha3_256(s: str) -> str:
    return (hashlib.sha3_256(s.encode("utf-8"))).hexdigest()