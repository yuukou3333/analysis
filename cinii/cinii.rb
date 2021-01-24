require "csv"
data = CSV.read("cinii.csv")


2.upto(75){|n|
  writer = data[n][2].gsub(",", ", ") 
  title = data[n][3]
  year = data[n][4]

  puts "#{writer}: #{title}. #{year}"
  puts "\n"
}

