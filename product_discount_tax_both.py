#The solution we came up with has a key problem. Data for mobiles and shoes are mixed up in the same code. If we have to make changes to the logic for purchasing shoes, we have to modify method that has logic for both shoes and mobiles. For example, if we have to add 'material' to the shoe and have a 5% tax on 'leather' shoes, then we have to go through code related to mobile as well, as shown below:
def purchase_product(product_type,price,mobile_brand,material):
  if product_type =="Mobile":
    if mobile_brand == "Apple":
      discount = 10
    else:
      discount = 5
    total_price = price - price * discount / 100
  else:
    if material=="leather":
      tax = 5
    else:
      tax = 2
    total_price = price + price * tax / 100

  print("Total price of "+product_type+" is "+str(total_price))

purchase_product("Mobile",15000,"Apple",None)
purchase_product("laptop",45000,None,"leather")
