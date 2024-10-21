#string concantation
#combine two strings you can use the operater +

a="ganesh"
b="harish"
c=a+b              #with out space in between names
d=a + " " + b     #with space in between names
print(c)
print(d)

#combaining two strings by using the operater is called concantination

akhil="data_analist"
ganesh="cloud_engeneer"
harish= akhil + "    " + ganesh
print(harish)

#formatted strings (F-strings)===> {} 
#which is introduced in python like 6.6 version and this is now prefered as formating string

age=24
text=f"my name is honey,  i am {age} "
print(text)

price=56
DA=f"the price is {price}"
print(DA)

price=120000
text=f"the price is {price} rupees"
print(text)

#using colon

price=10000
DA=f"the price is {price:.2f} rupees"
print(DA)

#how to calculate string

price=1000
DE=f"the price is {20-5:.2f}rupees"
print(DE)

price=1000
DE=f"the price is {20/5:.2f}rupees"
print(DE)

price=1000
DE=f"the price is {20*5:.2f}rupees"
print(DE)

price=1000
DE=f"the price is {20+5:.2f}rupees"
print(DE)

price=45
mohan=f"the price is {price}dollers"
print(mohan)

price=10
venkatesh=f"the price is {price}bath"
print(venkatesh)

age=23
gani=f"my age is {age}years old"
print(gani)

#string methods

#capitalize()
#casefold()
#count()

vishwanath="data_analyst"
print(vishwanath.capitalize())

vishwanath="Data_Analyst"
print(vishwanath.casefold())