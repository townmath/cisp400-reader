..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".
.. This file is adapted from the OpenDSA eTextbook project. See
.. http://opendsa.org for more details.
.. Copyright (c) 2012-2020 by the OpenDSA Project Contributors, and
.. distributed under an MIT open source license.

.. index::
   single: factorial
   single: permutation
   single: modulus
   single: logic notation
   single: floor function
   single: ceiling function

Selected functions
==================

This page collects together definitions for a few
significant mathematical concepts and functions which are used
frequently throughout the text.

**Modulus function**
The modulus function returns the remainder of
an integer division.
Sometimes written :math:`n \bmod m` in mathematical expressions,
the syntax in C++ is ``n % m``.
From the definition of remainder, :math:`n \bmod m` is the integer
:math:`r` such that :math:`n = qm + r` for :math:`q` an integer,
and :math:`|r| < |m|`.

Therefore, the result of :math:`n \bmod m` must be between 0 and
:math:`m-1` when :math:`n` and :math:`m` are positive integers.
For example, :math:`5 \bmod 3 = 2`; :math:`25 \bmod 3 = 1`,
:math:`5 \bmod 7 = 5`, and :math:`5 \bmod 5 = 0`.

There is more than one way to assign values to :math:`q`
and :math:`r`, depending on how integer division is interpreted.
The most common mathematical definition computes the mod function as
:math:`n \bmod m = n - m\lfloor n/m\rfloor`.
In this case, :math:`-3 \bmod 5 = 2`.
However, Java and C++ compilers typically use the underlying
processor's machine instruction for computing integer arithmetic.
On many computers this is done by truncating the resulting fraction,
meaning :math:`n \bmod m = n - m (\mathrm{trunc}(n/m))`.
Under this definition, :math:`-3 \bmod 5 = -3`.
Another language might do something different.

Unfortunately, for many applications this is not what the user wants
or expects.
For example, many hash systems
will perform some computation on a record's :term:`key` value and then
take the result modulo the hash table size.
The expectation here would be that the result is a legal index into
the hash table, not a negative number.
Implementers of hash functions must either ensure that the
result of the computation is always positive, or else add the hash
table size to the result of the modulo function when that result is
negative.


**Factorial function**
The factorial function, written :math:`n!` for :math:`n` an
integer greater than 0, is the product of
the integers between 1 and :math:`n`, inclusive.
Thus, :math:`5! = 1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 = 120`.
As a special case, :math:`0! = 1`.
The factorial function grows quickly as :math:`n` becomes larger.
Because computing the factorial function directly is a time-consuming
process, it can be useful to have an equation that provides a
good approximation.
Stirling's approximation states that
:math:`n! \approx \sqrt{2\pi n}(\frac{n}{e})^n`,
where :math:`e \approx 2.71828`
(:math:`e` is the base for the system of natural logarithms) [#]_.
Thus we see that while :math:`n!` grows
slower than :math:`n^n` (because :math:`\sqrt{2\pi n}/e^n < 1`),
it grows faster than :math:`c^n` for any positive integer constant
:math:`c`.

.. index:: permutations
   single: random uniform_int_distribution
   single: random shuffle
   single: shuffle

**Permutations**
A permutation of a sequence :math:`\mathbf{S}`
is simply the members of :math:`\mathbf{S}` arranged in some order.
For example, a permutation of the integers 1 through :math:`n` would
be those values arranged in some order.
If the sequence contains :math:`n` distinct members, then there are
:math:`n!` different permutations for the sequence.
This is because there are :math:`n` choices for the first member in
the permutation; for each choice of first member there are :math:`n-1`
choices for the second member, and so on.

.. tabbed:: permute

   .. tab:: permute

      Sometimes one would like to obtain a random permutation for a
      sequence, that is, one of the :math:`n!` possible permutations is
      selected in such a way that each permutation has equal probability of
      being selected.
      A simple function for generating a random permutation is as
      follows.

      .. code-block:: cpp

         //Randomly permute the values in array
         void permute(int data[], int n) {
           for (int i = n; i > 0; --i) {
             int j = std::uniform_int_distribution<int> {0, i-1} (eng);
             std::swap(data[i-1], data[j]);  // swap data[i-1] with a random
           }                                 // position in the range 0 to i-1.
         }

      Here, the :math:`n` values of the sequence are stored in
      positions 0 through :math:`n-1` of array ``data``.
      Function :utility:`swap`
      exchanges elements in array ``data``,
      and :numeric:`uniform_int_distribution <random/uniform_int_distribution>`
      returns an integer value uniformly distributed 
      in the range 0 to :math:`i-1`.

   .. tab:: Run It

      .. activecode:: math_permute_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++11']
         :nocodelens:

         #include <iostream>
         #include <random>
         #include <utility>

         namespace {
           // make a random number generator
           std::random_device r;
           std::default_random_engine eng(r());
         }

         //Randomly permute the values in array
         void permute(int data[], int n) {
           for (int i = n; i > 0; --i) {
             int j = std::uniform_int_distribution<int> {0, i-1} (eng);
             std::swap(data[i-1], data[j]);  // swap data[i-1] with a random
           }                                 // position in the range 0 to i-1.
         }
         void print(int data[], int n) {
           for (int i = 0; i<n; ++i) {
             std::cout << data[i] << '\t';
           }
           std::cout << std::endl;
         }
         int main() {
           int data[] = {1,1,2,3,5,8,13,21,34};

           for (int i = 0; i<5; ++i) {
             permute(data, 9);
             print(data, 9);
           }
           std::cout << '\n';
         }


   .. tab:: shuffle

      Randomly shuffling a range of data is a common enough activity
      that it is implemented in the standard library.
      The :algorithm:`shuffle <random_shuffle>` function
      does what our permute function does, but a bit more generically.

      .. code-block:: cpp
         
         std::shuffle(std::begin(data), std::end(data), eng);

      Instead of an entire array it takes a range of data and
      a random number generator.

   .. tab:: Run shuffle

      .. activecode:: math_permute_shuffle_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++11']
         :nocodelens:

         #include <algorithm>
         #include <iostream>
         #include <iterator>
         #include <random>

         namespace {
           std::random_device r;
           std::default_random_engine eng(r());  // make a random number generator
         }

         void print(int data[], int n) {
           for (int i = 0; i<n; ++i) {
             std::cout << data[i] << '\t';
           }
           std::cout << std::endl;
         }
         int main() {
           int data[] = {1,1,2,3,5,8,13,21,34};

           for (int i = 0; i<5; ++i) {
             std::shuffle(std::begin(data), std::end(data), eng);
             print(data, 9);
           }
           std::cout << std::endl;
         }


**Boolean variables** 
A boolean variable
is a variable that takes one of two values:
``true`` or ``false``.
These two values are often associated with the values 1 and 0,
respectively, although there is no reason why this needs to be the
case.
It is poor programming practice to rely on the
correspondence between 0 and False, because these are logically
distinct objects of different types.

**Logic Notation** 
We will occasionally make use of the notation of symbolic or boolean
logic.
:math:`A \Rightarrow B` means ":math:`A` implies :math:`B`" or
"If :math:`A` then :math:`B`".
:math:`A \Leftrightarrow B` means ":math:`A` if and only if :math:`B`"
or ":math:`A` is equivalent to :math:`B`".
:math:`A \vee B` means ":math:`A` or :math:`B`"
(useful both in the context of symbolic
logic or when performing a boolean operation).
:math:`A \wedge B` means ":math:`A` and :math:`B`".
:math:`\sim\!A` and :math:`\overline{A}` both mean "not :math:`A`" or
the negation of :math:`A` where :math:`A` is a boolean variable.

**Floor and ceiling** 
The :term:`floor` of :math:`x` (written :math:`\lfloor x \rfloor`)
takes real value :math:`x` and returns the greatest 
integer :math:`\leq x`.
For example, :math:`\lfloor 3.4 \rfloor = 3`,
as does :math:`\lfloor 3.0 \rfloor`, 
while :math:`\lfloor -3.4 \rfloor = -4` and
:math:`\lfloor -3.0 \rfloor = -3`.
The :term:`ceiling` of :math:`x` (written
:math:`\lceil x \rceil`) takes real value :math:`x` and returns the
least integer :math:`\geq x`.
For example, :math:`\lceil 3.4 \rceil = 4`, as does
:math:`\lceil 4.0 \rceil`,
while :math:`\lceil -3.4 \rceil = \lceil -3.0 \rceil = -3`.

.. [#] The symbol ":math:`\approx`" means "approximately equal."

.. admonition:: More to Explore

   - From cppreference.com

     - :numeric:`Random number generation <random>` and
       :algorithm:`random_shuffle`
     - :numeric:`Common math functions <math>`
     - :algorithm:`is_permuation` and :algorithm:`next_permuation` 
     - :lang:`types` - including ``bool``

