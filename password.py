import random
chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789&*_@$'
totalPassword=input("Enter the total number of Passwords required:")
length=input("Enter the size of Passwords:")
i=1
while totalPassword!=0 :
	password=''
	store=length
	while store!=0 :
		password=password+random.choice(chars)
		store=store-1;
	print("Password {0}  : {1}".format(i,password))
	i=i+1
	totalPassword=totalPassword-1
if length<8:
	print("WEAK PASSWORD!")
elif length<12:
	print("GOOD PASSWORD!")
else : 
	print("STRONG PASSWORD!")