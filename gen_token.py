import secrets


def generate_token() -> str:
    return secrets.token_urlsafe(32)


def verify_token(plain_token: str, user_token: str) -> bool:
    return plain_token == user_token
