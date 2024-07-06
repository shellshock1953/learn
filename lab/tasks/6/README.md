# CHAPTER 4 (page 87-111)
## Lab 6
### Creating, Viewing and Editing text files
#### Stdout, stderr, tee and /dev/null
##### Tasks:
**Junior level (3 points)**
Inside ~/labs/6 create new file called lab_6.sh. Modify this file, in any text editor.

First line of ~/labs/6/lab_6.sh must be:

```shell script
#!/bin/bash
```

Next lines must:
* Create ~/labs/6/6.log
```shell script
touch ~/labs/6/6.log
```
* Redirect your name into ~/labs/6/6.log (because file is empty, we can overwrite it)
```shell script
echo "YOU_NAME" > ~/labs/6/6.log
```
* Append current date into ~/labs/6/6.log file
```shell script
date >> ~/labs/6/6.log
```

* Append last login into ~/labs/6/6.log
```shell script
last -n 1 >> ~/labs/6/6.log
```

* `cat` non existing file (you should get an error message)
```shell script
cat ~/i_dont_exists.txt
```

* `cat` non existing file, but without any error messages(tips: /dev/null is like shredder)
```shell script
cat ~/i_dont_exists.txt 2> /dev/null
```

* `cat` existing file, but without any **error** messages
```shell script
cat ~/labs/6/6.log 2> /dev/null
```


---
**Middle level (4 points)**
* Send 10 ping-packets into i.ua site, append output into ~/labs/6/6.log
* Send 10 ping-packets into non existing a.a site, append output into ~/labs/6/6.errors
* Append random number into ~/labs/6/6.log, in such format:

This is random number: $RANDOM_NUMBER

* To get more familiar with VIM, run vimtutor.
* EXIT THE VIM :)
* Using one command, open ~/labs/6/6.log on 3rd line. (tip: run vim with `+`)


---
**Senior level (5 points)**
* Using script, install vim NerdTREE plugin

* Ask user to enter site name. Ping this site (10 times), and log successful packets into ~/labs/6/6.log and unsuccessful into ~/labs/6/6.error. 
**Bonus Level** (for hardcore players): Use `tee` print stdout and stderr outputs in realtime.
(tip: http://www.softpanorama.org/Tools/tee.shtml)
