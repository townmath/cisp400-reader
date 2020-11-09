..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: binsry search trees

Binary Search Trees
=================== 
A binary tree T is a binary search tree if, for each node ``n``
with sub-trees ``left`` and ``right``,

- The value in ``n`` is **greater than** the values in every node in ``left``.
- The value in ``n`` is **less than** the values in every node in ``right``.
- Both ``left`` and ``right`` are binary search trees.

These assertions define the **binary tree property**.

.. digraph:: a_bst
   :alt: Is this a binary search tree

   graph [
          nodesep=0.25, ranksep=0.3, splines=line;
          labelloc=b;
          label="Is this a binary search tree?";
       ];
   node [fontname = "Bitstream Vera Sans", fontsize=14,
         style=filled, fillcolor=lightblue,
         shape=circle, fixedsize=true, width=0.3];
   edge [weight=1, arrowsize=0.5, dir=none];

   a, b, am, c, d, bm, f, l, cm, dm, fm, m;
   am, bm, cm, dm, fm [style=invis, label=""];

   a [label=30]
   b [label=20]
   d [label=10]

   c [label=70]
   f [label=50]
   l [label=40]
   m [label=60]

   a->b 
   a->c;
   b->d [weight=2]; // nudge b: trees b & c are not balanced
   c->f
   f->l,m;

   edge [style=invis, weight=100];
   d->dm; 
   b->bm;
   f->fm;
   c->cm;
   a->am;

.. reveal:: reveal-bst-1
   :showtitle: Is this a BST?

   Yes.

   Each node is greater than or equal to all of its left descendants,
   and is less than or equal than all of its right descendants.

The Binary Search Tree ADT
--------------------------
Structurally, a BST contains pointers to it's left and right children.
As discussed in :doc:`../recursion/index`,
a binary tree can be implemented simply as a recursive data structure.
A binary search tree can also be implemented recursively.

It is a bit simpler to define the tree nodes as a separate type.
Whether you design this class as a completely independent
class, like this one,
or implement it as a nested (inner) class, is largely a matter of
choice.

Since a ``tree_node`` is a data structure that can exist independently
of a tree that enforces the binary search tree property,
it makes sense in this case to define it as a completely separate
struct with no invariants.

The ``tree_node`` encapsulates the general characteristics
common to all binary trees:

- A variable to store the node value
- Pointers to the left and right child nodes,
  which might themselves be sub-trees.
- We are adding an additional pointer to the parent node.

  Every tree node except for the root contains exactly 1 parent node.

  A parent pointer makes tree iterating more flexible as we
  will see later.


.. code-block:: cpp

   namespace mesa {
     namespace tree {

      // a binary tree node
      template<class T>
        struct tree_node {
          T value;
          tree_node<T>* left;
          tree_node<T>* right;
          tree_node<T>* parent; // link to parent simplifies iterators
          tree_node(const T& value = T{}, 
              tree_node<T>* left = nullptr,
              tree_node<T>* right = nullptr,
              tree_node<T>* parent = nullptr)
            : value{value}
          , left{left}
          , right{right}
          , parent{parent}
          { }
        };
     } // end namespace tree
   } // end namespace mesa

In other words, a ``tree_node`` is a general purpose
binary tree data structure and has no knowledge of
any binary search tree properties or behavior.

.. admonition:: Binary Search Tree Traversal

   One benefit of a binary search tree is that when the
   nodes are visited using infix traversal,
   the data is sorted ascending.

   .. code-block:: cpp
    
      // write a tree to an output stream, infix
      template <class T>
         std::ostream& operator<< (std::ostream& os, const mesa::tree::tree_node<T>* node)
         {
           if (node == nullptr) return os;
           os << node->left; 
           os << node->value << ' ';
           os << node->right;
           return os;
         }

   Notice we stream ``tree_node`` objects here,
   not ``bstree`` objects.

Much like our earlier tree objects, all of the functions used to manipulate
a ``tree_node`` will be free functions.
To avoid collision with other similarly named functions,
all the functions will be defined in the ``mesa::tree`` namespace.

The binary search tree is built up from individual ``tree_node`` objects.

The ``bstree`` class has 1 private member variable: a pointer
to a ``tree_node``.
The basic skeleton of the class should look familiar:

.. code-block:: cpp

   namespace mesa {

     // a binary search tree
     template<class T>
       class bstree {
         public:
           typedef T value_type;

           bstree() = default;
           // convert a value into a tree
           explicit
             bstree(const T& value)
             : root{new tree::tree_node<T>{value}}
           { }

           // copy construct and assign
           bstree(const bstree& other);
           bstree& operator=(const bstree& other);

           // move construct and assign
           bstree(bstree&& other);
           bstree& operator=(const bstree&& other);

           constexpr
             bool empty() const noexcept { return root == nullptr; }

         private:
           tree::tree_node<T>* root = nullptr;

       };

   } // end namespace mesa

Our primary focus for the rest of this section is on the functions
that define the key operations associated with a BST:

- contains
- insert
- erase


We always search a binary search tree by comparing the value we’re
searching for to the 'current' node value. 
If the target value is smaller,
then we search the left subtree. 
If the target value is larger, then we search the right subtree.









-----

.. admonition:: More to Explore

   - Wikipedia

     - `binary search tree <https://en.wikipedia.org/wiki/Binary_search_tree>`__

   - `Binary tree visualizer <http://btv.melezinek.cz>`__

