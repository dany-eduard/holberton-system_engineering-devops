# 0x00. Shell, basics
This repo is by me and for me, for me future self.  
This is the commands basics in the Linux Shell.  
![Read The Fuking Manual](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/205/image.jpg)  
  
## Recources
* [What Is “The Shell”?](http://linuxcommand.org/lc3_lts0010.php)
* [Navigation](http://linuxcommand.org/lc3_lts0020.php)
* [Looking Around](http://linuxcommand.org/lc3_lts0030.php)
* [A Guided Tour](http://linuxcommand.org/lc3_lts0040.php)
* [Manipulating Files](http://linuxcommand.org/lc3_lts0050.php)
* [Working With Commands](http://linuxcommand.org/lc3_lts0060.php)
* [Reading Man pages](http://linuxcommand.org/lc3_man_pages/man1.html)
* [Keyboard shortcuts for Bash](https://www.howtogeek.com/howto/ubuntu/keyboard-shortcuts-for-bash-command-shell-for-ubuntu-debian-suse-redhat-linux-etc/)
* [LTS](https://wiki.ubuntu.com/LTS)
* [Shebang](https://en.wikipedia.org/wiki/Shebang_%28Unix%29)  
  
**Man or Help**  
```cd```: Change the shell working directory (_cd, cd .., cd ~, cd /path_).  
```ls```: List directory contents (_ls, ls -l, ls -1, ls -R, ls -s_).  
```pwd```: Print the full filename of the current working diretory (_pwd --> /user/dir/current_).  
```less```: Show the contents of a file (_less filename_).  
```file```: Show file type (_file namefile_).  
```ln```: Make links between files (_ln --symbolic DIRECTORY/ LINK_NAME, ln --physical DIRECTORY/ LINK_NAME_).  
```cp```: Copy files and directories (_cp SOURCE DIRECTORY/_).  
```mv```: Move files or rename files or directories (_mv SOURCE DIRECTORY/, mv NAME NEWNAME_).  
```rm```: Remove files or directories (_rm FILES, rm --force FILES, rm --recursive FILES_).  
```mkdir```: Make directories (_mkdir NAME_DIR_).  
```type```: Display information about command type (_type COMMAND, type less --> less is hashed (/usr/bin/less), type pwd --> pwd is a shell builtin_).  
```which```: Shows the full path of (shell) commands.  
```help```: Display information about builtin commands.  
```man```: An interface to the system reference manuals (_man COMMAND_).  
  
## Requirements
* All your scripts should be exactly two lines long ($ wc -l file should print 2)
* All your files should end with a new line ([why?](https://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789))
* The first line of all your files should be exactly ```#!/bin/bash```
* You are not allowed to use backticks, ```&&```, ```||```or ```;```
* All your scripts must be executable. To make your file executable, use the ```chmod``` command: ```chmod u+x file```  
  
## Task
### 0. Where am I?
_Write a script that prints the absolute path name of the current working directory._
* File: **[0-current_working_directory](https://github.com/dany-eduard/holberton-system_engineering-devops/blob/master/0x00-shell_basics/0-current_working_directory)**  
  
***Example***
```
$ ./0-current_working_directory
/Users/holbertonschool/holbertonschool-sysadmin_devops/0x00-shell_basics
$
```
  
______________________________________________________
### 1. What’s in there?
_Display the contents list of your current directory._
* File: **[1-listit](https://github.com/dany-eduard/holberton-system_engineering-devops/blob/master/0x00-shell_basics/1-listit)**  
  
***Example***
```
$ ./1-listit
Applications    Documents   Dropbox Movies Pictures
Desktop Downloads   Library Music Public
$
```
  
______________________________________________________
### 2. There is no place like home 
_Write a script that changes the working directory to the user’s home directory._
* File: **[2-bring_me_home](https://github.com/dany-eduard/holberton-system_engineering-devops/blob/master/0x00-shell_basics/2-bring_me_home)**  
  
***Example***
```
julien@ubuntu:/tmp$ pwd
/tmp
julien@ubuntu:/tmp$ echo $HOME
/home/julien
julien@ubuntu:/tmp$ source ./2-bring_me_home
julien@ubuntu:~$ pwd
/home/julien
julien@ubuntu:~$ 
```
  
______________________________________________________
### 3. The long format 
_Display current directory contents in a long format_
* File: **[3-listfiles](https://github.com/dany-eduard/holberton-system_engineering-devops/blob/master/0x00-shell_basics/3-listfiles)**  
  
***Example***
```
$ ./3-listfiles
total 32
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
$
```
  
______________________________________________________
### 4. Hidden files 
_Display current directory contents, including hidden files (starting with .). Use the long format._
* File: **[4-listmorefiles](https://github.com/dany-eduard/holberton-system_engineering-devops/blob/master/0x00-shell_basics/4-listmorefiles)**  
  
***Example***
```
$ ./4-listmorefiles
total 32
drwxr-xr-x@ 6 sylvain staff 204 Jan 25 00:29 .
drwxr-xr-x@ 43 sylvain staff 1462 Jan 25 00:19 ..
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:41 4-listmorefiles
$
```
  
______________________________________________________
### 5. I love numbers 
_Display current directory contents._
* Long format
* with user and group IDs displayed numerically
* And hidden files (starting with .)
* File: **[5-listfilesdigitonly](https://github.com/dany-eduard/holberton-system_engineering-devops/blob/master/0x00-shell_basics/5-listfilesdigitonly)**  
  
***Example***
```
$ ./5-listfilesdigitonly
total 32
drwxr-xr-x@ 6 501 20 204 Jan 25 00:29 .
drwxr-xr-x@ 43 501 20 1462 Jan 25 00:19 ..
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:23 1-listfiles
-rwxr-xr-x@ 1 501 20 19 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 501 20 20 Jan 25 00:39 3-listfiles
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:41 4-listmorefiles
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:43 5-listfilesdigitonly
$
```
  
______________________________________________________
### 6. Welcome holberton
_Create a script that creates a directory named ```holberton``` in the ```/tmp/``` directory._
* File: **[6-firstdirectory](https://github.com/dany-eduard/holberton-system_engineering-devops/blob/master/0x00-shell_basics/6-firstdirectory)**  
  
***Example***
```
$ ./6-firstdirectory
$ file /tmp/holberton/
/tmp/holberton/: directory
$
```
  
______________________________________________________
### 7. Betty in Holberton 
_Move the file ```betty``` from ```/tmp/``` to ```/tmp/holberton```._
* File: **[7-movethatfile](https://github.com/dany-eduard/holberton-system_engineering-devops/blob/master/0x00-shell_basics/7-movethatfile)**  
  
***Example***
```
$ ./7-movethatfile
$ ls /tmp/holberton/
betty
$
```
  
______________________________________________________
### 8. Bye bye Betty 
_Delete the file ```betty```._
* The file ```betty``` is in ```/tmp/holberton```
* File: **[8-firstdelete](https://github.com/dany-eduard/holberton-system_engineering-devops/blob/master/0x00-shell_basics/8-firstdelete)**  
  
***Example***
```
$ ./8-firstdelete
$ ls /tmp/holberton/
$
```
  
______________________________________________________
### 9. Bye bye Holberton 
_Delete the directory ```holberton``` that is in the ```/tmp directory```._
* File: **[9-firstdirdeletion](https://github.com/dany-eduard/holberton-system_engineering-devops/blob/master/0x00-shell_basics/9-firstdirdeletion)**  
  
***Example***
```
$ ./9-firstdirdeletion
$ file /tmp/holberton
/tmp/holberton: cannot open `/tmp/holberton' (No such file or directory)
$
```
  
______________________________________________________
### 10. Back to the future 
_Write a script that changes the working directory to the previous one._
* File: **[10-back](https://github.com/dany-eduard/holberton-system_engineering-devops/blob/master/0x00-shell_basics/10-back)**  
  
***Example***
```
julien@ubuntu:/tmp$ pwd
/tmp
julien@ubuntu:/tmp$ cd /var
julien@ubuntu:/var$ pwd
/var
julien@ubuntu:/var$ source ./10-back
/tmp
julien@ubuntu:/tmp$ pwd
/tmp
```
  
______________________________________________________
### 11. Lists 
_Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the ```/boot``` directory (in this order), in long format._
* File: **[11-lists](https://github.com/dany-eduard/holberton-system_engineering-devops/blob/master/0x00-shell_basics/11-lists)**  
  
______________________________________________________
### 12. File type 
_Write a script that prints the type of the file named ```iamafile```. The file ```iamafile``` will be in the ```/tmp``` directory when we will run your script._
* File: **[12-file_type](https://github.com/dany-eduard/holberton-system_engineering-devops/blob/master/0x00-shell_basics/12-file_type)**  
  
***Example***
```
ubuntu@ip-172-31-63-244:~$ ./12-file_type
/tmp/iamafile: ELF 64-bit LSB  executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=bd39c07194a778ccc066fc963ca152bdfaa3f971, stripped
```
  
______________________________________________________
### 13. We are symbols, and inhabit symbols 
_Create a symbolic link to ```/bin/ls```, named ```__ls__```. The symbolic link should be created in the current working directory._
* File: **[13-symbolic_link](https://github.com/dany-eduard/holberton-system_engineering-devops/blob/master/0x00-shell_basics/13-symbolic_link)**  
  
***Example***
```
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
total 144
drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 03:24 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:24 ..
ubuntu@ip-172-31-63-244:/tmp/sym$./13-symbolic_link
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
total 144
drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 03:24 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:24 ..
lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -> /bin/ls
```
  
______________________________________________________
### 14. Copy HTML files 
_Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory._
_You can consider that all HTML files have the extension .html_
* File: **[14-copy_html](https://github.com/dany-eduard/holberton-system_engineering-devops/blob/master/0x00-shell_basics/14-copy_html)**  
  
______________________________________________________
### 15. Let’s move 
_Create a script that moves all files beginning with an uppercase letter to the directory ```/tmp/u```._
_You can assume that the directory ```/tmp/u``` will exist when we will run your script_
* File: **[15-lets_move](https://github.com/dany-eduard/holberton-system_engineering-devops/blob/master/0x00-shell_basics/15-lets_move)**  
  
***Example***
```
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
total 148
drwxrwxr-x  3 ubuntu ubuntu   4096 Sep 20 03:33 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:26 ..
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 Holberton
lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -> /bin/ls
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 Notrebloh
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 random_file
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la /tmp/u
total 8
drwxrwxr-x 2 ubuntu ubuntu 4096 Sep 20 03:33 .
drwxrwxr-x 3 ubuntu ubuntu 4096 Sep 20 03:33 ..
ubuntu@ip-172-31-63-244:/tmp/sym$ ./15-lets_move
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
total 148
drwxrwxr-x  3 ubuntu ubuntu   4096 Sep 20 03:33 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:26 ..
lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -> /bin/ls
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 random_file
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la /tmp/u
total 8
drwxrwxr-x 2 ubuntu ubuntu 4096 Sep 20 03:33 .
drwxrwxr-x 3 ubuntu ubuntu 4096 Sep 20 03:33 ..
-rw-rw-r-- 1 ubuntu ubuntu    0 Sep 20 03:32 Holberton
-rw-rw-r-- 1 ubuntu ubuntu    0 Sep 20 03:32 Notrebloh
```
  
______________________________________________________
### 16. Clean Emacs 
_Create a script that deletes all files in the current working directory that end with the character ```~```._
* File: **[16-clean_emacs](https://github.com/dany-eduard/holberton-system_engineering-devops/blob/master/0x00-shell_basics/16-clean_emacs)**  
  
***Example***
```
ubuntu@ip-172-31-63-244:/tmp/sym$ ls
main.c  main.c~  Makefile~
ubuntu@ip-172-31-63-244:/tmp/sym$ ./16-clean_emacs
ubuntu@ip-172-31-63-244:/tmp/emacs$ ls
main.c
ubuntu@ip-172-31-63-244:/tmp/emacs$
```
  
______________________________________________________
### 17. Tree 
_Create a script that creates the directories ```welcome/```, ```welcome/to/``` and ```welcome/to/holberton``` in the current directory._ 
_You are only allowed to use two spaces in your script, not more._
* File: **[17-tree](https://github.com/dany-eduard/holberton-system_engineering-devops/blob/master/0x00-shell_basics/17-tree)**  
  
***Example***
```
julien@ubuntu:/tmp/h$ ls -l
total 4
-rwxrw-r-- 1 julien julien 44 Sep 20 12:09 17-tree
julien@ubuntu:/tmp/h$ wc -l 17-tree 
2 17-tree
julien@ubuntu:/tmp/h$ head -1 17-tree 
#!/bin/bash
julien@ubuntu:/tmp/h$ tr -cd ' ' < 17-tree | wc -c # you do not have to understand this yet, but the result should be 2, 1 or 0
2
julien@ubuntu:/tmp/h$ ./17-tree 
julien@ubuntu:/tmp/h$ ls
17-tree  welcome
julien@ubuntu:/tmp/h$ ls welcome/
to
julien@ubuntu:/tmp/h$ ls -l welcome/to
total 4
drwxrwxr-x 2 julien julien 4096 Sep 20 12:11 holberton
julien@ubuntu:/tmp/h$ 
```
  
______________________________________________________
### 18. Life is a series of commas, not periods 
_Write a command that lists all the files and directories of the current directory, separated by commas (,)._
* Directory names should end with a slash (/)
* Files and directories starting with a dot (.) should be listed
* The listing should be alpha ordered, except for the directories . and .. which should be listed at the very beginning
* Only digits and letters are used to sort; Digits should come first
* You can assume that all the files we will test with will have at least one letter or one digit
* The listing should end with a new line
* File: **[18-commas](https://github.com/dany-eduard/holberton-system_engineering-devops/blob/master/0x00-shell_basics/18-commas)**  
  
***Example***
```
ubuntu@ip-172-31-63-244:~/holbertonschool$ ls -a

.  ..  0-commas  0-commas-checks  1-empty_casks  2-gifs  3-directories  4-zeros  5-rot13  6-odd  7-sort_rot13  Makefile  quote  .test  test_dir  test.var

ubuntu@ip-172-31-63-244:~/holbertonschool$ ./18-commas

./, ../, 0-commas, 0-commas-checks/, 1-empty_casks, 2-gifs, 3-directories, 4-zeros, 5-rot13, 6-odd, 7-sort_rot13, Makefile, quote, .test, test_dir/, test.var

ubuntu@ip-172-31-63-244:~/holbertonschool$
```
  
______________________________________________________
### 19. File type: Holberton
_Create a magic file ```holberton.mgc``` that can be used with the command ```file``` to detect ```Holberton``` data files. ```Holberton``` data files always contain the string ```HOlBERTON``` at offset 0._
* File: **[holberton.mgc](https://github.com/dany-eduard/holberton-system_engineering-devops/blob/master/0x00-shell_basics/holberton.mgc)**  
  
***Example***
```
ubuntu@ip-172-31-63-244:/tmp/magic$ cp /bin/ls .
ubuntu@ip-172-31-63-244:/tmp/magic$ ls -la
total 268
drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 02:44 .
drwxrwxrwt 11 root   root   139264 Sep 20 02:44 ..
-rw-r--r--  1 ubuntu ubuntu    496 Sep 20 02:42 holberton.mgc
-rwxr-xr-x  1 ubuntu ubuntu 110080 Sep 20 02:43 ls
-rw-rw-r--  1 ubuntu ubuntu     50 Sep 20 02:06 thisisanholbertonfile
-rw-rw-r--  1 ubuntu ubuntu     30 Sep 20 02:16 thisisatextfile
ubuntu@ip-172-31-63-244:/tmp/magic$ file --mime-type -m holberton.mgc *
holberton.mgc:         application/octet-stream
ls:                    application/octet-stream
thisisanholbertonfile: Holberton
thisisatextfile:       text/plain
ubuntu@ip-172-31-63-244:/tmp/magic$ file -m holberton.mgc *
holberton.mgc:         data
ls:                    data
thisisanholbertonfile: Holberton data
thisisatextfile:       ASCII text
ubuntu@ip-172-31-63-244:/tmp/magic$
```  
  
________________________________________________________________  
  
⌨️ con ❤️ por [dany eduard](https://github.com/dany-eduard) 😊
