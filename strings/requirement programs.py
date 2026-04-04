######## Requirement 1  #############

# input: a4b2c5
# output: aaaabbccccc

#read the user input
str1=input("Enter a string letter followed by digit: ")

#access each character in str
output=""

for ch in str1:
    #if alpha, then save it in variable x
    if ch.isalpha():
        x=ch

    #if not alpha. then multiply ch by next digit, but every ch in str is string
    #we cant multiply string by string
    else:
        #converting ch into digit
        dig=int(ch)
        output=output+dig*x

print(output)


##################### Requirement 2  ##################

#input: a2z4b2
#output: aabbzzzz


#reading user input
str1=input("Enter the input string in alpha+num form eg. a2m3b4: ")

#reading each character of string
target=""

for ch in str1:
     #check if ch is alpha
     if ch.isalpha():
         x=ch

     #if not alpha, then conver next ch into int for multiplication
     else:
         #converting
         digi=int(ch)
         target=target+(x*digi)   # aammmbb

#sort the output
output=''.join(sorted(target))

#print output
print("The output is: ",output)  # aabbmmm


############ Requirement 3  ################

#input:aaabbbbccccc
#output:3a4b5c

#user input
str3=input("Enter the string eg. aaaaaabbbccccccdddddd: ")

#core logic:
output=''

previous=str3[1]
previous_count=1

next_index=1

#compare ch at index 0 with ch at index 1 and afterwards
while next_index<len(str3):
    #previous and next characters are same
    if str3[next_index]==previous:
        previous_count=previous_count+1

    #previous and next character is not same
    else:
        output = output + str(previous_count) + previous
        previous=str3[next_index]
        previous_count=1

        #in this block we will have previous and str3[next_index] is always different

    #if next_index is last character
    if next_index==len(str3)-1:
        output = output + str(previous_count) + previous

    next_index=next_index+1

#print output
print(output)


################  Requirement 4  #########3

#input:a1s2n2
#output:absunp

str4=input("Enter the input string in alpha+num form eg. a2m3b4: ")

#core logic
output=''

for ch in str4:
    #if ch is alpha
    if ch.isalpha():
        x=ch
        output=output+ch

    #if ch is number
    else:
        output = output + chr( ord(x) + int(ch) )

#print output
print(output)





