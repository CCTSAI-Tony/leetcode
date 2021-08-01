'''
Given a url startUrl and an interface HtmlParser, implement a web crawler to crawl all links that are under the same hostname as startUrl. 

Return all urls obtained by your web crawler in any order.

Your crawler should:

Start from the page: startUrl
Call HtmlParser.getUrls(url) to get all urls from a webpage of given url.
Do not crawl the same link twice.
Explore only the links that are under the same hostname as startUrl.


As shown in the example url above, the hostname is example.org. 
For simplicity sake, you may assume all urls use http protocol without any port specified. For example, 
the urls http://leetcode.com/problems and http://leetcode.com/contest are under the same hostname, 
while urls http://example.org/test and http://example.com/abc are not under the same hostname.

The HtmlParser interface is defined as such: 

interface HtmlParser {
  // Return a list of all urls from a webpage of given url.
  public List<String> getUrls(String url);
}
Below are two examples explaining the functionality of the problem, 
for custom testing purposes you'll have three variables urls, edges and startUrl. 
Notice that you will only have access to startUrl in your code, while urls and edges are not directly accessible to you in code.

 

Example 1:



Input:
urls = [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.google.com",
  "http://news.yahoo.com/us"
]
edges = [[2,0],[2,1],[3,2],[3,1],[0,4]]
startUrl = "http://news.yahoo.com/news/topics/"
Output: [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.yahoo.com/us"
]
Example 2:



Input: 
urls = [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.google.com"
]
edges = [[0,2],[2,1],[3,2],[3,1],[3,0]]
startUrl = "http://news.google.com"
Output: ["http://news.google.com"]
Explanation: The startUrl links to all other pages that do not share the same hostname.
 

Constraints:

1 <= urls.length <= 1000
1 <= urls[i].length <= 300
startUrl is one of the urls.
Hostname label must be from 1 to 63 characters long, including the dots, 
may contain only the ASCII letters from 'a' to 'z', digits  from '0' to '9' and the hyphen-minus character ('-').
The hostname may not start or end with the hyphen-minus character ('-'). 
See:  https://en.wikipedia.org/wiki/Hostname#Restrictions_on_valid_hostnames
You may assume there're no duplicates in url library.
'''

#dfs, time complexity O(n), n: 同個hostsite 連結到的 urls, 刷題用這個
#思路: 此題是執行一個crawler 指定一個 hostsite, 抓取hostsite 全部的內部urls, 內部url就是在同個hostsite底下的url
#執行 htmlParser.getUrls(Url) 能得到該Url 裡面的所有links 包含外部與內部url
#想像成一個directed graph, 每個edge都是代表該webpage 底下指向的urls, 我們只能遍歷某些edge 其出發點是特定hostsite底下的url
#在遍歷的途中收集特定hostsite 底下的url, 記得要設visited 以免重復遍歷同個hostsite底下的url
#技巧: 善用split
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostsite = startUrl.split("http://")[1].split("/")[0]
        visited = set()
        self.ans = []
        self.dfs(startUrl, htmlParser, visited, hostsite)
        return self.ans
        
    def dfs(self, Url, htmlParser, visited, hostsite):
        if Url.split("http://")[1].split("/")[0] == hostsite:
            if Url not in visited:
                self.ans.append(Url)
                visited.add(Url)
                for new_url in htmlParser.getUrls(Url):
                    self.dfs(new_url, htmlParser, visited, hostsite)





#bfs
from collections import deque
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        visited = {startUrl}
        domain = startUrl.split("http://")[1].split("/")[0]
        ans = [startUrl]
        queue = collections.deque([startUrl])
        while queue:
            for _ in range(len(queue)):
                url = queue.popleft()
                check = htmlParser.getUrls(url)
                for new_url in check:
                    if new_url in visited:
                        continue
                    if new_url.split("http://")[1].split("/")[0] != domain:
                        continue
                    ans.append(new_url)
                    visited.add(new_url)
                    queue.append(new_url)        
        return ans



#重寫第二次, time complexity O(v+e), space complexity O(v+e)
from collections import deque
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        res = [startUrl]
        queue = deque([startUrl])
        visited = set([startUrl])
        while queue:
            for _ in range(len(queue)):
                url = queue.popleft()
                host = self.check_host(url)
                for next_url in htmlParser.getUrls(url):
                    next_host = self.check_host(next_url)
                    if host == next_host and next_url not in visited:
                        queue.append(next_url)
                        res.append(next_url)
                        visited.add(next_url)
        return res
        
        
    def check_host(self, url):
        url_split = url.split("/")
        return url_split[2]






















