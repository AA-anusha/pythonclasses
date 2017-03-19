names = ['anusha' , 'ayush' , 'purnima' ,'sonima']
names[0] = "Foo Bar"
print("Names now:",names)
names.append("Neekita Pudasaini")
names.append("Aayush Thapa")
print("Names finally:", names)
print("Last name in the list: %s" % names [-1])
joined_names = "\n".join(names)
print("\n list of names:")
print(joined_names)