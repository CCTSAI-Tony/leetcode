'''
Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. If it is a file path, return a list that only contains this file's name. 
If it is a directory path, return the list of file and directory names in this directory. Your output (file and directory names together) should in lexicographic order.

mkdir: Given a directory path that does not exist, you should make a new directory according to the path. 
If the middle directories in the path don't exist either, you should create them as well. This function has void return type.

addContentToFile: Given a file path and file content in string format. If the file doesn't exist, 
you need to create that file containing given content. If the file already exists, you need to append given content to original content. 
This function has void return type.

readContentFromFile: Given a file path, return its content in string format.

 

Example:

Input: 
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]

Output:
[null,[],null,null,["a"],"hello"]

Explanation:
filesystem
 

Note:

You can assume all file or directory paths are absolute paths which begin with / and do not end with / except that the path is just "/".
You can assume that all operations will be passed valid parameters and users will not attempt to retrieve file content or list a directory or file that does not exist.
You can assume that all directory names and file names only contain lower-case letters, and same names won't exist in the same directory.
'''
#刷題用這個, 56ms
#思路: 利用Trie 結構來解題, 增加trienode content property 來模仿file, TrieNode.child = 該node資料夾裡面裡面的東西
#ls 時 利用sorted 來return node.child.keys() in lexicographic order, 因為defaultdict的關係, self.find的途中會自動建立路徑
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.child=defaultdict(TrieNode)
        self.content=""
        
class FileSystem(object):

    def __init__(self):
        self.root=TrieNode()
        
    def find(self,path):#find and return node at path.
        curr=self.root
        if len(path)==1:  # path = "/"
            return self.root
        for word in path.split("/")[1:]: #split("/")[0] = ""
            curr=curr.child[word]
        return curr
        
    def ls(self, path):
        curr=self.find(path)
        if curr.content:#it's a file path,return this file name
            return [path.split('/')[-1]] #記得外面要加一層[], return a list
        return sorted(curr.child.keys()) #列出所有在此資料夾的子dir 還有files, sorted 會把genetator dict_keys list化, 也就是一個迭代器
        
    def mkdir(self, path): #find的途中就建立路徑
        self.find(path)

    def addContentToFile(self, filePath, content):
        curr=self.find(filePath)
        curr.content+=content

    def readContentFromFile(self, filePath):
        curr=self.find(filePath)
        return curr.content


#自己重寫
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.content = ""
        
class FileSystem:

    def __init__(self):
        self.root = TrieNode()
        
    def find(self, path):
        node = self.root
        if len(path) == 1:
            return node
        for word in path.split("/")[1:]:
            node = node.child[word]
        return node
        

    def ls(self, path: str) -> List[str]:
        node = self.find(path)
        if node.content:
            return [path.split("/")[-1]]
        return sorted(node.child.keys())
        

    def mkdir(self, path: str) -> None:
        self.find(path)
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.find(filePath)
        node.content += content
        

    def readContentFromFile(self, filePath: str) -> str:
        node = self.find(filePath)
        return node.content


#重寫第二次, time complexity O(path)
from collections import defaultdict
class TrieNode:
    
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.content = ""
        
class FileSystem:

    def __init__(self):
        self.root = TrieNode()
        
    def find(self, path):
        cur = self.root
        if len(path) == 1: #這很重要, return root
            return cur
        for w in path.split("/")[1:]:
            cur = cur.child[w]
        return cur
        
    def ls(self, path: str) -> List[str]:
        cur = self.find(path)
        if cur.content:
            return [path.split("/")[-1]]
        return sorted(cur.child.keys())
        

    def mkdir(self, path: str) -> None:
        self.find(path)
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.find(filePath)
        cur.content += content
        

    def readContentFromFile(self, filePath: str) -> str:
        cur = self.find(filePath)
        return cur.content


#重寫第三次
from collections import defaultdict
class TreeNode:
    
    def __init__(self):
        self.child = defaultdict(TreeNode)
        self.content = ""

class FileSystem:

    def __init__(self):
        self.root = TreeNode()
        
    def find(self, path):
        if len(path) == 1:
            return self.root
        cur = self.root
        for item in path.split("/")[1:]:
            cur = cur.child[item]
        return cur

    def ls(self, path: str) -> List[str]:
        file = self.find(path)
        if file.content:
            return [path.split("/")[-1]]
        else:
            return sorted(file.child.keys())
        

    def mkdir(self, path: str) -> None:
        self.find(path)
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        file = self.find(filePath)
        file.content += content
        

    def readContentFromFile(self, filePath: str) -> str:
        file = self.find(filePath)
        return file.content










