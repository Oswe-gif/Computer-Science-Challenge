# Move zeroes:
The script aims to solve the problem called [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/description/).
* Time complexity is O(n) because iterates through the 'nums' list once.
* Space complexity is O(n)
![image](https://github.com/user-attachments/assets/a2e26dd5-6b13-47b4-908f-63bac82352d5)

# Reverse Odd Levels of Binary Tree:
The script aims to solve the problem called [2415. Reverse Odd Levels of Binary Tree](https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/).
* Time complexity is O(n) because we have a loop that iterates through the levels of the binary tree once (the biggest iteration).
![image](https://github.com/user-attachments/assets/abcbee44-8fae-4b03-8bbc-3455ab3446c5)
* Space complexity is O(n + V) where n number of dictionary elements (keys or levels) and V is the vertices  
* Note. On line 30 of the file, ignore this complexity, since it was only used to make it easier for the evaluator to view the graphs. ```print({i: [node.val for node in k] for i, k in levels.items()})```

# Critical Connections in a Network:
The script aims to solve the problem called [1192. Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/description/).
* Time complexity is O(V + E) where V is the number of vertices and E is the number of edges (we visit each vertex and edge).
* Space complexity is O(n+E) where n is nodes and E is edges
![image](https://github.com/user-attachments/assets/141e0d38-b379-4f50-9c3c-7256ae763186)

# Partition Array Into Two Arrays to Minimize Sum Difference:
The script aims to solve the problem called [2035. Partition Array Into Two Arrays to Minimize Sum Difference](https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/description/).
* Time complexity is O(n * 2^n)
* Space complexity is O(2^n)
![image](https://github.com/user-attachments/assets/0e1a963f-95b8-4c83-ba9f-f032d927fd19)
