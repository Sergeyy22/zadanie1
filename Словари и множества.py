my_dict = {"Имя":"Сергей", 'Город':"Новосибирск","Возраст":"22"}
print(my_dict)
print(my_dict["Имя"])
print(my_dict.get("Рост"))
my_dict.update({"Дата рождениия":27.09,"Год рождения": 2001})
print(my_dict)
del my_dict["Возраст"]
print(my_dict)
my_set ={2, 3, 1, 2, 31, 21, 1, "MIR",2.9}
print(my_set)
my_set.add('mir')
my_set.add(12.2)
my_set.discard("MIR")
print(my_set)