#we can use global variables. We calculate the price during purchase and store it in a global variable. Later during return we access the calculated price from the global variable. But this brings more complications than it tries to solve.
total_price_mobile=0
total_price_shoe=0
def purchase_mobile(price,brand):
  global total_price_mobile
  if brand == "Apple":
     discount = 10
  else:
    discount = 5
  total_price_mobile = price - price * discount / 100
  print("Total price of "+brand+" mobile is "+str(total_price_mobile))
  
def purchase_shoe(price,material):  
  global total_price_shoe
  if material=="leather":
    tax = 5
  else:
    tax = 2
  total_price_shoe = price + price * tax / 100
  print("Total price of "+material+" shoe is "+str(total_price_shoe))
def return_mobile():
  print ("Refund price for mobile is ",total_price_mobile)
def return_shoe():
  print("Refund price for shoe is ",total_price_shoe)
purchase_mobile(15000,"Apple")
purchase_shoe(5000,"leather")
return_mobile()
return_shoe()
