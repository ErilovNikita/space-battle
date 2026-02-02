import logging

logger = logging.getLogger("test_logger")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s %(levelname)s | %(emoji)s %(message)s",
    datefmt="%H:%M:%S",
)

class EmojiFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        if not hasattr(record, "emoji"):
            record.emoji = "ℹ️"
        return True

console_handler.addFilter(EmojiFilter())
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def scenario(msg: str) -> None:
    logger.info(msg, extra={"emoji": "🧪"})

def expect(msg: str) -> None:
    logger.info(msg, extra={"emoji": "⚡"})

def result(msg: str) -> None:
    logger.info(msg, extra={"emoji": "✅"})
