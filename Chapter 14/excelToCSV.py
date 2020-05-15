import os, csv, openpyxl

os.chdir('C:\\Users\\Szymon\\Documents\\Python file\\pythonAttemptTwo\\csv json')

wb = openpyxl.load_workbook('test.xlsx', data_only=True)
sheet = wb.active
outputFile = open('output.csv', 'w', newline='')
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
