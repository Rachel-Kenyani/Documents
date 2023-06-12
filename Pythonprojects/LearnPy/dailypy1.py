#Write a function that takes two numbers as input and returns their sum.
def sum(num1,num2):
    add=num1+num2 
    return add
print("Q1",sum(2,1))    

#Write a function that takes a string as input and returns the length of the string.
def length(str):
    return len(str)
print("Q2",length("Rachel"))

#Write a function that takes a list of numbers as input and returns the average of the numbers.
def average(nums):
    sum=0
    for i in nums:
        sum+=i
    print("Q3",sum/len(nums))
average([2,1,3,4])

#Write a function that takes a string as input and returns True if the string is a palindrome, 
# and False otherwise.
def word(strg):
    reversed(strg)
    if strg==strg[::-1]:
        return True
    else:
        return False
print("Q4",word("Mahalia"))
print("Q5",word("civic"))

#Write a function that takes a list of numbers as input and returns the maximum number in the list.

def area_codes(numbers):
    largest=numbers[0]
    for n in numbers:
        if(n>largest):
            largest=n
    return largest
numbers=[2,54,68,6,27]
print("Q5",area_codes(numbers))

#Write a function that takes a list of numbers as input and returns the minimum number in the list.
def ages(digits):
    smallest=digits[0]
    for d in digits:
        if d<smallest:
            smallest=d
    return smallest
digits=[34,12,22,90]
print("Q6",ages(digits))

#Write a function that takes a list of strings as input and returns the longest string in the list.
def music(instruments):
    longest=instruments[0]
    for i in instruments:
        if len(i)>len(longest):
            longest=i
    return longest
instruments=["harp","guitar","piano","saxophone"]
print("Q7",music(instruments))

#Write a function that takes a list of strings as input and returns the shortest string in the list.
def shoes(brands):
    shortest=brands[0]
    new=[]
    for b in brands:
        if len(b)<len(shortest):
            shortest=b
    return shortest
brands=["Filaa","Puuuuma","Adidas","Nike"]
print("Q8",shoes(brands))

#Write a function that takes a string as input and returns a new string with all vowels removed.
def person(name):
    name.lower()  
    vowels="a,e,i,o,u"
    empty=""
    for n in name:
        if n not in vowels:
            empty+=n
    return empty  
print("Q9",person("Imali"))
    
#Write a function that takes a list of numbers as input and 
# returns a new list with all even numbers removed.
def even_numbers(fruits):
    new_fruits=[]
    for f in fruits:
        if f%2!=0:
            new_fruits.append(f)
    return new_fruits
fruits=[20,17,89,36,33]
print("Q10",even_numbers(fruits))
# Write a function that takes a list of strings as input and
# returns a new list with all strings that contain the letter 'a' removed.
def remove_letter(tools):
    new_tools=[]
    letter='a'
    for t in tools:
        if letter not in t:
            new_tools.append(t)
    return new_tools
tools=["panga","fork","rake","spade"]
print("Q11",remove_letter(tools))


#Write a function that takes a list of numbers as input 
#and returns a new list with all duplicate numbers removed.

#method 1...........using set
nums=[2,7,9,7,10,2]
b=set(nums)
print("Q12",b)
nums=list(b)
print("Q12",nums)

# #with function.....using set
# numbers=[2,7,9,7,10,2]
# def digits(num):
#     return list(set(num))
# print(digits(numbers))

#Given the variables name and age, how can you format a string to print "My name is John and I am 30 years old."?
def person(name,age):
    data=f'My name is {name} and I am {age} years old'
    return data
print("Q13",person("Mia",20))

#Given the variables num1, num2, and result, how can you format a string to print "The result of adding 5 and 10 is 15."?
def ages(num1,num2):
    result=num1+num2
    return f'The result of adding {num1} and {num2} is {result}.'
print("Q14",ages(2,1))

#Given the variable pi, how can you format a string to print "The value of pi is 3.14159."?
def math():
    pi=3.14159
    return f'The value of pi is {pi}'
print("Q15",math())

#Given the variables item and price, how can you format a string to print "The price of a banana is $0.99."?
def grocery(item,price):
    return f'The price of a {item} is {price}'
print("Q16",grocery("banana","0.99"))

#Given the variables first_name, last_name, and city, how can you format a string to 
# print "My name is John Smith and I live in New York City."?
def details(first_name,last_name,city):
    return f'My name is {first_name} {last_name} and I live in {city} City.'
print("Q17",details("John","Smith","New York"))

#Given the variable date, which is in the format YYYY-MM-DD,
# how can you format a string to print "Today's date is 12/31/2022."?
def date(year,month,day):
    if len(year)==4 and len(month)==2 and len(day)==2:
        return f"Today's date is {month}/{day}/{year}."
print("Q18",date("2023","04","22"))


#Given the variable sentence, how can you format a string to print
# "The quick brown fox jumped over the lazy dog." with the first letter of each word capitalized?
def title_case(strg):
    return strg.title()
print("Q19",title_case("The quick brown fox jumped over the lazy dog." ))


# Create a variable name and assign it the value "John". Print out the value of the variable.
name="John"
print("Q20",name)


# Create a variable age and assign it the value 30.
# Convert the value to a string and concatenate it with the string " years old". Print out the resulting string.
def info(age):
   convert=str(age)
   return f'{convert} years old'
print("Q21",info(30))


# Create a variable sentence and assign it the value "The quick brown fox jumps over the lazy dog".
# Convert the string to all uppercase letters and print out the resulting string.
def capitalise(str):
    return str.upper()
print("Q22",capitalise("The quick brown fox jumps over the lazy dog"))


# Create a variable sentence and assign it the value "The quick brown fox jumps over the lazy dog".
# Convert the string to all lowercase letters and print out the resulting string.
def decapitalise(str):
    return str.lower()
print("Q23",decapitalise("The quick brown fox jumps over the lazy dog"))


# Create a variable sentence and assign it the value "The quick brown fox jumps over the lazy dog".
# Use string slicing to print out the word "brown" from the string.
def find_word(string):
    string2=string.lower()
    return [word for word in string2.split() if "brown" in word]
print("Q24",find_word("The quick brown fox jumps over the lazy dog"))


# Create a variable sentence and assign it the value "The quick brown fox jumps over the lazy dog".
# Use string slicing to print out the word "lazy" from the string.
def search_word(string):
    length = len(string)
    for i in range(length - 3):  # loop over all substrings of length 4 in the string
        if string[i:i+4] == "lazy":  # check if the current substring is "lazy"
            print("Q25","lazy")
            return  # exit the function after the first occurrence of "lazy" is found
    print("Q25","No lazy word found")  # print this if "lazy" is not found in any of the substrings
search_word("The quick brown fox jumps over the lazy dog")


# Create a variable sentence and assign it the value "The quick brown fox jumps over the lazy dog".
#  Use the split() method to split the string into a list of words. Print out the resulting list.


# Create a variable sentence and assign it the value "The quick brown fox jumps over the lazy dog".
#  Use the replace() method to replace the word "lazy" with the word "sleepy". Print out the resulting string.

# Create a variable word and assign it the value "racecar". Use string slicing to print out the word in reverse order.
# Create a variable sentence and assign it the value "The quick brown fox jumps over the lazy dog". Use string concatenation to add the string " and the hare" to the end of the sentence. Print out the resulting string.
# 1:53
# Given the variables name = "John" and age = 30, how can you format a string to say "My name is John and I am 30 years old"?
# Given the variables price = 49.99 and discount = 0.15, how can you format a string to say "The price after a 15% discount is $42.49"?
# Given the variables num1 = 10 and num2 = 5, how can you format a string to say "10 divided by 5 is 2"?
# Given the variables first_name = "John" and last_name = "Doe", how can you format a string to say "Doe, John"?
# Given the variables num1 = 10 and num2 = 3, how can you format a string to say "10 divided by 3 is 3.33"?
# Given the variables product = "apple" and price = 0.99, how can you format a string to say "The price of an apple is $0.99"?
# Given the variables hours = 5 and rate = 10.5, how can you format a string to say "You worked 5 hours at a rate of $10.50 per hour, and earned $52.50"?

# Given the variables num1 = 10 and num2 = 3, how can you format a string to say "10 divided by 3 is 3 with a remainder of 1"?
# Given the variables first_name = "John" and last_name = "Doe", how can you format a string to say "Hello, John Doe"




#Given the variable num, how can you format a string to print
#  "The number is 5." with a minimum field width of 10 characters?
num1=10
num2=3
result=10/3
solution=f"The result of dividing {num1} by {num2} is {result:.2f}"
print(solution)

#Given the variable num, how can you format a string to print
#"The number is 5.00." with a precision of 2 decimal places?
num=5
wording=f"The number is {num:>{10}}" #Here, the > character is used to right-align the string
#and the 10 specifies the minimum field width of the string to be 10
print(wording)


#Given the variables num1, num2, and result, how can you format a string to print
#"The result of dividing 10 by 3 is 3.33." with a precision of 2 decimal places?

num=5.00
value=f"The number is {num:.2f}"
print(value)







