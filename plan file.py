step 1: if t = "", return ""
step 2: count the frequency of characters of string t in count_t map as char -> freq,
step 3: start i=0 and track each characetr in string s.  start adding one by one string s characters from index "i" till len(s),
step 3: add first char to window_s -> check if it was also in count_t and if frequency of char in count_t and count_s is equal, increase have by 1.
step 4: check have == need - > if yes, checl length of substring, if its smalled than res_len -> res = [left,  ]
step 4: while count_s == count_t -> find length of substring len = i - left + 1, compare and find minimum with minimum window min_window. and record result [left, i],  start removeing s[left] and left+= 1 until count_t == count_s
step 5: return s[left, i]

2. example: s="ADOBECODEBANC", t = "ABC"
result = [-1, -1],res_len = 0, left = 0, i = 0
count_t = {A:1, B:1, C:1}, count_s = {A:1, D:1, O:1} -> count_t != count_s

step 2:
start i = 3 till 12

left = 0, i = 3 -> count_s = {A:1, D:1, O:1, B:1}, res = [-1,-1], res_len = 0
left = 0, i = 4 -> count_s = {A:1, D:1, O:1, B:1, E:1}, res = [-1,-1], res_len = 0
left = 0, i = 5 -> count_s = {A:1, D:1, O:1, B:1, C:1}, ount_t == count_s -> res = [left,i] = [0, 5], res_len = 6

step 3:
start removing from left index while condition is valid -> left = 1, i = 5 -> count_s = {D:1, O:1, B:1, C:1} -> condition false

step 4: start adding remaing characters -> step 2 ->
left = 1, right =6 -> count_s = {D:1, O:2, B:1, C:1}
left = 1, right =7 -> count_s = {D:2, O:2, B:1, C:1, }
left = 1, right =8 -> count_s = {D:1, O:2, B:1, C:1, E:1}
left = 1, right =9 -> count_s = {D:1, O:2, B:2, C:1, E:1}
left = 1, right =10 -> count_s = {D:1, O:2, B:1, C:1, E:1, A;1} -> count_t == count_s ->res = [left,i] = [1, 11], res_len = 10

step 5:
step 3 -> left =7 , count_ = { O:1, D: 1, E:1, B:1, A:1}

step 6: start adding char again
left =7 , right = 11, count_ = {O:1, D: 1, E:1, B:1, A:1, N:1}
left =7 , right = 12, count_ = {O:1, D: 1, E:1, B:1, A:1, N:1, C:1 } -> count_t == count_s -> remove left

step 7:

left =7 , right = 12, count_ = {O:1, D: 1, E:1, B:1, A:1, N:1, C:1 } => res = s[7:12]
left =8 , right = 12, count_ = {D: 1, E:1, B:1, A:1, N:1, C:1 } => res = s[8:12]
left =9 , right = 12, count_ = { E:1, B:1, A:1, N:1, C:1 } => res = s[9:12]
left =10 , right = 12, count_ = { B:1, A:1, N:1, C:1 } => res = s[10:12] => BANC