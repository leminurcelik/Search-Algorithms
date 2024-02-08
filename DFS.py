from algorithms.base import SearchAlgorithmBase

class DFS(SearchAlgorithmBase):
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
    
    def findPath(self):
        start_in_reverse = self._goal
        self._path.insert(0, start_in_reverse)
        while(start_in_reverse != self._start):
            self._path.insert(0, self._backtracking[start_in_reverse])
            start_in_reverse = self._backtracking[start_in_reverse]
    
    def step(self):   
        if not self._frontier:
            self._frontier.append(self._start)   

        current_position = self._frontier[-1]
        
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
        
        else:
            changed = False
            for direction in directions:
                next_position = (current_position[0] + direction[0], current_position[1] + direction[1])

                if (self._grid[next_position] != 1 and next_position
                        not in self._explored and next_position
                        not in self._frontier):

                    self._frontier.append(next_position)
                    self._backtracking[next_position] = current_position
                    changed = True
                    break
                
            if not changed:
                self._frontier.pop(-1)

        self._explored.append(current_position)