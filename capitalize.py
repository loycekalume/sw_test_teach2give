
'''
5. Write a program that accepts a string as input, capitalizes the first letter of each
word in the string, and then returns the result string.
Examples:
"hi"=> returns "Hi"
"i love programming"=> returns "I Love Programming"
'''

def capitalize_word(input_string):
    return input_string.title()

my_input = input("Enter a word:")
result = capitalize_word(my_input)
print(result)













