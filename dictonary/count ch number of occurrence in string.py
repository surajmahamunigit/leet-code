# write a program to count number of occurrences of character in the given string
#without using count()

# we will be using dictionary for this

#user input
s1="AAACCDDAVV"

#core logic
output={}

#trace each character of the given string
for ch in s1:

    #if not present in dictionary --> add the ch to the dictionary as key and 1 as value
    #if present, retrieve the item and add 1 to value
    output[ch]= output.get(ch,0)+1

#print output
for k,v in output.items():
    print(k,v)
