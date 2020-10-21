'''
Given a file and assume that you can only read the file using a given method read4, implement a method read to read n characters. Your method read may be called multiple times.

 

Method read4:

The API read4 reads 4 consecutive characters from the file, then writes those characters into the buffer array buf.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:

    Parameter:  char[] buf4
    Returns:    int

Note: buf4[] is destination not source, the results from read4 will be copied to buf4[]
Below is a high level example of how read4 works:



File file("abcde"); // File is "abcde", initially file pointer (fp) points to 'a'
char[] buf = new char[4]; // Create buffer with enough space to store characters
read4(buf4); // read4 returns 4. Now buf = "abcd", fp points to 'e'
read4(buf4); // read4 returns 1. Now buf = "e", fp points to end of file
read4(buf4); // read4 returns 0. Now buf = "", fp points to end of file
 

Method read:

By using the read4 method, implement the method read that reads n characters from the file and store it in the buffer array buf. 
Consider that you cannot manipulate the file directly.

The return value is the number of actual characters read.

Definition of read:

    Parameters: char[] buf, int n
    Returns:    int

Note: buf[] is destination not source, you will need to write the results to buf[]
 

Example 1:

File file("abc");
Solution sol;
// Assume buf is allocated and guaranteed to have enough space for storing all characters from the file.
sol.read(buf, 1); // After calling your read method, buf should contain "a". We read a total of 1 character from the file, so return 1.
sol.read(buf, 2); // Now buf should contain "bc". We read a total of 2 characters from the file, so return 2.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
Example 2:

File file("abc");
Solution sol;
sol.read(buf, 4); // After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so return 3.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
 

Note:

Consider that you cannot manipulate the file directly, the file is only accesible for read4 but not for read.
The read function may be called multiple times.
Please remember to RESET your class variables declared in Solution, as static/class variables are persisted across multiple test cases. Please see here for more details.
You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.
It is guaranteed that in a given test case the same buffer buf is called by read.
'''

# I separate the process into two steps

# Get data from read4 and store it in a queue
# Transfer data from queue to buf
# Initially, we will go to else clause, we get data from read4, and use the return value to store non-empty data. 
# If it returns 3, put first 3 characters into the queue. If it returns 0, it means we come to the end. So just end the process.

# Then we go to if clause, just pop from the queue head and put it into buf, and increase i by 1.

# Continue the process until i equal n, or when there is no more data to read. In the first case, we put data of length n into buf. 
# In the second case, the actual data is of size less than n, so we end earlier.

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int: => form api interface we can see it need buf4: [""] * 4

#刷題用這個, time complexity O(n)
#思路: the method read has its own buf array used to store char from read4 method, read(guf, n) needs to return how many words it actually read
#warning: read4 api need a [""]*4 input as buf4
#how to solve this, use index pointer to record how many chars in actually read every time it call read, => can know from read4 api
#index pointer set to 0 initailly and set a limit to < n, atmost read n chars
#if read4 return 0 it means we reach to the end, return index immediately
#warning: if read n is less than 4, we need another place to store left chars cause read4 atmost read 4 chars, and next time read n will start from the left chars
#warning: read buf array is already exist as [""]*infinity, so we need to store our chara via replace
#everytime it call read, buf array will be reset to [""]*infinity
class Solution(object):
    def __init__(self):
        self.q = []
        
    def read(self, buf, n):
        i = 0
        while i < n: #at most read n words
            if self.q: #store letter in buf from self.q
                buf[i] = self.q.pop(0) 
                i += 1
            else:
                buf4 = ['']*4
                v = read4(buf4) #return how many words it read
                if v == 0:
                    break #out of while loop, finished
                self.q += buf4[:v]
        return i


#自己重寫, time complexity O(n)
from collections import deque
class Solution:
    def __init__(self):
        self.q = deque()
            
    def read(self, buf: List[str], n: int) -> int:
        index = 0
        while index < n:
            if self.q:
                buf[index] = self.q.popleft()
                index += 1
            else:
                buf4 = [""]*4
                v = read4(buf4)
                if v == 0:
                    break
                self.q += buf4[:v]
        return index






