import random
import matplotlib.pyplot as plt

def generate_dfs_maze(rows, cols):
    def carve_passages_from(cx, cy, grid):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < cols and 0 <= ny < rows and grid[ny][nx] == 1:
                if sum([grid[ny + dy][nx + dx] == 0 for dx, dy in directions if 0 <= nx + dx < cols and 0 <= ny + dy < rows]) <= 1:
                    grid[cy][cx] = 0
                    grid[ny][nx] = 0
                    carve_passages_from(nx, ny, grid)

    maze = [[1 for _ in range(cols)] for _ in range(rows)]
    carve_passages_from(0, 0, maze)
    maze[0][0] = 0  # Ensure the start point is open
    maze[rows-1][cols-1] = 0  # Ensure the end point is open
    return maze

def plot_maze(maze, start_node=None, end_node=None):
    rows, cols = len(maze), len(maze[0])
    fig, ax = plt.subplots()
    
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1:
                ax.add_patch(plt.Rectangle((j, rows-i-1), 1, 1, facecolor='black', edgecolor='black'))
            else:
                ax.add_patch(plt.Rectangle((j, rows-i-1), 1, 1, facecolor='white', edgecolor='black'))
    
    if start_node:
        ax.add_patch(plt.Rectangle((start_node[1], rows-start_node[0]-1), 1, 1, facecolor='blue', edgecolor='black'))
    
    if end_node:
        ax.add_patch(plt.Rectangle((end_node[1], rows-end_node[0]-1), 1, 1, facecolor='green', edgecolor='black'))
    
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_aspect('equal')
    plt.gca().invert_yaxis()
    plt.show()

# Generate a solvable maze
maze = generate_dfs_maze(20, 20)

# Define start and end nodes
start_node = (0, 0)
end_node = (len(maze)-1, len(maze[0])-1)

# Plot the maze
plot_maze(maze, start_node, end_node)
