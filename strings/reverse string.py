# Write a program to reverse the content of the given string

######## Option 1: using slice operator  ##########

s="Python is"
reversed_string=s[::-1]  # +1 --> start to end , -1 --> end to start
print(reversed_string)   # nohtyP



####### Option 2: Using reversed() method  #########

s="software engineer"

reversed_string = reversed(s)
output = "".join(reversed_string)  # we need to join it with ""

print(output)


########  Option 3: using while loop  #########

s="python"
output=""
i=len(s)-1  # len-1 so we can start from index of last character


while i>=0:         # start from last go till first character
    output+=s[i]
    i-=1

print(output)  # nohtyp