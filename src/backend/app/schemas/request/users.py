from pydantic import BaseModel


class UserRegistrationSchema(BaseModel):
    username: str
    full_name: str | None = None
    password: str

    def safe_data(self) -> dict:
        return self.model_dump(exclude={"password"})


class UserChangeInfoSchema(BaseModel):
    username: str | None = None
    full_name: str | None = None


class UserChangePasswordSchema(BaseModel):
    password: str
    new_password: str


class UserLoginSchema(BaseModel):
    username: str
    password: str

    def safe_data(self) -> dict:
        return self.model_dump(exclude={"password"})
