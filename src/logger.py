import logging

logger = logging.getLogger(__name__)

logger.propagate = 0

logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

handler = logging.StreamHandler()
handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(handler)
