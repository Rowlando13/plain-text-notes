.. a_small_git

A short Git list
============================================

Apologies for the many typos. This page is still under construction. 

The best git reference docs: `Git Docs by Atlassian <https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-init>`_
They are concise and have great illustrations.

A short list of git commands to make everyday workflows easier. I only explain why I find each command particularly helpful. Also, please forgive the terse git messages.  

git log --oneline --all
-------------------------

.. code-block:: text

    >  git log --oneline 
    efcc307 (HEAD -> master) Start a short Git list.
    84a36ce (origin/master, CHERRY-PICK_EXAMPLE) Finished plain text notes.
    1d01377 Finish all but the closing.
    5d66115 Edited some more.
    2a9081b Rewrite a few sections.
    7e7c1ff Fix some typos.
    06e6241 Fix typos. 

One commit per line. --all ? - generally useful, shows other branches

git push origin HEAD 
-----------------------
Shorter alternative to ``git push origin <BRANCH_NAME>`` 

git cherry-pick <commit_hash>
-------------------------------

.. code-block:: text

    >  git checkout CHERRY-PICK_EXAMPLE
    Switched to branch 'CHERRY-PICK_EXAMPLE' 
    >  git cherry-pick efcc307
    [CHERRY-PICK_EXAMPLE fe006e4] Start a short Git list.
    Date: Sat Oct 28 00:06:52 2023 -0700
    2 files changed, 33 insertions(+), 4 deletions(-)
    create mode 100644 docs/source/general/a_small_git.rst 

Apply the changes introduced by an existing commit to your current branch. I find this super useful when I forget to checkout a branch and make a commit on master. I just move the commit then reset the head. 

git fetch origin 
--------------------

git commit -am "Commit message."
---------------------------------------

Useful finer points
----------------------

Your working tree does not need to be clean to use ``git checkout -b FEATURE/SWEET_NEW_ARTICLE``, so you can use it if you forgot to create a branch and are still on master. 