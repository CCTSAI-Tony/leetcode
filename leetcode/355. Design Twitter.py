'''
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and 
is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. 
Each item in the news feed must be posted by users who the user followed or by the user herself. 
Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
'''

# I use a dict of (int, deque) to save tweets each user has posted and another dict to point to the users he's following. 
# Deque can be used because only the most recent tweets matter to us in this system.
# I use a post counter as a time stamp to track most recent.
# When getNewsFeed is called, I build a min heap of all the tweets of the user first. Then iterate over all the users he follows.
# For each other user a user follows, I iterate over all of his tweets from last to first since tweets array will be sorted by default, 
# and if current element if greater than root of min heap, then I do a push if heap's not full or if it's full, I do a pushpop.
# Since, we only need 10 tweets and each person can at max have only 10 tweets. All the heap operatons can be considered constant.
# Hence, the time complexity is O(Number of people a user follows).

from heapq import *
from collections import defaultdict, deque
class Twitter:

    # Each user has a separate min heap
    # if size of heap is lesser than 10 keep pushing tweets and when it's full, poppush
    # use a defaultdict to associate user id's to their heaps
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.following = defaultdict(set)
        self.user_tweets = defaultdict(deque)
        self.post = 0  #use self.post to track, class 全域變數

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        """
        self.post += 1
        tweets = self.user_tweets[userId]
        tweets.append((self.post, tweetId))
        if len(tweets) > 10:
            tweets.popleft()  #pop 掉最久遠的
        

    def getNewsFeed(self, userId): #O(len(h))+O(n*mlog(len(h))), h = 10(at nost), m: followee總共的posta at most 10, O(n*10log(len(10)))=> O(Number of people a user follows)
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. 
        Each item in the news feed must be posted by users who the user followed or by the user herself. 
        Tweets must be ordered from most recent to least recent.
        """
        h = []
        u = self.user_tweets[userId]  #deque
        h.extend(u)
        heapify(h)
        for user in self.following[userId]:
            tweets = self.user_tweets[user]
            for x in range(len(tweets) - 1, -1, -1):  #倒序, followee 最新到最舊的posts
                if len(h) < 10:
                    heappush(h, tweets[x])  #push the latest
                else:
                    if h[0][0] < tweets[x][0]:  #heap裡的第一個post時間若比followee的x post還早的話, 執行heappushpop, 先push 再pop h裡時間最久的
                        heappushpop(h, tweets[x])
                    else:
                        break  #out of inner for, the followee的其他post 都比heap最早的post還早
        return [heappop(h)[1] for _ in range(len(h))][::-1]  #[::-1] 最晚的擺第一個

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
                self.following[followerId].discard(followeeId)






a = [2]
a.extend([3]) #不能a.extend(3), 'int' object is not iterable
a
[2, 3]

a = set([1,2,3,4,5])
a
{1, 2, 3, 4, 5}
a.discard(5)
a
{1, 2, 3, 4}
a.discard(9)
a
{1, 2, 3, 4}






