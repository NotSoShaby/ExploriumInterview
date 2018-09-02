import os
import logging


class Utils():
    """ A class to hold utilities to be used across the module """
    logger = None

    @staticmethod
    def get_all_files_from_data_folder():
        """ :return a list of absolute paths to all the files in the data folder. """
        return [os.path.join(x[0],y) for x in os.walk(os.environ["DATAFOLDER"]) for y in x[2]]

    @classmethod
    def get_main_app_logger(cls):
        """ Make logger if it doesn't exist yet, then return the logger """

        if not cls.logger:

            # set the logger path under the PYTHONLOGGER environment variable (this is a mandatory env variable)
            log_path = os.path.join(os.environ["PYTHONLOGGER"], "general.log")
            logging.basicConfig(filename=log_path, filemode='w', level=logging.DEBUG)

            #make new logger
            logging.Logger("application_logger")
            cls.logger = logging.getLogger("application_logger")

            # set format
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch = logging.StreamHandler()
            ch.setFormatter(formatter)
            ch.setLevel(logging.DEBUG)

            # set fileHandler
            fh = logging.FileHandler(os.path.join(os.environ["PYTHONLOGGER"], 'application.log'))
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(formatter)

            # adding handlers to the logger
            cls.logger.addHandler(fh)
            cls.logger.addHandler(ch)

            cls.logger.info("Logger initiated")

        return cls.logger