def perfectNumbers(n):
    elements = set([1])
    ans = set()
    for i in range(2, int(n**0.5) + 1):
        i *= i
        while i <= n - 1:
            elements.add(i)
            i *= i
    temp = sorted(list(elements))
    for i in range(len(temp)):
        for j in range(i, len(temp)):
            if temp[i] + temp[j] <= n:
                ans.add(temp[i] + temp[j])
            else:
                break
    return len(ans)
            
    
    

perfectNumbers(1000000)
215908
            
    
    
from collections import defaultdict
def bigramsWithSynonym(text, synonyms):
    u = {}
    def find(x):
        u.setdefault(x, x)
        if u[x] != x:
            u[x] = find(u[x])
        return u[x]
    
    def union(x, y):
        u[find(y)] = find(x)
        
    for s in synonyms:
        t = s.split(",")
        for i in range(len(t)):
            if t[i] in text:
                root = t[i]
        for i in range(1, len(t)):
            union(root, t[i])
    
    d = defaultdict(set)
    for s in synonyms:
        t = s.split(",")
        root = find(t[0])
        d[root] |= set(t)
        
    res = []
    while text:
        flag = False
        for x in d:
            if text.startswith(x):
                n = len(x)
                text = text[n+1:]
                res.append(list(d[x]))
                flag = True
        if flag == False:
            if " " in text:
                i = text.index(" ")
                res.append([text[:i]])
                text = text[i+1:]
            else:
                res.append([text])
                break
                
    
    ans = set()
    for i in range(len(res) - 1):
        nxt = []
        for p in res[i + 1]:
            p = p.split()
            nxt.append(p[0])
            
        for k in res[i]:
            k = k.split()
            for j in range(len(k) - 1):
                ans.add(k[j] + " " + k[j + 1])
            for x in nxt:
                ans.add(k[-1] + " " + x)
                
                
    for k in res[-1]:
        k = k.split()
        for j in range(len(k) - 1):
            ans.add(k[i] + " " + k[i + 1])
    return sorted(ans)

bigramsWithSynonym("the sofa is too big", ["big,large"])
['is too', 'sofa is', 'the sofa', 'too big', 'too large']

bigramsWithSynonym("i am fed up with you", ["fed up,annoyed"])
['am annoyed',
 'am fed',
 'annoyed with',
 'fed up',
 'i am',
 'up with',
 'with you']


def evennumber():
    print([i for i in range(2, 99) if i % 2 == 0])




