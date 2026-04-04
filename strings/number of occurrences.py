#write a program to print number of occurrences of each character in the given string

#input:AAAVVVCCC
#output: A-->3,C-->3,V-->3


#user input
str1=input("Enter the string: ")


# we can write this program using list or using set

########## using list  #######


l=[]

#find unique characters in string
for ch in str1:

    #check if the ch is present in given string
    if ch not in l:

        #add ch to the list if not present
        l.append(ch)   # [A,D,V,N]

#find how many times those characters appeared in the string
for ch in sorted(l):
    print("{} character appeared {} times in the given string".format(ch,str1.count(ch)))


#output:
# A character appeared 6 times in the given string
# F character appeared 7 times in the given string
# S character appeared 5 times in the given string