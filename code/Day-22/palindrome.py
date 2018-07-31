str=input("Enter any string:")
# make it suitable for caseless comparison
str=str.casefold()
# reverse the string
rev_str = reversed(str)
# check if the string is equal to its reverse
if list(str) == list(rev_str):
   print("It is Palindrome")
else:
   print("It is not Palindrome")
