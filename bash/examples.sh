TMP_DIR=/tmp/$USER
INNER_DIR=$TMP_DIR/inner_dir

source $UTILS/lib.sh

function example_pwd() {
  header "pwd"
  example "pwd" "Print current dir" "pwd"
  footer
}

function example_ls() {
  header "ls"
  example "ls" """List files in dir (default is current dir)
  ls -a: show hidden files (which starts with '.')
  ls -R: recursively list directory contents
  ls -r: reverse order while sorting
  ls -t: sort by modification time, newest first
""" "ls -l `pwd`"
  show "mkdir $TMP_DIR"
  show "touch $TMP_DIR/file"
  show "touch $TMP_DIR/.hidden_file"
  show "ls -l $TMP_DIR/"
  show "ls -la $TMP_DIR/"
  show "rm -r $TMP_DIR"
  footer
}

function example_touch() {
  TOUCH_FILE=doc.txt
  header "touch"
  example "touch" "Creates file"
  show "touch $TOUCH_FILE"
  show "ls -l $TOUCH_FILE"
  show "rm $TOUCH_FILE"
  footer
}

function example_file() {
  GIF=http://example.com/ascii.gif
  header "file"
  example "file" "Show kind of file" "file 1.sh"
  show "curl $GIF --output some.file --silent"
  show "file some.file"
  show "rm some.file"
  footer
}

function example_cat() {
  header "cat"
  example "cat" "Show contend of file" "cat /etc/os-release"
  show "mkdir $TMP_DIR"
  echo "'Hello world' >> $TMP_DIR/hello.txt"
  echo 'Hello world' >> $TMP_DIR/hello.txt
  show "cat $TMP_DIR/hello.txt"
  show "rm -r $TMP_DIR"
  footer
}
function example_less() {
  header "less"
  example "less" """View file(s)
Press 'up'/'down' to go up and down in file
Press 'q' to exit
  """
  echo "less some_file"
  footer
}

function example_history() {
  header "history"
  example "history" "Print history of entered commands"
  echo "history | tail -10"
  echo "history | grep ls | tail -n1 "
  footer
}

function example_cp() {
  header "cp"
  example "cp" """Copy file from one place to another.
This will override existing files.
  cp -r: copy directories
  cp -p: copy with original file permissions
"""
  show "mkdir $TMP_DIR"
  show "touch $TMP_DIR/1.txt"
  show "cp $TMP_DIR/1.txt $TMP_DIR/2.txt"
  show "ls $TMP_DIR"
  show "rm -r $TMP_DIR"
  footer
}

function example_mv() {
  header "mv"
  example "mv" """Move file from one place to another.
  It can be done to rename file.
  """
  show "mkdir $TMP_DIR"
  show "touch $TMP_DIR/one.file $TMP_DIR/second.file"
  show "mv $TMP_DIR/one.file $TMP_DIR/one.file-NEW"
  show "ls -l $TMP_DIR"
  show "mkdir $TMP_DIR/inner_dir"
  show "mv $TMP_DIR/one.file-NEW $TMP_DIR/second.file $INNER_DIR"
  show "ls -l $INNER_DIR"
  show "rm -r $TMP_DIR"
  footer
}

function example_mkdir() {
  header "mkdir"
  example "mkdir" "Creates directore (like 'touch' but for directories)"
  show "mkdir $TMP_DIR"
  show "mkdir $INNER_DIR"
  show "touch $TMP_DIR/1.txt $INNER_DIR/1.txt"
  show "ls -lR $TMP_DIR"
  show "rm -r $TMP_DIR"
  footer
}

function example_rm() {
  header "rm"
  example "rm" """Removes files and directories
WARNING: there is no 'trash' - so your removed files
will be totally removed!
  rm -r: recursively rm -- used to delete directories
  rm -i: ask to remove
  rm -f: force to remove
"""
  show "mkdir $TMP_DIR"
  show "touch $TMP_DIR/remove.me"
  show "ls $TMP_DIR/remove.me"
  show "rm $TMP_DIR/remove.me"
  show "ls $TMP_DIR/remove.me"
  show "rm -r $TMP_DIR"
  show "ls $TMP_DIR"
  footer
}

function example_find() {
  header "fine"
  example "find" "Search for file(s)"
  echo "find /etc/ -name sshd_config"
  find /etc/ -name sshd_config 2>&1 | grep -v 'Permission denied'
  footer
}

function example_help() {
  header "HELP"
  example "help" """Almoust all commands has its own help.
  <command> -h
  or (depends from <command> itself)
  <command> --help
  for more info check 'man'
  $ man mkdir
"""
  show "mkdir --help"
  footer

}
