..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: error-handling
   pair: assert macro; NDEBUG macro
   single: errno macro

Error handling
==============
Programmers are expected to create programs that function correctly and run as expected.
Programs need to function 'correctly' even in the face of unexpected or unusual conditions.

When the unexpected happens, we need to recover as gracefully as possible.
Sometimes the best option is to clearly communicate what happened and exit.
Abruptly halting or crashing is not generally acceptable.

Error handling involves:

- Detecting an error
- Transmitting information about an error
- Preserving the valid state of a program
- Avoiding resource leaks

The rest of this section describes simple error reporting strategies that are compatible with C.


.. tabbed:: assert

   One tried and true way to communicate errors is by returning error values from functions.
   We already have been introduced to the :cpp:`assert <error/assert>` macro to handle errors
   in the section :ref:`build_tools_assert`.

   The assert macro is a 'function-like' macro that evaluates a boolean expression
   and aborts the program if the condition is ``false``.
   The assert macro is most useful for debugging, but be aware that since it can
   easily be disabled, it is hard to depend on in production software.

   The macro ``NDEBUG``, if defined, will disable all the assert functions in a program.

   .. tab:: assert


      The assert macro takes a single expression.
      It does not provide a built-in mechanism for a c

      .. activecode:: error_handling_assert_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++17']
         :nocodelens:

         Try changing the assertions to generate errors.

         Then define ``NDEBUG`` and see what happens.
         ~~~~
         // uncomment to disable assert()
         // #define NDEBUG
         #include <cassert>
         #include <iostream>
          
         int main()
         {
             assert(2 + 2 == 4);
             std::cout << "Checkpoint #1\n";
          
             assert(2*2*2 == 8);
             std::cout << "Checkpoint #2\n";
         }
          

   .. tab:: assert messages

      The assert macro does not provide a built-in mechanism for a
      custom user message, but there are a few tricks we can use to 
      create a compound expression.

      While it is treated as a single expressin by assert,
      it provides a way to insert a customer error message when the
      assertion fails.

      Using the comma operator is one technique.
      The entire expression is still a single boolean exppression.

      After the left-hand side expression is evaluates, it is discarded.
      Any side-effects from the evaluated expression remain.
      This is what the comma operator does and why
      it's use is generally discouraged.
      However, in this case, it's our message and the program does not need it.

      Next the right-hand side is evaluated.
      If the expression evaluates to false, the entire expression, along with the
      string literal is displayed by assert before the program exits.

      .. activecode:: error_handling_assert_message1_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++17']
         :nocodelens:

         #include <cassert>
         int main()
         {
             assert((void("The 'void' here avoids an 'unused value' warning"), 1 == 0));
         }
          

      Using the relational 'and' operator ``&&`` is another technique.
      The entire expression is still a single boolean exppression.

      If the left-hand side expression is true, then the right-hand side
      is evaluated, but since it is a non-zero literal, it will always be ``true``.

      If the expression evaluates to false, the entire expression, along with the
      string literal is displayed by assert before the program exits.

      .. activecode:: error_handling_assert_message2_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++17']
         :nocodelens:

         #include <cassert>
         int main()
         {
             assert((010 + 010 == 15) && "What is 8+8 again?");
         }
          
How does the assert macro support our error handling goals?

- Detecting an error

  Detection is handled in the boolean expression passed to the macro.
  It can only be a single expression and some caution needs to be taken
  because "function like" macros are not functions and can behave in unexpected ways.

- Transmitting information about an error

  The assert macro immediately aborts the program and prints the line number
  of the source were the error occurred.

- Preserving the valid state of a program

  The program immediately terminates.
  If your program manages external resources like a file, it may be corrupted
  if the program left it in an indeterminate state on exit.

- Avoiding resource leaks

  This is not applicable since the program terminates.
  Any resources opened by the program (memory, file handles, etc.)
  will be recovered by the operating system when the program exits.


Another facility C++ inherits from C is the :cpp:`errno<error/errno>` macro.
errno is a preprocessor macro used for error indication.
The exact definition is implementation defined, but expands to a modifiable ``int``.
Several standard library functions indicate errors by writing positive integers to ``errno``.
Typically, the value of errno is set to one of the error codes,
listed in the header :cpp:`cerrno<header/cerrno>` as macro constants that begin with
the letter **E**, followed by uppercase letters or digits.

.. tabbed:: errno

   .. tab:: errno

      The value of errno is ``0`` at program startup,
      and although library functions are allowed to write positive integers to errno whether
      or not an error occurred, library functions never store ``0`` in errno.

      .. activecode:: error_handling_errno_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++17']
         :nocodelens:

         Print an error if we use the log function incorrectly.
         ~~~~
         #include <cerrno>
         #include <cmath>
         #include <cstring>
         #include <iostream>
          
         int main()
         {
             const double value = std::log(-1.0);
             std::cout << "Log result: " << value << '\n';
          
             if (errno == EDOM)
             {
                 std::cout << "log(-1) failed: " << std::strerror(errno) << '\n';
             }
         }

How does errno support our error handling goals?

In all 4 cases, the answer is the same: *it's up to you*.

You need to check ``errno`` to see if it has been set.
It is your resposibility to reset error if needed.
No function that sets ``errno`` will ever reset it to 0.
Any messages communicated are yours.
No error messages are automatically generated.
It is also your responsibility to preserve the state of your program
and cleanup resources that may be partially or improperly allocated.


One big advantage of ``errno`` is that for functions that use it, you get
a simple error code you can use to recover from an error without
the entire program aborting.


.. index:: error masks
   single: std::bitset

Handling multiple errors at once
--------------------------------
Each of the previous error handling techniques are simple, but each allows us
to communicate only a single error at a time.
Sometimes we need to communicate more information.

We could create a data structure to store each error we care about in a ``bool``.

.. code-block:: cpp

   struct my_errors {
      constexpr const bool busy = false;
      constexpr const bool cancelled = false;
      constexpr const bool domain_error = false;
      constexpr const bool invalid_argument = false;
   };

However, we notice this is quite verbose.
There is no easy way, for example to discover that no errors are set,
which hopefully is the normal situation for our program.
As programmers, we always want the typical uses or our data structures to be
as simple as possible.
We want the atypical ones to be simple too!

Can we make this easier to work with? Yes.

Once way is to pack all the boolean values into a single variable.



-----

.. admonition:: More to Explore

   - `Wikibooks: C Error Handling <https://en.wikibooks.org/wiki/C_Programming/Error_handling>`_
   - On cpp reference.com:
     
     - The :cpp:`assert<error/assert>` macro
     - The :cpp:`errno<error/errno>` macro
     - Keyword :lang:`static_assert`



