A Telegram _Web-Screenshot_ Bot Based on Pyrogram
# Introduction

Telegram Bot that creates screenshot _[PNG/JPEG]_ or PDF of a given link. Can be matched with various other settings like resolution, partial or full-page rendering. The bot can currently be found in @BetterWebShotBot.

### Available Resolutions are :

1. 640x480
2. 800x600
3. 1280x720
4. 2560x1440

Splitting of long pages are available for png and jpeg.

# Installing 

> Note: the bot requires chromium/chrome binary to render websites.
### <b>The Legacy Way</b>
Simply clone the repository and run the main file:

```sh
git clone https://github.com/alenpaul2001/Web-Screenshot-Bot.git
cd Web-Screenshot-Bot
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip3 install -r requirements.txt
# <Create config.py appropriately>
python3 __main__.py
```
#### an example config.py 👇
```py
class Config:
    BOT_TOKEN = "12345:49dc3eeb1aehda3cI2TesHNHc"
    API_ID = 256123
    API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
    # Leave this None to automatically download chrome binary
    EXEC_PATH = None
    # Optional Fields
    LOG_GROUP = -123990002
    SUPPORT_GROUP_LINK = "https://t.me/example"
```




#Report bugs and suggest new features

[PapyProjects](https://telegram.me/Papyprojects) and 
[PapyProjectsbot](https://telegram.me/Papyprojectsbot) for suggesting new features.

### Made by Papy
