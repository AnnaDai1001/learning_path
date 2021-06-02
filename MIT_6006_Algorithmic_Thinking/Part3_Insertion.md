`Date: 2021/06/01 Tuesday` 
`Location: SW`

**Notes:**
1. Why sorting?
    1) Obvious - make sth easier: e.g. find median, binary search
    2) Not Obvious - data compression, computer graphics  
2. Insertion sort - simple but not best
     1) For i=1,2,...,n, insert A[i] into sorted array A[0:(i-1)] by pairwise swaps down to the correct position
     2) 5,2,4,6,1,3 -> 2,5,4,6,1,3 -> 2,4,5,6,1,3 -> not change ->(4 swaps)-> 1,2,4,5,6,3 ->(3 swaps)-> 1,2,3,4,5,6
     3) O(n) steps(key position); each step is O(n) swaps/compares
     4) Complexity: O(n^2)
3. Merge sort - divide & conqur
4. Recurrsion solving 