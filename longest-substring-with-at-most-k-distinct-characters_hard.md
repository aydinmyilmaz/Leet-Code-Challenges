
Find the longest substring with k unique characters in a given string

Given a string you need to print longest possible substring that has exactly M unique characters. If there are more than one substring of longest possible length, then print any one of them.
Examples:

"aaaccbb", k = 1
Max substring can be any one from {"aa" , "bb" , "cc"}.

"aabbcc", k = 2
Max substring can be any one from {"aabb" , "bbcc"}.

"aabbcc", k = 3
There are substrings with exactly 3 unique characters
{"aabbcc" , "abbcc" , "aabbc" , "abbc" }
Max is "aabbcc" with length 6.

"aaabbb", k = 3
There are only two unique characters, thus show error message.


```python
s = "aaaccbb"
k = 1

substrlist = []

for idx,item in enumerate(s):
    for i in range(0,len(s)):
        if s[idx:idx+i:] not in substrlist :
            substrlist.append([len(s[idx:idx+i:]),s[idx:idx+i:],len(set(s[idx:idx+i:])) ])


for t in (sorted(substrlist))[::-1]:
    if t[2]<k:
        print("Error")
        break
    elif t[2] == k:
        print("length of longest substring with {} unique element; {} is : {}".format(k,t[1], len(t[1])))
        break
    
        
```

    length of longest substring with 1 unique element; aaa is : 3
    
