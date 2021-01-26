# Linux

## Linux OS
- The operating system is made of three parts:
    - The Programs: a user executes programs. When a program is launched, it creates processes. Program or process will be used interchangeably.
    - The Kernel: handles the main work of an operating system
        - Allocate time and memory to programs
        - Handles File System
        - Responds to various Calls
    - The Shell: a user interacts with the Kernel via the Shell. A user writes instructions in the shell to execute commands. Shell is also a program that keeps asking you to type the name of other programs to run.

## Linux Files and Processes
- Everything in Unix is either a file or a process.
- __Process__: is created when you run a program. Every process is identified by a number called process ID.
    - Check process: `ps`
    - The same program is may be different of process ID
- __File__: is a sequence of data. A program is kept in the form of a file.
    - A file is generally written on the disk. Either HDD or SSD
    - A file is identified by a name called file path. In Unix, everything is represented as file:
        - Devices such as Mouse, Keyboard
        - Programs are saved as file
        - Disk and Monitor

## The Directory Structure
- The top-level directory is `/` called root. `/` directory does not have a parent.
**Relative & Absolute Paths**
- There are two ways to represent a file/directory path
- __Absolute__: represent a file/directory is independent of the current directory of the user.
- __Relative__: relative to the current working directory.

- Create Text File Using Nano
    - `nano textfile.txt`
- Copy a dir into another dir
    - `cp -r dir1 dir2`
    - `-r` means recursively the directories
- Seeing inside File
    - `cat file` see the whole content
    - `tail -10 file` see the last 10 lines
    - `tail -f logfile` --> keep it running on printing newly added lines
    - `head file` see the few first lines
- Use find command
    - `find . -name '*.txt'` find all the text file in the current directory
    - `find / -name '*.txt'` find in the entire system
- Use grep command
    - `grep word file1 file2` list all the lines for files in which a particular word
    - `grep -r file dir` search file in directory
    - `grep -i word file1 file2` search case insensitive
- Use wc command
    - `wc -l file` find the number of lines (words, and chareacters)

## Permissions
- Using chmod to changge the permissions: `chmod permission_cmd file`
- You can allow or disallow the user (u), group (g) or other(o) the following actions: read (r), write (w) and execute (x).
    - `chmod u+x file` allow the user to execute
    - `chmod u-x file` disallow the user to execute
    - `chmod u+rw g+rw file` give the read&write permissions to owner and group
- You can also use numbers to represent the permissions.
- 4 is for Read, 2 is for Write and 1 is for Execute permissions

## Process
- When the file is run, the content of the program is read from file and loaded into the memory and the instructions are executed by operating system.
- All the commands that we have been using like `ls`, `cat` are program
- Find information about processes
    - `ps` list the processes of the system.
    - `ps aux` all of the processes by all users
    - `top` processes are running, taking up most CPU or memory
- To run a program in the background, put an `&` at the end of the command
    - `cmd &`
    - `sleep 1000 &` wait for specificed seconds
    -  `kill processid` kill running process