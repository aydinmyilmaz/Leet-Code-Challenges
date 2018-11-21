
# coding: utf-8

# In[ ]:



Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0


# In[23]:


A = [ 1, 2,3,-4,5,6 ]
B = [-2,-1,0,3,-2]
C = [-1, 2,0,-5,6,4]
D = [ 0, 2,3,5,-5]
counter = 0

for i in  A:
    for j in B:
        for k in C:
            for l in D:
                if i+j+k+l == 0 :
                    counter+=1
                    #print("A[{}] + B[{}] + C[{}]+ D[{}] = 0" .format(i,j,k,l) )
print(counter)


# In[21]:


ab = {}
for i in A:
    for j in B:
        ab[i+j] = ab.get(i+j, 0) + 1
        
ans = 0
for i in C:
    for j in D:
        ans += ab.get(-i-j, 0)       
print (ans)

