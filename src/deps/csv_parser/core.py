import csv
from typing import Callable


class CsvParser:

    @staticmethod
    def parse_csv(path, row_handler: Callable = None, without_headers: bool = True):
        parsed_data = []
        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            if without_headers:
                next(reader)
            for row in reader:
                if row_handler is not None:
                    parsed_data.append(row_handler(row))
                else:
                    parsed_data.append(tuple(row))
        return parsed_data
