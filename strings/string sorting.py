# write a program to sort the characters of the string, first alphabet symbols and then numbers

#input: A2B3C1  --> output: ABC123

##### failed try  ###

s1='A2B3C1'
print(sorted(s1))

#Note: sorted() function always returns numbers first and then alphabets and its return type is list

##### worked  #####

#user input
s1=input("Enter the string: ")

#sort the string

alphabets=[]
num=[]

for ch in s1:
    #check if ch is alpha
    if ch.isalpha():
        alphabets.append(ch)  # alphabets[B,A,C] --> unsorted

    else:
        num.append(ch)         # num[2,3,1] --> unsorted

    # sort the list individually
    output=sorted(alphabets)+sorted(num)

#print the output
print("".join(output))