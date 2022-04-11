'''
Given a robot cleaner in a room modeled as a grid.

Each cell in the grid can be empty or blocked.

The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.

When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.

Design an algorithm to clean the entire room using only the 4 given APIs shown below.

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
Example:

Input:
room = [
  [1,1,1,1,1,0,1,1],
  [1,1,1,1,1,0,1,1],
  [1,0,1,1,1,1,1,1],
  [0,0,0,1,0,0,0,0],
  [1,1,1,1,1,1,1,1]
],
row = 1,
col = 3

Explanation:
All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.
Notes:

The input is only given to initialize the room and the robot's position internally. You must solve this problem "blindfolded". 
In other words, you must control the robot using only the mentioned 4 APIs, without knowing the room layout and the initial robot's position.
The robot's initial position will always be in an accessible cell.
The initial direction of the robot will be facing up.
All accessible cells are connected, which means the all cells marked as 1 will be accessible by the robot.
Assume all four edges of the grid are all surrounded by wall.
'''

#刷題用這個
#思路: 利用directions x, y 來記錄目前機器人面對的方向, 利用visited 來記錄打掃過的cell
#利用backtrack 的方式返回前一個cell, 並把方向轉成向右轉90 => (0, -1) => (1, 0) => (0, 1) => (-1, 0)
#技巧: 每退回該cell, 方向轉變 => direction_x, direction_y = -direction_y, direction_x
#同一個cell每轉一次方向就代表該方向已打掃完
class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.dfs(robot, 0, 0, 0, -1, set())  #初始是facing up
    
    def dfs(self, robot, x, y, direction_x, direction_y, visited):
        robot.clean()
        visited.add((x, y))
        
        for k in range(4): #四個方向
            neighbor_x = x + direction_x
            neighbor_y = y + direction_y
            if (neighbor_x, neighbor_y) not in visited and robot.move():
                self.dfs(robot, neighbor_x, neighbor_y, direction_x, direction_y, visited) #持續掃
                robot.turnRight()
                robot.turnRight()
                robot.move() #回到前一格
                # 回到當初方向
                robot.turnRight()
                robot.turnRight()
            robot.turnRight()
            direction_x, direction_y = -direction_y, direction_x  #改變前進預知方向


#重寫第二次, time complexity O(N-M) => N: number of cells, M: number of obstacles
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.dfs(robot, 0, 0, 0, -1, set())
        
    def dfs(self, robot, x, y, dirx, diry, visited):
        robot.clean()
        visited.add((x, y))
        for _ in range(4):
            nxt_x, nxt_y = x + dirx, y + diry
            if (nxt_x, nxt_y) not in visited and robot.move():
                self.dfs(robot, nxt_x, nxt_y, dirx, diry, visited)
                robot.turnRight()
                robot.turnRight()
                robot.move()
                robot.turnRight()
                robot.turnRight()
            robot.turnRight()
            dirx, diry = -diry, dirx


# 重寫第三次
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        def dfs(x, y, dir_x, dir_y):
            visited.add((x, y))
            robot.clean()
            for _ in range(4):
                nxt_x, nxt_y = x + dir_x, y + dir_y
                if (nxt_x, nxt_y) not in visited and robot.move():
                    dfs(nxt_x, nxt_y, dir_x, dir_y)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                robot.turnRight()
                dir_x, dir_y = -dir_y, dir_x
        dfs(0, 0, 0, -1)



















