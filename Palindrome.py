line = input("Enter a string to check palindrome.").replace(" ","").lower()
reversed_line = line[::-1]
# reverse = "".join(reversed(line))
if line == reversed_line:
    print("Palindrome string")
else:
    print("Not a palindrome string")