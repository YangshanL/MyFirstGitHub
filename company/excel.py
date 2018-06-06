import xlrd


class excel():
    def __init__(self, excelPath, newPath):
        self.excelPath = excelPath
        self.newPath = newPath
        self.start()

    def start(self):
        self.read_excel()
        for i in range(self.nrows):
            data = self.table.row_values(i)
            print(data)
            print(type(data[0]),type(data[1]))
        # newFile = open(self.newPath, 'w')
        pass

    def read_excel(self):
        data = xlrd.open_workbook(self.excelPath)
        self.table = data.sheets()[0]
        self.nrows = self.table.nrows

        pass


if __name__ == '__main__':
    excelPath = r'D:\tank\config.xlsx'
    newPath = r'D:\tank\test.py'
    run = excel(excelPath, newPath)
    pass
