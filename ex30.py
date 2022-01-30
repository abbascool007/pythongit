import xlrd
loc=("C:\\Users\\iabba\\Desktop\\PI samples\\datadriven.xlsx")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
p1=sheet.cell(1,0).value
print(p1)
#to get tot no of rows and columns
print(sheet.nrows)
print(sheet.ncols)
#to get all row values
for i in range(sheet.nrows):
    p2 = sheet.cell(i, 0).value
    print(p2)
#o/p will be all row values from first to last