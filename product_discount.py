#Consider the below code which allows you to purchase different products. All products have discount of 10%.

def purchase_product(product_type,price):
  discount = 10
  total_price = price - price* discount / 100
  print("Total price of "+product_type+"is "+str(total_price))

purchase_product("mobile",15000)
purchase_product("laptop",45000)
