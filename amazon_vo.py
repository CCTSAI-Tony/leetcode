# Time complexity: O(n^2), space complexity: O(n^2).
# 思路: 使用hashmap 來紀錄當前石塊是從多少jump跳過來的, 再以該值跳到之後的石塊, 若該值 <= 1, 則不能選擇少跳一步這個選項, 若最後在hashmap出現最後一個石塊, 代表成功
rom collections import defaultdict
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dic = defaultdict(set)
        dic[0] = {0}
        for i in range(len(stones)):
            if stones[i] not in dic:
                continue
            for val in dic[stones[i]]:
                if val > 0:
                    dic[stones[i] + val].add(val)
                if val > 1:
                    dic[stones[i] + (val - 1)].add(val - 1)
                dic[stones[i] + (val + 1)].add(val + 1)
        if stones[-1] in dic:
            return True
        return False


lc: 76, 41, 268, 121, 122, 188, 207, 210, 62, 451, 206, 92, 284, 623, 535, 403, 468, 974, 212, 104, 20, *98, 1, 102, 69, *230, 987, 110, 200, 225, 692, 74, 797, 323, 735, 347, 27, *146, *99, 33, *81, 108, 449, 105, 218, *173, *329, **57, **352, **84, **862
完成: 76, 41, 268, 121, 122, 188, 207, 210, 62, 451, 797, 206, 92, 284, 623, 535, 403, 468, 974, 212, 104, 20, 98, 1, 102, 69, 230, 987, 110, 200, 225, 692, 74, 797, 323, 735, 347, 27, 146, 99, 33, 81, 108, 449, 105, 218, 173, 329

longest increasing path in graph => 每个node有val和neighbors(list of nodes)=> 就是leetcode 329 => 使用top down dp
思路就是遍历当前node的所有neighbors，如果比它大就recursively从接下来这个node往下，可以写个helper function，同时更新当前的最大值。

#問hashmap 實現與collision處理
#问基础data structure的，比如hashmap 怎么实现的，array和list的区别，queue和stack的区别，graph tree解释一下概念
#Why amazon, Calculated risk, 還問了hashmap, tree, graph, list的real world examples



Coding:  
validate Binary Search Tree
Best time to buy and sell stock 1 2
Two Sum
Level Order traversal
sqrt x
kth smallest in bst
Binary Tree Vertical Order Traversal

Bq: 
1. a tight deadline 
2. help your teammates
3. a mistake
4. ambiguous task
5. difficult decision
6. take risk decision
7. challange project
8 different opinion with manager
9. beyond expectation
10. independent decision
11. course schedule
12. minstack
13. important decision
 why amazon, 学习新技术, convince someone
 1.队友不想干活怎么办
 2.没法Meet DDL
 3.针对2，假如可以Extend DDL怎么办


# Describe a situation where you had a tight deadline and how did you handle that deadline.

# This happened when I built the student tracking system project that I need to give a demo to our customer with only two days to complete it.
# In order to reduce the stress of a deadline, I make sure that I have mapped out all of the tasks that I need to complete to finish the project before deadline, 
# It includes quality checks and confirming all aspects of the project are in place. 
# In general, I would try to complete all of the most difficult paerts first, so that the deadline does not feel as dreadful as I expected before. 
# I also communicate with every member of the team and the client to make sure that everyone is on the same page and let them know what needs to be completed next.

# 6. Hire and Develop The Best
# Leaders raise the performance bar with every hire and promotion. They recognize exceptional talent and will move them throughout the organization. 
# Leaders develop leaders and take seriously their role in coaching others.  We work on behalf of our people to invent mechanisms for development like Career Choice.

# Case 1: (umc) Few years ago, there was an intern assigned to my project. He was helping me build the inspection system. 
# But I found that he got lost about what we are doing and what he is going to do. So, I told him that it was not as complex as what he was thinking about. 
# I explained the basic inspection concepts to him one by one and categorized the things what we are doing and what we are going to do. 
# After he was getting comfortable of the whole environment and what I needed him to do, I started to assign him some specific task. And he was doing pretty well.
# So when someone comes to a new environment, getting lost is quite normal. 
# We need to have patience to make him feel comfortable of the new environment. Otherwise the efficiency will be very low. 
# If he gets to be on the right track as soon as possible, he would have more enthusiasm and devote more to the work.


# The biggest mistake you made and what did you learn from it? (earn trust, customer obsession)
# Case 1: The biggest mistake I’ve made happened when I led the student's tracking system project for the first time. 
# The original schedule was in one week, but I suddenly received a message from my course professor, 
# says that he wanted to see the simple demo with the customer after two days. 
# And at that time I was working on building the profile's ui, that would be an important part of the demo. But I paid too much attention on the details, 
# I wanted to make everything perfect. I didn’t notice that I don’t have enough time to finish all of that. Last day before the demo day, 
# my professor pointed that out. I apologized to him and then we started to figure it out if there was a way to keep the demo the same as what we wanted it to be, 
# but sacrificing some features, cause it was just a demo. After the demo, I can rewrite the code to meet all the requirements. 
# Fortunately, the demonstration was not affected in the end. But from this mistake, I learnt that details are definitely important, 
# but I also need to pay attention to the whole schedule, I need to always keep good communication with my teammates when I have my plan. 
# I need to make sure that my schedule won’t affect other’s schedule.

# ambiguous task

# Case 1: When I worked on the student tracking system project, I was required to deploy file storage system. 
# Our storage system main goal is that customer can upload student's file and save securely. 
# Customer just gave us a story like uploading transcript pdf file. Since I was the person who was leading this project, 
# I want my customers to always have the best experience. So I started to think about other file format like doc, csv even mp3, vedio file format. 
# After the agreement from my professor, I start to create different storage sections. 
# I also created different APIs for those files format, so if the customer want to save different file format in the future, 
# he can just click the specific button to save the file. After delivery, we had strong positive feedbacks from our customer. 
# Even though our customer don't put these additional functions on the requirements, if we don't think far, our customer can still notice the quality's difference. 



# difficult decision, indepentdent decision
# • Tell me about a time when you took a calculated risk.
# When I was building the student tracking system, When it was at the final stage, we need to deployed all the work onto google app engine to see if it works, 
# After it be deployed, I found some problems about the environment incompatible issue which could lead some functions broke. 
# Before I started to fixed that, I know that changing different version libraries and replacing some python 2 scripts with python3 may bring some other bugs, 
# or destroy the underlying architecture. If I failed, we need to spend more time to solve these bugs and our customer would not get our product in time. 
# However, I quick review the project and google search the solution immediately, I decided to solve this problem because I know once old version migrate to new version, 
# I can definitely find out some suggestive code to replace old one. Fortunately, the final result went well and most importantly, our customer feel very satisfied with it.


# challange project
# The most challenging project I’ve done was a student's tracking system, it’s like a profile website but with interactive features. 
# The most challenging part was to incorporate cloud drive system onto our website, that is, students or teachers can upload any material to their profile, 
# being securely saved and fetched directly.
# It was challenging because I was supposed to come up with a solution and implement it by myself, and I have never developed something like this before.
# So I started with composing a simple demo first, the work I’ve done included researching google drive document code, 
# listing core features I needed, building functions, and designing UI. With the sample demo, I had a good understanding on how the application would work. 
# Then, I googled and read some external api solutions for products with similar features, like Google drive, dropbox, etc. With what I’ve read, 
# I was able to draft out my own solutions and selected corresponding technologies.
# I implemented it successfully within the given time, and my solution received a positive feedback because it is not only working well, 
# but user-friendly. Throughout this process, I learned that it is important to be curious and keep learning, try to read as many technical blogs or articles as you can, 
# the more you read, the better you’ll solve a problem or design. The feeling of ownership is very important, 
# some other students just gave up with the excuse “I don’t know how to do it"



# different opinion with manager
# When we built the student tracking system project, there is a important feature which is every student can create their own profile that record all kind of information in it, 
# like GPA, degree plan, graduate year, etc. At first, our professor comment that we should use relational SQL to be our database, 
# cause it can be set up on our django framework very easily. We are all familiar with relational SQL like postgreSQL. I respect his idea. 
# However, I issued that when the project scaled, the efficiency may go down very quickly, because all the information stored in one big table, 
# any operation of data in this table would be very slow. And if we wanted to add new fields to our database in the future, it would be a pain. 
# Communication was very important at this time, so I quickly made some demos and showed him the issues. After group discussion, 
# we choosed MongoDB which was new for us, the reason why we choosed it is that MongoDB is a non-relational database, every student profile's fields could be different, 
# so it would be very flexible and very suitable to our project, cause some students may need to submit their thesis but others don't, 
# or some students have competition record but others don't. 
# Eventually, our web project went very well, it can smoothly search specific student's profile very quickly and correctly, 
# even when the database is very big and everyone's profile is different.

# beyond expectation
# • Tell me about a time when you went way beyond the scope of the project and delivered.
# When I was building the student tracking system, when the first version was delivered with only pdf file can be uploaded, 
# I was starting to think about other file formats to be uploaded and saved. But each file format has its own data storage interface, 
# so we need to build specific api for them to store. So the end users can choose any format they want to uplaod. 
# Eventually, by using google cloud api, we can realize the need for the users. After making a new release, they all feel satisfied with that.

# Dive Deep
# •Give me two examples of when you did more than what was required in any job experience.
# When I built the student tracking system project, we have created student's profile page or dashboard, 
# however I found it would be tedious for students or teachers to type in all the information into the profile fields, 
# so I search a little bit to find a solution to solve this issue. 
# And, I create csv parsor to automatically load all the information to our database and we just need to upload a csv file that include all the information of students. 
# So, it can save tons of time of users.
# Another is creating a file upload system which can upload any kind of file format while the original requrement is just pdf format.


# • Tell me about a time when you had to tell someone a harsh truth.
# It's a hard question, when I led student tracking system project, 
# I found one of our teamate was slacked that did't reply other's email promptly and delay whole project many days, 
# being a leader I must say the harsh truth to the person cause he had already made other teammates anxious and nervous. 
# Some people may say I'm so harsh, but I have told him if he needs any help, he needs to tell us and we could deal it together, 
# what let me unconfortable is no any communication between him and us, and that doesn't solve any question, 
# so I decided to tell him if he somewhat did't respond to our questions anymore we should report this kind of behavior to our professor.


# Couldn’t finish tasks before deadline
# I remember last time I was building the document storage system of the course project, my original schedule is one week, 
# but my course professor suddenly sent me an email said that he needs to show a demo to another teacher two days later. 
# One core feature of the demo is the document storage system. So I was asked to realize the function before two days deadline. 
# If I still follow the original schedule, I definitely can not finish that. My original schedule is to implement the document storage system under our university web domain . 
# But I can not finish that in such a short time. So I figured out another temporary solution with my professor, is to make it run by integrating google cloud drive api. 
# If you run it, it will behave like the normal document storage system, so for the demo, the customer will have exactly the same experience. 
# And I can also finish that before deadline. After that, I can make it stored under private domain.
# If I couldn’t finish tasks before deadline, I will discuss with my teamates, trying to figure out a way that can improve the efficiency and If necessary, 
# I will use my private time to keep working on the task. After all, finishing the task with high quality as soon as possible is what we want. 
# I’ll never sacrifice the customer experience or the quality of the product because of that. Customer experience is always the most important. 
# We must make sure that the product we are gonna deliver is qualified. We can sacrifice our own time to try to finish the tasks. 
# If we still can not finish the tasks, we will communicate with customers and related people, to tell them why and earn their trust. At the same time, 
# we will try our best to finish the tasks as soon as possible.











array和list的区别。arraylist和linkedlist的区别以及各自常用操作的时间复杂度，hashmap是怎么实现的，冲突怎么处理，stack和queue区别，怎么实现，常见api时间复杂度

In python
Similarities between Lists and Arrays
Both are used for storing data
Both are mutable
Both can be indexed and iterated through
Both can be sliced

# Differences
# The main difference between these two data types is the operation you can perform on them. 
# Arrays are specially optimised for arithmetic computations so if you’re going to perform similar operations you should consider using an array instead of a list.
# Also lists are containers for elements having differing data types but arrays are used as containers for elements of the same data type.

# In java
# An array is basic functionality provided by Java. ArrayList is part of collection framework in Java. 
# Therefore array members are accessed using [], while ArrayList has a set of methods to access elements and modify them.
# You can't remove an element from the basic Java array. Take a look at various Collections and ArrayList instead.

# Array is a fixed size data structure while ArrayList is not. One need not to mention the size of Arraylist while creating its object. 
# Even if we specify some initial capacity, we can add more elements.

# Array can contain both primitive data types as well as objects of a class depending on the definition of the array. 
# However, ArrayList only supports object entries, not the primitive data types.

# Since ArrayList can’t be created for primitive data types, members of ArrayList are always references to objects at different memory locations (See this for details). 
# Therefore in ArrayList, the actual objects are never stored at contiguous locations. References of the actual objects are stored at contiguous locations.
# In array, it depends whether the arrays is of primitive type or object type. 
# In case of primitive types, actual values are contiguous locations, but in case of objects, allocation is similar to ArrayList.
# Java ArrayList supports many additional operations like indexOf(), remove(), etc. These functions are not supported by Arrays.

# ARRAYLIST vs linkedlist: 
# In java, this class uses a dynamic array to store the elements in it. With the introduction of generics, this class supports the storage of all types of objects.
# Manipulating ArrayList takes more time due to the internal implementation. Whenever we remove an element, internally, the array is traversed and the memory bits are shifted.
# This class implements a List interface. Therefore, this acts as a list.
# This class works better when the application demands storing the data and accessing it.

# Linkedlist:
# This class uses a doubly linked list to store the elements in it. Similar to the ArrayList, this class also supports the storage of all types of objects.
# Manipulating LinkedList takes less time compared to ArrayList because, in a doubly-linked list, there is no concept of shifting the memory bits. 
# The list is traversed and the reference link is changed.
# This class implements both the List interface and the Deque interface. Therefore, it can act as a list and a deque.
# This class works better when the application demands manipulation of the stored data.


# queue vs stack
# A Queue is a linear structure that follows a particular order in which the operations are performed. 
# The order is First In First Out (FIFO). A good example of a queue is any queue of consumers for a resource where the consumer that came first is served first. 
# The difference between stacks and queues is in removing. In a stack we remove the item the most recently added; in a queue, we remove the item the least recently added.

# A Stack is a linear data structure in which elements can be inserted and deleted only from one side of the list, 
# called the top. A stack follows the LIFO (Last In First Out) principle, i.e., the element inserted at the last is the first element to come out. 
# The insertion of an element into the stack is called push operation, and the deletion of an element from the stack is called pop operation. 
# In stack, we always keep track of the last element present in the list with a pointer called top.


# Collision Resolution

# One method for resolving collisions looks into the hash table and tries to find another open slot to hold the item that caused the collision. 
# A simple way to do this is to start at the original hash value position and then move in a sequential manner through the slots until we encounter the first slot that is empty. 
# Note that we may need to go back to the first slot (circularly) to cover the entire hash table. 
# This collision resolution process is referred to as open addressing in that it tries to find the next open slot or address in the hash table. 
# By systematically visiting each slot one at a time, we are performing an open addressing technique called linear probing.
# A disadvantage to linear probing is the tendency for clustering; items become clustered in the table. This means that if many collisions occur at the same hash value, 
# a number of surrounding slots will be filled by the linear probing resolution.
# One way to deal with clustering is to extend the linear probing technique so that instead of looking sequentially for the next open slot, we skip slots, 
# thereby more evenly distributing the items that have caused collisions. This will potentially reduce the clustering that occurs
# The general name for this process of looking for another slot after a collision is rehashing. 

# With simple linear probing, the rehash function is 𝑛𝑒𝑤ℎ𝑎𝑠ℎ𝑣𝑎𝑙𝑢𝑒=𝑟𝑒ℎ𝑎𝑠ℎ(𝑜𝑙𝑑ℎ𝑎𝑠ℎ𝑣𝑎𝑙𝑢𝑒) where 𝑟𝑒ℎ𝑎𝑠ℎ(𝑝𝑜𝑠)=(𝑝𝑜𝑠+1)%𝑠𝑖𝑧𝑒𝑜𝑓𝑡𝑎𝑏𝑙𝑒. 
# The “plus 3” rehash can be defined as 𝑟𝑒ℎ𝑎𝑠ℎ(𝑝𝑜𝑠)=(𝑝𝑜𝑠+3)%𝑠𝑖𝑧𝑒𝑜𝑓𝑡𝑎𝑏𝑙𝑒. In general, 𝑟𝑒ℎ𝑎𝑠ℎ(𝑝𝑜𝑠)=(𝑝𝑜𝑠+𝑠𝑘𝑖𝑝)%𝑠𝑖𝑧𝑒𝑜𝑓𝑡𝑎𝑏𝑙𝑒. 
# It is important to note that the size of the “skip” must be such that all the slots in the table will eventually be visited. Otherwise, 
# part of the table will be unused. To ensure this, it is often suggested that the table size be a prime number. 

# An alternative method for handling the collision problem is to allow each slot to hold a reference to a collection (or chain) of items. 
# Chaining allows many items to exist at the same location in the hash table. When collisions happen, the item is still placed in the proper slot of the hash table. 
# As more and more items hash to the same location, the difficulty of searching for the item in the collection increases.
# When we want to search for an item, we use the hash function to generate the slot where it should reside. 
# Since each slot holds a collection, we use a searching technique to decide whether the item is present. 
# The advantage is that on the average there are likely to be many fewer items in each slot, so the search is perhaps more efficient. 機率

# A critical statistic for a hash table is the load factor, defined as = n/k
# where, n is the number of entries occupied in the hash table, k is the number of buckets.
# As the load factor grows larger, the hash table becomes slower, and it may even fail to work (depending on the method used). 
# The expected constant time property of a hash table assumes that the load factor be kept below some bound. 
# For a fixed number of buckets, the time for a lookup grows with the number of entries, and therefore the desired constant time is not achieved. 
# In some implementations, the solution is to automatically grow (usually, double) the size of the table when the load factor bound is reached, 
# thus forcing to re-hash all entries. As a real-world example, the default load factor for a HashMap in Java 10 is 0.75, 
# which "offers a good trade-off between time and space costs.













