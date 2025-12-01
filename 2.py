import logging
import sys
def configure_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    fh = logging.FileHandler("errors.log", encoding="utf-8")
    fh.setLevel(logging.ERROR)
    fmt = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    ch.setFormatter(fmt)
    fh.setFormatter(fmt)
    if not logger.hasHandlers():
        logger.addHandler(ch)
        logger.addHandler(fh)
    else:
        logger.handlers = [ch, fh]
def risky_operation(x, y):
    return x / y
def main():
    configure_logging()
    logger = logging.getLogger(__name__)
    try:
        result = risky_operation(10, 0)
        logger.info("Result: %s", result)
    except Exception as exc:
        logger.exception("An error occurred in risky_operation")
if __name__ == "__main__":
    main()
