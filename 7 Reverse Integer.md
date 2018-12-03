
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit 
signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function 
returns 0 when the reversed integer overflows.




```python
x = int(str(x)[::-1]) if x >= 0 else - int(str(-x)[::-1])
if  -2147483648 < x <= 2147483647: 
    print (x )
else:
    print (0)
```

    -123
    
