#input1: "cat"
#input2:"dog"
#input3:"mouse"

#output:
# cdr
# aoo
# tgu
# s
# e

# cdr, aoo, tgu, s, e

#user input
s1="cat"
s2="dog"
s3="mouse"

#core logic

#indexes for s1,s2,s3
i,j,k=0,0,0

#while any index is less than len(s)
while i<len(s1) or j<len(s2) or k<len(s3):

    output=""

    # check if i < len(s1)
    if i<len(s1):
        output=output+s1[i]
        i=i+1

    # check if j<len(s2)
    if j<len(s2):
        output=output+s2[j]
        j=j+1

    #check if k < len(s3)
    if k<len(s3):
        output=output+s3[k]
        k=k+1

    print(output)

#output:
# cdm
# aoo
# tgu
# s
# e