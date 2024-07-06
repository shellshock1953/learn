# CHAPTER 2 (page 27-34)
## Lab 2
### Managing Files From the Command Line
#### Absolute and Relative path
##### Tasks:
**Junior level (3 points)**

Inside ~/labs/1 create new file called lab_1.sh. Modify this file, in any text editor.

First line of ~/labs/1/lab_1.sh must be:

```shell script
#!/bin/bash
```
Next lines must:
* CD to **/etc** using *absolute* path: 
```shell script
cd /etc/
```
* CD to **/home/** using *absolute* path: 
```shell script
cd /home/
```
* From **/home/** CD to **~/lab_tasks/2/example_folder** using *relative* path: 
```shell script
cd lab_tasks/2/example_folder
```
* From **~/lab_tasks/2/example_folder/** CD to upper directory: 
```shell script
cd ../
```
* List files of **~/lab_tasks/2** using: 
```shell script
ls ~/lab_tasks/
```

---
**Middle level (4 points)**

* CD to **users home** using *absolute* path and print current directory
* CD to **this folder** using *absolute* path and print current directory
* From **users home** CD to **~/lab_tasks/2/example_folder** using *relative* path and than CD to previous directory
* From **users home** list files of **~/lab_tasks/2** using *relative* path

---
**Senior level (5 points)**

* LIST all files (including hidden in **~/lab_tasks/2/example_dir**)
* LIST files of **users home**, without use **~/**. Script must be working for any user, who is running it, so you cant hardcode username (cant use user_name in path, but some variable instead)
---
