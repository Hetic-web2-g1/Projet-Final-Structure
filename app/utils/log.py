import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Logging is activated.")

# logging.debug("La fonction a bien été exécutée")
# logging.info("Message d'information général")
# logging.warning("Attention !")
# logging.error("Une erreur est arrivée")
# logging.critical("Erreur critique")