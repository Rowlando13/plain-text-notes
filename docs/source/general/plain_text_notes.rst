Plain text notes 
====================

.. contents:: Overview
   :depth: 2
   :local: 

Quickstart 
--------------------
Plain text notes is my personal format for note taking. It works best for coding, but well for other topics. An explanation in X points:

*  plain text
*  Writing style: concise to terse 
*  Flat rather than nested 
*  Soft limit of 80 characters

An example of my notes on git from when I was just learning it

.. code-block:: text 
   :caption: git.txt

            git

            general 

   Terms
   branch = separate line of development, generally used for different features. 
   <> When a branch is done, then it is merged into the master. 
   commit = equivalent to a save, but does not push to remote
   detached head state = not working on any branch. If commit in this state, 
   commit will be orphaned  (not attached to any branch), and up for garbage 
   collection and deletion. 
   Repository (REPO) = virtual storage container with your project in it
   remote (remote REPO) = Central REPO
   staging area = holding area used prior to committing to review changes
   tracked = file/directory that has been previously staged or committed. 
   untrack = file/directory that has not previously been staged or committed. 
   ignored = file/directory included in .gitignore 

   Useful commands
   config --global user.name "<Your Name>" = configures username 
   config --global user.email <you@gmail.com> = configures email 
   commit -m "<My Django Girls app, first commit>" = pushes a snapshot at that 
   point in time to my local respository. At some later time, I can merge with 
   the central repository. -m " " uses the quoted message as the message for 
   the commit. 
   remote add origin <url> = adds repository(remotes) named origin using url. 
   remote set-url origin <newurl.com> = changes the url for origin to newurl.com
   push -u origin master = updates remote refs with local refs from origin to 
   branch named master 
   reset --hard = discard local changes
   pull origin master = pulls remote called origin branch named master to location
   checkout -b <NEW_BRANCH> = in local repo create branch "new branch" based 
   on last commit from master.

You should feel like text is too dense and the sections are very clear. The notes format is for your personal notes. As a coder you read a lot. Whether for learning purposes or to have a section of documentation that is more convenient for you, you will create a ton of notes. You want to be able to scan or control f the doc and easily jump between sections. You made these notes, so you know exactly whats in them. When you get to the right section, you want it all on the page. You can quickly scan to the right line and read it, just like code. 

You should also feel that the writing might not be perfectly clear to you. You want to write the minimum so that YOU can look back at it in 3-6 months and know exactly what you meant. 

You should also see the reason for the 80 character soft limit. If it does not kill you to keep it to 80 characters, then it much nice to read. When I was first learning what exactly a commit was doing, I could not fit it in 80 characters. That is fine. 

Plain text notes as a full spec.
----------------------------------- 

*  File type: utf-8 encoded plain text 
*  Writing style: Prefer phrases to complete sentence. Maximum clarity with minimum text.
*  File name: <topic> <subtopic> .txt , eg "Python 3 datetime.txt". The subtopic is optional 
*  Symbol substitution:

      * substitution start and stop symbol: ``<`` ``>`` 
      * The command ``git status`` would be written as is since you just type it in. The command ``git remote add url`` would be written as git remote add <url.com>, since you have to replace <url.com> with an actual url. 
      * The default substitution start and stop symbols may not be suitable for all conditions and can be set on a per document basis.
      * The text between < and > may hint at how the text is formatted it , eg git config --global user.email <you@gmail.com>. 

*  There are only 3 division levels available in a document. 

      * The section name is indented 12 spaces, ie 3 tabes of 4 spaces. The number of spaces per tab may vary by user preference between 2 and 4.
      * The paragraph name is aligned left. 
      * The sub statements are preceded by <> and one space.

      .. code-block:: text 
         :caption: <Topic> <subtopic>.txt

                  <Section name>

         <Paragraph name>
         <statement>
         <> <sub statement>

      .. code-block:: text 
         :caption: selections from notes on git 

                  General 

         Commands: (All commands prefaced by git)
         add --all = adds all files to the staging area, except those removed by git ignore.
         <> add file_name.txt = add file_name.txt to the staging area 
         <> add -i = starts an interactive session to sort files into staging area 

*  (Optional) The document may start with a section name that is the same as the document name.  
*  (Recommended) Soft limit of 80 characters per line. 

Useful patterns for taking coding notes.
------------------------------------------

.. code-block:: text 
   :caption: Good defaults as statement. Less frequent ones as substatements.

   git commands 
   log --oneline = show the current log with 1 commit per line
   <> log --graph --decorate --oneline = draws text based graph, adds the 
   names of branches or tags
   <> log <file_path> = shows commit history for file 