..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: std::string vs C strings

The string class
================

A short review of how string abstractions are handled in C,
followed by a short :cpp:`string` primer.

String abstractions in C
------------------------

In the C language, 
the abstract idea of a string is implemented with an array of characters.

.. code-block:: c

   // the char array must be null terminated
   char a[] = {'h', 'e', 'l', 'l', 'o', '\0'};  // null == '\0'

   char b[] = {'h', 'e', 'l', 'l', 'o', 0};     // null == 0 also

   // a quoted literal is just a special case of a char array
   char* c = "hello";

Arrays of ``char`` that are null terminated are commonly called :cref:`C strings`.
Given the C string:

.. code-block:: c

   char[] howdy = "hi there!";

   
.. index:: 
   pair: graph; char array

In memory, ``howdy`` is automatically transformed into:

.. graphviz::

   digraph char_array {
     fontname = "Bitstream Vera Sans"
     label="Character array in memory"
     node [
        fontname = "Courier"
        fontsize = 14
        shape = "record"
        style=filled
        fillcolor=lightblue
     ]
     arr [
        label = "{'h'|'i'|' '|'t'|'h'|'e'|'r'|'e'|'!'|'\\0'}";
     ]
     idx [ 
        color = white;
        fillcolor=white;
        label = "{howdy[0]|howdy[1]|howdy[2]|howdy[3]|howdy[4]|howdy[5]|howdy[6]|howdy[7]|howdy[8]|howdy[9]}";
     ]


   }

The last character in the array, ``'\0'`` is the *null character*,
and is used to indicate the end of the string.

.. note::

    Care must be taken to ensure that the array is large enough to hold 
    all of the characters AND the null terminator.
    Forgetting to account for null, 
    or having a 'off by one error' is one of the most 
    common mistakes when working with C strings.

    
.. index:: 
   pair: graph; c-string

A C string may allocate more memory that the characters currently stored in it.
An array declaration like this:

.. code-block:: c

   char hi[10] = "Hello";

results in an in-memory representation like this:

.. graphviz::

   digraph c {
     rankdir=LR
     fontname = "Bitstream Vera Sans"
     label="Character array with reserve memory"
     node [
        fontname = "Courier"
        fontsize = 14
        shape = "record"
        style=filled
        fillcolor=lightblue
     ]
     arr [
        label = "{H|e|l|l|o|\\0| | | | }"
     ]

   }

The array elements after the null are unused, but could be.
So, an array of size 10 has space for 4 more characters, 9 total.

A key limitation of C strings is that because they are arrays,
you must declare in advance how many characters the string will hold.
The compiler will always statically determine the size, 
even if an explicit size is not provided.

.. code-block:: c

   char[] hi     = "Hello";  // size 6
   char   hi[10] = "Hello";  // size 10


C strings have an advantage of being extremely lightweight and simple.
Their main disadvantage is that they are too simple for many applications.
Their simplicity makes them a pain to work with,
which is why the Standard Template Library (STL) contains the :cpp:`string` class.

A string class primer
---------------------

Like a C string, a ``std::string`` is simply a sequence of characters:

.. code-block:: cpp

   #include <string>        // access std::string functions
   
   using std::string;       // alias type std::string to 'string'

   int main() {
     string x;                          // empty string
     string greet =  "Hello, World!";   // create from C string
     string hello   ("Hello, World!");  // as above, constructor style syntax
     string howdy = {"Hello, World!"};  // C++11 only
     string howdy   {"Hello, World!"};  // as above, = is optional
     return 0;
   }

Unlike a C string, a ``std::string`` is a full-fledged *object*.
It knows it's own size, and comes with many convenience functions.

Notice that unlike a built-in variable declaration such as ``int x;``,
the declaratino ``string x`` is **not** incomplete.
The variable ``x`` is a complete and valid ``string`` object
that stores no character data.

.. index:: 
   pair: string functions; operator[]
   pair: string functions; operator+=
   pair: string functions; operator==

.. tabbed:: tab_string_simple

   .. tab:: Simple operations

      .. activecode:: string_simple_operator_ac1
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-std=c++11']
         :nocodelens:

         #include <iostream>
         #include <string>

         using std::string;

         int main() {
           string a = "hello";
           a += ", world!";        // joining strings is pretty easy

           // Copying or creating one string from another feels as natural
           // as a fundamental type.
           string b = a;

           if (a == b)             // Same goes for comparisons
           {
             // modify values
             b[0] = 'H';           // and a string feels like an 'array of char' 
             b[7] = 'W';
           }

           std::cout << a << '\n'; // and has stream support
           std::cout << b << '\n';

           return 0;
         }


   .. tab:: front() and back()

      This tab shows alternate functions for accessing the first and last
      characters in a string.

      .. activecode:: string_front_back_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-std=c++11']
         :nocodelens:

         #include <iostream>
         #include <string>

         int main() {
           std::string value = "hello, world!";

           std::cout << "first: " << value.front() << '\n';
           std::cout << "last: " << value.back() << '\n';
           return 0;
         }

   .. tab:: append()

      The ``append`` function allows you to append *N* copies of a character or
      an array of characters to the end of a string.

      .. activecode:: string_append_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-std=c++11']
         :nocodelens:

         #include <iostream>
         #include <string>

         int main() {
          using std::cout;
           std::string hi = "hello";
           std::string howdy = hi;

           cout << "original: " << hi   << '\n';

           hi.append(5, 'o');   // append 5 o's
           hi.append(", world!");
           cout << hi << '\n';

           cout << "original: " << howdy   << '\n';

           // append returns a new string value, so
           // calls to append can be chained together
           howdy.append(5, 'o').append(", world!");
           cout << howdy << '\n';

           return 0;
         }

   .. tab:: insert()

      The ``insert`` function allows you to insert 1 character or
      an array of characters at a position in a string.

      .. activecode:: string_insert_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-std=c++11']
         :nocodelens:

         #include <iostream>
         #include <string>

         int main() {
           std::string value = "hello, world!";

           std::cout << "original: " << value << '\n';

           value.insert(0,3,'*');       // insert "***" at position 0
           std::cout << value << '\n';

           // insert a char array before the '!'
           value.insert(value.size()-1," (this means you)");
           std::cout << value << '\n';

           return 0;
         }

Using the :string:`operator[]<operator_at>` to access select characters in a string is,
like an array,
not range checked.
This means that if you use an index referring to an invalid position,
then your program might have undefined behavior, or fail unexpectedly.
You can use the function :string:`at` anywhere ``operator[]`` is allowed.
The ``at`` function is range checked.
While there is a cost associated with this check, 
if the index provided is out of range, 
then an :cref:`std::out_of_range` exception is thrown,
which must be caught,
otherwise the program will terminate.

.. code-block:: cpp

   if (a == b)
   {
     b.at(0)  = 'H';   // might be OK
     b.at(-1) = 'W';   // never OK.  throws exception
   }


Remember that a ``std::string`` is **not** a C string.
Declarations like this are a common source of confusion for new programmers:

.. code-block:: cpp

   auto my_string = "Howdy!";


What type is ``my_string``?

.. reveal:: reveal_my_string

   ``my_string`` is **not** a std::string.

   The default type for characters enclosed in double quotes is ``const char*``.

This is one of those situations where :lang:`auto` may not be deducing the type
you actually want.
There are several simple ways to use auto *and* get the type
deduced to be a ``std::string``.

In C++14, you can simply append a ``s`` to the end of the string literal.
This identifies the literal as type std::string.

.. code-block:: cpp

   auto my_string = "Howdy!"s;    // preferred

Alternatively, you can call the string constructor explicitly, which
works for C++ versions older than C++14.

.. code-block:: cpp

   auto my_string = string("Howdy!");

   auto your_str  = string{"Howdy!"};  // C++11 initialization syntax

.. index::
   pair: toupper; locale

Change a character to upper case
................................
Not every string modification is handled using string member functions.
Sometimes, the standard library provides the facility we are looking for.
One example is changing character case.
Many languages provide utilities to change character case as part of the
string class.

Not C++.

C++ uses the legacy :string:`null-terminated byte strings library </byte>` 
to provide the features.  They are defined in header ``cctypes``.

.. tabbed:: cctype_toupper

   .. tab:: toupper()

      The ``std::toupper`` function takes a single ``char``,
      which is not modified, and returns an ``int``.
      The return value can be used as the upper case
      version of the input character.

      This function uses the default **C** locale to replace the
      lowercase letters ``abcdefghijklmnopqrstuvwxyz``
      with respective uppercase letters 
      ``ABCDEFGHIJKLMNOPQRSTUVWXYZ``.
      Non-ASCII acharacters are not handled.

      Recall that ``char`` implicitly convert to ``int``.

      .. activecode:: string_toupper_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-std=c++11']
         :nocodelens:

         #include <cctype>
         #include <iostream>
         #include <string>

         int main() {
           std::string value = "hello, world!";
           char& first = value.front();
           // failure to assign the return value of toupper
           // to a variable is a common source of error.
           first =  std::toupper(first);
           std::cout << value << '\n';
           return 0;
         }

      To handle non-ASCII or extended characters, the C++ version
      of std::toupper is needed.
      
   .. tab:: std::locale()

      The ``std::toupper`` function takes a single ``char``,
      which can be **any** character type, 
      is not modified, and returns a character of the same type
      as the character type provided.

      .. activecode:: string_toupper_locale_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-std=c++11']
         :nocodelens:

         #include <iostream>
         #include <locale>
         #include <string>

         int main() {
           unsigned char c = '\xb8'; // the character ž in ISO-8859-15
                                     // but ¸ (cedilla) in ISO-8859-1

           std::setlocale(LC_ALL, "en_US.iso88591");
           std::cout << std::hex << std::showbase;
           std::cout << "in iso8859-1, toupper('0xb8') gives " << std::toupper(c) << '\n';
           std::setlocale(LC_ALL, "en_US.iso885915");
           std::cout << "in iso8859-15, toupper('0xb8') gives " << std::toupper(c) << '\n';

           return 0;
         }




.. index::
   pair: string functions; empty
   pair: string functions; find
   pair: string functions; find_first_of
   pair: string functions; rfind
   pair: string functions; size


Getting information out of a string
...................................

A ``string`` knows its own size and can provide other useful information.

.. code-block:: cpp
   
   #include <cassert>
   #include <string>
   using std::string;
   int main() {
     string my_string = "Hello";

     assert( my_string.size() == 5 );  // .length() is available also
     if (!my_string.empty()) {
       my_string += ", there.";       // my_string == "Hello, there."
     }
     return 0;
   }

And the string class provides many functions dedicated to finding substrings
within a string.

.. tabbed:: tab_find_string

   .. tab:: Example: find

      The simplest example is the :string:`find` function.

      Given any string object, for example, this string:

      .. literalinclude:: find-string.txt
         :language: cpp
         :lines: 12
         :dedent: 3

      defined using the C++14 string literal syntax,
      creates a new object ``us``.

      Once we have a ``string``, calling the string member function 
      find always returns a position:

      - Either a position within the string, or
      - The special value :string:`std::string::npos<npos>` 
        which means the value was not found in the string.

      We can use this to check if we found what we were looking for:
      
      .. literalinclude:: find-string.txt
         :language: cpp
         :lines: 13-16
         :dedent: 3

      The position returned by find is a zero-based index
      into the string.

      Find can also take a sequence of characters.
      In that case, it returns the position to the first ``char``
      where the entire sequence is matched.

      **Reverse find**

      Similar to ``find``, :string:`rfind` performs the same
      task as find, but iterates through the string in reverse order:
      starting at the end and moving towards the first character.
      Keep in mind that the position returned is still based
      on the same index positions as regular ``find``.

      **Find first of**

      The :string:`find_first_of` function takes a ``char`` sequence,
      but unlike find where the entire sequence is used to find a match,
      ``find_first_of`` examines each character in the sequence,
      on at a time, and returns the *minimum position* of **any**
      of the characters listed as function arguments in the string.
      For example:

      .. literalinclude:: find-string.txt
         :language: cpp
         :lines: 17, 23
         :dedent: 3

      The function returns the position of 'e' in 'Hello world',
      even though 'e' and 'o' are both present,
      because 'e' is first.

      The order of the character arguments do not matter.
      The results would be exactly the same if the arguments were
      'uoiea'.
      Don't take my word for it, try it yourself.

   .. tab:: Run It

      .. include:: find-string.txt

.. index::
   single: std::string::npos 

The special value :string:`std::string::npos<npos>` is used both as an end of string indicator
by functions that expect a string and
as an indicator of *not found* by functions that return an index (like find).

.. youtube:: nkKeA74p3RY
   :http: https

.. index::
   pair: string functions; c_str

Converting a std::string to C string 
....................................

You cannot use ``std::string`` in a function 
that expects ``const char*`` - you must convert it
to a null terminated character array.

.. code-block:: cpp

   auto my_name = "Alice"s;


  printf ("Hello again, %s\n", my_name);       // compile error!

  // the c_str() function converts a string into a c string
  printf ("Hello again, %s\n", my_name.c_str());


Final words
-----------
This was a very brief introduction and barely captures what std::string
is capable of.
Check out the documentation at cppreference.com to get a feel for the functions
and capabilities available.

Skill Check
-----------
The questions in this hidden section provide a chance to demonstrate
your understanding of the concepts discussed so far.

.. reveal:: reveal-skill-check-string

   .. fillintheblank:: string_fitb1

      Given the following:

      .. code-block:: cpp

         std::string x = "The rain in Spain. . . ";
         size_t pos = x.find("in");

      What is the value of ``pos``?

      - :6: Correct.
        :9: No. There is another substring 'in'
        :7: String positions are zero-based
        :x: Try again.

   .. parsonsprob:: string_pp1
      :adaptive:
      :noindent:
      :language: c

      int main() {
      =====
        std::string  us = "Team USA";
      =====
        auto snowflake = us.find_first_of("Korea");
      =====
        if (snowflake == std::string::npos) {
      =====
          std::cout << "Did not find anything\n";
      =====
        } else {
      =====
          std::cout << "Found it!\n";
      =====
        }
        return snowflake;
      =====
      }

   .. fillintheblank:: string_fitb2

      Given the following:

      .. code-block:: c

         char text[32];
         strcpy(text, "hello");
         int len = strlen(text);

      What is the value of ``len``?

      - :5: Correct.
        :6: String length does not include the null character.
        :4: Sizes are not indexes.
        :x: Try again.

   .. activecode:: string_sc_ac1
      :language: cpp
      :compileargs: ['-Wall', '-Wextra', '-std=c++11']
      :nocodelens:

      Fix the errors in the ``printf`` line below:

      ~~~~
      #include <cstdio>
      #include <string>

      int main() {
        std::string yazoo = "ritish alternative band";
        char c = 'B';
          
        printf ("%c%s\n",c, yazoo);
      }

   .. fillintheblank:: string_fitb3

      Which ``#include`` is required to use functions such as
      ``std::atoi`` and ``std::atof``?

      - :cstdlib: Correct.
        :cstring: These are C library functions
        :string: These are C library functions
        :x: Try again.


   .. fillintheblank:: string_fitb4

      Which ``#include`` is required to use functions such as
      ``std::stoi`` and ``std::stol``?

      - :string: Correct.
        :cstring: These are not C functions
        :cstdlib: These are string functions added in C++11
        :x: Try again.

   .. fillintheblank:: string_fitb5

      Given the following:

      .. code-block:: cpp

         #include <string>

         int main (){
           std::string s = "Donald Duck";
           int value = 0;
           if (s.find_first_of(' ') == s.find_last_of(' ')) {
             value = 3;
           } else {
             value = 5;
           }
           return value;
         }

      What value is returned from main?

      - :3: Correct.
        :0: In an if/else block one of the blocks must always be
            entered.
        :5: What positions are returned from both find statements?
        :x: Try again.


-----

.. admonition:: More to Explore

   - cppreference.com `Strings library <http://en.cppreference.com/w/cpp/string>`_ overview
   - YoLinux `String class tutorial <http://www.yolinux.com/TUTORIALS/LinuxTutorialC++StringClass.html>`_
   - Bjarne Stroustrup's C++11 FAQ: `Raw String literals <http://www.stroustrup.com/C++11FAQ.html#raw-strings>`_
   - Mike Shahar post: `Exploring std::string <https://shaharmike.com/cpp/std-string/>`_
   - Locales:

     - `Thinking in C++: Locales <https://www.linuxtopia.org/online_books/programming_books/c++_practical_programming/c++_practical_programming_101.html>`__
     - `Differences between the C Locale and the C++ Locales <https://stdcxx.apache.org/doc/stdlibug/24-3.html>`__

