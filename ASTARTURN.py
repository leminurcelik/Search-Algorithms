from algorithms.base import SearchAlgorithmBase

class ASTARTURN(SearchAlgorithmBase): 
    def __init__(self) -> None:
        super().__init__()
        self._backtracking = {}
        

    def reset(self, grid, start, goal):
        self._grid = grid
        self._start = start
        self._goal = goal
        self._frontier = []
        self._explored = []
        self._path = []
        self._cost = 0
        self._done = False
        
    def findPathCost(self, current_position):
        reverse_cost_start = current_position
        pathCost = 0
        while(reverse_cost_start != self._start):
            reverse_cost_start = self._backtracking[reverse_cost_start]
            pathCost += 1
        return pathCost
    
    def findPath(self):
        start_in_reverse = self._goal
        self._path.insert(0, start_in_reverse)
        while(start_in_reverse != self._start):
            self._path.insert(0, self._backtracking[start_in_reverse])
            start_in_reverse = self._backtracking[start_in_reverse]

    def heuristic(self, current_position):
        not_empty = len(self._backtracking)
        if(not_empty > 0):
            turningCost = 0
            turning =- 1
            previousTurning =- 2
            new_current = current_position
            while(current_position != self._start):
                previous_position = self._backtracking[current_position]
                dx = current_position[0] - previous_position[0]
                if dx == 0:
                    turning = 1
                else:
                    turning = 0

                if(previousTurning != turning):
                    turningCost += 1
                
                previousTurning = turning
                current_position = previous_position

            heuristic_distance_with_turning = turningCost + abs(self._goal[0] - new_current[0]) + abs(self._goal[1] - new_current[1]) 
            return heuristic_distance_with_turning
        else:
            heuristic_distance = abs(self._goal[0] - current_position[0]) + abs(self._goal[1] - current_position[1]) 
            return heuristic_distance 

    
    def step(self):
        if self._frontier == []:
            self._frontier.append(self._start)
        
        minimum_length = self.heuristic(self._frontier[0]) + self.findPathCost(self._frontier[0])
        node = 0
        for n in range(0, len(self._frontier)):
            if(self.heuristic(self._frontier[n]) + self.findPathCost(self._frontier[n]) < minimum_length):
                minimum_length = self.heuristic(self._frontier[n]) + self.findPathCost(self._frontier[n])
                node = n

        current_position = self._frontier.pop(node)

        directions = [
            (1, 0),   
            (0, -1),  
            (-1, 0),  
            (0, 1)   
        ]

        if(current_position == self._goal):
            self.findPath()
            self._cost = len(self._path)
            self._done = True
            return
        
        for direction in directions:
                next_position = (current_position[0] + direction[0], current_position[1] + direction[1])

                if (next_position not in self._explored and
                        next_position not in self._frontier and
                        self._grid[next_position] != 1):
                    self._frontier.append(next_position)
                    self._backtracking[next_position] = current_position

        self._explored.append(current_position)