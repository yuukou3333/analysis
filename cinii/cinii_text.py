import csv

csv_file = open("cinii.csv", "r", encoding="utf-8")

# リストで取得 =======================================
# f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
# header = next(f)
# print(header) # イテレータを出力
      # next関数とは、イテレータ内から要素を取り出すための関数です。
      # イテレータは、「繰り返し可能なオブジェクト（イテラブル）の分身のようなオブジェクト」のことを指します。
  # => ['\ufeff', 'rank', 'writer', 'title', 'year', 'url']
  # \ufeffは通称BOMと呼ばれ、テキストの始まりをプログラムに伝えるためのデータ内のマーク。表示したくない場合は『utf-8-sig』をエンコーディングすれば良い。https://qiita.com/msk02/items/c3a1c4a1e1ef94c37228
# for row in f:
  # print(row)

# 辞書で取得 ============================================
f = csv.DictReader(csv_file)
for row in f:
  # print(dict)
    #rowはdictionary
    #row["column_name"] or row.get("column_name")で必要な項目を取得することができる
  print(
    row['writer'].replace(',', ', ') + ":" 
    + row['title'] + ". " 
    + row['year'] + "\n"
  )

# 最終的なコード ====================================

# import csv

# csv_file = open("cinii.csv", "r", encoding="utf-8")
# f = csv.DictReader(csv_file)
# for row in f:
#   print(
#     row['writer'].replace(',', ', ') + ":" + 
#     row['title'] + ". " + 
#     row['year'] + "\n"
#   )
