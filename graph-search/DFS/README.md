# Depth-First-Search (DFS)

Depth-First-Search is an uninformed (systematic) search strategy.
## DFS characteristics
#### Nodes at deeper level in G are preferred
A solution base that is most complete is preferred.

#### The smallest, indivisible (= atomic) step is node expansion
If a node is explored (= reached), all of its direct successors n1, . . . , nk 
are generated at once. Among the n1, . . . , nk one node is chosen for expansion in the next step.

#### If node expansion comes to an end, backtracking is invoked
Node expansion is continued with the deepest node that has non-explored
alternatives.

#### Terminates (on finite, cyclefree graphs) with a solution, if one exists
Caveat: Cyclic paths or infinite paths cannot be handled properly.

### Issues
Search may run deeper and deeper and follow some fruitless path.

### When to use DFS?
Depth-first search can be the favorite strategy in certain situations:

1. We are given plenty of equivalent solutions.
2. Dead ends can be recognized early,i.e.,with a considerable look-ahead.
3. There are no cyclic or infinite paths resp. cyclic or infinite paths can be avoided.

---
####Remarks 
* Operationalization of DFS: The OPEN list is organized as a stack, i.e., nodes are explored in
a LIFO (last in first out) manner.

* The depth in trees is a naturally defined: The most recently generated node is also a deepest node.

* The DFS paradigm requires that a node will not be expanded as long as a deeper node is on the OPEN list.