# 100 Days Of Code - Log


### Day 26 Jun 1, 2018

**Today's Progress**: Continue with Git

**Thoughts:** Strategies to avoid Merge conflict (see below). Stash is not part of working directory, staging or repo. It is often used when switching branches but not quite ready to make a commit on changes. No SHA value assigned for Stash.
. 
- keep the lines short
- keep commits small and focused
- beware stray edits to whitespaces : tab, spaces, line returns
- merge often
- track changes to master

**Link to work:** None


### Day 25 Jun 8, 2018

**Today's Progress**: Continue with Git

**Thoughts:** More on branches

To merge a branch:
- checkout to receiving branch eg ```git check master```
- ```git merge <sending branch>```
- ``` git diff master..<sending branch>``` will show no differenc after merge operation
- ```git branch --merged``` will show <sending branch> fully incorporate in receiving branch; may delete sending branch


**Link to work:** None


### Day 24 Jun 6, 2018

**Today's Progress**: Continue with Git

**Thoughts:** More on branches

-```git branch -m <old branch name> <new branch name>``` (rename branch)

**Link to work:** None


### Day 23 Jun 5, 2018

**Today's Progress**: Continue with Git

**Thoughts:** Branches
-```git checkout <branch name>``` (creates branch)
- ```git checkout -b <branch name>``` (creates branch and switches to it)
-```git branch``` (list branches and which is the current branch)
-```git diff master..<branchB>``` (compare tip of  master and Branch B)

**Link to work:** None


### Day 22: Jun 4, 2018

**Today's Progress**: Continue with Git

**Thoughts:** Useful git log commands to compare different commits :
```git diff --stat --summary <SHA Value>..HEAD``` (pretty summary showing changes from range of commits)
```git diff -w <SHA Value>..HEAD``` (Ignore space changes)

Branch allows you to :
- try new ideas
- section of work areas to allow teams to collaborate on different parts

**Link to work:** None


### Day 21: Jun 3, 2018

**Today's Progress**: Continue with Git
ich 
**Thoughts:** Learned '''git reset'''. Options are '''--soft''' and '''--mixed'' which reset the HEAD pointer to earlier commits while leaving the files in working or staging directory. '''--hard''' resets to the another repository.

.gitignore file is placed in the root project directory. Commit .gitignore file.

For user-specific .gitignore use ```git config --global core.excludefiles ~/.gitignore_gobal``` (or any descriptive filename)

```git rm --cached <filename>``` remove <filename> from the staging index but not the repo. Use case : initial log committed to repo but not needed to track changes to log file
  
Git tracks files not directories. So to track empty directories, convention is to create a small .gitkeep file in the empty directory you wish to track

**Link to work:** None


### Day 20: Jun 2, 2018

**Today's Progress**: Continue with Git. 

**Thoughts:** 
- Another fundamental in Git is that ***changes are applied in set***. 
- Git refers to Commits (snapshots of changes) by their hash values,and metadata such as author, parent, message, 
- Learned commands such as ```git diff``` (check differences in modified file and original in ***working*** directory, ```git checkout -- <filename>``` (revert to original file committed to repository; ```--``` means using current branch instead of switching to a different branch) 

List of git commands learnt so far:
- git config --list
- git init
- git status
- git diff (working directory)
- git diff --staged (staging directory)
- git add
- git commit -m "..."
- git log
- git checkout
- git commit --amend -m "..." (changes to last commit; not possible to change earlier commits)

**Link to work:** None


### Day 19: Jun 1, 2018

**Today's Progress**: Back from break. Started Git Tutorial from LinkedIn Tutorial.

**Thoughts:** Got a good grasp of fundamentals of Working Director, Staging Directory, and Repository. Git Windows did not seem to recognize modified file in working directory. Switched to Ubuntu for tutorial. Also used linux commands like find and sed and xargs to make changes to text in multiple files, eg ```find . -type f -not -path '*/\.git/*' | xargs sed -i 's/_backpack.html/_backpack_cal.html/'```

**Link to work:** None


### Day 18: Aprl 21, 2018

**Today's Progress**: Swithched gears. Think Stats. No coding. Reviewed data of NSFG (CDC's National Survey of Family Growth)

**Thoughts:** NSFG is a cross-sectional study, ie snapshot of a group at a point in time. Longitudinal study observes a group repeatedly over a period of time

**Link to work:** None


### Day 17: Aprl 18, 2018

**Today's Progress**: Tried out examples on namedtuple, Counter, defaultdict, and gather/scatter keyword argument

**Thoughts:** note argument in defautldict

**Link to work:** goodies.py


### Day 16: Aprl 16, 2018

**Today's Progress**: Tried out examples on Set and Generators.

**Thoughts:** Defined Set as 'a collection of dictionary keys with no values'; previously thought of Set as List with no duplicates

**Link to work:** goodies.py


### Day 15: Aprl 14, 2018

**Today's Progress**: Reviewed example of Markov Analysis. Looked up https://www.investopedia.com/terms/m/markov-analysis.asp. Had some problem with *prefix* tuple datas structure (single element require a comma at the end).  Dpn't understand how the variable/arguement *script* is used. Also, tried examples of conditional expression, list comprehension.

**Thoughts:** Need to review data structures like tuple and dictionary again

**Link to work:** markov.py, goodies.py


### Day 14: Aprl 12, 2018

**Today's Progress**: Took a break from Inheritance in Think Python to learn about file operations in Python

**Thoughts:** use *with open(filepath) as fp* pattern; strip() method; split(' ') method for words

**Link to work:** file.py


### Day 13: Aprl 8, 2018

**Today's Progress**: Started on Chapter 18 : Inheritance

**Thoughts:** learned class inheritance. Hand class inherited methods from Deck class. Tried Visual Studio Code with Python extension and vim key bindings. quite cool. will try out both vim with extensions and vs code

**Link to work:** Card.py


### Day 12: Aprl 7, 2018

**Today's Progress**: Started on Chapter 18 : Inheritance

**Thoughts:** distinguish between class attributes (which are defined inside a class but outside any method) and instance attribute. Alsu used new Python 3.6 f formatter. 

**Link to work:** Card.py


### Day 11: Aprl 6, 2018

**Today's Progress**: last exercise in  chapter 17 : Classes and Method

**Thoughts:** struggled with __str__ method. remember not to put () after class name when defining class. when instantiating class, then use () with parameters if needed. To uncomment code in vim in Windows, use Ctrl-Q (not Ctrl-V) to go into visual block, highlight block then Shift-I to go into Insert mode, then # and escape. Do reverse when uncommenting, but use x on the # character

**Link to work:** Kangaroo.py

### Day 10: Aprl 5, 2018

**Today's Progress**: Worked on more exercise in chapter 17 : Classes and Method

**Thoughts:** learned about .gitignore in git. not sure how to hide dotfile and un files created by vim (persistent undo and backup) https://stackoverflow.com/questions/15660669/what-is-a-un-file-or-or-why-does-vim-in-the-terminal-make-the-un-file

**Link to work:** Point2.py, Time2.py


### Day 9: Aprl 3, 2018

**Today's Progress**: Worked on exercise in chatper 17 : Classes and Method

**Thoughts:** __init__ makes it easier to instantiate objects and __str__ which is useful for debugging. Other special methods include __add__, __lt__, ... http://docs.python.org/3/reference/datamodel.html#specialnames

**Link to work:** Point2.py, Time2.py

### Day 8: Aprl 2, 2018

**Today's Progress**: No coding. Just read chapter 17 of Think Python 2nd Ed

**Thoughts:** introduce methods to programmer defined types, ie class

**Link to work:** NA


### Day 7: Aprl 1, 2018

**Today's Progress**: Finished exercises on datetime objects

**Thoughts:** not quite sure about timedelta object and attributes

**Link to work:** Time1.py


### Day 6: March 31, 2018

**Today's Progress**: More exercise on Time class

**Thoughts:** use replace r in vim to edit characters more efficiently

**Link to work:** Time1.py

### Day 5: March 30, 2018

**Today's Progress**: worked on time. learned about Functional Program which doesn't change the objects it takes as its parameter

**Thoughts:** don't know how to efficently comment out code in vim. Control v paste instead of go into visual block

**Link to work:** Time1.py

### Day 4: March 29, 2018

**Today's Progress**: skipped 28 Mar because of work. Resumed last fuction : draw rectangle

**Thoughts:** for loop : instead of iterable object (for x in range(5)), use explicit expression, ie for x in a, b, c, d.

**Link to work:** draw.py

### Day 3: March 27, 2018

**Today's Progress**: Worked on Classes and Objects exercises 15.2 from Think Complexity. 

**Thoughts:** Learn that when import module polygon, refer to function by using dot notation : eg polygon.circle. Also vim plug-ins show useful hints if imported modules/fuction are available

**Link to work:** draw.py

### Day 2: March 26, 2018

**Today's Progress**: Worked on Classes and Objects exercises 15.1 from Think Complexity. 

**Thoughts:** Learn how reuse classes and functions by importing Point.py as module and how to navigate in VIM and also add-on NERDTree)

**Link to work:** Cicle.py (worked on function Rectangle in Circle; pending one more function)

### Day 1: March 25, 2018

**Today's Progress**: Worked on Classes and Objects exercises 15.1 from Think Complexity. 

**Thoughts:** Learn how reuse classes and functions by importing Point.py as module and how to navigate in VIM and also add-on NERDTree)

**Link to work:** Cicle.py (still WIP; haven't worked on 2 more functions)


### Day 0: March 24, 2018

**Today's Progress**: Worked on Classes and Objects exercises, Chatper 15 from Think Complexity. 

**Thoughts:** Spent a lot of time setting up VIM and github on Windows 10. Learnt basics of Github from https://try.github.io/levels/1/challenges/1 and StackFlow https://stackoverflow.com/questions/37937984/git-refusing-to-merge-unrelated-histories-on-rebase when couldn't get git pull and push to work (first pull forked repository with --allow-unrelated-histories flag then git push)

**Link to work:** Point.py
