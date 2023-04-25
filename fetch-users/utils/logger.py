import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler_stdout = logging.StreamHandler(stream=sys.stdout)
handler_stdout.setFormatter(logging.Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))

logger.addHandler(handler_stdout)
