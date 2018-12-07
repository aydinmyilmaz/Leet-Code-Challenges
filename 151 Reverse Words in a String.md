

Given an input string, reverse the string word by word.

Example:  

Input: "the sky is blue",
Output: "blue is sky the".
Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.



```python
s = "the sky is blue"
        
" ".join(([item for item in s.split() if item != ""])[::-1])
```




    'blue is sky the'


