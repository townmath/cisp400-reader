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

Given a ``std::stack<T>``, the defining operations of a :container:`stack` are:

void push (T value)
   Add a new element to the top of the stack.

void pop()
   Remove an element from the top of the stack.

T top()
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


.. tabbed:: tab_stack_ex_1

   .. tab:: Using std::stack

      Before running the following example, predict the output,
      then check yourself.

      .. activecode:: stack_using_stack_simple_ac1
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-std=c++11']
         :nocodelens:

         #include <iostream>
         #include <stack>
         #include <string>

         using std::cout;
         using std::stack;

         // remove all elements from a stack and print them out
         template <class Container>
         void pop_all(Container& s) {
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

It is also possible to initialize a stack from another container.
The initializing container must match the container adapted for the
stack instance.
By default, :container:`deque` is used,
but any container that provides

- ``back()``
- ``push_back()``
- ``pop_back()``

can be used as a stack adapter.
In the STL, besides deque, :container:`vector` and :container:`list` also
can be adapted by a stack.

.. tabbed:: tab_stack_initializers_1

   .. tab:: Initializers

      Because the default backing store for a stack is a deque,
      a container adapter does not need to be specified.

      .. code-block:: cpp

         // initialize stack from deque
         std::deque<int> x = { 1, 2, 3, 4, 5 };
         stack<int>> numbers(x);

      To copy a list into a stack will only work if the
      stack instance uses a list as its backing store.

      .. code-block:: cpp

         // initialize stack from list
         std::list<int> y = { 1, 2, 3, 4, 5 };
         stack<int, std::list<int>> numbers(y);

   .. tab:: Run It

      Before running the following example, predict the output,
      then check yourself.

      .. activecode:: stack_list_initializer_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-std=c++11']
         :nocodelens:

         #include <iostream>
         #include <stack>
         #include <string>

         using std::cout;
         using std::stack;

         // remove all elements from a stack and print them out
         template <class Container>
         void pop_all(Container& s) {
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

Notice the elements from the list are pushed onto the stack in the order
they are retrieved from the list.
The number ``1`` is pushed first, so when initialization is complete,
it is on the bottom of the stack.
   
Stack elements **cannot** be accessed directly in the way
you are used to with other sequential containers like
arrays, vectors, and lists.
To 'visit' each element in a ``stack``, the items need to be popped off.

If you think you need to visit all the elements in a ``stack``, 
then you probably should not be using a ``stack``.

-----

.. admonition:: More to Explore

   - `STL containers library <http://en.cppreference.com/w/cpp/container>`_
   - STL :container:`stack` class

