# CHAPTER 3 (page 61-85)
## Lab 5
### Getting help
#### Man, pinfo, whatis
##### Tasks:
**Junior level (3 points)**
Inside ~/labs/5 create new file called lab_5.sh. Modify this file, in any text editor.

First line of ~/labs/5/lab_5.sh must be:

```shell script
#!/bin/bash
```

Next lines must:
* Get short info about notify-send
```shell script
man -f notify-send
```
or
```shell script
whatis notify-send
```

* Check full man about notify-send
```shell script
man notify-send
```

* Basic on man, try to send desktop notification.
For additional help (if any), you can check:
```shell script
notify-send --help
```

* Use `pinfo` for more guided way, of getting info.

Check how to use nano (use arrows to navigate):
```shell script
pinfo nano
```


---
**Middle level (4 points)**
* Calculate, how many times (it must be a number) ssh appears in man-pages (tip: `man -k ssh`). 

* Get all info about nano, using `whatis, where, which, whereis`. Using `echo` describe differences in those commands.

* Print ssh version.


---
**Senior level (5 points)**
* Check, from which repo/package nano has been installed.

* Print nano version, using notify-send in format:

title: Nano Version

body: $NANO_VERSION

* Do the same for ssh. >;)
