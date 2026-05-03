from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGO_URL: str
    DB_NAME: str
    APP_ENV: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    JWT_EXPIRE_MINUTES: int
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASSWORD: str
    OTP_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"


settings = Settings()
