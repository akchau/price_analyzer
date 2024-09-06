import csv
import os
import re


def find_index(lst, options):
    return next((i for i, item in enumerate(lst) if item in options), None)


def load_prices(folder_path):
    data = []
    key_mapping = {
        'название': ['название', 'продукт', 'товар', 'наименование'],
        'цена': ['цена', 'розница'],
        'вес': ['фасовка', 'масса', 'вес']
    }

    for fname in os.listdir(folder_path):
        if re.match(r'^price_\d+\.csv$', fname):
            with open(os.path.join(folder_path, fname), mode='r', newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                headers = next(csv_reader)
                indices = {key: find_index(headers, options) for key, options in key_mapping.items()}
                data.extend(
                    (
                        *[row[indices[key]] for key in key_mapping.keys()],
                        round(int(row[indices["цена"]]) / int(row[indices["вес"]]), 0),
                        fname
                    )
                    for row in csv_reader
                )
    return sorted(data, key=lambda x: x[3], reverse=True)


def search(folder_path, value):
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Не найден путь к папке: {folder_path}")
    all_data = load_prices(folder_path)
    return [x for x in all_data if value in x[0]]


def export_to_html(data, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write('''
        <!DOCTYPE html>
        <html lang='ru'>
        <head>
            <meta charset='UTF-8'>
            <title>Позиции продуктов</title>
        </head>
        <body>
            <table>
                <tr>
                    <th>№</th>
                    <th>Наименование</th>
                    <th>Цена</th>
                    <th>Вес</th>
                    <th>Цена за кг.</th>
                    <th>Файл</th>
                </tr>
        ''')
        for index, row in enumerate(data):
            file.write(f"<tr>{''.join(f'<td>{cell}</td>' for cell in [index, *row])}</tr>\n")
        file.write('''
            </table>
        </body>
        </html>
        ''')
    print(f"HTML файл успешно создан: {output_file_path}")


def main():
    result = None
    try:
        while True:
            input_str = input("Укажите значение: ")
            if input_str == "exit":
                break
            result = search("<Укажите путь к папке>", input_str)
            print(result)
    except KeyboardInterrupt:
        pass

    finally:
        if result:
            export_to_html(result, "<Укажите путь к html файлу>")


if __name__ == '__main__':
    main()
