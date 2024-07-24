from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


# Настройки PostgreSQL
class PostgresConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="postgres_")

    host: str = Field(default="localhost")
    port: int = Field(default=5432)
    db: str = Field(default="web_notepad")
    user: str = Field(default="web_notepad")
    password: str = Field(default="web_notepad")
    echo_log: bool = Field(default=False)

    @property
    def database_url(self):
        return f"postgresql+psycopg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


class ProjectConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="project_")

    debug: bool = True
    jwt_secret_key: str
    name: str = Field(default='web_notepad_api')
    log_level: str = Field(default="DEBUG")


class Settings(BaseSettings):
    project: ProjectConfig = ProjectConfig()  # type: ignore
    postgres: PostgresConfig = PostgresConfig()
