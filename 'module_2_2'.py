a=456
b=456
c=456
#numbers = int(input("Ввести число"))  #first,second,third
if (a==b==c):
    print(3)
elif ((a==b)or(a==c)or(b==c)):
    print(2)
elif ((a!=b)and(b!=c)and(c!=a)):
    print(0)
