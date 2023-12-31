from pydantic import BaseModel


class User(BaseModel):
    """User."""

    user: str
    pwd: str


class UserNoPwd(BaseModel):
    """User no password."""

    user: str


class LoginSucess(BaseModel):
    """Login sucess."""

    user: str
    access_token: str
