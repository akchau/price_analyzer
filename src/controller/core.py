import threading
import time
from multiprocessing import Event, Queue

from src.service.product_search.core import ProductSearch
from src.service.report_generator.core import ReportGenerator
from src.settings import settings
from src.service.price_reader.core import PriceReader


CURRENT_PRICES = []

IS_CYCLE_STOP = Event()


class PriceAnalyzer:

    EXIT_COMMAND = 'exit'

    def __init__(self):
        self.__reader = PriceReader(dir_path=settings.PRICE_DIR)
        self.__product_search = ProductSearch()
        self.__report_generator = ReportGenerator()

    def _reading_cycle(self):
        global CURRENT_PRICES
        while not IS_CYCLE_STOP.is_set():
            CURRENT_PRICES = self.__reader.read_prices()
            time.sleep(1)

    def _pool_prices(self):
        polling_thread = threading.Thread(target=self._reading_cycle, daemon=True)
        polling_thread.start()

    def start(self):
        self._pool_prices()
        command = ""
        while command != self.EXIT_COMMAND:
            try:
                command = input("Найти продукт: ")
            except (UnicodeDecodeError, KeyboardInterrupt):
                pass
            if command == "exit":
                IS_CYCLE_STOP.set()
                break
            parsed_data = self.__product_search.search_product(CURRENT_PRICES, command)
            report = self.__report_generator.generate_report(data=parsed_data)
            print(report)
