#write a program to check if the give string is palindrome or not

#inpt:"eye"
#output:"eye"

#user input
s1="apple"

#core logic

#compare it with its mirror image
if s1 == s1[::-1]:
    print("String is palindrome")

else:
    print("String is not palindrome")