import csv
import openpyxl
 
wb = openpyxl.Workbook()
ws = wb.active

def csv_xlsx_converter(filename, output_name): 
  with open(filename) as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        ws.append(row)
  wb.save(output_name)


# L+B init ===========================================================================================

# for i in range(1,10):
#   filename = f'/Users/sendahiroshikou/Desktop/卒論_分析結果/元素分析/L+B__init__1/CSV/-fq_00{i}SMPL.csv'
#   output_name = f'/Users/sendahiroshikou/Desktop/卒論_分析結果/元素分析/L+B__init__1/Exel/fq_00{i}SMPL.xlsx'
#   csv_xlsx_converter(filename, output_name)


for i in range(10,21):
  filename = f'/Users/sendahiroshikou/Desktop/卒論_分析結果/元素分析/L+B__init__1/CSV/-fq_0{i}SMPL.csv'
  output_name = f'/Users/sendahiroshikou/Desktop/卒論_分析結果/元素分析/L+B__init__1/Exel/fq_0{i}SMPL.xlsx'
  csv_xlsx_converter(filename, output_name)


