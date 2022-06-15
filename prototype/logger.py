import logging

logging.basicConfig(filename='amps.log',
    format='%(asctime)s %(levelname)s: %(message)s',
 level=logging.INFO)
logger = logging.getLogger(__name__)
