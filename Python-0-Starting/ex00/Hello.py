ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World"
lstTup = list(ft_tuple)
lstTup[1] = "Lebanon"
ft_tuple = tuple(lstTup)
ft_set.remove("tutu!")
ft_set.add("Beirut")
ft_dict["Hello"] = "42Beirut" 

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)