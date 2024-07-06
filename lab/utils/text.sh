function banner() {
  echo "Hello $USER"
#  echo """
#ooooo  .oooooo..o           .oooo.     .o
#'888' d8P'    'Y8         .dP''Y88b  o888
# 888  Y88bo.                    ]8P'  888
# 888   ''Y8888o.              .d8P'   888
# 888       ''Y88b 8888888   .dP'      888
# 888  oo     .d8P         .oP     .o  888
#o888o 8''88888P'          8888888888 o888o
#  """
#
  echo """
  Some info HOW TO use this learning program:
  - when you login into dnull.systems You'll see current lesson.
  - Lesson is divided into teoretical examples and practical part.
  -   Examples in teoretical part are excually execured, so You can see real
      results of shown commands!

  -   Practical part is separated into 3 Levels: Junior, Middle and Seniour
      Every next Level is based on the previous one. So to get Seniour level,
      You need to complete Junior and Middle (usually all next Levels means 
      upgrade scripts from the previous). 
      You resulting scores in based on this Levels:
      - Junior -- 3
      - Middle -- 4
      - Seniour - 5

  -  Complete practical part means follow instructions, and create files/scripts/etc
     DO NOT DELETE created files - it is your proff and you score!
     
  -  All lines starting with $ means it is code - run it in you terminal
     (but DO NOT PASTE $ sign into you terminal - just command after $)

  - Everytime you login into systems, examples and practical tasks will appear.
    BUT you can always run command 'learn' to get current lesson in your terminal.
    MOREOVER you can ask 'learn' to show you only one part for the lesson like so:
    $ learn lesson1     -- will print you all lesson1
    $ learn lesson1 pwd -- will print you 'pwd' section from lesson1
    $ learn             -- will print you current lesson

  # TODO: add lessons #1, #2, etc
  # TODO: all sections into lessons
  # TODO: learn show lessons 
  # TODO: learn show sections
  # TODO: learn show sections --lesson 1 (ask for what lesson)
  # TODO: learn --lesson 3
  # TODO: learn --lesson 3 --section pwd  
  # TODO: learn --help
  # TODO: lessons are maps YAML-like:
  # ---
  # current: lesson2
  # lessons:
  #   lesson1:
  #     name: 'Lesson 1'
  #     meta: 'learn how to use pwd and mkdir'
  #     sections:
  #      - example_pwd
  #      - example_mkdir
  #      - practice_pwd
  #      - practice_mkdir
  #   lesson2:
  #     name: 'Lesson 2'
  #     meta: 'learn how to print formated date'
  #     sections:
  #      - format_date
  #      - some other sections
"""
  echo """
  There is shared terminal, feel free to check if:
      url : http://tty.dnull.systems
      user: tty
      pass: observer
"""
read -p "ok..." ok
}

function signature() {
  echo """
If any problems - contact me
"""
}
