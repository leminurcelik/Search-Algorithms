from algorithms.base import SearchAlgorithmBase

class ASTAR(SearchAlgorithmBase):
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
        self._backtracking = {}

    def findPathCost(self, current_position):
        start_in_reverse = current_position
        path_cost = 0
        while(start_in_reverse != self._start):
            start_in_reverse = self._backtracking[start_in_reverse]
            path_cost += 1
        return path_cost

    def findPath(self):
        start_in_reverse = self._goal
        self._path.insert(0, start_in_reverse)
        while(start_in_reverse != self._start):
            self._path.insert(0, self._backtracking[start_in_reverse])
            start_in_reverse = self._backtracking[start_in_reverse]

    def heuristic(self, current_position):
        heuristic_distance = abs(self._goal[0] - current_position[0]) + abs(self._goal[1] - current_position[1]) 
        return heuristic_distance
    
    def step(self):
        if not self._frontier:
            self._frontier.append(self._start)
        
        minimum_length = self.findPathCost(self._frontier[0]) + self.heuristic(self._frontier[0])
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
            self._explored.append(current_position)
            return
        
        else:
            for direction in directions:
                next_position = (current_position[0] + direction[0], current_position[1] + direction[1])

                if (self._grid[next_position] != 1 and 
                    next_position not in self._explored and
                    next_position not in self._frontier):

                    self._frontier.append(next_position)
                    self._backtracking[next_position] = current_position

        self._explored.append(current_position)