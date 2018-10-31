
# coding: utf-8

# Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
# 
# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
# 
# Example 1: Input: [4,2,3] Output: True Explanation: You could modify the first 4 to 1 to get a non-decreasing array. Example 2: Input: [4,2,1] Output: False Explanation: You can't get a non-decreasing array by modify at most one element. Note: The n belongs to [1, 10,000].

# In[8]:


nums=[3,3,2,2]

nums2=nums

sayac=0

value=True


for i in range(0, len(nums)-1):
    
    for ii in range (i+1,len(nums)): 
        
        if nums[i]>nums2[ii] and nums[i]!=nums[i+1]:
            
            sayac+=1
            print(sayac,nums[i]," sayısı", nums2[ii], " den büyük olduğundan sayaç -1- arttırıldı ve sonraki sayı olan",nums[i+1],  "- e gecildi")
            break
        else:
            continue
    

if sayac>=2:
    
    value=False
    
print(value)           

