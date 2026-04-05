#input: AAABBBBZZZDD
#output: A3B4D2Z3   sorted

#user input
s1="AAABBBBZZZDD"

#core logic

d={}  #dictionary
#trace over each character in s string
for ch in s1:

    #add the ch to dictionary if not present with value 1
    #if already present, then retrieve the value and add 1 to it.

        d[ch]= d.get(ch,0) + 1

#sort the dictionary before printing the output

output=''
for k,v in sorted(d.items()):
    output= output + k +str(v)

print("output: ",output)  #output:  A3B4D2Z3