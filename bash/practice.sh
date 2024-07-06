source $UTILS/lib.sh
# TODO: edit practice

function practice_pwd() {
echo "PRACTICAL PART"
echo """JUNIOR Level:
  Create file pwd.sh in your home directory:
  $ cd ~/
  $ touch pwd.sh
  Use 'nano' editor to change pwd.sh:
  $ nano pwd.sh
  Write next content:

  #!/bin/bash
  pwd

  To save and exit file use 'Ctrl+O', 'Enter', 'Ctrl+X'

  To be able to run (execute) this file, it is needed to make exec-rights:
  $ chmod +x pwd.sh
  And now run it:
  $ ./pwd.sh

  Done!
  """
sleep 2


echo """MIDDLE Level:
  modify pwd.sh in such way:
  Store 'pwd' into variable CURRENT_DIR:

  CURRENT_DIR=\$(pwd)

  and print (echo) it like so:

  echo 'Current dir: \$CURRENT_DIR'
  """
sleep 2


echo """SENIOR Level:
  modify pwd.sh:
  Print who is owner of pwd.
  Check, if pwd is home for any user - print this user (if any)
"""
sleep 2
}

function practice_touch_rm() {
echo """JUNIOR Level:
  Create file touch.sh in your home directory:
  $ cd ~/
  $ touch touch.sh
  Use 'nano' editor to change touch.sh:
  $ nano touch.sh
  Write next content (you can skip #comments):

  #!/bin/bash
  touch some.file # create file
  ls some.file # check file
  rm some.file # remove file

  To save and exit file use 'Ctrl+O', 'Enter', 'Ctrl+X'

  To be able to run (execute) this file, it is needed to make exec-rights:
  $ chmod +x touch.sh
  And now run it:
  $ ./touch.sh

  Done!
"""
sleep 2

echo """MIDDLE Level:
  Modify touch.sh to be able to
  create, ls, and remove 10 txt files
  in the same time

  touch {1..10}.file # create 10 files
  ls {1..10}.file # check 10 files
  rm {1..10}.file # remove 10 files

"""
sleep 2

echo """
  Modify touch.sh to:
  create var REGEX_FILES='.file'
  if in current directory there is any files like REGEX_FILE
  examples:
    'some_new.file' is like '.file'
    'some.file.in.dir' is like '.file'
    'some_new.txt' is NOT like '.file'
  print this files and delete them
  if no, create up to 10 new files ({1..10}.file)
"""
sleep 2
}


}
