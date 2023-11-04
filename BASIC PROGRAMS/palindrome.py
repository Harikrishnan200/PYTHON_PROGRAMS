def isPalindrome(str):
    return str == str[::-1]
 
 

str = input("Enter the string:")
ans = isPalindrome(str)
 
if ans:
    print("The string is palindrome")
else:
    print("The string is not palindrome")


#output

#Enter the string:malayalam
#The string is palindrome