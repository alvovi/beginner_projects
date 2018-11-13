string = str(input("Please enter a word: "))
string_reverse = string[:: -1]

print(string)
print(string_reverse)

if string.lower() == string_reverse.lower():
    print("This word is a palindrome.")
else:
    print("This word is not a palindrome.")
