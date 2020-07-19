..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".
   
.. index:: function writing guidelines

General function writing guidelines
===================================
#. Write for clarity and correctness **first**
#. Avoid *premature optimization*
#. Avoid *premature "pessimization"*
   That is, prefer faster when **equally** clear
#. Minimize side-effects

   A function that modifies its parameters is said to have *side-effects*.
   Programs with too many side-effects are hard to predict and debug.

   Returning to our call-stack example.
   What if the function signatures were changed to accept a pass-by-reference parameter?

   .. tabbed:: side_effects

      .. tab:: Side effects

         .. code-block:: cpp

            void dig(double& x);
            void deeper(double& x);

         Given that the names of these functions provide no insight to their purpose,
         there is no way to know without inspecting the source if
         the variable x is modified when passed to these functions.

         .. code-block:: cpp

            void dig(double& val) {
              std::cout << "Digging...\n";
              val /= 2;
              deeper(val);
              std::cout << "Done digging...\n";
            }

            Unless it's obvious from the name of the function,
            side effects are almost always unexpected.

      .. tab:: Run It

         .. activecode:: functions_guidelines_side_effects_ac
            :language: cpp
            :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++11']
            :nocodelens: 

            #include <iostream>

            void dig(double& val);
            void deeper(double& val);

            int main() {
              double pi = 3.14159;
              std::cout << "in main.\npi = " << pi << '\n';
              dig(pi);

              std::cout << "Returned to main.\npi = " << pi << '\n';
              return 0;
            }

            void dig(double& val) {
              std::cout << "Digging...\n";
              val = val * 2;
              deeper(val);
              std::cout << "Done digging...\n";
            }

            void deeper(double& val) {
              val -= 1;
              std::cout << "now even deeper....\n";
            }

   This is one of the reasons why some programmers **only** use pass-by-reference
   when the parameter is ``const``.
   Some programmers prefer passing pointers over non-``const`` parameters.
   This requires the caller to explicitly pass in an address and 
   clearly states that the function may modify the parameter.

#. Keep functions short

   - A function should do *one* thing well

     If you see a function doing more than one thing
     consider breaking it up into multiple functions

   - Is this (slightly) more work?

     In the short run, perhaps.

     In the long run, your total time spent
     debugging, testing, maintaining, and modifying
     will be far, far less than if you packed everything into one monster function


   - Note that :term:`unit testing <unit test>` is practically impossible 
     once functions reach a certain size.

#. Strive to write a function *once* and never modify it again.
#. Check function parameters for validity.
   Unless you *completely* trust the caller (and their caller...)

   - It should be obvious: do not trust ``argv[]``


.. index::
   pair: video; function returns

.. youtube:: 9mWWNYRHAIQ
   :http: https


-----

.. admonition:: More to Explore

   - `C++ Core Guidelines for functions 
      <https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md#S-functions>`_
      from GitHub

   - `Unit testing library list <https://en.cppreference.com/w/cpp/links/libs#Testing>`__


