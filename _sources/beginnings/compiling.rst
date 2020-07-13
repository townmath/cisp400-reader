..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: compiling,
   single: cmake
   single: clang; clang-tidy; clang-format
   single: git
   single: doctest; catch2

Building software
=================
In this section we will learn one way to compile and run programs.
If you plan to use the Mesa Linux server,
then this section describes what you need to know.
If you plan to use other programs to compile and run your programs
you **still** need to review at least the section describing 
`CMake <https://cmake.org>`__.
All of the labs and projects use the *CMake* build system.

What do we really mean when we say "build software"?
A **software build** (when used as a verb)
is the process of converting a set of **text** and
related **build files** into machine-readable format.
Our job as programmers almost always boils down to converting
plain text files into something else.
A *build* often creates an executable file or a library that
can be included as part of a larger executable.
But just as often programmers convert text into some other 
form of text:

- Convert XML to HTML, for example with `XSLT <https://developer.mozilla.org/en-US/docs/Web/XSLT>`__
- Convert JSON to XML
- Convert a 
  `language independent interface definition <https://developers.google.com/protocol-buffers/docs/cpptutorial>`__
  into a language specific one
- Transpile `Java code into JavaScript <https://stackoverflow.com/a/51349655>`__

We could list more, but you get the point.
We generally do not perform these conversions manually, we use tools.

In this class we will be using a core set of tools to build and test programs:

CMake
   An open-source, cross-platform family of tools designed to build, 
   test and package software.
   CMake is used to control the software compilation process using simple platform
   and compiler independent configuration files. 
   It generates native makefiles, projects, and workspaces
   that can be used in the compiler environment of your choice.

Clang
   The Clang project provides a language front-end and tooling infrastructure for
   languages in the C language family (C, C++, Objective C/C++, OpenCL, CUDA, and RenderScript).
   For our purposes the Clang project provides:

   - ``clang++``: a C++ compiler
   - ``clang-tidy``: a C++ "linter"

     A linting tools is a program that analyzes your source code statically
     (without running it) to check for possible issues or bugs.

   - ``clang-format``: a source code (re) formatter.

   There are many other tools in the Clang suite, but these are the ones
   you'll interact with most often.


Doctest
   ``doctest`` is a fast C++ testing framework based on the popular
   `Catch Unit Test <https://github.com/catchorg/Catch2>`__ framework.

Git
   `Git <https://git-scm.com>`__ is a distributed version-control system
   for tracking changes in source code during software development.
   It is designed for coordinating work among programmers,
   but it can be used to track changes in any set of files.

.. index:: 
   pair: ssh; secure shell
   pair: Linus Torvalds; Linux

How to access the Mesa Server
-----------------------------
All projects and some of the lab assignments are required to be handed in on the
San Diego Mesa College server **buffy**.
Access is only available using a *secure shell* client program (ssh).
There are a few ways to access the server using ``ssh``.
If you have a MacOS X or Linux computer available already, then you already have ssh installed.
If you have a Windows computer, 
then `git <https://git-scm.com>`__ is recommended.
Technically, ``git`` is a source code revision control program,
but it also provides a minimal GNU/Linux environment.
Not too surprising, since the creator, Linus Torvalds, 
is also the creator of Linux).

Another good choice for an SSH
client if you run Microsoft Windows is PuTTY:

.. code-block:: none

   http://www.chiark.greenend.org.uk/~sgtatham/putty/

In ``git`` you would type the following in the *GIT Bash* to connect to the buffy server:

.. code-block:: none

   host@user: ssh fireNN@209.129.16.61

where *fireNN** is the user name assigned to you by the instructor.


.. index:: build steps
   single: Windows System for Linux
   single: WSL

For the impatient: A quick summary
----------------------------------
Lab build files are generated using 
`CMake <https://cmake.org>`__.
Once you have a build file generated for your particular environment,
then you may compile the software and run tests.

.. note::

   All of these steps are demonstrated on a `*nix` style operating system:
   GNU/Linux, Unix, Mac OSX, or Cygwin on Windows.

   I do not know if you could run them on the *Windows System for Linux (WSL)*
   as I have never tried that.

1. First, open a terminal since all of the command that follow are typed
   on the command line.
2. Login to the Mesa server using ``ssh``.
3. Once logged in, change directory to the folder containing a lab
4. Create a new directory to hold the build files and
   have ``cmake`` generate the makefiles:

   .. code-block:: none

      mkdir build
      cd build
      cmake ..

   You only need to do this step once when you make the build
   directory initially.

5. Now you can build the project:

   .. code-block:: none

      make

   and run the tests

   .. code-block:: none

      make test

That it!


This video demonstrates these steps and shows what normal results should look like.

.. youtube:: nQ31ApyU7_o
   :http: https


Most of the time you'll just be compiling code and running lab tests:

- `cd build`
- `make`
- `make test`

The make target ``test`` runs **all** the tests.
Usually when working on a lab, you just want to compile and test that step.
All labs are 'chunked' into steps with a separate test program to test it.

You can compile a single test step by referring to the numbered lab step,
for example:

.. code-block:: none

   make step1

You can run a single test using either the ``make`` target provided
or by running the test using the ``ctest`` program provided by ``CMake``.
for example:

.. code-block:: none

   test/step1
   ctest -R step1

Both of these commands return the exact same output.


-----

.. admonition:: More to Explore

   - `Sofware build <https://en.wikipedia.org/wiki/Software_build>`__
   - `Git Documentation <https://git-scm.com/doc>`__
   - Clang docs

     - `clang-tidy <https://clang.llvm.org/extra/clang-tidy/>`__
     - `clang forst <https://clang.llvm.org/docs/ClangFormat.html>`__
     - `Clang C++ status <https://clang.llvm.org/cxx_status.html>`__
   
   - :doc:`../back-matter/app-a/make`


