
315. Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.


```python
nums = [5,2,6,1]

output = [] 

for i, num in enumerate(nums):
    
    count = 0
    
    for j in range(i+1,len(nums)):
                       
        if num > nums[j]:
            
            count +=1

    output.append(count)
    
output
```




    [2, 1, 1, 0]




```python
import numpy as np

nums = [5,2,6,1]

x = np.array(nums)

[len(x[i+1::][x[i+1::]<num] ) for i, num in enumerate(x)]
```




    [2, 1, 1, 0]


