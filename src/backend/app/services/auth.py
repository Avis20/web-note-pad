import logging
from datetime import datetime, timedelta
from uuid import UUID, uuid4

import jwt

from app.constants.auth import EXPIRE_ACCESS_TOKEN
from app.dto.auth import AuthDataDTO, TokenDTO
from app.exceptions.auth import AuthException


logger = logging.getLogger(__name__)


class AuthService:
    _encode_algorithm: str = "HS256"

    def __init__(self, jwt_secret_key: str):
        self._jwt_secret_key = jwt_secret_key

    async def extract_auth_data(self, access_token: str) -> AuthDataDTO:
        """Валидация access токена."""
        try:
            payload: dict = jwt.decode(access_token, self._jwt_secret_key, algorithms=[self._encode_algorithm])
        except (
            jwt.DecodeError,
            jwt.InvalidKeyError,
            jwt.InvalidIssuerError,
            jwt.InvalidSignatureError,
        ):
            raise AuthException.TokenDecodeException(f"Can't decode jwt token! See {access_token}")
        except jwt.exceptions.ExpiredSignatureError as error:
            raise AuthException.TokenExpiredException(f"Token is expired! error = {error}")

        logger.info(">>> Payload %s", payload)
        return AuthDataDTO(user_id=payload.get("sub", None))

    async def create_access_token(self, user_id: UUID) -> str:
        """Генерация access токена."""

        access_expire = (datetime.now() + timedelta(seconds=EXPIRE_ACCESS_TOKEN)).timestamp()

        payload = {
            'sub': str(user_id),
            'exp': int(access_expire),
            'iat': int(datetime.utcnow().timestamp()),
        }

        try:
            access_token = jwt.encode(payload, self._jwt_secret_key, algorithm=self._encode_algorithm)
        except (ValueError, TypeError):
            logger.error("Can't create jwt token! See JWT_SECRET_KEY in env, or something else...", exc_info=True)
            raise AuthException.TokenEncodeException()

        return access_token

    async def create_token_pair(self, user_id: UUID) -> TokenDTO:
        access_token = await self.create_access_token(user_id)
        refresh_token = uuid4()

        # TODO: save from redis

        return TokenDTO(
            access_token=access_token,
            refresh_token=refresh_token,
        )
