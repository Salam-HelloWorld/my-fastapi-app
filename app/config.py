import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Reads settings from environment variables (with defaults)."""

    def __init__(self) -> None:
        self.app_name = os.getenv("APP_NAME", "FastAPI Template")
        self.app_env = os.getenv("APP_ENV", "development")
        self.app_version = os.getenv("APP_VERSION", "0.1.0")
        self.welcome_message = os.getenv(
            "WELCOME_MESSAGE", "Welcome to the Simple Backend Example API."
        )
        self.api_secret = os.getenv("API_SECRET", "")


def get_settings() -> Settings:
    # Re-read the environment on every call, so tests can change it.
    return Settings()
