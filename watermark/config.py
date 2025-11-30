import os

class BotConfig:
    DOWNLOAD_DIR = "downloads"
    OUTPUT_DIR = "output"
    SAVED_WATERMARK = "watermark/default.png"
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    def save_watermark(self, file_path):
        os.makedirs(os.path.dirname(self.SAVED_WATERMARK), exist_ok=True)
        os.replace(file_path, self.SAVED_WATERMARK)

bot_config = BotConfig()
