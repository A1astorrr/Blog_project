from pydantic_settings import BaseSettings
from pydantic import SecretStr, Field

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int = Field(ge=1, le=65535)
    DB_USER: str
    DB_PASS: SecretStr
    DB_NAME: str
    
    @property
    def DATABASE_URL(self):
        return f"postgres://{self.DB_USER}:{self.DB_PASS.get_secret_value()}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    class Config:
        env_file = ".env"

settings = Settings()

TORTOISE_ORM = {
    "connections": {"default": settings.DATABASE_URL},
    "apps": {
        "models": {
            "models": ["app.models"],
            "default_connection": "default",
        }
    }
}