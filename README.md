HPL
===
Hyeyoung's Python Library (HPL) is a collection of Python programs by Hyeyoung Shin.

The wjd_debug branch contains some comments, suggestions, and minor modifications 
by William.  (These are usually merged into the master branch.)

You can clone (i.e., import) the HPL repository onto your local computer as
follows (on a Mac):

1.  Open a terminal window.

2.  Make sure you have the git program installed.  Type git --help at the command line.
    If you get unexpected results, install git as described here:

    http://git-scm.com/book/en/Getting-Started-Installing-Git#Installing-on-Mac

3.  Create a directory on your computer called git, as follows:

        cd              # (change to your come directory)
        mkdir -p git    # (make a directory called git)

4.  Change to the git directory and clone the HPL repository:

        cd git
        git clone git@github.com:williamdemeo/HPL.git

You will now have a directory called ~/git/HPL, where the files in the HPL
repository are stored.  You can modify these files and then check them back 
in with the command:

    git commit -a -m "description of the changes you made"
    git push origin master

Please let me know if you have questions!

-William