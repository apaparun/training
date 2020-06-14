#get a list of name and make them title caps and print the list using python
inpt=input()
strn=inpt.split()
out =list( map(lambda x:x.title(), strn) )
print(out) 
