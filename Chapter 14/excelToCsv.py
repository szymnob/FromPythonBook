import os, csv, openpyxl

path = 'C:\\Users\\Szymon\\Documents\\Python file\\pythonAttemptTwo\\csv json'
os.chdir(path + '\\examples')

for file in os.listdir('.'):

    if file.endswith('.xlsx'):

        wb = openpyxl.load_workbook(file, data_only=True)
        for sheetName in wb.sheetnames:
            sheet = wb.get_sheet_by_name(sheetName)
            outputFile = open(os.path.join(path + '\\examplesinCSV', file+'_'+sheetName+'.csv'), 'w', newline='')
            csvWriter = csv.writer(outputFile)

            max_column = sheet.max_column
            max_row = sheet.max_row

            mainList = [[] for i in range(max_row)]

            for rw in range(1, max_row+1):
                for col in range(1, max_column+1):
                    mainList[rw-1].append(sheet.cell(column=col, row=rw).value)

            print(mainList)

            for i in mainList:
                print(i)
                csvWriter.writerow(i)

            outputFile.close()