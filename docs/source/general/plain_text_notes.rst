Plain Text Notes 
====================

.. contents:: Overview
   :depth: 2
   :local: 

PLEASE PARDON THE MANY TYPOS. THIS IS STILL UNDER CONSTRUCTION.

Quickstart 
--------------------
Plain Text Notes is my personal format for note taking. It works best for coding, but well for other topics. An explanation in 4 points:

*  plain text
*  Writing style: concise to terse 
*  Flat organization rather than nested 
*  Soft limit of 80 characters per line

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

You should feel like the text is too dense and the sections are very clear. Plain Text Notes format is for your personal notes. As a coder you will read a lot. Whether for learning purposes or to have a section of documentation that is more convenient for you, you should create a ton of notes. Since you will have a lot of text, you want it to be very compact but easily navigable.  You can navigate section to section very easily since they are visible and you made them all, and when you get to the right section, you want it all on the screen.  

You should also feel that the writing is not be perfectly clear to you. You want to write the minimum so that YOU can look back at it in 3-6 months and know exactly what you meant. 

You should also see the reason for the 80 character soft limit. If it does not kill you to keep it to 80 characters, then it much nicer to read. When I was first learning what exactly a commit was doing, I could not fit it in 80 characters. That is fine. See the line that starts: commit -m "<My Django Girls app, first commit>" ...

Plain text notes as a full spec.
----------------------------------- 

*  File type: utf-8 encoded plain text 
*  Writing style: Prefer phrases to complete sentence. Maximum clarity with minimum text.
*  File name: <topic> <subtopic> .txt , eg "Python 3 datetime.txt". The subtopic is optional.
*  Symbol substitution:

      *  substitution start and stop symbol: ``<`` ``>`` 
      *  The command ``git status`` would be written as is since you just type it in. The command ``git remote add url`` would be written as git remote add <url.com>, since you have to replace <url.com> with an actual url. 
      *  The default substitution start and stop symbols may not be suitable for all conditions and can be set on a per document basis.
      *  The text between < and > may hint at how the text is formatted it , eg git config --global user.email <you@gmail.com>. 

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
         <> add file_name.txt = add file_name.txt to the staging area 
         <> add -i = starts an interactive session to sort files into staging area 

*  (Optional) The document may start with a section name that is the same as the document name.  
*  (Recommended) Soft limit of 80 characters per line. 

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

*  Plain text is the fastest most reliable medium in the current era. You can open it on anything. I used to take notes in Google docs / MS word, but they were just to slow to open and I can't open them in my editor. 
*  When I write notes, I target myself three to six months in the future. If I have not thought about something for a while I like to be able to pick back up right where I left off. Your memory is only so good. As of Summer 2023, I have 78 documents on things as mundane as git or as unusual as notes on Attention is All You Need, the paper that sparked the Transformer architecture for Natural Language Processing. Some are only a page, some are 8 pages. There is no way, I could remember all that, but I mostly can because I have my notes. Since there is so much, I need it the notes to be incredibly dense. So I write as concisely as possible with the target clarity in mind. 
*  The substitution start and stop symbol allow you to separate syntax from input date with no context. You know exactly how to modify a shell command for use without looking at another line of the notes.  
*  There are only 5 division levels (2 in the document title and 3 in the document) because you should not need any more. Generally a person can only hold a few things in the front of their mind. Try to hold more and some fall out the back. Where exactly the knowledge you are currently taking notes on falls in the grand organization of knowledge is just noise. You need to be able to connect it closely to something else you can generally place in the overall heireachry. 
*  Starting the document with what section that is its name comes in handy. For me, it is useful when I have a ton of tabs open in my editor.  

Closing thoughts 
---------------------
If I have not yet convinced you to use my format, then make your own. Note taking really can become a super power whereby you expand your working memory immensely. 

The first part of the process is having a format that works you. You may be tempted to put off coming up with a format, but my doing so you choke the growth of you notes which is proportional to their usefulness. I created the plain text notes on document 3 but  was not really convinced I needed a format until I had about 80 pages of notes spread across 20 documents. Your format should be easy for YOU to write. Don't worry about anyone but yourself. Writing is hard for me so that means few words, but the right ones.

The next part is using the notes. They are living documents that need effort to keep them alive. My notes usually lag my knowledge a bit, but not too much. I keep my notes synced between my work and personal computer so I can grow them at work or when working on a personal project. My work time tends to grow my esoteric knowledge of the mundane like a git command to do exactly what I need. My personal projects tend to grow the breadth like what is Mongo DB. 
