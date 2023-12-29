from pydantic_settings import BaseSettings


class MicroserviceSettings(BaseSettings):
    server_port: int = 8080
    # enables auto-reload based on uvicorn
    enable_reload: bool = False


class LogSettings(BaseSettings):
    log_level: str = "info"
    enable_access_log: bool = True
    enable_pretty_json_logs: bool = False
    enable_dev_logs: bool = False


microservice_settings = MicroserviceSettings()
log_settings = LogSettings()
