
#1. what is string concantation?
# Ans> string concantation is the processs of joining two or more strings together to form a single strring

#2. how string concantation wworks ?
# Ans> in python you can concattenate strings using the ( + )operator

#3. what are format strings?
# Ans> format string is also called as f-string which is introducess in python 
#      like 6.6 version & this is preffered as formatting string

#4. give as example for formated string?
#Anns>     age=24
#          text=f"my name is honey,  i am {age} "
#          print(text)

#5. whaat is colon and why it is used in Python?
#Ans> ( : )it is a versatile symbol used in many programming languages and contexts
#      the colon used in python because to slice listss,tuples and strings to extract a portion of the sequence.
# ex:  price=10000
#      DA=f"the price is {price:.2f} rupees"
#      print(DA)

#6. dout reffers to?
#Ans> doubt(.) reffers to 2 decimal number after value


#string concantation
#combine two strings you can use the operater +

a="ganesh"
b="harish"
c=a+b              #with out space in between names
d=a + " " + b     #with space in between names
print(c)
print(d)

#combaining two strings by using the operater is called concantination

harish="data_analist"
ganesh="cloud_engeneer"
harish= harish + "    " + ganesh
print(harish)

#formatted strings (F-strings)===> {} 
#which is introduced in python like 6.6 version and this is now prefered as formating string

age=24
text=f"my name is honey,  i am {age} "
print(text)

price=50
DA=f"the price is {price}"
print(DA)

price=100
text=f"the price is {price} rupees"
print(text)

#using colon

price=100
DA=f"the price is {price:.2f} rupees"
print(DA)

#how to calculate string

price=1000
DE=f"the price is {20-5:.2f}rupees"
print(DE)

#string methods

#capitalize()
#casefold()
#count()

ganesh="data_analyst"
print(ganesh.capitalize())

harish="Data_Analyst"
print(harish.casefold())