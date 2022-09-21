# return reverse of word
def isPalindrome(word):
    return word == word[::-1]

# check if palindrome is palindrome
word = "kajak"
palindrome = isPalindrome(word)

if palindrome:
    print("Yes")
else:
    print("No")