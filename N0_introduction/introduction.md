## Algorithm

> An **algorithm** is a set of well-defined instructions to solve a particular problem. 
> It takes a set of input and produces a desired output

### Qualities of Good Algorithms

1. (Precise) Input and output should be defined precisely.
2. (Clear) Each step in the algorithm should be clear and unambiguous.
3. (Optimized) Algorithm should be most effective among many different ways to solve a problem.
4. (Abstract) An algorithm shouldn't include computer code. Instead, the algorithm should be written in such a way that it can be used in different programming languages (pseudocode).



## Data Structure and Types

> **Data Structure** is a storage that is used to store and organize data. It is a way of arranging data on a computer so that it can be accessed and updated efficiently.
>
> It is the collection of **data types** arranged in a specific order.

Basically, data structures are divided into two categories: Linear and non-linear.

1. Linear: elements are arranged in sequence one after the other.
- `Array`: elements in memory are arranged in continuous memory. All the elements of an array are of the same type.
- `Stack`: **LIFO**: the last element stored in a stack will be removed first.
- `Queue`: **FIFO**: first element stored in the queue will be removed first.
- `Linked List`: elements are connected through a series of nodes. And, each node contains the data items and address to the next node.

2. Non Linear: arranged in a **hierarchical** manner where one element will be connected to one or more elements.
- `Graph`: In graph data structure, each node is called vertex and each vertex is connected to other vertices through edges.
- `Trees`: imilar to a graph, a tree is also a collection of vertices and edges. However, in tree data structure, there can only be one edge between two vertices.
	- Binary Tree, Binary Search Tree, AVL Tree, B- Tree, B+ Tree, Red-Black Tree

| Linear                      | Non Linear                    |
| --------------------------- | ----------------------------- |
| sequential order            | hierarchical manner           |
| single layer                | different layers              |
| single pass from 1st to end | multiple runs                 |
| not efficient               | efficient depends on the need |
| O increase with size        | O remains the same            |                            |                               |

