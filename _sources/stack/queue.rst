..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: sequence containers; stack
   pair: graph; std::stack

The queue class
===============
The :container:`std::queue <queue>` is a container adapter that gives the programmer the 
functionality of a queue - specifically, a FIFO (first-in, first-out) data structure.

The class template acts as a wrapper to the underlying container - only 
a specific set of functions is provided. 
The queue pushes elements on the back of the underlying container, 
and pops them from the front.

.. graphviz::
   :alt: std::queue elements

   digraph g {
       graph [
          labelloc=b;
          label="std::queue elements";
       ];
       node [fontname = "Bitstream Vera Sans", fontsize=14,
             style=filled, fillcolor=lightblue,
             shape=box, width=0.5, height=.25, label=""];

       a,b,d,e;
       node [style=none];
       c [label=". . .", color=white];

       back [shape=none, label="back()"];
       front [shape=none, label="front()"];

       a -> b -> c -> d -> e [ arrowhead=vee];
       back -> a:w [dir=back];
       e:e -> front;

       node [style=invis] x,y;
       x -> a [style=invis];
       y -> e [style=invis];
       {rank=sink; a b c d e}
   }


   
.. index:: 
   pair: graph; queue operations

The defining operations of a :container:`queue` are:

push 
   Add a new element to the back (end) of the queue.

pop
   Remove an element from the front (beginning) of the queue.

front
   Get the value of the element at the beginning of the queue.

back
   Get the value of the element at the end of the queue.

.. graphviz::
   :alt: std::queue operations

   // shows push and pop, enqueue / dequeue
   digraph g {
       graph [
          labelloc=b;
          label="std::queue operations";
       ];
       node [fontname = "Bitstream Vera Sans", fontsize=14,
             style=filled, fillcolor=lightblue,
             shape=box, width=0.5, height=.25, label=""];


       o,z [style=dotted];
       a,b,d,e;
       node [style=none];
       c [label=". . .", color=white];

       back [shape=none, label="push()"];
       front [shape=none, label="pop()"];

       o -> a -> b -> c -> d -> e [ arrowhead=vee];
       e -> z [ arrowhead=none];
       back -> o [style=dotted];
       front -> z [style=dotted, dir=back];

       {rank=sink; o a b c d e z}
   }


Minor modifications change ``pop_all()`` from a function
performing ``stack`` operations into one
performing ``queue`` operations:

.. code-block:: cpp

   #include <iostream>
   #include <queue>

   #define QueueContainer typename

   template <QueueContainer C>
   void pop_all(C& q) {
     while(!q.empty()) {
       std::cout << q.front() << " ";
       q.pop();
     }
     std::cout << "\npopped all from queue\n";
   }

The STL containers ``std::list`` and ``std::deque`` can be adapted to create a queue.

-----

.. admonition:: More to Explore

   - `STL containers library <http://en.cppreference.com/w/cpp/container>`_
   - STL :container:`queue` class


