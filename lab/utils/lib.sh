function next() {
  # TODO exit command from example() ?
  echo
  USER_TMP=/home/$USER/tmp
  echo "creating $USER_TMP (will be deleted after use!)"
  mkdir -p $USER_TMP
  cd $USER_TMP

  echo "Try youself:"
  while read -p "${USER_TMP}/> " resp && [[ "$resp" != 'n' ]]
  do
    $resp
    echo
    echo "enter 'n' to go to the next lesson"
  done
  echo "deleting $USER_TMP"
  rm -r /home/$USER/tmp
}

function example() {
  # $1 -- command itself
  # $2 -- describe
  # $3 -- run example, default is $1
   echo -e "[ $1 ] -- $2"
   if [ ! -z "$3" ]; then
     echo -e "$ ${3}"
     ${3} || true
   fi
   echo "check more examples of '$1':"
   echo
}

function show() {
   echo "$ $1"
   $1 || true
}

function header() {
  # http://artii.herokuapp.com
  echo "$(curl http://artii.herokuapp.com/make\?text\=$1\&font\=roman --silent --max-time 2)" 2>/dev/null
#  echo "-> More examples of '$1':"
}

function footer() {
  next
  echo "-------"
#  clear # nice but removes all previout output
  echo -e "\n\n\n"
}

function weather() {
  curl wttr.in/~"$1"
}

#function jun() {
#  echo "JUNIOR level:"
#  echo $1
#}
#
#function mid() {
#  echo "MIDDLE level:"
#  echo $1
#}
#
#function sen() {
#  echo "SENIOUR level:"
#  echo -e "$1"
#}
