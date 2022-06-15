import os
import settings
from datetime import timedelta, datetime
from jose import jwt


def create_access_token(
    userid: str,
):
    return create_token(
        token_type="access_token",
        lifetime=timedelta(minutes=int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))),
        userid=userid,
    )


def create_token(
    token_type: str,
    lifetime: timedelta,
    userid: str,
):
    payload = {}
    expire = datetime.utcnow() + lifetime
    payload["type"] = token_type
    payload["exp"] = expire
    payload["iat"] = datetime.utcnow()
    payload["userid"] = str(userid)

    return jwt.encode(payload, os.getenv('SECRET_KEY'))
