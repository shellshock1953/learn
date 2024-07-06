# CHAPTER 2 (page 41-45)
## Lab 3
### Managing Files From the Command Line
#### File manipulations
##### Tasks:
**Junior level (3 points)**
Inside ~/labs/3 create new file called lab_3.sh. Modify this file, in any text editor.

First line of ~/labs/3/lab_3.sh must be:

```shell script
#!/bin/bash
```

Next lines must:
* COPY all files from ~/lab_tasks/3/files into ~/labs/3/
```shell script
cp ~/lab_tasks/3/files/* ~/labs/3/
```
* in ~/labs/3/ RENAME file_1.txt into file_1.mp3
```shell script
cd ~/labs/3/
mv file_1.txt file_1.mp3
```
* DELETE file_2.txt
```shell script
rm file_2.txt
```
* COPY directory ~/lab_tasks/3/directory into ~/labs/3/
```shell script
cp -r ~/lab_tasks/3/directory ~/labs/3/
```
---
**Middle level (4 points)**

* MOVE all files from ~/labs/3/directory into ~/labs/3/ using relative path
* COPY file_3.txt into ~/labs/3/directory/
* MOVE file_4.txt from ~/labs/3/ into ~/labs/3/directory
* LIST ALL files in ~/labs/3/
* LIST ALL files in ~/labs/3/directory

---
**Senior level (5 points)**

* Create directory ~/labs/3/a/b/c using one command
* Delete directoty ~/labs/3/a using one command
---
