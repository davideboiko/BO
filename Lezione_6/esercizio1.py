"""""
8-1
"""""
def display_message():
    print("Ma io che c ne so")
display_message()
"""""
8-2
"""""
def favorite_book(title:str):
    print(f"One of my favorite books is {title}.")
favorite_book("Alice in Wonderland")

"""""
8-3
"""""
def make_shirt(size:str, message:str):
    print(f"The shirt size: {size} and it has the message: '{message}'")

make_shirt("Large", "buuuuuuuuuuu")

make_shirt(size="Medium", message="Boooooooooo")
"""""
8-4
"""""
def make_shirt(size:str="Large", message:str="I love Python"):
    print(f"The shirt size: {size} and it has the message: '{message}'")

# Making a large shirt with the default message
make_shirt()

# Making a medium shirt with the default message
make_shirt(size="Medium")

# Making a shirt of any size (small) with a custom message
make_shirt(size="Small", message="Code is Life!")
"""""
8-5
"""""
def describe_city(name:str, country:str="Iceland"):
    print(f"{name} is in {country}")

# Call the function for three different cities

describe_city(name="Reykjavik")  # Uses the default country
describe_city(name="Akureyri")   # Uses the default country
describe_city(name="Tokyo", country="Japan")   # Overrides the default country
"""""
8-6
"""""
def describe_city(name:str="Santiago", country:str="Chie"):
    print(f"{name},{country}")

# Call the function for three different cities

describe_city(name="Reykjavik")  # Uses the default country
describe_city(name="Akureyri")   # Uses the default country
describe_city(name="Tokyo", country="Japan")   # Overrides the default country


"""""
8-15
"""""

