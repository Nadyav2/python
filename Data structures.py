# list data structure
my_list = ["Bmw", "Subaru", "Porsche", "Range Rover", "Mercedes benz", "Audi"]
my_list.append("Mazda")
print(my_list)
print(my_list[0])
print(my_list[0],"is manufactured in Germany")

my_list[0]="Bentley"

my_list = ["1", "4", "11", "6"]
my_list.insert(1, "21")
print(my_list)

print(type(my_list))

# tuple data structure
my_tuple=("Mango", "Apple", "Pineapple", "Kiwi")
print(my_tuple)
print(f"I love the taste of this {my_tuple[1]}")
# set data structure
my_set={"purple", "red", "grey", "green"}
print(my_set)

# dictionary data structure
my_dictionary={"name": "Hassan", "age": "18", "gender": "female", "height": "5'7"}
print(my_dictionary)
print(my_dictionary["gender"])
print(f"My name is Nadya and I'm 18 years old{my_dictionary}")

the_dictionary={"Style": "Streetwear","Position":"Ambassador"}
print(the_dictionary)
print(the_dictionary["Position"])
print(f"I love dressing up in Fenty{the_dictionary}")