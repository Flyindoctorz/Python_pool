

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "tata!"}

ft_list[1] = "World!"
ft_tuple = ("Hello", "France!")
ft_set.discard('tutu!')
ft_set.add('Paris!') #set are not ordered, the 2 elements must just be present regardless of their position
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)