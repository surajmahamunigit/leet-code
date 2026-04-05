# input: AAABCCA
# output: 4A1B2C

#user input
s1="AAABCCA"

#core logic

output={}

#trace each character of the string
for ch in s1:

    #if not present in dictionary, then return value 0 and add 1 to it.
    #if present, then retrieve and add 1 to the value
    output[ch] = output.get(ch,0) + 1

#print output
count_str=''
for k,v in output.items():
    count_str=count_str + str(v) + k

print(count_str)