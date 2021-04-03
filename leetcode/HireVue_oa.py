Balanced Smileys

This problem was attempted by 7096 contestants, but only 2860 solved it. There are a lot of ways to solve this problem. You could go for the brute force solution, 
which was O(2^N), a dynamic programming/memoization approach, which would be O(N^2)/O(N^3), or the solution intended by the writer, which was O(N). 
We decided to let everyone who made a correct solution pass, so any of the above actually passes our tests. 
The number of passing submissions for this problem is just what we wanted from the qualification round, 
so we think it was a good call. This post will only cover the O(N) solution.

 

 

The idea is to keep track of the possible range of open parentheses.

We use two values, 'minOpen' and 'maxOpen'. Initialize both of these to 0.

Iterate over the message, character by character.

Whenever you encounter a '(', you increment maxOpen, and if it wasn't part of a smiley, you also increment minOpen.

Whenever you encounter a ')', you decrement minOpen, and if it wasn't part of a frowny face, decrement maxOpen. If minOpen is negative, reset it to 0.

 

 

If maxOpen ever was negative, or minOpen isn't 0, it wasn't possible that the message had balanced parentheses. Otherwise it was possible. 
Python code that solves this problem is below.

 

def isBalanced(message):

    minOpen = 0

    maxOpen = 0

 

    for i in range(len(message)):

        if message[i] == '(':

            maxOpen += 1

            if i == 0 or message[i-1] != ':':

                minOpen += 1

        elif message[i] == ')':

            minOpen = max(0, minOpen-1) #重要, (:) :) => 先扣除1 先使得minOpen = 0 => (:), 然而之後遇到")" 有可能為 :) 所以minOpen 小於0時, reset to 0

            if i == 0 or message[i-1] != ':':

                maxOpen -= 1

                if maxOpen < 0:

                    break

 
#最後判斷maxOpen >= 0 代表沒有")" 多餘的情況, 加上是否minOpen == 0, 代表沒有多餘'('的情況
    if maxOpen >= 0 and minOpen == 0:

        return "YES"

    else:

        return "NO"


Consider this ,whenever we get a ‘(‘ we increment maxOpen and whenever we get a ‘)’ we decrement minOpen.  
minOpen can never be negative this is because we can have “:) :)” which is a valid smiley.Now say we have “(:)))” . 
First we increment both maxOpen and minOpen as the first ‘(‘ is not a part of any smiley.Then for the next ‘)’ 
we decrement only minOpen and not maxOpen as ‘:)’ forms a smiley.So now maxOpen=1 and minOpen=0;Now as many times we get a ‘)’ 
we decrement maxOpen and also minOpen(minOpen=0).So if there are unbalanced ‘)’ in the message then maxOpen <0 which will print a NO .

Similarly consider a case when message = “(((:)” . Here there are more ‘(‘ than ‘)’ .
For each ‘(‘ that is not a part of a smiley we increment both maxOpen and minOpen.But we decrement minOpen only when we get a closing brace.
In this case since there are less ‘)’ that ‘(‘ ,minOpen will not be equal to 0 and hence answer will be NO.

So,the main thing is that we need to make minOpen=0 for valid messages.minOpen++ only when we get a ‘(‘ which is not a part of a smiley and minOpen– whenever we get ‘)’.
So minOpen will be =0 for all cases like “((:))” and “(:()”.

Lets consider an example  “(:()” . Here the first brace should be considered a valid parentheses so we increment minOpen. 
But for the second ‘(‘ we donot increment minOpen as it is a part of smiley. 
At any instance minOpen= number of ‘(‘ which is not a part of  any smiley. So after the message scans this number should always be 0.














