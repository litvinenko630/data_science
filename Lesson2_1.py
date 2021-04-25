
general_list = [2, "some text", True, set("some_letters"), tuple("this is tuple"), 2.324756,
                frozenset("come on"), dict(country='USA')]
for el in range(len(general_list)):
    print(type(general_list[el]))
