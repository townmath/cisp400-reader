..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   single: heap

Heaps
=====
A :term:`heap` is a special tree-like data structure.
There are many types of heaps, however, in this chapter,
we will discuss only *binary heaps*.
In this section, we will refer to binary heaps merely as heaps. 
Like binary search trees, heaps have two key attributes:

- The underlying tree must be **complete**
- The order of elements must obey the *heap property*

  For a :term:`min heap` a parent element must be ``<=`` all its children.

  For a :term:`max heap` a parent element must be ``>=`` all its children.

One of the side-effects of heap is that the minimum (or maximum)
value can always be found at the tree root.

.. digraph:: min_heap
   :alt: An example min heap
   :align: center

   graph [
          nodesep=0.25, ranksep=0.3, splines=line
          labelloc=b
          label="A min heap"
       ];
   node [fontname = "Bitstream Vera Sans", fontsize=14,
         style=filled, fillcolor=lightblue,
         shape=circle, fixedsize=true, width=0.3]
   edge [weight=1, arrowsize=0.5, dir=none]

   a, b, am, c, d, bm, e, f, cm, g, h, dm, i, j, em
   am, bm, cm, dm, em, fm [style=invis, label=""]

   a->b
   a->c
   b->d [weight=2]; // nudge b: trees b & c are not balanced
   b->e 
   c->f,g
   d->h,i
   e->j

   edge [style=invis, weight=100]
   d->dm
   e->em
   b->bm
   c->cm
   a->am

We can show that a complete binary tree of height :math:`h` has between 
:math:`2h` and :math:`2(h+1) − 1` nodes.
This implies that the height of a complete binary tree is :math:`\lfloor \log N \rfloor`,
which results in :math:`O(\log N)` performance.

Although logically a heap is a tree-like data structure,
because the tree must be complete, it fits easily into an array.
It is very common to use an array for the *physical implementation* of a heap,
since it is much more efficient than a general purpose tree
bound together with pointers.
For a tree of height :math:`2^h - 1`:

- The parent of a node `i` is located at index :math:`\lfloor \frac{i}{2} \rfloor`
- The left child of a node `i` is located at index :math:`2i`
- The right child of a node `i` is located at index :math:`2i + 1`

To get our math to work out nicely, we place the root node at index position 1.
This storage location won't go to waste -- it is used when nodes removed from the
tree and maintaining the heap property is required.

The array representation of the min heap is:

.. graphviz::
   :alt: Array representation of a min heap
   :align: center


   digraph c {
     rankdir=LR
     fontname = "Bitstream Vera Sans"
     label="Array implementation of a min heap"
     node [
        fontname = "Courier"
        fontsize = 14
        shape = "record"
        style=filled
        fillcolor=lightblue
     ]
     arr [
        label = "{ |a|b|c|d|e|f|g|h|i|j| | | }"
     ]

   }

Depending on the implementation,
the backing store may or may not have extra storage.

The heap interface can be implemented as follows:

.. code-block:: cpp

   template <class T, 
          class Container = std::vector<T>
          class Compare = std::greater<typename Container::value_type>>
      // require T is comparable
      class binary_heap
      {
        public:
          using value_type = T;
          using value_compare = Compare;
          static_assert((std::is_same<T, Container::value_type>::value), 
            "heap type must match underlying container value type" );

          binary_heap() = default;

          // Construct a heap from an unsorted container
          explicit binary_heap(const Container& items);

          constexpr void     clear() noexcept;
          constexpr bool     empty() const noexcept;
          constexpr bool      full() const noexcept;
          constexpr size_t    size() const noexcept;
          constexpr const T& front() const noexcept;

          void pop();
          void push (const T& value) noexcept;

        private:
          size_t size_ = 0;
          Container heap_ = {T{}};

          void percolate_down(size_t hole) noexcept;
          void build_heap() noexcept;
          void percolate_up(const T& value) noexcept;

      };

The defining operations of a heap are:

Constructors
   Creates a new underlying container of the container adaptor from a variety of data sources.
   
   Calls ``build_heap`` to ensure the heap property satisfied when 
   construction is complete.

push
   Add a new value to the heap, while maintaining the heap property.

   Calls ``percolate_up`` to perform the work.

pop
   Remove a value while maintaining the heap property.

   Calls ``percolate_down`` to perform the work.

front
   Peek at the heap root element.



In this implementation, any container that implements
``front()``, ``push_back()``, and ``pop_back()`` are candidates
for the backing store. This example uses vector by default.
The Compare class allows the same class to function as either a min heap
(the default), or another comparison function.
Using :functional:`less` would transform the heap into a max heap.







.. index:: 
   single: priority queue

Priority queues
---------------
A :term:`priority queue` is conceptually similar to a normal queue.
It is a queue in which each element has an associated *priority*.
Unlike a standard queue which is strictly :term:`FIFO`,
a priority queue always removes the highest priority item first,
regardless of when the item was inserted.



This key difference means that a queue is not a good starting point
for a priority queue implementation.









-----

.. admonition:: More to Explore

   - :container:`std::priority_queue <priority_queue>`
   - :wiki:`Heap data structures <Heap_(data_structure)>`

