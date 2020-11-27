..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: binary search tree; iterators

Binary Search Tree iterators
============================
The recursive traversal algorithms work well for implementing 
tree-based ADT member functions, 
but if we are trying to hide the trees inside some ADT 
for example, using binary search trees to implement std::set
or using STL algorithms or rang-for loops, 
then we need to provide iterators for walking though the contents of the tree.

Iterators for tree-based data structures can be more complicated than those 
for linear structures.

For arrays (and vectors and deques and other array-like structures)
and linked lists, a single pointer can implement an iterator.

Given the current position, it is easy to move forward to the next element.

For anything but a singly-linked list, we can also easily move backwards.

But look at this binary search tree,
and suppose that you were implementing tree iterators as a single pointer.
Let's see if we can "think" our way through the process of traversing this tree
one step at a time,
without needing to keep a whole stack of unfinished recursive calls around.

We're going to try to visit the nodes in the same order we would process them
during an "in-order" traversal.
For a BST, in-order traversal means that we will visit the data in ascending order.

It's not immediately obvious what our data structure for storing the
"current position" (i.e., an iterator) will be.
We might suspect that a pointer to a tree node will be part of 
that data structure, because that worked with iterators over linked lists.

BST iterator ``begin()`` and ``end()``
--------------------------------------
TBD

BST iterator ``operator++()``
-----------------------------
TBD

BST iterator using parent pointers
----------------------------------
TBD

Implementing BST iterators
==========================
TBD

Implementing ``begin()`` and ``end()``
--------------------------------------
TBD

Implementing ``operator++()``
-----------------------------
TBD

BST iterator using parent pointers
----------------------------------
TBD

BST Threads
===========
TBD



-----

.. admonition:: More to Explore

   - The content on this page was adapted from
     `Binary Search Trees <https://www.cs.odu.edu/~zeil/cs361/f16/Public/treetraversal/index.html>`__,
     by Steven J. Zeil for his data structures course CS361.


