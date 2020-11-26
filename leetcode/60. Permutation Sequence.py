from math import factorial

class Solution(object):
    def getPermutation(self, n, k): #ie n=3 k=4
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result = ""
        k = k-1 # k = 3 這一行是關鍵
        lis = list(range(1, n+1)) #[1,2,3] [1.2.3.......n]
        for _ in range(n-1): # range(3-1) = 0,1    
            p = factorial(n-1) #p=2*1 = 2 ## p=1
            result = result + str(lis[k//p]) #''+str(lis[3//2]) = ''+str(lis[1])='2' ## '2'+str(lis[1//1]) = '2'+str(lis[1]) = '2','3'
            lis.pop(k//p) #lis = [1,3] ##lis = [1]
            k = k%p #k = 3 => 3%2=1 
            n = n-1 #n=3 => 2    
        result =  result + str(lis[0]) # '2','3'+'1'
        return result  #'2','3','1'
        
        '''
        
        math.factorial(5) = 5*4*3*2*1 = 120

        print('divmod(8, 3) = ', divmod(8, 3))
		print('divmod(3, 8) = ', divmod(3, 8))
		print('divmod(5, 5) = ', divmod(5, 5))

		divmod(8, 3) =  (2, 2)
		divmod(3, 8) =  (0, 3)
		divmod(5, 5) =  (1, 0)

		# divmod() with Floats
		print('divmod(8.0, 3) = ', divmod(8.0, 3))
		print('divmod(3, 8.0) = ', divmod(3, 8.0))
		print('divmod(7.5, 2.5) = ', divmod(7.5, 2.5))
		print('divmod(2.6, 0.5) = ', divmod(2.6, 0.5))


		divmod(8.0, 3) =  (2.0, 2.0)
		divmod(3, 8.0) =  (0.0, 3.0)
		divmod(7.5, 2.5) =  (3.0, 0.0)
		divmod(2.6, 0.5) =  (5.0, 0.10000000000000009)

        '''


        '''


        The idea is as follow:

		For permutations of n, the first (n-1)! permutations start with 1, next (n-1)! ones start with 2, ... and so on. 
		And in each group of (n-1)! permutations, the first (n-2)! permutations start with the smallest remaining number, ...

		take n = 3 as an example, the first 2 (that is, (3-1)! ) permutations start with 1, next 2 start with 2 and last 2 start with 3. 
		For the first 2 permutations (123 and 132), the 1st one (1!) starts with 2, which is the smallest remaining number (2 and 3). 
		So we can use a loop to check the region that the sequence number falls in and get the starting digit. 
		Then we adjust the sequence number and continue.




        '''



        '''
		the set [1,2,3,...,n] contains a total of n! unique permutations.

		By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

		"123"
		"132"
		"213"
		"231"
		"312"
		"321"
		Given n and k, return the kth permutation sequence.

		Note:

		Given n will be between 1 and 9 inclusive.
		Given k will be between 1 and n! inclusive.
		Example 1:

		Input: n = 3, k = 3
		Output: "213"
		Example 2:

		Input: n = 4, k = 9
		Output: "2314"        




map函数的原型是map(function, iterable, …)，它的返回结果是一个列表。

a=(1,2,3,4,5)
b=[1,2,3,4,5]
c="zhangkang"

la=map(str,a)
lb=map(str,b)
lc=map(str,c)

print(la)
print(lb)
print(lc)

输出：
['1', '2', '3', '4', '5']
['1', '2', '3', '4', '5']
['z', 'h', 'a', 'n', 'g', 'k', 'a', 'n', 'g']
————————————————
版权声明：本文为CSDN博主「neu_张康」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/csdn15698845876/article/details/73321593


def mul(x):
    return x*x

n=[1,2,3,4,5]
res=map(mul,n)

输出：[1, 4, 9, 16, 25]

map()函数的返回值是个Iterator，你所列出的这些语句，真的可以得到你给出的这些输出么？

在python2中，返回的是map函数返回的是一个列表，正如博主所写的那样，但是python3中不是，map函数返回的是一个内存地址，如果想要和博主一样的输出，list(map(……))就可以了。

















        '''