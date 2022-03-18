..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: hash table; collisions

Resolving collisions
====================
Since we know that perfect hash functions are not generally
possible except in limited cases,
we must assume that sometimes a hash function will generate
the same value for two different objects.

For example, in our simple hash table example,
if we need to add another value that *collides*
with an existing entry,
then how can we store it?

.. graphviz::
   :align: center
   :alt: Simple hash table

   digraph c {
     rankdir=LR
     fontname = "Bitstream Vera Sans"
     label="Where can we store 93?"
     node [
        fontname = "Courier"
        fontsize = 14
        shape = "record"
        style=filled
        fillcolor=lightblue
     ]
     arr [
        label = "{0\n60|1\n11|2\n312|<p1>3\n23|4\n14|5\n35|6\n26|7\n17|8\n268|9\n799}"
     ]

     value [shape=box, label=93]
   }

There are two general approaches:

- :term:`Open hashing <open hashing>`: 
  The hash table stores data structures that each holds multiple items.
- :term:`Closed hashing <closed hashing>`
  The keys are stored directly in the table.
  This requires finding an open bucket in the table for each value.


























.. tabbed:: tab_graph

   .. tab:: Example set

      .. digraph:: hashtable
         :alt: Fruit set

         graph [ 
           fontname = "Bitstream Vera Sans", 
           labelloc=b,
           label="Fruit set hash table"
           nodesep = .05;
           rankdir = LR;
         ];

         node[shape = record,  width = .1,  height = .1, 
              fontsize=14, style=filled, fillcolor=lightblue];
         edge [arrowhead=vee, arrowsize=0.5];

         node0[label = "<f0>0 | <f1>1 | <f2>2 | <f3>3 | <f4>4 | <f5>5 | <f6>6 ",  height = 2.5];

         node [width = 1.5];
         node1[label = "{<n> kiwi | <p>}"];
         node2[label = "{<n> pear | <p>}"];
         node3[label = "{<n> apple | <p>}"];
         node4[label = "{<n> lemon | <p>}"];
         node5[label = "{<n> grape | <p>}"];
         node6[label = "{<n> lime | <p>}"];
         node7[label = "{<n> banana | <p>}"];

         node0:f0->node1:n;
         node0:f1->node2:n;
         node0:f2->node3:n;
         node0:f5->node4:n;
         node0:f6->node5:n;
         node2:p->node6:n;
         node4:p->node7:n;

   .. tab:: Example map

      When the ADT is a map, the process is similar.
      In a map ADT, the value hashed is the map :term:`key`,
      since this is what uniquely identifies map items.

      Each :term:`bucket` provides access to one or more map entries
      (:term:`key-value pairs <key-value pair>`).

      .. digraph:: hashtable
         :alt: Fruit inventory map

         graph [ 
           fontname = "Bitstream Vera Sans", 
           labelloc=b,
           label="Fruit inventory hash table"
           nodesep = .05;
           rankdir = LR;
         ];

         node[shape = record,  width = .1,  height = .1, 
              fontsize=14, style=filled, fillcolor=lightblue];
         edge [arrowhead=vee, arrowsize=0.5];

         node0[label = "<f0>0 | <f1>1 | <f2>2 | <f3>3 | <f4>4 | <f5>5 | <f6>6 ",  height = 2.5];

         node [width = 1.5];
         node1[label = "{<n> kiwi | 8 | <p>}"];
         node2[label = "{<n> pear | 5 | <p>}"];
         node3[label = "{<n> apple | 12 | <p>}"];
         node4[label = "{<n> lemon | 1 | <p>}"];
         node5[label = "{<n> grape | 13 | <p>}"];
         node6[label = "{<n> lime | 35 | <p>}"];
         node7[label = "{<n> banana | 3 | <p>}"];

         node0:f0->node1:n;
         node0:f1->node2:n;
         node0:f2->node3:n;
         node0:f5->node4:n;
         node0:f6->node5:n;
         node2:p->node6:n;
         node4:p->node7:n;


In order to use a type in an unordered container,
the type must override 3 functions:

- override :cref:`std::hash`
- override ``operator==``
- override ``operator<``

before the type will compile when added to an unordered container.

Consider the following :term:`hash table`:

.. digraph:: hashtable
   :alt: Simple hash table

   graph [ 
     fontname = "Bitstream Vera Sans", 
     labelloc=b,
     label="Simple hash table"
     nodesep = .05;
     rankdir = LR;
   ];

   node [fontname = "Bitstream Vera Sans", fontsize=14,
         style=filled, fillcolor=lightblue,
         width = .1,  height = .1
         shape=record];
   edge [arrowhead=vee, arrowsize=0.5];

   bucket[label = "<f0>0 | <f1>1 | <f2>2 | <f3>3 | <f4>4 | <f5>5 | <f6>6 \
                   | <f7>7 | <f8>8 | <f9>9 ",  height = 2.5];

   a [label="{ <data> 8 | <ref>  }"];
   b [label="{ <data> 3 | <ref>  }"];
   c [label="{ <data> 21 | <ref>  }"];
   d [label="{ <data> 55 | <ref>  }"];
   e [label="{ <data> 5 | <ref>  }"];
   f [label="{ <data> 34 | <ref>  }"];
   g [label="{ <data> 89 | <ref>  }"];
   h [label="{ <data> 13 | <ref>  }"];

   bucket:f1 -> a:data:w;
   bucket:f2 -> b:data;
   bucket:f4 -> c:data;
   bucket:f5 -> d:data;
   bucket:f8 -> e:data:w;
   e:ref:c -> f:data  [arrowtail=dot, dir=both, tailclip=false];
   f:ref:c -> g:data  [arrowtail=dot, dir=both, tailclip=false];
   b:ref:c -> h:data  [arrowtail=dot, dir=both, tailclip=false];

How does the software find the value ``34`` in this data structure?

The ``hash`` override is used to compute the bucket.
In this case the bucket is at index position ``8``.

Each element in the list stored in the bucket is evaluated using
``operator==``.
As soon as ``operator==`` evaluates to ``true`` the value is returned.

The ``operator<`` function is used when adding new elements to buckets.
New elements are kept sorted when added in order to reduce the time it takes to extract values from buckets.
It should be clear that the performance of this data structure is 
highly dependent upon the quality of the :term:`hash function`.
Always returning ``42`` is a *legitimate* value for a hash,
but an extremely poor one,
because your :term:`hash table` is no better than a :term:`linked list`.

All of the built in fundamental types and some other library types such as :cref:`std::string`
already have hash overrides defined.
If you define your own ``struct`` or ``class``, you need to write your own override.
Consider a ``struct Point``:

.. code-block:: cpp

   struct Point {
     int x;
     int y;
   }

   namespace std {   // must override std::hash
     template <>
     struct hash<Point>
     {
       std::size_t operator()(const Point& p) const
       {
         return ((std::hash<int>()(7919)
               ^ (std::hash<int>()(p.x) << 1)) >> 1)
               ^ (std::hash<int>()(p.y) << 1);
       }
     };
   }

The override must be a function template,
although in this case, no template parameter is needed.
The template declaration ``template <>`` is perfectly valid.

A :cref:`std::hash` override must be defined as a function object that takes the type as a parameter
and returns a :cref:`std::size_t`.


-----

.. admonition:: More to Explore

 - `General purpose hash function algorithms <http://www.partow.net/programming/hashfunctions/>`_

