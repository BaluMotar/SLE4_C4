# SLE-3 Viva / Oral Preparation

1. What is SLE-3?
SLE-3 is an architectural design task using the Full C4 Model.

2. What is C4?
C4 means Context, Container, Component and Code.

3. What does Level 1 show?
The system, user and important external interactions.

4. What does Level 2 show?
The major building blocks or containers inside the system.

5. What does Level 3 show?
The smaller internal parts of one important container.

6. What does Level 4 show?
Main classes and functions, not large source code.

7. Why did you choose BFS/DFS Maze Search?
It continues the SLE-2 search/maze work and is recommended by the SLE-3 guideline.

8. What is BFS?
Breadth-First Search explores nodes level by level and normally uses a queue.

9. What is DFS?
Depth-First Search explores deeply along a path before backtracking and normally uses a stack or recursion.

10. What is the Search Engine?
It runs the selected BFS or DFS search algorithm.

11. What is the Frontier?
It stores discovered nodes that are waiting to be explored.

12. What is a Visited Set?
It stores already explored states to avoid repeated processing.

13. What is Goal Test?
It checks whether the current state is the required goal.

14. What is Path Reconstruction?
It rebuilds the final path using stored parent/path information.

15. Why only one container at Component level?
To keep the architecture simple and readable, as required by the guideline.

16. What is a design decision?
A reason explaining why the system was organized in a particular way.

17. What did AI help you with?
Understanding C4, organizing diagrams and preparing explanations. I reviewed and understood the final design.

30-second presentation:
“My project is a BFS/DFS Maze Search System. The user provides a maze, start and goal information, and selects a search method. The Search Engine runs BFS or DFS, Visited Memory prevents repeated exploration, and the Output Module provides the result. I represented the system using all four C4 levels: Context, Container, Component and Code.”
