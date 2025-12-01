import logging
from datetime import datetime
LOG_FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
current_date_formatted = datetime.now().strftime("%Y-%m-%d")
log_message = f"Current date: {current_date_formatted}"
logging.info(log_message)
