ch = input("Enter a character:")
if(ord(ch)>=65 and ord(ch)<=90):
  print("Upper")
elif(ord(ch)>=97 and ord(ch)<=122):
  print("Lower")
elif(ord(ch)>=48 and ord(ch)<=57):
  print("Number")
else:
  print("Symbol")
