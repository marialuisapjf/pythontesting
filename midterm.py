print("Hello world! testing with malu")
## Question 1
a = 16
a = a // 2
print(a**2)
a = a + 11
print(a+1)
a = a - 3

a_squared = a**2
a = a + 11
a_plus_one = a + 1
a = a - 3
print(a)

##Question 2
print((2+3)*6/2 and 18.0)



##Question 3 - pass chat
import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

##Question 4
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

numbers = [
    "7798338247658278460338648728567428338977",
    "4257304920394478392772938744930294037524",
    "0974101607733149676776769413377061014790",
    "2704702208931031198668911301398022074072"
]

non_palindromes = [num for num in numbers if not palindrome(num)]
print(non_palindromes)

##Question 5
def find_pattern_occurrences_corrected(text):
    match_count = 0
    i = 0

# iterate through the text to find occurrences of the pattern
    while i < len(text): #used in class, while , len
#check if the current position is the start of a b...Bob pattern
        if text[i] == 'b' and text[i:].find('Bob') != -1:
            #find the position of 'Bob' starting from the current b
            bob_position = text[i:].find('Bob') + i
            #increment the counter since we found a valid pattern
            match_count += 1
            #move the index to the character after the found Bob to avoid overlapping
            i = bob_position + 3
        else: #used in class
            #move to the next if no pattern starts at the position
            i += 1

    return match_count

#example
text_example = "babcBobbbobbBobbcBob"
find_pattern_occurrences_corrected(text_example)
print(find_pattern_occurrences_corrected(text_example))

##Question 6
#lists - mutable
original_list = [1, 2, 3]
print(original_list)
#changing the list
original_list[1] = 20
print("Changed list:", original_list)
#new element to list
original_list.append(4)
print("List adding an element:", original_list)

#strings - immutable
string = "hello"
print("Original string:", string)
#changing a character
try:
    string[1] = 'a'  # it will give an error
except TypeError as e:
    print("Error:", e)
#creating new string
new_string = string + " world"
print("after addition:", new_string)
print("original string is still unchanged:", string)

##Question 7
import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
#continue
for number in random_numbers[:]:
    if number % 2 == 1:
        random_numbers.remove(number)
    else:
        index = random_numbers.index(number)
        random_numbers[index] = number * 2

print(random_numbers)

##Question 8
def is_valid_url(url):
    if "://" not in url:
        return False
    scheme, rest = url.split("://", 1)
    if scheme not in ["http", "https"]:
        return False
    if '.' not in rest.split('/', 1)[0]:
        return False
    #if all checks passed, the URL has a basic valid format
    return True

#example
test_urls = [
    "https://www.example.com",
    "http://example",
    "ftp://example.com",
    "https://www.example.com/path?query#fragment",
    "example.com"
]

validity_checks = {url: is_valid_url(url) for url in test_urls}
print(validity_checks)

##Question 9
import datetime
def days_since_birthday(birthday_str):
    birthday = datetime.datetime.strptime(birthday_str, "%d-%m-%Y")
    today = datetime.datetime.today()
    total_days = 0
    for year in range(birthday.year + 1, today.year):
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            total_days += 366
        else:
            total_days += 365
    return total_days

example_birthday = "19-03-2004"
days_since_birthday(example_birthday)
print(days_since_birthday(example_birthday))
