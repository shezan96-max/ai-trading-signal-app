from passlib.hash import bcrypt

def hash_password(pw : str) -> str:
    return bcrypt.hash(pw)

