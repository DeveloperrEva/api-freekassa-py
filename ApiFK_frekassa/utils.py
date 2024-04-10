import hashlib
import hmac


def hash_by_sha256(key: str, string: str) -> str:
    result = hmac.new(key.encode(), string.encode(), digestmod=hashlib.sha256)
    return result.hexdigest()


def hash_by_md5(string: str) -> str:
    return hashlib.md5(string.encode()).hexdigest()