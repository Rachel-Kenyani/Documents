# Positional arguments

def addition(age,town):
    print(f"{town} town is {age} years old.")
addition(50,"Mombasa")


# Keyword arguments

#A function that can accept any number of positional arguments

def study(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
study(name="Alice",friend="Mia",age=25, city="Paris") 


# Default arguments

def greet(greeting, name="world"):
    print(greeting, name)

greet("Hello") # prints "Hello world"

def my_country(country="Kenya"):
    print(f"Hello my country is {country}")
my_country()


# def max_sum(ages):
#     ages2=sorted(ages)
#     sum=ages2[-1]+ages2[-2]
#     return sum
# print(max_sum([1,2,3,4,5]))

# def max_sum(ages):
#     maximum=current=ages[0]
#     for a in (1,len(ages)):
#         current=max(ages[a],current +ages[a])
#         maximum=max(maximum,current)
#     return maximum
# print(max_sum([1,2,3,4,5]))

def grammar(words):
    sorted_word=sorted(words,reverse=True)
    return sorted_word
print(grammar(["mable","apple","dance"]))
