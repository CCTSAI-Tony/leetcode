'''
Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.

Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.

When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

Example:

Given width = 3, height = 2, and food = [[1,2],[0,1]].

Snake snake = new Snake(width, height, food);

Initially the snake appears at position (0,0) and the food at (1,2).

|S| | |
| | |F|

snake.move("R"); -> Returns 0

| |S| |
| | |F|

snake.move("D"); -> Returns 0

| | | |
| |S|F|

snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )

| |F| |
| |S|S|

snake.move("U"); -> Returns 1

| |F|S|
| | |S|

snake.move("L"); -> Returns 2 (Snake eats the second food)

| |S|S|
| | |S|

snake.move("U"); -> Returns -1 (Game over because snake collides with border)
'''

#time complexity MOVE O(1), space complexity O(n)
#思路: 使用deque 來添加newhead, 若move = food[0], 把food變成new_head添加進去身體, 若沒有吃到food, 每move, 添加newhead, 身體的尾端pop掉(維持長度)
#注意: 貪吃蛇吃到身體or 越界 => game over => 但吃掉尾端ㄧ格不會有事, 如何判斷有無吃到身體, 看是否newhead in self.snake
#注意: (1,1) != [1,1], 因為food 裡面是用list, 所以為了一致, self.snake and self.food 全部也用list=> [x, y] 而不是(x, y)
class SnakeGame(object):
    def __init__(self, width,height,food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.snake = collections.deque([[0,0]])    # snake head is at the front
        self.width = width
        self.height = height
        self.food = collections.deque(food)
        self.direct = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}
        

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        newHead = [self.snake[0][0]+self.direct[direction][0], self.snake[0][1]+self.direct[direction][1]]
        
        # notice that the newHead can be equal to self.snake[-1]
        if (newHead[0] < 0 or newHead[0] >= self.height) or (newHead[1] < 0 or newHead[1] >= self.width) or (newHead in self.snake and newHead != self.snake[-1]): 
            #吃到自己的身體 return -1
            return -1

        if self.food and self.food[0] == newHead:  # eat food,  水果是否吃完了, if self.food 確認
            self.snake.appendleft(newHead)   # just make the food be part of snake
            self.food.popleft()   # delete the food that's already eaten
        else:    # not eating food: append head and delete tail                 
            self.snake.appendleft(newHead)   
            self.snake.pop()   
            
        return len(self.snake)-1





#重寫第二次, time complexity move O(1), space complexity O(n)
from collections import deque
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.snake = deque([(0,0)])
        self.food = deque(food)
        self.width = width
        self.height = height
        self.direc = {"U": (-1, 0), "L": (0, -1), "R": (0, 1), "D": (1, 0)}
        
        

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        newHead = (self.snake[0][0] + self.direc[direction][0], self.snake[0][1] + self.direc[direction][1])
        if newHead[0] < 0 or newHead[0] >= self.height or newHead[1] < 0 or newHead[1] >= self.width or \
        (newHead in self.snake and newHead != self.snake[-1]):
            return  -1
        if self.food and list(newHead) == self.food[0]:
            self.food.popleft()
            self.snake.appendleft(newHead)
        else:
            self.snake.appendleft(newHead)
            self.snake.pop()
        return len(self.snake) - 1














