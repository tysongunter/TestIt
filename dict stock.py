stocks_dict = {
  "AAL": "34.56",
  "IBM": "44.56",
  "AAPL": "78.56",
  "ACI": "12.45", 
  "AGI": "45.11",
  "BKR": "11.99",
  "AMZN": "109.80",
  "GOOGL": "106.25", 
  "TSLA": "186.70", 
  "GPRO": "6.47",
  
}

x = input("Please enter your stock symbol: ")
z = stocks_dict.get(x)
print (z)
