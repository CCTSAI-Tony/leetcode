'''Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
'''

'''
初步看到这道题，我首先是懵逼的，阶乘结果有多少个0？what??!
硬来肯定是不行的，仔细一想，会出现零只有一种情况嘛：2*5=10；
所以我们可以将阶乘进行因式分解，比如5！=1*2*3*4*5=1*2*3*2*2*5,共有1对2*5，所以结果就只有一个0嘛；有几对2*5,结果就有几个0！
所以问题就简化为找有几对2*5,能不能进一步简化捏？必须可以啊!
我们发现2的个数是远远多于5的，所以最终简化为了找出5的个数！
如果找出5的个数呢，比如20!，从1到20,共有5，10，15,20,共有4个5，即结尾0的个数为n/5！
这样就ok么？当然没ok，25!结果不只是25/5=5个0，25结果有6个0,因为25=5*5，有两个5。所以结果f(n)=n/5+f(n/5)

所以结果f(n)=n/5+f(n/5)
这个所以是什么数学原理，能解释一下嘛。

本质上是找阶乘里能拆除几个5（2够用这个不说了），其实f(n)方程不是找出阶乘能拆出几个5，而是找出有几个5的倍数的数，所以需要用f(n/5)进一步找到这些5的倍数的数，
有哪些还能再拆出5。以625的阶乘为例子：第一次除以5找到了125个5的倍数的数，但其中有25、50、75、100...这样数字，是包含了多个5相乘，所以我们给阶乘里每个数字除以5，
把之前统计过的5去掉，然后再找一遍剩下的5的倍数的数，也就是计算 (626/5)的阶乘。以此类推....一直计算到(625/5/5/5/5)的阶乘。

可以以125举例，125/5可以得到25个数都是带5的，它们可以各自和2结合得到一个0，然后再从这25个数里找有多少个数带多余的5，多余的5也可以和2结合得到一个0，
也就是5 * 5 * 1 =25, 5 * 5 * 2 = 50, 5 * 5* 3 = 75, 5 * 5 * 4 = 100, 5 * 5 * 5 =125, 这里有5个数，然后再看这5个数里有多少个数还有多余的5的，
那就是5 * 5 * 5= 125, 所以答案就是25 + 5 + 1 = 31.
'''

#自己重寫 time complexity O(logn)
#思路: 這題要靠數學思考, 組成10 不外乎靠 2 and 5, 2 因為太多, 我們把目標放在少數的5, 有一個5代表能組一個0
#n // 5, 先得知n階層有幾個數帶一個5 (5,10,15,20,25,), 再 n//5 再得知n階層有幾個數帶2個5.....(25,50,75,100), 再 n//5 再得知n階層有幾個數帶三個5.....(125,250)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        five = 0
        while n:
            n = n // 5
            five += n
        return five



class Solution:
    def trailingZeroes(self, n: int) -> int:
        num_zeros = 0
        while n > 0:
            n //= 5
            num_zeros += n
        return num_zeros



class Solution:
    def trailingZeroes(self, n):
        factor, count = 5, 0
        
        while True:
            curCount = n // factor
            if not curCount:
                break
            
            count += curCount
            factor *= 5

        return count





        