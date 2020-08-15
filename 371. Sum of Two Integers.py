'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1
'''

# Understanding the mask in a Python solution

# Two's Complement binary for Negative Integers:
# Negative numbers are written with a leading one instead of a leading zero. So if you are using only 8 bits for your twos-complement numbers, 
# then you treat patterns from "00000000" to "01111111" as the whole numbers from 0 to 127, and reserve "1xxxxxxx" for writing negative numbers. 
# A negative number, -x, is written using the bit pattern for (x-1) with all of the bits complemented (switched from 1 to 0 or 0 to 1). 
# So -1 is complement(1 - 1) = complement(0) = "11111111", and -10 is complement(10 - 1) = complement(9) = complement("00001001") = "11110110". 
# This means that negative numbers go all the way down to -128 ("10000000").

# Of course, Python doesn't use 8-bit numbers. It USED to use however many bits were native to your machine, but since that was non-portable, 
# it has recently switched to using an INFINITE number of bits. Thus the number -5 is treated by bitwise operators as if it were written "...1111111111111111111011".

# Since there are infinite leading 1 bits for negative integers, the operands in recursive calls getSum(-1, 1) of python will be:

#這個結果驗證過了, 他說的是對的
# 1 -1
# 2 -2
# 4 -4
# ... forever 
# On the other hand, other language like C and java, 32-bit signed integer will ends with


# 1073741824 -1073741824 (0x40000000 0xc0000000)
# -2147483648 -2147483648 (0x80000000 0x80000000)
# 0 0
# That is why we need to mask integers in python.


# Python solution with no "+-*/%", completely bit manipulation guaranteed

#這一題很棒! 可以用1101(13) + 0100(4) 當作例子練習, 關鍵點 & mask 是用來消除leading 1's

# 這個方法比較直觀, time complexity O(32) => O(1), 刷題用這個 
# 思路: 此題 a + b 的操作不會overflow, 也就是若a+b 是正數 不會超過2^31-1, 若a+b是負數不會< - 2^32
# 但python 沒有特定sign bit, 也就是說負數的sign bit 是infinite的 => infinite leading 1 bits for negative integers
# 所以一般在sign integer 是負數 在 python 會變正數, 除非這數的leading bits 都是1, python 才會認定為負數
# 利用mask = 0xFFFFFFFF (32個1bits) 來杜絕負數無限進位的狀況, 消除leading 1, num & mask, 但這樣會使此數在python 變成正數
# 所以之後a+b 是負數的話 => 也就是發生 a+b > MAX, 要轉換成負數, 
# 技巧: 先把32bit 裡的bits 都相互轉換 0>1, 1>0 => num ^ mask, 之後在一次轉置, 這樣就能恢復infinite leading 1 bits
# binary a+b相加, 先找互異的1bits => a ^ b = a, 再找互同的1 bits=> (a & b) << 1 = b 進位用的, 直到無法進位 a & b == 0, 此時a 就是答案
# if a > Max, 代表overflow => negative, num & mask 就是消除infinite leading 1 bits, ex: 負數+負數 or 正數加負數 若不消除都有可能造成無限進位
# 此題觀點, 為了不要無限進位=>使用mask, 為了變回負數=> 使用~ 
class Solution(object):
    def getSum(self, a, b):
        # 32 bits integer max:2147483647, sign integer 最大值的表示 ->31個1's => 2^31-1 == 2^3*16^7-1
        MAX = 0x7FFFFFFF  
        # 32 bits interger, sign integer 最小值的表示 https://en.wikipedia.org/wiki/Signed_number_representations
        MIN = 0x80000000  #但在python 一樣視為正數, 所以>= min 在singn integer 表示負數
        # mask to get last 32 bits 4294967295 上面兩者相加
        mask = 0xFFFFFFFF  #like 1111111111111111111111111111111111 => 16^8-1
        while b != 0: #直到進位結束
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)  #if a <= MAX 代表結果是正的, (a ^ mask):在32bits中 1's -> 0's, 0's -> 1's, ~(a ^ mask) 再0's 1's 互換並還原leading 1's

#自己重寫, time complexity O(1)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 2**31-1
        mask = 2**32-1
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= MAX else ~(a ^ mask)






#如果a是負的, 32bits的最後一個是1, 這樣就大於 MAX 
# ~   NOT   Inverts all the bits

# Read this if you want to learn about masks

# In Python unlike other languages the range of bits for representing a value is not 32, its much much larger than that. 
# This is great when dealing with non negative integers, however this becomes a big issue when dealing with negative numbers ( two's compliment)

# Why ?

# Lets have a look, say we are adding -2 and 3, which = 1

# In Python this would be ( showing only 3 bits for clarity )

# 1 1 0 +
# 0 1 1

# Using binary addition you would get

# 0 0 1

# That seems fine but what happended to the extra carry bit ? ( 1 0 0 0 ), if you were doing this by hand you would simply ignore it, 
# but Python does not, instead it continues 'adding' that bit and continuing the sum.

# 1 1 1 1 1 1 0 +
# 0 0 0 0 0 1 1
# 0 0 0 1 0 0 0 + ( carry bit )

# so this actually continues on forever unless ...

# Mask ! cutting off the leading 1's!!

# The logic behind a mask is really simple, you should know that x & 1 = 1 right, so using that simple principle,

# if we create a series of 4 1's(4 bits mask) and & them to any larger size series, we will get just that part of the series we want, so

# 1 1 1 1 1 0 0 1   (any larger size series)
# 0 0 0 0 1 1 1 1 & (a series of 4 1's)

# 0 0 0 0 1 0 0 1 ( Important to note that using a mask removes the two's compliment)

# For this question leetcode uses 32 bits, so you just need to create a 32 bit mask of 1's , 
# the quickest way is to use hexadecimal and 0xffffffff, you can write the binary form if you prefer it will work the same.

# Here is my code ,

#這個要想很久
class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # 32 bit mask in hexadecimal 全部都是1's
        mask = 0xffffffff
        
        # works both as while loop and single value check 
        while (b & mask) > 0:  #直到b=0
            
            carry = ( a & b ) << 1  #identicle bits 進位
            a = (a ^ b)  #相異bits 相加 ex: 101 + 010 = 111 -> 101^010, 若b是負數, a也會有leading 1's
            b = carry
        
        # handles overflow
        return (a & mask) if b > 0 else a  #這邊b不會<0 最多=0, 也可以 return a if b == 0 else (a & mask)

#注意以下解釋
# Note the final check, here if the final answer is positive the carry may be something like 1 0 0 0 ...0 0 0 ex: getSum(-2,3), or just 0
# so we use the mask to ignore the leading 1's like we would by hand, but if the final answer is negative the a will be something like 1 1 1 1 1 ....0 0 0, 
# so we DO NOT use the mask, that way Python continues to show the negative value.

# Hope that helps, let me know if you have any further questions in comments.


# mask = 0xFFFFFFFF
# -11 & mask
# 4294967285
# 0 & mask
# 0

# Bitwise Operators:
# XOR: ^
# And: &
# Left Shift: << n (Shifts a binary value n digits to the left by adding zeros at the end.
# Conceptual: We first need to come up with a variable called carry. Carry will record the component of the addition that needs to be shifted. 
# Here is an example

# First, let's look at what happens when we add binary digits that are identical to one another:

# adding 111 + 111 will result in 1110 // 7 + 7 = 14
# adding 1100 + 1100 = 11000 //12 + 12 = 24
# adding 101 + 101 = 1010 //5 + 5 = 10
# We can logically reduce adding identical binary digits using the left shift operator. 
# This means that for any identical binary digits a, and b the sum will always be a << 1 which is the same as b << 1

# Let's Look at adding Binary Digits that are opposites of each other

# 101 + 010 = 111 //
# 1001 + 0110 = 1111 //
# We can see that adding binary digits that are the opposites of each other are as simpl as taking
# a XOR b which gives us the answer.

# So the task of this question is to simply separate the identical components of the two digits with the complementary components. 
# Shift the identical component to the left by one. Then add it to the separate component.

# This is accomplished with the following code java

# public sum(int a, int b) {
#     while (b != 0) {
#     //filter out identical component
#     int carry = a & b;
#     //filter out complementary component
#     a = a ^ b;
    
#     //shift b to the left the common components. and assign it to b
#     //on the next iteration there will be fewer and fewer common components
#     //and gradually b will converge to 0 conce we have shifted the integer left 
#     //the appropriate amount of times. 
#     b = carry << 1;
#     }
#     return a;
# }

bin(25)
'0b11001'
















