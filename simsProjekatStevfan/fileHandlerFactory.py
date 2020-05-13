from sequential_file_handler import *
from serial_file_handler import *

class FileHandlerFactory():
    @staticmethod
    def check_file(database_type, file_path, meta_path):
        if database_type == "serial":
            return SerialFileHandler(file_path, meta_path)
        if database_type == "sequential":
            return SequentialFileHandler(file_path, meta_path)
                 
        assert 0, "Ne postoji taj tip baze "+ type         