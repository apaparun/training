
def purchase_mobile(price,brand):
  if brand == "Apple":
     discount = 10
  else:
    discount = 5
  total_price = price - price * discount / 100
  print("Total price of "+brand+" mobile is "+str(total_price))
  
def purchase_shoe(price,material):  
  
  if material=="leather":
    tax = 5
  else:
    tax = 2
  total_price = price + price * tax / 100
  print("Total price of "+material+" shoe is "+str(total_price))
purchase_mobile(15000,"Apple")
purchase_shoe(5000,"leather")
