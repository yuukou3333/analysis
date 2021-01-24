import openpyxl

# ブックを取得
def open_xl(x_filename, end_num):
  end_num += 1
  book = openpyxl.load_workbook(x_filename)
  # シートを取得 
  sheet = book['Sheet']
  # セルを取得
  # print (sheet[f'D45'].value)
  for i in range(0, end_num):
    print (sheet[f'D{45 + i * 58}'].value)


# L+B init ===========================================================================================
# end_num = 9
# x_filename =  f'/Users/sendahiroshikou/Desktop/卒論_分析結果/元素分析/L+B__init__1/Excel/fq_00{end_num}SMPL.xlsx'

# end_num = 20
# x_filename =  f'/Users/sendahiroshikou/Desktop/卒論_分析結果/元素分析/L+B__init__1/Excel/fq_0{end_num}SMPL.xlsx'



# L+B_Ctr+Se ==================================================
# end_num = 9
# x_filename =  f'/Users/sendahiroshikou/Desktop/卒論_分析結果/元素分析/L+B__Ctr+Se__1/Excel/fq_00{end_num}SMPL.xlsx'

end_num = 79
x_filename =  f'/Users/sendahiroshikou/Desktop/卒論_分析結果/元素分析/L+B__Ctr+Se__1/Excel/fq_0{end_num}SMPL.xlsx'

open_xl(x_filename, end_num)
