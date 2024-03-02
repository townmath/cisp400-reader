..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: error-handling
   :pair: assert macro; NDEBUG macro
   :single: errno macro

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


One tried and true way to communicate errors is by returning error values from functions.
We already have been introduced to the :cpp:`assert <error/assert>` macro to handle errors
in the section :ref:`build_tools_assert`.

The assert macro is a 'function-like' macro that evaluates a boolean expression
and aborts the program if the condition is ``false``.
The assert macro is most useful for debugging, but be aware that since it can
easily be disabled, it is hard to depend on in production software.

The macro ``NDEBUG``, if defined, will disable all the assert functions in a program.

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
    
       assert((void("void helps to avoid 'unused value' warning"), 2 * 2 == 4));
       std::cout << "Checkpoint #2\n";
    
       assert((010 + 010 == 16) && "Octal 8+8 did not == 16!");
       std::cout << "Checkpoint #3\n";
   }
    

Another facility C++ inherits from C is the :cpp:`errno<error/errno>` macro.
errno is a preprocessor macro used for error indication.
The exact definition is implementation defined, but expands to a modifiable ``int``.
Several standard library functions indicate errors by writing positive integers to ``errno``.
Typically, the value of errno is set to one of the error codes,
listed in the header :cpp:`cerrno<header/cerrno>` as macro constants that begin with
the letter **E**, followed by uppercase letters or digits.
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



