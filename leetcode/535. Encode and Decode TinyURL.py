'''
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL 
such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. 
There is no restriction on how your encode/decode algorithm should work. 
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
'''



#time complexity encode: O(1), decode: O(1), space complexity O(n)
#思路: 使用string and OrderedDict 先建立 letter:int pair, 建立self.urls = [] 來儲存未encode 的urls, 使用建立的self.base來加密此url在self.urls 的位置 index + 1 => 輸出成加密url
#每個不同的n (self.urls 的index + 1) 加密後的結果都不同
#解密 加密的url => 轉化成index => self.urls[n-1] => 原本的url
#加密機制 n%62 => letter, n//62 => 解密機制 n = 0 => n*62 + self.base[ch]
# Map index of the urls to the 62 digit system, 0,1...8,9,a,b...y,z,A,B...Y,Z.
# I avoid 0 to simplfy the 0 case for while loop
# 使用餘數 0 - 61 與商 n // 62 => 來encode, 還有可以不用OrderedDict
import string
from collections import OrderedDict
class Codec:
    def __init__(self):
        self.urls = [] #紀錄所有的urls
        self.base = OrderedDict((k, i) for i, k in enumerate(string.digits + string.ascii_letters)) #轉化letter to key:val pairs
        
    def encode(self, longUrl):
        self.urls.append(longUrl)
        n = len(self.urls) #紀錄在self.urls 的位置 => n = index + 1
        code = []
        while n > 0: #有url 才能encode, n > 0, => 每個不同的n 加密後的結果都不同
            code.append(list(self.base.keys())[n % len(self.base)]) #ex: 106 % 62 = 44 => 106//62 => 1, self.base.keys()[44] = "I", self.base.keys()[1] = "1"
            n = n // len(self.base)
            
        return 'http://tinyurl.com/' + ''.join(code) #ex: 'http://tinyurl.com/I1"

    def decode(self, shortUrl):
        code = shortUrl.split('/')[-1][::-1]
        n = 0
        for ch in code:
            n = n * len(self.base) + self.base[ch] #0*62 + 1 => 1*62 + 44 = 106
        
        return self.urls[n-1]

# a = OrderedDict([("c",2)])
# a
# OrderedDict([('c', 2)])
# a["c"]
# 2

#自己重寫
import string
from collections import OrderedDict
class Codec:
    def __init__(self):
        self.urls = []
        self.base = OrderedDict((k, i) for i, k in enumerate(string.digits + string.ascii_letters))

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        code = []
        self.urls.append(longUrl)
        n = len(self.urls)
        while n > 0:
            code.append(list(self.base.keys())[n % len(self.base)])
            n = n // len(self.base)
        return "http://tinyurl.com/" + "".join(code)
            
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        code = shortUrl.split("/")[-1][::-1]
        n = 0
        for ch in code:
            n = n * len(self.base) + self.base[ch]
        return self.urls[n-1]


#自己重寫第二次, time complexity encode: O(1), decode: O(1), space complexity O(n)
import string
class Codec:
    def __init__(self):
        self.url = []
        self.base = {j:i for i, j in enumerate(string.digits + string.ascii_letters)}
        self.m = len(self.base)

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.url.append(longUrl)
        n = len(self.url)
        code = ""
        while n != 0:
            code += list(self.base.keys())[n % self.m]
            n //= self.m
        return "http://tinyurl.com/" + code
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        code = shortUrl.split("/")[-1][::-1]
        n = 0
        for c in code:
            n += n*self.m + self.base[c]
        return self.url[n-1]

#重寫第三次
import string
class Codec:
    def __init__(self):
        self.base = {v:i for i, v in enumerate(string.digits + string.ascii_letters)}
        self.url = []
        self.m = len(self.base)
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.url.append(longUrl)
        n = len(self.url)
        code = ""
        while n != 0:
            code += list(self.base.keys())[n % self.m]
            n //= self.m
        return "http://tinyurl.com/" + code
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        code = shortUrl.split("/")[-1][::-1]
        n = 0
        for c in code:
            n = n * self.m + self.base[c]
        return self.url[n-1]


#重寫第四次, time complexity encode: O(1), decode: O(1), space complexity O(n)
import string
class Codec:
    def __init__(self):
        self.url = []
        self.base = {v:i for i, v in enumerate(string.digits + string.ascii_letters)}
        self.m = len(self.base)

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.url.append(longUrl)
        n = len(self.url)
        code = ""
        while n > 0:
            code += list(self.base.keys())[n % self.m]
            n //= self.m
        return "http://tinyurl.com/" + code
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        code = shortUrl.split("/")[-1]
        n = 0
        for w in code[::-1]:
            n = n * self.m + self.base[w]
        return self.url[n-1]

# 重寫第五次
import string
class Codec:
    def __init__(self):
        self.urls = []
        self.base = {v:i for i, v in enumerate(string.digits + string.ascii_letters)}
        self.m = len(self.base)
        
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.urls.append(longUrl)
        n = len(self.urls)
        code = ""
        while n:
            c = n % self.m
            code += list(self.base.keys())[c]
            n //= self.m
        return "http://tinyurl.com/{}".format(code)
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        code = shortUrl.split("/")[-1][::-1]
        n = 0
        for c in code:
            idx = self.base[c]
            n = n * self.m + idx
        return self.urls[n-1]







