Count Inversions of size three in a given array
Difficulty Level : Hard
Last Updated : 30 Jan, 2019
Given an array arr[] of size n. Three elements arr[i], arr[j] and arr[k] form an inversion of size 3 if a[i] > a[j] >a[k] and i < j < k. 
Find total number of inversions of size 3.

Example :

Input:  {8, 4, 2, 1}
Output: 4
The four inversions are (8,4,2), (8,4,1), (4,2,1) and (8,2,1).

Input:  {9, 6, 4, 5, 8}
Output:  2
The two inversions are {9, 6, 4} and {9, 6, 5}

# use binary search tree

def getSum(BITree, index):
    sum = 0 # Initialize result 
      
    # Traverse ancestors of BITree[index] 
    while (index > 0): 
  
        # Add current element of 
        # BITree to sum 
        sum += BITree[index] 
  
        # Move index to parent node 
        # in getSum View 
        index -= index & (-index) 
  
    return sum
  
# Updates a node in Binary Index Tree 
# (BITree) at given index in BITree.
# The given value 'val' is added to BITree[i] 
# and all of its ancestors in tree. 
def updateBIT( BITree, n, index, val):
  
    # Traverse all ancestors and add 'val' 
    while (index <= n): 
  
        # Add 'val' to current node of BI Tree 
        BITree[index] += val 
  
        # Update index to that of parent 
        # in update View 
        index += index & (-index) 
  
# Converts an array to an array with values 
# from 1 to n and relative order of smaller 
# and greater elements remains same. For example, 
# 7, -90, 100, 1 is converted to 3, 1, 4 ,2 
def convert(arr, n) :
  
    # Create a copy of arrp[] in temp and 
    # sort the temp array in increasing order 
    temp = [0] * n 
    for i in range(n):
        temp[i] = arr[i] 
    temp = sorted(temp)
    j = 1
      
    # Traverse all array elements 
    for i in temp: 
  
        # lower_bound() Returns poer to 
        # the first element greater than
        # or equal to arr[i] 
        arr[arr.index(i)] = j
        j += 1
  
# Returns count of inversions of size three 
def getInvCount( arr, n):
  
    # Convert arr[] to an array with values 
    # from 1 to n and relative order of smaller 
    # and greater elements remains same. For example,
    # 7, -90, 100, 1 is converted to 3, 1, 4 ,2 
    convert(arr, n) 
  
    # Create and initialize smaller and 
    # greater arrays 
    greater1 = [0] * n
    smaller1 = [0] * n 
    for i in range(n):
        greater1[i], smaller1[i] = 0, 0
  
    # Create and initialize an array to 
    # store Binary Indexed Tree 
    BIT = [0] * (n + 1) 
    for i in range(1, n + 1): 
        BIT[i] = 0
    for i in range(n - 1, -1, -1):
  
        smaller1[i] = getSum(BIT, arr[i] - 1) 
        updateBIT(BIT, n, arr[i], 1) 
  
    # Reset BIT 
    for i in range(1, n + 1): 
        BIT[i] = 0
  
    # Count greater elements 
    for i in range(n): 
  
        greater1[i] = i - getSum(BIT, arr[i])  #  getSum(BIT, arr[i]), 目前的元素數量(不包含自己) - 計算小於等於自己的元素數目 => 比自己大的元素數目
        updateBIT(BIT, n, arr[i], 1) 
  
    # Compute Inversion count using smaller[] 
    # and greater[]. 
    invcount = 0
    for i in range(n): 
        invcount += smaller1[i] * greater1[i] 
  
    return invcount 
      
# Driver code 
if __name__ =="__main__":
    arr= [8, 4, 2, 1] 
    n = 4
    print("Inversion Count : ", 
           getInvCount(arr, n))




Remove duplicates from an unsorted linked list
time complexity O(n), space complexity O(n)
# Python3 program to remove duplicates
# from unsorted linkedlist
class Node:
     
    def __init__(self, data):
         
        self.data = data
        self.next = None
 
class LinkedList:
     
    def __init__(self):
         
        self.head = None
         
    # Function to print nodes in a 
    # given linked list
    def printlist(self):
         
        temp = self.head
         
        while (temp):
            print(temp.data, end = " ")
            temp = temp.next
             
    # Function to remove duplicates from a
    # unsorted linked list
    def removeDuplicates(self, head):
         
        # Base case of empty list or
        # list with only one element
        if self.head is None or self.head.next is None:
            return head
             
        # Hash to store seen values
        hash = set() 
 
        current = head
        hash.add(self.head.data)
 
        while current.next is not None:
 
            if current.next.data in hash:
                current.next = current.next.next
            else:
                hash.add(current.next.data)
                current = current.next
 
        return head
 
# Driver code
if __name__ == "__main__":
     
    # Creating Empty list
    llist = LinkedList()
    llist.head = Node(10)
    second = Node(12)
    third = Node(11)
    fourth = Node(11)
    fifth = Node(12)
    sixth = Node(11)
    seventh = Node(10)
     
    # Connecting second and third
    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seventh
 
    # Printing data
    print("Linked List before removing Duplicates.")
    llist.printlist()
    llist.removeDuplicates(llist.head)
    print("\nLinked List after removing duplicates.")
    llist.printlist()