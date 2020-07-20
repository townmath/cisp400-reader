..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".
..  Some of the content in this section is adapted from
    http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html
   
.. index:: 
   pair: functions; passing parameters
   single: pass by value
   pair: parameter passing; by value

Passing parameters
==================
In C and C++, parameter passing defaults to **pass by value**.
Unless you specify otherwise,
function parameters are initialized with *copies* of the actual arguments, 
and function callers get back a *copy* of the value returned by the function.
Pass by value is the simplest way to get data into and out of functions.

.. code-block:: cpp

   #include <iostream>

   // Declare a function that takes a parameter.
   void printFavorite(int x);

   int main() {
   int favorite = 72;
     printFavorite(favorite); // Call the function.
     return 0;
   }

   // define the function
   void printFavorite(int x) {
     std::cout << "my favorite number is " << x << '\n';
   }

You can also step through `example 2.1.5-1 here <http://pythontutor.com/cpp.html#code=%23include%20%3Ciostream%3E%0A%0A//%20Declare%20a%20function%20that%20takes%20a%20parameter.%0Avoid%20printFavorite%28int%20x%29%3B%0A%0Aint%20main%28%29%20%7B%0A%20%20int%20favorite%20%3D%2072%3B%0A%20%20printFavorite%28favorite%29%3B%20//%20Call%20the%20function.%0A%20%20return%200%3B%0A%7D%0A%0A//%20define%20the%20function%0Avoid%20printFavorite%28int%20x%29%20%7B%0A%20%20std%3A%3Acout%20%3C%3C%20%22my%20favorite%20number%20is%20%22%20%3C%3C%20x%20%3C%3C%20'%5Cn'%3B%0A%7D%0A&curInstr=0&mode=display&origin=opt-frontend.js&py=cpp&rawInputLstJSON=%5B%5D>`_.  

The important point is that two copies of my favorite number are stored.
The one declared in main, ``favorite``, and
the one declared in printFavorite, ``x``.
The parameter ``x`` is initialized using the value of ``favorite`` in main.


More than one parameter can be passed.
For example, a function to add two numbers:

.. code-block:: cpp

   #include <iostream>

   // This function takes two parameters.
   int addNumbers(int x, int y);

   int main() {
     int a = 13;
     int b = 21;
     int sum = addNumbers(a, b);
     std::cout << sum << '\n';
     return 0;
   }

   int addNumbers(int x, int y){
     int answer = x + y;
     return answer;
   }

Step through `example 2.1.5-2 <http://pythontutor.com/cpp.html#code=%23include%20%3Ciostream%3E%0A%0A//%20This%20function%20takes%20two%20parameters.%0Aint%20addNumbers%28int%20x,%20int%20y%29%3B%0A%0Aint%20main%28%29%20%7B%0A%20%20int%20a%20%3D%2013%3B%0A%20%20int%20b%20%3D%2021%3B%0A%20%20int%20sum%20%3D%20addNumbers%28a,%20b%29%3B%0A%20%20std%3A%3Acout%20%3C%3C%20sum%20%3C%3C%20'%5Cn'%3B%0A%20%20return%200%3B%0A%7D%0A%0Aint%20addNumbers%28int%20x,%20int%20y%29%7B%0A%20%20int%20answer%20%3D%20x%20%2B%20y%3B%0A%20%20return%20answer%3B%0A%7D%0A&curInstr=0&mode=display&origin=opt-frontend.js&py=cpp&rawInputLstJSON=%5B%5D>`_
and see how the copies of both local variables and return values are managed on the stack.

.. index:: 
   single: pass by reference
   pair: parameter passing; by reference

For large / complex data types, however, pass by value becomes expensive even in small programs.
An alternative to pass by value, is called **pass by reference**.
Rather than passing a *copy* of the object, 
instead only the *address* of the object (the object reference),
is passed instead.
We use the *address of operator* ``&`` to declare that only the address of the 
variable is passed, rather than a copy.
The primary advantage is that since all addresses are the same size,
the cost of passing is the same, 
regardless of how large the object is.


.. code-block:: cpp

   #include <iostream>

   /**
    * A copy of x is passed to this function.
    * Changes to x are not reflected in the caller.
    */
   void by_value(int x) {
     std::cout << "in by_val the address of x is   " << &x << '\n';
     x = 99;
   }

   /**
    * A reference to x is passed to this function.
    * Changes to x are not reflected in the caller.
    */
   void by_reference (int& x) {
     std::cout << "in by_ref the address of x is   " << &x << '\n';
     x = -1;
   }

   int main () {
     auto alpha = 11;
     auto beta = 11;

     std::cout << "in main the address of alpha is " << &alpha << '\n';
     std::cout << "in main the address of beta is  " << &beta << '\n';

     by_value(alpha);
     by_reference(beta);

     std::cout << "alpha is now " << alpha << '\n';
     std::cout << "beta is now " << beta << '\n';
     return 0;
   }

Step through `example 2.1.5-3 <http://pythontutor.com/cpp.html#code=%23include%20%3Ciostream%3E%0A%0A/**%0A%20*%20A%20copy%20of%20x%20is%20passed%20to%20this%20function.%0A%20*%20Changes%20to%20x%20are%20not%20reflected%20in%20the%20caller.%0A%20*/%0Avoid%20by_value%28int%20x%29%20%7B%0A%20%20std%3A%3Acout%20%3C%3C%20%22in%20by_val%20the%20address%20of%20x%20is%20%20%20%22%20%3C%3C%20%26x%20%3C%3C%20'%5Cn'%3B%0A%20%20x%20%3D%2099%3B%0A%7D%0A%0A/**%0A%20*%20A%20reference%20to%20x%20is%20passed%20to%20this%20function.%0A%20*%20Changes%20to%20x%20are%20not%20reflected%20in%20the%20caller.%0A%20*/%0Avoid%20by_reference%20%28int%26%20x%29%20%7B%0A%20%20std%3A%3Acout%20%3C%3C%20%22in%20by_ref%20the%20address%20of%20x%20is%20%20%20%22%20%3C%3C%20%26x%20%3C%3C%20'%5Cn'%3B%0A%20%20x%20%3D%20-1%3B%0A%7D%0A%0Aint%20main%20%28%29%20%7B%0A%20%20auto%20alpha%20%3D%2011%3B%0A%20%20auto%20beta%20%3D%2011%3B%0A%0A%20%20std%3A%3Acout%20%3C%3C%20%22in%20main%20the%20address%20of%20alpha%20is%20%22%20%3C%3C%20%26alpha%20%3C%3C%20'%5Cn'%3B%0A%20%20std%3A%3Acout%20%3C%3C%20%22in%20main%20the%20address%20of%20beta%20is%20%20%22%20%3C%3C%20%26beta%20%3C%3C%20'%5Cn'%3B%0A%0A%20%20by_value%28alpha%29%3B%0A%20%20by_reference%28beta%29%3B%0A%0A%20%20std%3A%3Acout%20%3C%3C%20%22alpha%20is%20now%20%22%20%3C%3C%20alpha%20%3C%3C%20'%5Cn'%3B%0A%20%20std%3A%3Acout%20%3C%3C%20%22beta%20is%20now%20%22%20%3C%3C%20beta%20%3C%3C%20'%5Cn'%3B%0A%20%20return%200%3B%0A%7D%0A&curInstr=0&mode=display&origin=opt-frontend.js&py=cpp&rawInputLstJSON=%5B%5D>`_.

.. reveal:: reveal-skill-check-functions
   :showtitle: Show Skill Check
   :hidetitle: Hide Skill Check

   Given the following program:

   .. code-block:: cpp
      :linenos:

      #include <iostream>

      int change_and_add(int &a, int &b) {
        a = 3;
        b = 4;
        return a + b;
      }

      int main() {
        int a = 1;
        int b = 2;
        int c = change_and_add(a, a);
        std::cout << a << b << c;
      }

   .. fillintheblank:: fib_param_1

      What is the output from this program?

      - :428: Correct.
        :123: The variable a is modified in this program.
        :437: The variable b is never modified in this program.
        :427: Variable a is modified <em>twice</em> before the addition is performed.
        :.*: What is passed to the function change_and_add? What changes? What doesn't?



-----

.. admonition:: More to Explore

  - TBD

