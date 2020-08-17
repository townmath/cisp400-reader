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

The stack class
===============
The :container:`std::stack <stack>` is a container adapter that gives the programmer the 
functionality of a stack - specifically, a Last-In-First-Out (LIFO) data structure.

The class template acts as a wrapper to the underlying container - only 
a specific set of functions is provided. 
The stack pushes and pops the element from the back of the underlying container, 
known as the top of the stack.

The defining operations of a :container:`stack` are:

push
   Add a new element to the top of the stack.

pop
   Remove an element from the top of the stack.

top
   Get the value of the element at the top of the stack.
   
.. graphviz::
   :alt: std::stack elements

   // shows push and pop
   digraph g {
       graph [
          rankdir=LR;
          labelloc=b;
          label="std::stack elements";
       ];
       node [fontname = "Bitstream Vera Sans", fontsize=14,
             style=filled, fillcolor=lightblue,
             shape=box, width=0.5, height=.25, label=""];


       a,b,d,e;
       node [style=none];
       c [label=". . .", color=white];

       top [shape=none, label="top()"];
       push [shape=none, label="push()"];
       pop [shape=none, label="pop()"];

       a -> b -> c -> d -> e [dir=none, arrowhead=vee];
       push -> a [style=dotted];
       pop -> a [dir=back,style=dotted];

       pop:e -> top:w [style=invis]   
       top -> a [style=dotted, dir=back, constraint=false];
   }

.. code-block:: cpp

   #include <iostream>
   #include <stack>
   #include <string>
   using std::cout;
   using std::stack;

   #define StackContainer typename

   // remove all elements from a stack and print them out
   template <StackContainer C>
   void pop_all(C& s) {
     while(!s.empty()) {
       cout << s.top() << " ";
       s.pop();
     }
     cout << "\npopped all from stack\n";
   }

   int main () {
     stack<std::string> strings;
     cout << "push strings onto stack...\n";
     strings.push("one");
     strings.push("two");
     strings.push("three");
     strings.push("four");
     strings.push("five");

     cout << "size of stack before: " << strings.size() << '\n';
     pop_all (strings);
     cout << "size of stack after: " << strings.size() << '\n';
     if (strings.empty()) {
       cout << "stack is empty.\n";
     }


     return 0;
   }

which returns:

.. code-block:: none

   push strings onto stack...
   size of stack before: 5
   five four three two one
   popped all from stack
   size of stack after: 0
   stack is empty.
       
It is also possible to initialize a stack from a vector, list or array:

.. code-block:: cpp

   #include <iostream>
   #include <stack>
   #include <list>
   using std::cout;
   using std::stack;

   #define StackContainer typename

   template <StackContainer C>
   void pop_all(C& s) {
     while(!s.empty()) {
       cout << s.top() << " ";
       s.pop();
     }
     cout << "\npopped all from stack\n";
   }

   int main () {
     cout << "initialize stack from list:\n";
     std::list<int> tmp = { 1, 2, 3, 4, 5 };
     stack<int, std::list<int>> numbers(tmp);

     cout << "list has " << tmp.size() << " entries\n";
     pop_all (numbers);
     if (numbers.empty()) {
       cout << "stack is empty.\n";
     }

     return 0;
   }

which returns:

.. code-block:: none

   initialize stack from list:
   list has 5 entries
   5 4 3 2 1
   popped all from stack
   stack is empty.

Notice the elements from the list are pushed onto the stack in the order
they are retrieved from the list.
The number ``1`` is pushed first, so when iniitialization is complete,
it is on the bottom of the stack.
   
Stack elements **cannot** be accessed directly in the way
you are used to with other sequential containers like
arrays, vectors, and lists.
To 'visit' each element in a ``stack``, the items need to be popped off.

If you think you need to visit all the elements in a ``stack``, 
then you probably should not be using a ``stack``.

The STL containers ``std::vector``, ``std::list``, 
and ``std::deque`` can be adapted to create a ``stack``.


-----

.. admonition:: More to Explore

   - `STL containers library <http://en.cppreference.com/w/cpp/container>`_
   - STL :container:`stack` class

