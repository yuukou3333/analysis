
import csv

# テキストファイルを開いてCSVファイルに書き込む
def text_csv_converter(datas): # datasはテキストファイルの場所
   # 保存するCSVファイルの場所
   file_csv = datas.replace("txt", "csv")
   
  # テキストファイルを開く
   with open(datas)as rf:
       # 書き込むＣＳＶファイルを開く
       with open(file_csv, "w")as wf:
           # テキストを１行ずつ読み込む
           # テキストの１行を要素としたlistになる
           readfile = rf.readlines()
           
           for read_text in readfile:
               # listに分割
               read_text = read_text.replace("]","")
               read_text = read_text.replace("ppm","")
               read_text = read_text.replace("P","")
               read_text = read_text.replace("A","")
               read_text = read_text.replace("[","")
               read_text = read_text.replace("RSD(%)","")
               read_text = read_text.replace("質量数","")
               read_text = read_text.split()
               # csvに書き込む
               writer = csv.writer(wf, delimiter=',')
               writer.writerow(read_text)
if __name__ == '__main__':
   # filenameはテキストファイルの場所
   filename = "/Users/sendahiroshikou/Desktop/卒論_分析結果/元素分析/L-B_init_1/fq_001SMPL.txt"
   text_csv_converter(filename)
