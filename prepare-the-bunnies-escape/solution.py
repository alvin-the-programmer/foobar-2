def solution(grid):
  height = len(grid)
  width = len(grid[0])
  goal = (height - 1, width - 1)

  start_node = (0, 0, True)
  queue = [start_node]
  touched = set([start_node])

  count = 1
  while len(queue) > 0:
    next_queue = []
    for node in queue:
      if node[0:2] == goal:
        return count
      for neighbor in get_neighbors(grid, node):
        if neighbor not in touched:
          touched.add(neighbor)
          next_queue.append(neighbor)
    queue = next_queue
    count += 1
  
  return None

def get_neighbors(grid, node):
  row, col, free_wall = node
  height = len(grid)
  width = len(grid[0])
  
  neighbors = []
  deltas = [ (-1, 0), (0, 1), (1, 0), (0, -1) ]
  for d_row, d_col in deltas:
    neighbor_row = row + d_row
    neighbor_col = col + d_col

    if (0 <= neighbor_row < height) and (0 <= neighbor_col < width):
      if grid[neighbor_row][neighbor_col] == 0:
        neighbors.append((neighbor_row, neighbor_col, free_wall))
      elif grid[neighbor_row][neighbor_col] == 1 and free_wall:
        neighbors.append((neighbor_row, neighbor_col, False))
    
  return neighbors

grid_1 = [
  [0, 1, 1, 0], 
  [0, 0, 0, 1], 
  [1, 1, 0, 0], 
  [1, 1, 1, 0]
]


result_1 = solution(grid_1) # 7
print(result_1)



grid_2 = [
  [0, 0, 0, 0, 0, 0], 
  [1, 1, 1, 1, 1, 0], 
  [0, 0, 0, 0, 0, 0], 
  [0, 1, 1, 1, 1, 1], 
  [0, 1, 1, 1, 1, 1], 
  [0, 0, 0, 0, 0, 0]
]

result_2 = solution(grid_2) # 11
print(result_2)
