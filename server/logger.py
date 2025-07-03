import logging

def setup_logger(name="MedicalAssistant"):
    logger=logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    ch=logging.StreamHandler()
    ch.setLevel(logging.DEBUG)


    formatter=logging.Formatter("[%(asctime)s] [%(levelname)s] --- [%(message)s]")
    ch.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(ch)

    return logger



logger=setup_logger()

logger.info("RAG prcoess started")
logger.debug("Bebugging")
logger.error("Failed to load")
logger.critical("Critical message")