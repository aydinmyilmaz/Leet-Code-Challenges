
# coding: utf-8

# 890. Find and Replace Pattern
# 
# You have a list of words and a pattern, and you want to know which words in words matches the pattern.
# 
# A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.
# 
# (Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)
# 
# Return a list of the words in words that match the given pattern. 
# 
# You may return the answer in any order.
# 
#  
# 
# Example 1:
# 
# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
# since a and b map to the same letter.

# In[51]:


words = ["abc","deq","mee","aqq","dkd","ccc"]

pattern = "abb"

master_pattern = [[index,pattern.index(item)]for index,item in enumerate(pattern)]

print(master_pattern)

patternList=[]
for word in words:
    
    each_pattern = [[index,word.index(item) ]for index,item in enumerate(word)]
    patternList.append(each_pattern)
    
print(master_pattern)
print(patternList)

[words[idx] for idx,item in enumerate(patternList) if item  == master_pattern]


# In[56]:


words = ["abc","deq","mee","aqq","dkd","ccc"]

pattern = "abb"

master_pattern = [[index,pattern.index(item)]for index,item in enumerate(pattern)]

patternList=[]

for idx,word in enumerate( words):
    
    each_pattern = [[index,word.index(item) ]for index,item in enumerate(word)]
   
    if each_pattern == master_pattern :
        
        patternList.append(words[idx])

print(patternList)


