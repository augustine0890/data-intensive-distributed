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