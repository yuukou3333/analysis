# ICP-MSのテキストデータから欲しい部分の値を取得するプログラム

1. ICP-MSの取得したデータをディレクトリにいれ名前をつける。その際、`卒論_分析結果/元素分析`の中に`CSV`と`Excel`というディレクトリを作っておく。

2. change_txt.pyの中でファイルを指定し、テキストファイルをCSVファイルに変更する。（ファイル名は1~9までとそれ以外に分けて指定する）


3. change_csv.py でファイルを指定してエクセルファイルに変更する。（ファイル名は1~9までとそれ以外に分けて指定する）例は以下に記載。
 
```
L+B_Ctr+Se ==================================================
 for i in range(1,10):
   filename = f'/Users/sendahiroshikou/Desktop/卒論_分析結果/元素分析/L+B__init__1/CSV/-fq_00{i}SMPL.csv'
   output_name = f'/Users/sendahiroshikou/Desktop/卒論_分析結果/元素分析/L+B__init__1/Excel/fq_00{i}SMPL.xlsx'
   csv_xlsx_converter(filename, output_name)
```

4. open_excel.pyでエクセルの値を出力
