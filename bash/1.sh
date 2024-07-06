#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
UTILS=$DIR/../utils
source $DIR/examples.sh
source $DIR/practice.sh
source $UTILS/text.sh

banner


LESSON=${1:-'all'}

case $LESSON in
help)
  example_help
  ;;
pwd)
  example_pwd
  practice_pwd
  ;;
touch)
  example_touch
  example_rm
  practice_touch_rm
  ;;
all)
  example_help
  example_pwd
  practice_pwd
  example_touch
  example_rm
  practice_touch_rm
  #example_mkdir
  #example_ls
  #example_file
  #example_cat
  #example_less
  #example_history
  #example_mv
  #example_find
  ;;
*)
  echo "cant find such lesson."
  ;;
esac

signature


