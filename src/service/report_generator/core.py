class ReportGenerator:

    @staticmethod
    def header_string():
        return ("№" + ' '*5 + "Наименование" + ' '*50 + "Цена" + ' '*2 + "Вес"
                + ' '*5 + "файл" + ' '*10 + "цена за кг.\n")

    def generate_report(self, data):
        result = self.header_string()
        counter = 1
        for item in data:
            result += (str(counter) + " "*(6 - len(str(counter))) + item[0] + " "*(63 - len(item[0]))
                       + str(item[1]) + " "*(6 - len(str(item[1]))) + str(item[2])
                       + " "*(8 - len(str(item[2]))) + item[3] + " "*(14 - len(item[3])) + str(item[4]) + "\n")
            counter += 1
        return result
