`Date: 2021/05/30 Sunday` 
`Location: SW`

**Notes:**
1. What is Algorithm? algebra; operations; pseudocode; structural English
2. Model of computation specifies what operations an alg allow; cost (time ...) of each op
    1) Example 1 - Random Access Machine (RAM)
        - Random Access Memory
        - Modeled by big array
        - In O(1) time, alg can load O(1) words; do O(1) computation; store O(1) words
        - O(1) registers
    2) Example 2 (more abstract)
        - dynamically allocated objects
        - object has O(1) fields
        - field = word (e.g. int) or pointer to object or None
3. Python Model:
    1) List, e.g. L[i] = L[j] + 5. O(1) time
    2) Object with O(1) attributes e.g. x = x.next take O(1) TIME
    3) L.append(x), use table doubling tech (L9); O(1) time
    4) L = L(1) + L(2), this concation take O(1+|l1|+|l2|) time


stopped at 25'35"
