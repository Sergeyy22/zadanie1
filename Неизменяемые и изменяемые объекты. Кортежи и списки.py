immutable_var = (("a", 2, 4, 2.3),(12,"asd",11.2))
print(immutable_var)
# Кортежи это неизменяемый спосок (это его особенность от обычного списка)
mutable_list = [21,4,"qq"]
mutable_list.append(12)
mutable_list[0] = 23
print(mutable_list)