#write a program to count number of times each ovel occurred how many times in the given string

#input:"Apple Tree"
#output:
#A occurred 1 times
#e occurred 3 times    sorted

#user input:
s1="Apple Tree is tall"

#core logic:

d={}  #dictionary
s={'a','e','i','o','u','A','E','I','O','U'}

#trace over each ch in s1

for ch in s1:

    #check if ch is in set s. if present then only add it to the dict
    if ch in s:
        d[ch]= d.get(ch,0) + 1

#print the output

for k,v in sorted(d.items()):
    print("{} occured {} times".format(k,v))


#output:
# A occured 1 times
# a occured 1 times
# e occured 3 times
# i occured 1 times