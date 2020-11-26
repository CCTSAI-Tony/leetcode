'''
Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. 
(coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).


Example 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.
 

 

Example 2:

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.
 

 

Example 3:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.
 

 

Example 4:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.
'''

#time complexity O(n)
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        """
        Idea is from Huahua jiang,
        The main idea is that except the four corners of perfect square, all other corners of sub rectangles all
        appeare even times
        """
        corners = set()
        area = 0
        for rect in rectangles:
            p1 = (rect[0], rect[1])
            p2 = (rect[0], rect[3])
            p3 = (rect[2], rect[1])
            p4 = (rect[2], rect[3])
            for p in [p1, p2, p3, p4]:
                if p in corners:
                    corners.remove(p)
                else:
                    corners.add(p)
            area += (p4[0] - p1[0]) * (p4[1] - p1[1])  #each rectangle area
        
        if len(corners) != 4: #only left four corners of perfect square, 順便過濾這個case [[0,0,4,1],[0,0,4,1]] 以免p1, p4 = corners[0], corners[-1] list index out of range
            return False
        corners = sorted(list(corners))  #sorted() 會針對tuple裡元素做排序
        p1, p4 = corners[0], corners[-1]
        return area == (p4[0] - p1[0]) * (p4[1] - p1[1])  #why we need to confirm the area? [[1,1,2,2],[1,1,2,2],[2,1,3,2]] avoid overlapping




# a = set()
# a
# {1, 2, 3, 4, 5}
# a.remove(3)
# a
# {1, 2, 4, 5}

# d = [(1,1000),(1,10),(1,100),(2,0)]
# sorted(d)
# [(1, 10), (1, 100), (1, 1000), (2, 0)]


































