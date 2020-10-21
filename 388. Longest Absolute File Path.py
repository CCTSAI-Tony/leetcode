'''
Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1 #一級文件夾
        file1.ext
        subsubdir1 #二級文件夾
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext 
and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. 
For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. 
If there is no file in the system, return 0.

Note:
The name of a file contains at least a . and an extension.
The name of a directory or sub-directory will not contain a ..
Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.
'''

# python solution easy to understand

# 该算法的时间复杂度为O(N)，其中N为输入数组的长度。
# 思路: 
# *我们用新行字符分割输入数组后，我们有K行
# *对于每一行，我们需要使用内建'in'函数来确定它是否是一个文件。in函数的时间复杂度为O(M)，其中M为文件和目录名称的平均长度。由于K * M == N，时间复杂度为O(N)。
# 空间复杂度为O(N)，因为我们维护了一个字典
# 注意, 遍歷iterate file aystem的同時, 幾級資料夾的value會跟著變動, 所以file前面的資料夾的長度dic[key] : value 都是不斷隨著路徑更新的
# 技巧: split("\n"), count("\t"), replace("\t","")
class Solution(object):
    def lengthLongestPath(self, input):
        dict={}
        longest=0
        fileList=input.split("\n")
        for i in fileList:  #這句重要 逐步 iterate file aystem, 幾級資料夾的value會跟著變動
            if "." not in i:  #是文件夹
                key = i.count("\t") #是几级文件夹
                value = len(i.replace("\t","")) #除去\t后的长度，是实际长度
                dict[key]=value
            else: #是文件。
                key=i.count("\t") #是几级文件
                #　文件的长度：所有目录的长度(文件的上層資料夾)＋文件的长度＋“\”的数量
                length = sum([dict[j] for j in dict.keys() if j<key]) + len(i.replace("\t","")) + key  #key => “\”的数量 => 幾級文件
                longest=max(longest,length)
        return longest


#sum([1,2,3,4,5])

#15

# a = "\tioihlknkjh\tlijuhhkj\t"
# a.count("\t")
# 3

# the string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

# a = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" 

# a.split("\n")

# ['dir', '\tsubdir1', '\t\tfile1.ext', '\t\tsubsubdir1', '\tsubdir2', '\t\tsubsubdir2', '\t\t\tfile2.ext']



# dir
#     subdir1 #一級文件夾
#         file1.ext
#         subsubdir1 #二級文件夾
#     subdir2
#         subsubdir2
#             file2.ext



































