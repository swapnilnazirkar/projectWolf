import logging
class logGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\logs\\automatin.log",format='%(asctime)s:%(levelname)s:%(messge)s',datefmt='%m/%d%Y%I:%M:%S%P')
        logger=logging.getLogger()
        logger.setLevel((logging.INFO))
        return logger