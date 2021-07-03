import os


def init_log() -> int:
    return (
        int(log_group)  # type: ignore
        if (log_group := os.environ.get("LOG_GROUP")) is not None
        else None
    )


class Config:
    BOT_TOKEN = os.environ["1728087210:AAFj2wMxr_TFOYdASuy1NRJh3OFOHfvto5Y"]
    API_ID = int(os.environ["1378165"])
    API_HASH = os.environ["dd2e80c7745fa709a04842c081db3bc8"]
    EXEC_PATH = os.environ.get("GOOGLE_CHROME_SHIM", None)
    # OPTIONAL
    LOG_GROUP = init_log()
    SUPPORT_GROUP_LINK = os.environ.get("SUPPORT_GROUP", "https://t.me/webdevchat")
