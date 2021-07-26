..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   single: git setup; GitHub

Git setup
=========
All of the assignments in this course are turned in
using a source code change management tool called ``git``.
`Git <https://git-scm.com>`__ is a distributed version-control system
for tracking changes in source code during software development.
It is designed for coordinating work among programmers,
but it can be used to track changes in any set of files.
If you continue working as a programmer, even if your team
doe not use git, it most certainly will use a tool with similar capabilities.

To use Git on the command line, you'll need to download, install, 
and configure Git on your computer. 

.. note::

   You will not be able to turn in any assignments until
   all three steps have been completed.

**Step 1** 

Download and install the version of git appropriate for your operating system
from the  `git download site <https://git-scm.com/downloads>`__.
You may down load the GUI if you like, however, all of the examples
in this text will be on the command line.

If you are only using the Mesa server, you can skip this step.
Git has been installed for you.

**Step 2** 

Setup your username and email address in Git.

Git uses a username to associate commits with an identity.
The Git username is not the same as your GitHub username.
In this class, you should use the name you used to register for this course.

#. Open a terminal or Git Bash
#. Set your Git user name for all repositories on this computer:
   
   .. code-block:: none

      git config --global user.name "Mona Lisa"

#. Confirm your Git user name is set correctly:
   
   .. code-block:: none

      git config --global user.name

   which should display in this case:

   .. code-block:: none

      Mona Lisa

GitHub uses your commit email address to associate commits with your GitHub account.
You can choose the email address that will be associated with the commits you 
push from the command line as well as web-based Git operations you make.

#. Open a terminal or Git Bash
#. Set your Git email address for all repositories on this computer:

   .. code-block:: none

      git config --global user.email "email@example.com"

#. Confirm your Git user email is set correctly:
   
   .. code-block:: none

      git config --global user.email

   which should display in this case:

   .. code-block:: none

      email@example.com

If you want to receive email when I create issues or comment on your code,
then you should use a valid email address.

If you want to keep your email address private, you can do this on GitHub.
For more information see the `Manaing email page <https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/managing-email-preferences/setting-your-commit-email-address#about-commit-email-addresses>`__
on GitHub.

**Step 3** 

Setup authentication.



-----

.. admonition:: More to Explore

   - `Git Documentation <https://git-scm.com/doc>`__
   - `GitHub quickstart <https://docs.github.com/en/get-started/quickstart>`__



