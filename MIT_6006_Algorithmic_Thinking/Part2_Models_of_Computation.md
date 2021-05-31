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
3. Python Model 1:
    1) List, e.g. L[i] = L[j] + 5. O(1) time
    2) Object with O(1) attributes e.g. x = x.next take O(1) TIME
    3) L.append(x), use table doubling tech (L9); O(1) time
    4) L = L(1) + L(2), this concation take O(1+|l1|+|l2|) time


`Date: 2021/05/31 Monday` 
`Location: SW`

**Notes (Continued):**

4. Python Model 2:
    1) `x in L` , this take O(1+|l1|+|l2|) time
    2) `len(L)` , this take O(1) time - python has a counter
    3) `L.sort()` , this take O(|L|log_2(|L|)) time - in L3, python uses comparison sort
    4) dict: `D[key]=val`, this takes O(1) with high probability (w.h.p) - in L8~10
    5) long: x+y takes O(|x|+|y|); xy takes O((|x|+|y|)^(log_2(3))) time - in L11
    6) heapq: in L4
    
5. Document Distance Problem: motivation, algorithm, methods, time complexity etc. Note: re.findall(r'\wt', doc) - exponential time (use with caution)    
