..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Hello, world!
=============
Welcome to CISC187 and welcome to this book.

This book is intended for students taking CISC187 at SD Mesa.
You should already have a solid understanding of the
material presented in the vast majority of first semester C and C++ courses.

This entire course focuses on writing code.
Even this book provides opportunities for you to write,
compile, and evaluate code on may pages.
Often the interactive code is on a separate tab,
for example:

.. tabbed:: hello_world

   .. tab:: Example

      A C++ construct that may be new to you is the
      :lang:`range-based for <range-for>` loop.
      When your goal is to iterate over all the elements
      in a container or array, a range-for loop
      is easier to write and understand.

      .. code-block:: cpp

         for (auto value: data)           // for each value in data
         {
           std::cout << "value is " << value << '\n';
         }

      Introduced in C++11, a range-for loop extracts values
      from containers one at a time and assigns them to a variable.

   .. tab:: Run It

      A complete example program using the code explained
      on the *Example* tab.

      .. activecode:: hello_world_rangefor_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++11']
         :nocodelens:

         // compiled with: -std=c++11
 
         #include <iostream>

         int main () {
           int data[] = { 1, 2, 3, 5, 8 };
           for (auto value: data)           // for each value in data
           {
             std::cout << "value is " << value << '\n';
           }
           return 0;
         }

      Feel free to modify this code and re-run it to see what
      happens when you change it.

The remaining section on this page list some things I expect
everyone to know on the first day of class.
Review this material and if anything looks unfamiliar
then read the linked content and ask questions.

.. index:: 
   pair: introductory topics; header files

Source files and header files
-----------------------------

One of the primary goals of this course is to begin creating programs more
complex than those written previously.
One of the core skills required when writing large programs is to split 
different parts of the program source into separate files.

You may have only had to do this a few times previously, 
but you should know by now:

* What are the differences between source and header files?

  * Why do they exist?
  * What are :term:`header guards <header guard>`?
  * What is ``#pragma once``?

  See `cppreference.com <https://en.cppreference.com/w/cpp/preprocessor/include>`__
  for more information.

* What happens during compilation?  Linking?
* How to use function *main()*, *argc*, and *argv*
* :io:`cout` and the meaning of statements like:

.. code-block:: cpp

   #include <iostream>
   #include <stdio.h>

   int main() {
     std::cout << "Hello C++!" << std::endl;
     puts("Hello C!");
     printf("Hello Alice!\n");
     printf("Hello %s!\n", "Bob");
   }
   
You may not have seen :cstdio:`printf <fprintf>` and :cstdio:`puts` before.
They are output functions C++ inherits from C.
Normally, in C++ we use stream I/O functions and classes,
but the old C functions are still there if you need them.

.. tabbed:: command-line

   .. tab:: Command line

      The function `main` gets special treatment in C++.
      Every executable program must contain **exactly one**
      function named *main*.
      Only two signatures are valid:

      .. code-block:: cpp

         int main()

      and:

      .. code-block:: cpp

         int main(int, char* [])  // char** is also allowed

      The first form is preferred when main does not process arguments from the
      command line.

      The second form is required if the program **does** process command line
      arguments.
      The first parameter is a count of how many arguments are in the second parameter.
      The second parameter is an array of 'C strings'.
      A 'C string' is a character array, so the second parameter is
      a two-dimensional array of characters.

      .. code-block:: cpp

         int main(int argc, char** argv)

      The two parameters are commonly named `argc` (argument count) and
      `argv` (argument values).

      Another thing to notice is that `main` returns a value.
      Some example programs in this course omit the final return from main.
      Returning at least `0` from main is considered a best practice,
      however, if you don't most compilers will add a zero return value
      for you automatically.

   .. tab:: Try It

      .. activecode:: hello_world_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++11']
         :nocodelens:

         #include <iostream>

         int main(int argc, char** argv) {
           for (int i=0; i < argc; ++i) {
             std::cout << "Hello " << argv[i] << "!\n";
           }
           return argc;  // who receives this value?
         }
         
Built-in types and type conversions
-----------------------------------
You should already be familiar with declaring fundamental :cpp:`types`
(``int``, ``char``, ``double``, ``unsigned``, etc.).
You should also know that other :types:`fixed width integer types <integer>`
exist (``int16_t``, ``uint64_t``, etc.) 
even if you haven't used them very much.
You should also be familiar with the basic math operations and operators
(``+``, ``-``, ``=``, ``==``, etc.).
Including the shortcut operators (``++``, ``+=``, etc.).
We will be expanding our knowledge of operators and operations
extensively during this course.

You should know the difference between *declaring*, *initializing*, and
*assigning a value* to a variable.
It is (sometimes) valid to assign variables of one type to those of a different
type, for example, `double x = 12;` assigns the integer `12` to the `double x`.
This is a **widening conversion** and is always safe.
The opposite of a widening conversion is a **narrowing conversion**.
A narrowing conversion frequently involves the loss of information.
Most compilers will warn about narrowing conversions even in cases where
they are allowed.

Keep in mind that a common source of error in programs is unintentional
narrowing conversions that occur during math operations.
For example:

.. tabbed:: hello_world_narrowing

   .. tab:: Example

      What is the output, given the following?

      .. code-block:: cpp

         double value = 3 / 2;

   .. tab:: Run It

      .. activecode:: hello_world_narrowing_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++11']
         :nocodelens:

         #include <iostream>

         int main() {
           double value = 3 / 2;
           std::cout << "The value is: " << value << ".\n";
         }

      Fix this program so that the correct value is displayed.


You should know how to explicitly cast fundamental types from one
type to another.
Most people should be familiar with the ``static_cast`` form:

::
    
   auto almost_pi = static_cast<int>(3.14159);

Some people may have also learned the C-style cast:

::
    
   auto almost_pi = (int)3.14159;

Know that these two forms are equivalent, but the first is preferred.
We will be learning other ways to explicitly cast that are a bit more consistent
with C++11's more uniform initialization syntax.

Finally, you should know the basic keywords of the language,
at least those common to both C and C++, and legal identifier names
for functions and variables.



User-defined types
------------------

Although you may not have done any object oriented programming yourself,
you probably have used objects, even if you weren't aware of it.
The C++ standard provides many classes.
Two of the oldest classes handle stream formatted input and output:
:io:`cin` and :io:`cout`.

You should have already encountered code like:

.. code-block:: cpp

   std::string  name;
   std::cout << "Enter your name: ";
   std::cin  >> name;
   std::cout << "Hello," << name << "!\n";

Hopefully, you have been taught the basics of :cpp:`string` and :container:`vector`
as it is hard to imagine doing much (non-embedded) C++ programming without ever using either.
A bit like writing a paragraph in English without using the letter 'e'.
Try that sometime!

We will be working with ``std::string`` and ``std::vector``
often in this course, so if you haven't used them yet,
don't worry - you will.

File input and output
.....................

I expect you to know how to use some form of file input and output,
whether it is the C-style :cstdio:`printf` and :cstdio:`scanf`, or the
C++-style input and output file streams: :io:`ofstream` and :io:`ifstream <basic_ifstream>`.
Both are serviceable, have their own advantages and disadvantages.
This course emphasizes *contemporary* C++ and encourages the use of
C++ generally, but sometimes ``printf`` is a perfectly acceptable
alternative to ``cout``. 

Don't panic.

While file I/O is not a primary focus of this course, you will be expected to employ
basic I/O in labs and projects.

Using ``cin`` to access user data:

.. activecode:: hello_world_cin_ac
   :language: cpp
   :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++11']
   :nocodelens:
   :stdin: Alice

   #include <iostream>
   #include <string>

   int main () {
     std::string name;
     std::cin >> name;
     std::cout << "Hello, " << name << "!\n";
   }


Reading from a file to access external data:

.. code-block:: cpp

   #include <fstream>
   #include <iostream>

   int main () {
     // assuming the file 'poem.txt' exists in the current directory
     std::ifstream is("poem.txt");
     char c;
     while (is.get(c)) {  // read the text file one byte (char) at a time
       std::cout << c;
     }
     is.close();
     return 0;
   }


Statements and branching
------------------------

Writing basic statements and conditionally executing code,
or executing blocks of code repeatedly, are fundamental skills
common to all programming languages.

Everyone should be **extremely familiar** with writing
``if``, ``switch``, ``for``, and ``while`` blocks.

You should have used combinations of statements and branching 
to perform tasks perhaps as complex as:

* Computing an amortization table
* Computing population growth
* Parsing text


Fixing errors in code
---------------------

You should know the difference between basic types of errors:

* :term:`Compile-time errors <compile-time error>`
* Link-time (linker) errors 
* :term:`Runtime errors <runtime error>`
* :term:`Semantic errors <semantic error>`

I expect some basic experience using a debugger in whatever 
programming environment you may have used previously.

If not, refer to the section :doc:`../back-matter/app-a/debugging`.

.. note::

   If **any** of the material in the preceding sections sounds unfamiliar, then

   * Consider working through the `week 1 example source code <https://github.com/DaveParillo/cisc187/tree/master/examples/week01>`_

   * Review the material from your first semester text

-----

.. admonition:: More to Explore

   - :lang:`range-based for <range-for>` loop and :cref:`loops`
   - :lang:`if`
   - :doc:`../back-matter/app-a/debugging`
   - Jeff Atwood's blog: `Code smells <https://blog.codinghorror.com/code-smells/>`_


