import logging

# ログは追記される．上書きにしたい場合，basicConfig を filemode="w" とする
logging.basicConfig(filename="example.log", level=logging.DEBUG)
logging.debug("hey")
logging.info("hoy")
logging.warning("soy")
logging.error("hooo")
logging.critical("yooo")