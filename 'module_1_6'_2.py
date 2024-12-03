my_dict={'Иван':2010,'Алексей':2014}
my_dict['Иван']=2009
my_dict['Антон']=1980
print(my_dict)
print(my_dict.get('Иван'))
print(my_dict.get('Юра'))
my_dict.update({'Александр':2111,
                'Николай':1999})
print(my_dict)
del my_dict['Александр']
print(my_dict)



my_set = {5,6,7,5,6,7,8,9,'яблоки','бананы',}
print(set(my_set))
my_set.update({'ручки','тетради',})
print(my_set)
my_set.remove('бананы')
print(my_set)