# CHAPTER 5 (page 113-141)
## Lab 7
### Managing local linux users and groups
####  Useradd / Userdel / sudo
##### Tasks:
**Junior level (3 points)**
Inside ~/labs/7 create new file called lab_7.sh. Modify this file, in any text editor.

First line of ~/labs/7/lab_7.sh must be:

```shell script
#!/bin/bash
```

Next lines must:
* Print current user login:
```shell script
whoami
```
* Print current users (and his groups) id(s)
```shell script
id
```

* Print root`s (and his groups) id(s)
```shell script
id root
```

* Print all users in systems, with ids, groups, real names. home dirs and shells...
```shell script
cat /etc/passwd
```
...and count them:
```shell script
cat /etc/passwd | wc -l
```
* Try to cat /var/log/boot.log.1 (you should get an error)
##### if there is no /var/log/boot.log.1 you can use any file in /var/log/ dir
```shell script
cat /var/log/boot.log.1
```
* Do the same, but with root privileges
```shell script
sudo cat /var/log/boot.log.1
```



---
**Middle level (4 points)**
* Print user groups only (without ids)
* Do the same, but using `cat /etc/group | grep ... | cut ...`  (in this way it is easier to count them)
* Check root`s default shell
* Using sudo, create user vasya, with homedir, and full name "Vasya Testing User" in one command
* Using sudo, create file /home/vasya/some.file.
* Become vasya, and append current date into /home/vasya/some.file (`sudo -u vasya command_under_vasya`). (should get an error)
* Change owner of /home/vasya/some.file to user vasya, group root, using sudo:
```shell script 
sudo chown vasya:root /home/vasya/some.file
```
* Become vasya, and append current date into /home/vasya/some.file (`sudo -u vasya command_under_vasya`). (should NOT get an error)
* Change vasya`s default shell into /sbin/nologin
* Delete user vasya and his home dir. (using only `userdel`)


---
**Senior level (5 points)**
* Create new group with id 9999, prind id of this group.
* Create user vasya.
* Allow this user to become sudo.
* Run `/bin/bash` under vasya user, run `whoami` in this bash, and exit. (Use single command for this).
* Create password change policy, ask to change vasya`s password every month.
* Delete user vasya and his home dir.
