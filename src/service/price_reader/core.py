import os

from src.deps.csv_parser import CsvParser
from src.service.utils.filter_string import filter_string_list


class PriceReader:

    def __init__(self, dir_path: str):
        self.__dir_path = dir_path

    def __get_prices_names(self) -> list[str]:
        files = os.listdir(self.__dir_path)
        return filter_string_list(files, good_patterns=[r"price"])

    def read_prices(self) -> list:
        return [(CsvParser.parse_csv(path=os.path.join(self.__dir_path, filename), without_headers=False), filename)
                for filename in self.__get_prices_names()]

