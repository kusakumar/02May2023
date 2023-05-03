"""
String capitalize() method returns a copy of the original string and converts the first character of the string to a capital (uppercase) letter,
while making all other characters in the string lowercase letters
Syntax: string_name.capitalize()
Parameter:  The capitalize() function does not takes any parameter.
Return: The capitalize() function returns a string with the first character in the capital.

"""
###capitalize() and swapcase() -> Lower case becomes uppercase and viceversa
####swapcase() method does not take any parameter.
string="all roses are in red colour. few roses are white too"
print("Orginal string is :",string)
print(string.capitalize())
print(string.swapcase())
print()

####Join()->Joins the elements of an iterable to the end of the string
"""
This function joins elements of a sequence and makes it a string. 
Syntax: string_name.join(iterable) 
Parameters: 
Iterable – objects capable of returning their members one at a time. Some examples are List, Tuple, String, Dictionary, and Set
Return Value: The join() method returns a string concatenated with the elements of iterable. 
"""
# Joining with empty separator
list1=['1','2','3','4']
print("".join(list1))

# Joining with string
string = "Hello ! kusakumar, How are doing"
print("#".join(string))
print()

a ="-"
print(a.join("123"))

print()
a="Hello Python"
a="**"
print(a.join("Hello Python"))

# elements in tuples
tple= ("Hello", "!" ,"kusakumar,", "How", "are", "doing")
print("_".join(tple))


# elements in list
list = ['1', '2', '3', '4', '4']
s = "$"
s2 = "-#-"
print(s.join(list))
print(s2.join(list))
print(s.join(list1))
print()
print(s.join(tple))

# elements in dictionary
disc={"God": 1, "appears": 2, "everywhere": 3}
string = '_'.join(disc)
print(string)
print()


#### "count()"
"""
count() function is an inbuilt function in python programming language that returns the number of occurrences of a substring in the given string.
Syntax: 
string.count(substring, start=…, end=…)
Parameters: The count() function has one compulsory and two optional parameters. 
Mandatory parameter: 
substring – string whose count is to be found.
Optional Parameters: 
start (Optional) – starting index within the string where the search starts. 
end (Optional) – ending index within the string where the search ends.
Return Value: count() method returns an integer that denotes number of times a substring occurs in a given string. 
"""
string = "Hello ! kusakumar, How are doing and How do you do"
tple= ("Hello", "!" ,"kusa","kumar,", "How", "are", "doing")

# count() method without optional parameters

# counts the number of times substring occurs in
# the given string and returns an integer
print(string.count("H"))
print(string.count("o"))
print(string.count("k"))
print(string.count("a"))
print(string.count("u"))
print(string.count("are"))
print(string.count("P"))
print()
print(tple.count("Hello"))
print(tple.count("o"))
print(tple.count("kusa"))
print(tple.count("a"))
print(tple.count("u"))
print(tple.count("are"))
print(tple.count("P"))
print()
# count() method  using optional parameters
# counts the number of times substring occurs in
# the given string between index 0 and 5 and returns an integer
print(string.count("Hello", 0, 5))
print(string.count("How", 0, 40))
print()

###index()
"""
find() method returns the lowest index or first occurrence of the substring if it is found in a given string.
If it is not found, then it returns -1.

Syntax: str_obj.find(sub, start, end)
Parameters:
sub: Substring that needs to be searched in the given string.
start (optional): Starting position where the substring needs to be checked within the string.
end (optional): End position is the index of the last value for the specified range. It is excluded while checking.
Return:  Returns the lowest index of the substring if it is found in a given string. If it’s not found then it returns -1.

"""

a = "Hello Python"
string = "How Hello ! kusakumar, How are doing"
s = 'Machine Learning'
print(a.find("P"))
print(a.find("Python"))
print(string.find("are"))
print(string.find("How"))
print(string.find("how"))
print(s.find("L"))
print()
idx = s.find('a')
print(idx)
print(s[idx:])

idx = s.find('a', 2)
print(idx)  # 10
print(s[idx:])  # 'arning'


word = 'geeks for geeks'
print()
# Substring is searched in 'eks for geeks'
print(word.find('ge', 2))

# Substring is searched in 'eks for geeks'
print(word.find('geeks', 2))

# Substring is searched in 's for g'
print(word.find('g', 4, 10))

# Substring is searched in 's for g'
print(word.find('for ', 4, 11))
print()
# How to use find()
if string.find('kusa') != -1:
    print("Contains given substring ")
else:
    print("Doesn't contains given substring")

###find() method is similar to index(). The only difference is find() returns -1
###if the searched string is not found and index() throws an exception in this case.
##index() Method allows a user to find the index of the first occurrence of an existing substring inside a given string.
string = 'random'
print("index of 'and' in string:", string.index('and'))
test_string = "1234gfg4321"
print(test_string.index('gfg', 4, 8))
print(test_string.index("21", 8, len(test_string)))
print(test_string.index("32", 5, -1))
#print(string.index("punnana"))  ###throws error

#####rfind()
###rfind() method returns the rightmost index of the substring if found in the given string. If not found then it returns -1
print()
string = "How Hello ! kusakumar, How are doing"
print(string.rfind("How"))
print(idx)
print(word.rfind('for ', 4, 11))
print(word.rfind('ge', 2))
print(word.rfind('geeks', 2))
print(word.rfind('geeks ', 2))
# finding substring using -ve indexing
print(word.rfind('geeks', -5))
print()
mystr = "Hello-Python"
print(mystr.rfind("P"))
print(mystr.rfind("-"))
print(mystr.rfind("z"))
print()

####rindex() method returns the highest index of the substring inside the string if the substring is found.
# Otherwise, it raises ValueError.
print(word.rindex('geeks'))
string = "101001010"
print(string.rindex('101', 2))
mystr="ring ring bell"
print(mystr.rindex("ring", 0, 4))
print(mystr.rindex("ring", 0, -5))