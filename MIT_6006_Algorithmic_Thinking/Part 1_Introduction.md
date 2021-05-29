
Date: 2021/05/29 Saturday
Location: SW
Notes:
1. Course Overview: Efficient procedures to solve large-scale problems; Scalability; Classic data structures (classic algorithms); Real implementation
2. Content - 8 modules & Problem set
  1) Algorithm thinking -> Peak findings
  2) Sorting & Trees -> Event Simulation
  3) Hashing -> Genome Algorithm
  4) Numerics -> RSA encryption (SSL)
  5) Graphs -> Rubik's cube
  6) Shortest Paths -> Caltech to MIT
  7) Dynamic Programming -> Image Compression
  8) Advanced Topics if you'd like to continue
 
3. Peak Finding Problems - Binary Search
  1）One dimension version: 
 
    | a | b | c | d | e | f | g | h | i |
    | - | - | - | - | - | - | - | - | - |
    
    Position 2 is peak iff b>=a and b>=c.
    
    Problem: find the peak if it exists (actually always exist)
    
    Solution 1: Walk through one by one from left to right -> O(n) -> Can we get better?
    
    Solution 2: Start from the middle [n/2]. Move the left if position [n/2]-1 is bigger than position [n/2] else if [n/2]+1 bigger move to the right else [n/2]. Base case is one element then O(1). T(n) = T(n/2) + O(1) = SUM OF log_2(n) O(1) = O(log_2(n))
    
   2) Two dimension version: a is peak iff a is no less than all of b,c,d,e
   
    |   |   |   |   |   |   |   |   |   |
    | - | - | - | - | - | - | - | - | - |
    |   |   |   |   | c |   |   |   |   |
    |   |   |   | b | a | d |   |   |   |
    |   |   |   |   | e |   |   |   |   |
    |   |   |   |   |   |   |   |   |   |
    
    Solution 1: Greedy ascent algorithm - O(mn) supposing n rows, m columns
    Solution 2: Binary search - 1) Pick a column j = m/2 and find the global max (i,j) of column j. 2) Find the peak of row i from (i,j). 3) Base case: only one column
      T(n,m) = O(n) + T(n,m/2) = SUM OF log_2(m) O(n) = O(nlog_2(m))
