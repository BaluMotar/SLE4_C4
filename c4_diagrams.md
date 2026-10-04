# C4 Diagrams — BFS/DFS Maze Search

## Level 1 — Context
User → BFS/DFS Maze Search System → Path/Search Result

## Level 2 — Container
User → Input Module → Search Engine → Output Module
                         ↓
                    Visited Memory

## Level 3 — Components inside Search Engine
Search Engine contains:
- Frontier
- Explored / Visited Set
- Goal Test
- Path Reconstructor

## Level 4 — Code
- Node
- Maze
- bfs()
- dfs()
- goal_test()
- reconstruct_path()
