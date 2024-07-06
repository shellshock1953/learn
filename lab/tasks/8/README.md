# CHAPTER 6 (page 143-154)
## Lab 8
### Controlling access to files with linux file system permissions
#### Chmod / Chown
##### Tasks:
**Junior level (3 points)**
Inside ~/labs/8 create new file called lab_8.sh. Modify this file, in any text editor.

First line of ~/labs/8/lab_8.sh must be:

```shell script
#!/bin/bash
```

Next lines must:
* List files in your home dir
```shell script
ls /home/$USER
```
or (`~` is shortcut)
```shell script
ls ~/
```
* List permissions for your files:
```shell script
ls -l ~/
```
* ...also list hidden files (wich names starts with '.')
```shell script
ls -al ~/
```

* Create new file:
```shell script
touch ~/labs/8/new.file
```

* Print your name into this file
```shell script
echo $USER > ~/labs/8/new.file
```

* Disallow write to this file.

Remember about numeric rights:

<center>

| r | w | x |
|---|---|---|
| 4 | 2 | 1 |

</center>

```shell script
chmod 400 ~/labs/8/new.file
```

* Again add your name into this file (should get an error)
```shell script
echo $USER > ~/labs/8/new.file
```

* Allow write to file:
```shell script
chmod 644 ~/labs/8/new.file
```

---
**Middle level (4 points)**
* Create new dir ~/labs/8/recur/sion (use `-p` argument to create inner dirs in one command)
* Create 10 txt files inside ~/labs/8/recur/sion (`touch {1..10}.txt`)
* Change owner of ~/labs/8/recur and all inner dirs and files to root:nobody.
* Re-change owner of ~/labs/8/recur to your user.



---
**Senior level (5 points)**
* Create new dir ~/labs/8/recur/sion (use `-p` argument to create inner dirs in one command)
* Create 10 log files inside ~/labs/8/recur
* Create 10 txt files inside ~/labs/8/recur/sion
* Change owner of ~/labs/8/recur/5.log to root
* Change owner or ~/labs/8/recur/sion/5.txt to nobody
* Find all not users files in ~/labs/8
* Re-change owner of ~/labs/8/recur dir to your user.
