..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: sequence containers; vector

The vector class
================
The :container:`std::vector <vector>` is a sequence container 
that simulates a dynamically sized array.
If you have taken a class in linear algebra, 
the vector ADT has nothing to do with mathematics,
but is simply sequential data structure.

Like an array, elements are stored continuously.
This means that elements can be accessed not only through iterators, 
but also using offsets to regular pointers to elements.
The benefit of this is that a pointer to an element of a vector may be passed 
to any function that expects a pointer to an element of an array.

Unlike an array,
vector storage is handled automatically, being expanded and contracted as needed. 
Vectors usually occupy more space than static arrays, 
because more memory is allocated to handle future growth. 
This way a vector does not need to reallocate each time an element is inserted, 
but only when the additional memory is exhausted. 
The total amount of allocated memory can be queried using :cref:`vector::capacity()` function. 
Starting in C++11, extra memory can be returned to the system via a call to :cref:`vector::shrink_to_fit()`. 


.. index:: 
   pair: graph; std::vector

Given a vector declared as:

.. code-block:: cpp

   std::vector<int> v(6) = {2, 7, 1, 8};

This creates a vector of type ``int``, with size 6 and the first 4 values initialized:

.. graphviz:: 
   :alt: A vector of type int

   digraph {
     graph [fontname = "Bitstream Vera Sans", 
            labelloc=b,
            label="A vector of type int"
     ];
     node [fontname = "Bitstream Vera Sans", fontsize=14, shape=plaintext];
     "Indices:" -> "Values:" [color=white];
     "uninitialized values";

     node [shape=record, width=4.75, fixedsize=true];
     indices [label="v[0] | v[1] | v[2] | v[3]| v[4] | v[5]", color=white];
     values [label="<f0> 2 | <f1> 7 | <f2> 1 | <f3> 8 | <f4> ? | <f5> ? ", 
             color=black, fillcolor=lightblue, style=filled];

     values:f4,values:f5 -> "uninitialized values" [dir=back];
     { rank=same; "Values:"; values }
     { rank=same; "Indices:"; indices }
   }

The data layout of a vector makes it easy to pass a vector to a legacy C
function that expects a raw array.
This is something that comes up more often than you might expect.
The book *Effective STL* has a good discussion of 
passing string and vector objects to legacy C functions\ [1]_\ .

Given a legacy C function that expects a raw array:

.. code-block:: cpp

  void print_sum (const int* values, size_t array_size) {
    int sum = 0;
    for (size_t i = 0; i < array_size; ++i) {
      sum += values[i];
    }
    printf("Sum of ints in the array is %d\n", sum);
  }

We expect to be able to pass in an array and print the sum:

.. code-block:: cpp

   int main() {

     int data[] = { -30, 102, 55, -19, 0, 222, -3000, 4000, 8, -2 };
     const int numValues = sizeof data / sizeof(int);

     print_sum (data, num_values);

     return 0;
   }

We can pass a ``vector`` to this same legacy function:

.. code-block:: cpp

   int main() {
     int data[] = { -30, 102, 55, -19, 0, 222, -3000, 4000, 8, -2 };
     const int num_values = sizeof data / sizeof(int);

     print_sum (data, num_values);

     std::vector<int> v;
     v.insert (v.begin(), data, data + num_values);	// insert the ints in data
                                                    // into v at the front

     print_sum (&v[0], v.size());   // ok, unless v is empty

     if (!v.empty()) {              // safer
       print_sum (&v[0], v.size()); //&v[0] is better than v.begin()
     }

     return 0;
   }


-----

.. admonition:: More to Explore

   - `STL containers library <http://en.cppreference.com/w/cpp/container>`_

.. topic:: Footnotes

   .. [1] Effective STL (Item #16) by Scott Meyers (Addison-Wesley Professional).  Copyright 2001 Scott Meyers, 978-0-201-74962-5.

