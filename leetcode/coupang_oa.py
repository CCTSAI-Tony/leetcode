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
            
    
    

