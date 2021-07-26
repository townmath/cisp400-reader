..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: compiling,
   single: cmake; make
   single: clang; clang-tidy; clang-format; gcc
   single: git; ssh
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
   languages in the C language family.
   For our purposes the Clang project provides:

   - ``clang``: a C compiler
   - ``clang++``: a C++ compiler
   - ``clang-tidy``: a C++ "linter"

     A linting tools is a program that analyzes your source code statically
     (without running it) to check for possible issues or bugs.

   - ``clang-format``: a source code (re) formatter.
   - ``lldb``: a debugger.

     A debugger is a program that allows you to control and view internal
     details of your program.
     You can pause execution, view or change variables, and see source code.
     As the name implies, the tool is usually used to help find and fix bugs.


   There are many other tools in the Clang suite, but these are the ones
   you'll interact with most often.

   Clang is the default compiler on MacOS and is an option 
   on most Linux based systems.

Doctest
   `doctest <https://github.com/onqtam/doctest/blob/master/doc/markdown/tutorial.md>`__
   is a fast C++ testing framework based on the popular
   `Catch Unit Test <https://github.com/catchorg/Catch2>`__ framework.
   Most labs use doctest to assess your work as you progress through the lab.

GCC
   The GNU Compiler Collection (GCC) provides a tooling infrastructure for
   C, C++, FORTRAN, and a few other languages.
   For our purposes GCC provides:

   - ``gcc``: a C compiler
   - ``gcc++``: a C++ compiler
   - ``gdb``: a debugger.

   GCC is the default compiler for most Unix and Linux based systems.

Git
   `Git <https://git-scm.com>`__ is a distributed version-control system
   for tracking changes in source code during software development.
   It is designed for coordinating work among programmers,
   but it can be used to track changes in any set of files.

Make
   The ``make`` program is a tool used to help make things.
   Using *make* we define *targets* in a text file and each *target*
   runs a *recipe*. 
   Using targets and recipes in combination allows make to perform many
   complex tasks automatically.


On Linux based systems these tools work together like this:

- We use ``git`` to download the latest copy of our code.
- We use ``CMake`` to create our build files, which are generally Makefiles.
- Once the Makefile has been created, we use ``make`` to perform tasks.
  The simplest command ``make`` will try to build all the software in the
  current directory.

  Make will use either ``gcc`` or ``clang`` to actually compile code.

- Test cases are written using the ``doctest`` library and build using ``make``.

.. index:: 
   pair: ssh; secure shell
   pair: Linus Torvalds; Linux

How to access the Mesa Server
-----------------------------
All projects and some of the lab assignments are required to be handed in on the
San Diego Mesa College server **buffy**.
Access is only available using a *secure shell* client program (ssh).
There are a few ways to access the server using ``ssh``.
If you have a MacOS or Linux computer available already, then you already have ssh installed.
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

In ``git`` you would type the following in the *GIT Bash* 
to connect to the server:

.. code-block:: none

   ssh fireNN@209.129.16.61

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
   GNU/Linux, Unix, MacOS, or Cygwin on Windows.

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

.. index:: compiling locally
   single: IDE

.. _local-compile-label:

Compiling code on your local computer
=====================================
The following sections describe briefly how to get started with
a local development environment, if you wish.

If you plan to use the Mesa server,
then you can ignore the rest of this section.

In all cases, you still need to install 
`git <https://git-scm.com>`__ and
`CMake <https://cmake.org>`__.

This book does **not** explain how to install these :term:`IDE's<IDE>`.
Use the documentation provided with your IDE for that.

Compiling with Visual Studio
----------------------------
In this course you need to be using Visual Studio 2019
at a minimum to complete all the assignments.

In order to enable CMake integration with Visual Studio
ensure you have the additional software for Linux C++ development.

Use git to clone your assignments repository to your computer.
Now you are ready to compile an assignment.

.. tabbed:: tab_msvc

   .. tab:: GUI

      These instructions describe how to build software using the
      Visual Studio Graphical User Interface (GUI).

      1. Create a directory named build and open CMake GUI.
      2. Select 'Browse Source' and select the folder containing 
         the lab you want to build.
      3. Select 'Browse Build' and select the `build` folder you created.
      4. In the lower left corner, select 'Configure' and
         select 'Visual Studio 16 2019 Win64' from the list of
         available generators.

         Leave the remaining selections alone and
         press 'Finish` when done.

         Don't worry (yet) if you see any warnings or errors.
      5. Press 'Generate'. When finished ("Generating done")
         close CMake GUI.
      6. Open the generated solution (.sln) file in Visual Studio.

      Build the solution then open
      Test --> Windows --> Test Explorer to view test results or rerun tests.

      If this doesn't work, try
      the instructions on the 
      `Microsoft site <https://docs.microsoft.com/en-us/cpp/build/cmake-projects-in-visual-studio?view=vs-2017>`__.

      Select the documentation for your version of Visual Studio.

   .. tab:: Terminal

      These instructions describe how to build software using the
      Using the Visual Studio command line

      1. Create a directory named build adjacent, but **not in** your source directory.
      2. Open the Visual Studio Developer prompt.
         `cd` into the build directory created in the previous step.
      3. Type `cmake ..`

         This should create a standard Visual Studio solution that
         you can run from the command line or the IDE.

      4. Type `MSBuild lab1.sln` to build all projects in the **Debug** configuation
      5. Type `ctest -C Debug` to run all tests


      To remove all executable files:

      .. code-block:: none

         MSBuild lab1.sln -target:Clean
         MSBuild lab1.sln -t:Clean

      To build a single test:

      .. code-block:: none
         
         MSBuild lab1.sln -t:step1

      To build all files in **Release** configuration,
      without any Debug symbols:

      .. code-block:: none

         MSBuild lab1.sln -p:Configuration=Release
         # run tests
         ctest -C Release

      If this doesn't work, try
      `the instructions on the Microsoft site <https://docs.microsoft.com/en-us/cpp/build/walkthrough-compiling-a-native-cpp-program-on-the-command-line?view=vs-2019>`__


Compiling with Code Blocks
--------------------------
Use git to clone your assignments repository to your computer.
Now you are ready to compile an assignment.

1. Create a directory named build and open CMake GUI.
2. Select 'Browse Source' and select the folder containing 
   the lab you want to build.
3. Select 'Browse Build' and select the `build` folder.
4. In the lower left corner, select 'Configure' and
   select 'CodeBlocks - MinGW Makefiles' from the list of
   available generators.

   Leave the radio selections alone and
   press 'Finish` when done.

   Campus windows computers may complain about a `sh.exe` program in your path
   outside of CodeBlocks.
   To fix this error:

   - Delete the CMake variable `CMAKE_SH` in the variables list.
   - Press 'Configure' a second time.

5. Press 'Generate'. When finished ("Generating done")
   close CMake GUI.
6. Open the generated "CBP" file in CodeBlocks.
   It should be in the build folder you pointed at in step 3.

Build the 'all' target to compile and link programs and tests.
Test cases must be run individually - 
there is no target to run all the tests.

Compiling with XCode
--------------------
Use git to clone your assignments repository to your computer.
Now you are ready to compile an assignment.

Open a terminal in the directory containing your lab, then:

.. code-block:: none

   mkdir build
   cd build
   cmake -G Xcode ..

Open the Xcode project and build as usual.


-----

.. admonition:: More to Explore

   - `Sofware build <https://en.wikipedia.org/wiki/Software_build>`__
   - `Git Documentation <https://git-scm.com/doc>`__
   - Clang docs

     - `clang-tidy <https://clang.llvm.org/extra/clang-tidy/>`__
     - `clang format <https://clang.llvm.org/docs/ClangFormat.html>`__
     - `Clang C++ status <https://clang.llvm.org/cxx_status.html>`__
   
   - :doc:`make`


