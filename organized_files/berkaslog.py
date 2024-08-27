import logging

logger = logging.getLogger('roma_file')
logger.setLevel(logging.DEBUG)

process_handler = logging.FileHandler('process.log')
process_handler.setLevel(logging.INFO)

debug_error_handler = logging.FileHandler('debug_error.log')
debug_error_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
process_handler.setFormatter(formatter)
debug_error_handler.setFormatter(formatter)

logger.addHandler(process_handler)
logger.addHandler(debug_error_handler)

logger.info('Menyimpan Proses.')
logger.debug('Pesan debug untuk log debug dan error.')
logger.error('Pesan error untuk log debug dan error.')
