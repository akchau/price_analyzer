class ProductSearch:

    NAME_STRINGS = ["название", "продукт", "товар", "наименование"]
    PRICE_STRINGS = ["цена", "розница"]
    WEIGHT_STRINGS = ["фасовка", "масса", "вес"]

    def _get_indexes(self, headers):
        name_index = None
        price_index = None
        weight_index = None
        for index, header in enumerate(headers):
            if header in self.NAME_STRINGS:
                name_index = index
            elif header in self.PRICE_STRINGS:
                price_index = index
            elif header in self.WEIGHT_STRINGS:
                weight_index = index
        if name_index is not None and price_index is not None and weight_index is not None:
            return name_index, price_index, weight_index
        raise IndexError(f"не все индексы распарсились {name_index} {price_index}, {weight_index}")

    def _get_product_in_price(self, price_data, product_name: str, filename: str):
        products = []
        name_index, price_index, weight_index = self._get_indexes(price_data[0])
        for product in price_data[1:]:
            if product_name.lower() in product[name_index].lower():
                name = product[name_index]
                price = int(product[price_index])
                weight = int(product[weight_index])
                products.append((name, price, weight, filename, round(price/weight, 0)))
        return products

    def search_product(self, products_data: list, product_name: str):
        result = []
        for price_data, filename in products_data:
            result.extend(self._get_product_in_price(price_data, product_name, filename))
        return sorted(result, key=lambda x: x[4])
