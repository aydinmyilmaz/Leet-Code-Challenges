
# coding: utf-8

# In[ ]:



Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Output: ["eat","oath"]


# In[4]:


def findWords(board, words):
       

    # verilen sözcüklerdeki harflerin() board daki konumlarının bulunarak dict e yazılması
    my_dict = {}
    for i,item in enumerate(board):
        for j, let in enumerate(item):
            if let in my_dict.keys():
                my_dict[let].append((i,j))
                continue
            else:
                my_dict[let]=[]
                my_dict[let].append((i,j))    

    # Ust satırda tespit edilip my_dict'e yazılan harf konumlarından sözcük içindeki harflerin olası konumlarının tespit edilmesi

    nd={}
    for item in words : 
        nd[item] = []
        for l in item :
            if l in my_dict:
                nd[item].append(my_dict[l])
            else:
                break

    # üst satırda bulunan "sözcük içindeki harflerin olası noktaları arasından birbirine bitişik olan harf konumlarının 
    # birbirini takip eden 2li konumlar şeklinde çıkarılması

    poz_dict = {}
    for key,value in nd.items():   
        poz_list = []
        for i,item in enumerate(value):
            for a,b in item:
                ch=[]
                u = (a-1,b)
                lw = (a+1,b)
                lf = (a,b-1)
                rh = (a,b+1)
                ch = [u,lw,lf,rh]         
                try:
                    for item in value[i+1] :
                        if item in ch:
                            poz_list.append([(a,b),item])
                            poz_dict[key] = poz_list
                except:
                    pass

    # sözcük içindeki harflerin koordinatlarının birbirinin +/- 1 olması mantığından hareketle, sözcükte bulunan ancak board içinde
    # ayrıca bulunan ve sözcük sırasına uymayan koordinatların elenmesi.
    for key,value in poz_dict.items():
        for i,item in enumerate(value) :
            try:
                if item[1]!= value[i+1][0]:
                    del (value[i+1])
            except:
                    pass
                
    # toplam harf koordinat sayısının bulunması. eğer sözcükteki tüm harfler birbirini takip edecek şekilde harf sayısıyla
    # aynı sayıda koordinat veriyorsa verilen bu sözcük board da var demektir.
    from functools import reduce
    
    final_list = []
    for key,value in poz_dict.items():

        result = reduce(lambda item1,item2: item1+item2, value)
        
        if len(key) == len(set(result)):
                  
            final_list.append(key)  
    
    
    
    return final_list
    
findWords(words = ["oath","pea","eat","rain"],board =[  ['o','a','a','n'],  ['e','t','a','e'],  ['i','h','k','r'],  ['i','f','l','v']])

