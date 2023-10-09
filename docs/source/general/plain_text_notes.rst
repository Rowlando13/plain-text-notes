Plain Text Notes 
====================

.. contents:: Overview
   :depth: 2
   :local: 

Quickstart 
--------------------
Plain Text Notes is my personal format for note taking. It works best for coding, but well for other topics. I think it could work well for a lot of coders. An explanation in 4 points:

*  plain text
*  Writing style: concise to terse 
*  Flat organization rather than nested 
*  Soft limit of 80 characters per line

An example of my notes on git from when I was just learning it

.. code-block:: text 
   :caption: notes/git.txt

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

You should feel like the text with in sections is too dense and the section breaks are very clear. Plain Text Notes is for your personal notes. As a coder you will read a lot. You should create a lot notes. Since you will have a lot of text, you want it to be very compact but easily scannable.  Hence, the clear section breaks and dense sections.  

You should also feel that the writing is not be perfectly clear to you. You want to write the minimum amount so that YOU can look back at it in 3-6 months and know exactly what you meant. 

You should also see a reason for the 80 character soft limit. It is much nicer to read. Putting the character limit forces you to write with fewer words and break up complex statements into simpler ones. The character limit is soft because sometimes it's more trouble than it's worth. 

Plain text notes as a full spec.
----------------------------------- 

*  File type: utf-8 encoded plain text 
*  Writing style: Prefer phrases to complete sentence. Maximum clarity with minimum text.
*  File name: <topic> <subtopic> .txt , eg "Python3 datetime.txt". The subtopic is optional.
*  Symbol substitution:

      *  substitution start and stop symbol: ``<`` ``>`` 
      *  The command ``git status`` would be written as is since you just type it in. The command ``git remote add url`` would be written as git remote add <url.com>, since you have to replace <url.com> with an actual url. 
      *  The default substitution start and stop symbols may not be suitable for all conditions and can be set on a per document basis.
      *  The text between < and > may hint at how the text is formatted in it , eg git config --global user.email <you@gmail.com>. 

*  There are only 3 division levels available in a document. 

      *  The section name is indented 12 spaces, ie 3 tabes of 4 spaces. The number of spaces per tab may vary by user preference between 2 and 4.
      *  The paragraph name is aligned left. 
      *  The sub statements are preceded by <> and one space.

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
         <> add file_name.txt = adds file_name.txt to the staging area 
         <> add -i = starts an interactive session to sort files into staging area 

*  (Recommended) Soft limit of 80 characters per line. 
*  (Optional) The document may start with a section name that is the same as the document name.  

Useful patterns for taking coding notes.
------------------------------------------

.. code-block:: text 
   :caption: Good defaults as statement. Less frequent ones as sub statements.

   git commands 
   log --oneline = show the current log with 1 commit per line
   <> log --graph --decorate --oneline = draws text based graph, adds the 
   names of branches or tags
   <> log <file_path> = shows commit history for file 

*  Start a topic with a document with no sub topic. When the document grows too large, split it into a 2 or more documents and add a sub topic. I rarely split documents. The documents can grow quite large since you know everything in them.

*  Arrange lists alphabetically from the start. You don't often know how long a list will be until it is mostly done.

Reasoning
--------------------------

*  Plain text is the fastest most reliable medium in the current era. You can open it on anything. I used to take notes in Google docs / MS word, but they were just to slow to open and I can't open them in my text editor. 
*  When I write notes, I target myself three to six months in the future. If I have not thought about something for a while I like to be able to pick back up right where I left off. As of Summer 2023, I have 78 documents on things as mundane as git or as unusual as Attention is All You Need, a seminal paper for Natural Language Processing. Some are only a page, some are 8 pages. There is no way, I could remember all that, but I mostly can because I have my notes. Since there is so much, I need the notes to be incredibly dense. So I write as concisely as possible with the target clarity in mind. 
*  The substitution start and stop symbol allow you to separate syntax from input data with no context. You know exactly how to modify a command for use without looking at another line of the notes.  
*  There are only 5 division levels (2 in the document title and 3 in the document) because you should not need any more. With more levels, I spend to much time moving statements from level to level. 
*  Starting the document with a section that is its name comes in handy. For me, it is useful when I have a ton of tabs open in my editor.  

Closing thoughts 
---------------------
If I have not yet convinced you to use my format, then make your own. Note taking really can become a super power whereby you expand your working memory immensely.

The first part of the process is having a format that works you. You may be tempted to put off coming up with a format, but not doing so will choke the growth of you notes which is proportional to their usefulness. I created Plain Text Notes on document number 3, and by 20 documents I was glad that I had. Your format should be easy for YOU to write. Writing is hard for me so that means few words, but the right ones.

The next part is using the notes. They are living documents that need effort to stay alive. My notes usually lag my knowledge a bit, but not too much. I keep my notes synced between my work and personal computer so I can grow them at work or when working on a personal project. For me this is a must because work and play provide different things for the notes. My work time tends to grow my knowledge of the mundane like a git command to do exactly what I need. My personal projects tend to grow the breadth like MongoDB.
