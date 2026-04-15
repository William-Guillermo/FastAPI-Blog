# Instalar el paquete   "pip install python-jose" ya esta en el requirements.txt 
# uv pip install python-jose
from jose import jwt 
from jose.exceptions import JWTError
from datetime import datetime, timedelta, timezone

SECRET_KEY = "clave_super_secreta"
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes = 15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token (token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError as e:
        raise Exception (f"Token invalido o expirado: {e}")

if __name__ == "__main__":
    user_data = {"sub": "usuario123"}
    token = create_access_token(user_data)
    print(f"Token generado:\n{token}\n")
    try:
        decoded = decode_token(token)
        print(f"Token decodificado:\n{decoded}")
    except Exception as e:
        print(str(e))