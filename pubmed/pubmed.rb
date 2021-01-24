require "csv"
data = CSV.read("pubmed.csv")

1.upto(40){|n|
  writer = data[n][2]
  writer = writer.gsub(",", ", ") 
  title = data[n][3]
  year = data[n][4]

  puts "#{writer}: #{title} #{year}"
  puts "\n"
}

