import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 5998497082:AAGSEU-lcDX-TMV5vjK0MD71bExIqHK8Ekw)
    STRING_SESSION = os.environ.get("STRING_SESSION", BQA4pgpy3e091frCd5WTLXOUJ6G39jIVf93fyhBwSICtphosF3kY-pP5GAmcqOReojfV04OiPJA5xvtAAVc3ZIuMQ7-nPbqwb0TRsd2u9ZZZFFqx3NKh6nL05kDtuOYClhiER0CQmFsC5Y5xr7SagF_kZFvkbtYg536btZTjO5sMwh3zAvk7pO19PgubylFTZWdXiK2ErUi6YwdIaROtvkMoSLCJCBGDZ3Xo9wWFbGFZpTPeoBGtqsP6q7oxqc0RjPylh3pvhCPuHwoaQqt9fx9cVpy_kDsBbm6suxAUi5UplapcklV_KiaaZFucRNHDG8jizfqrVX1cmG1QbCwIAAD4AAAAAUI7BkMA)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
