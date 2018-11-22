## Backtracking

Backtracking is a variant of depth-first-search.

### Characteristics

* The LIFO principle is applied to node generation—as opposed to node expansion in DFS.
* When selecting a node n for exploration, only one of its direct successors n′ is generated.
* If n′ fulfills the termination criterion, ⊥ (n′) = True, backtracking is invoked 
and search is continued with the next non-expanded successor of n.
