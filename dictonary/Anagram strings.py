#write a program to compare two strings are anagram are not

#two strings are called anagram of both contain same letters, order of letters doesnt matter
#input1:"lazy"
#input2:"zaly"  #anagram strings

#user input
s1="lazy"
s2="zaly"

#core logic

#sort both the string before you compare them
#because if you just compare s1==s2, it will also consider the position of letters
#sorted(s1) --> will give you sorted list of the letters in the string

if sorted(s1)==sorted(s2):
    print("s1 and s2 are anagram strings")

else:
    print("s1 and s2 are not anagram strings")