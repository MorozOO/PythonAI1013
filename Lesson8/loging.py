import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w",
                    format="We have next logging message:%(asctime)s:%(levelname)s - %(message)s")

#
# logging.debug("Помикла найнижчого рівня")
# logging.info("info")

try:
    print(10/0)
except Exception:
    logging.exception("Zero division Error")