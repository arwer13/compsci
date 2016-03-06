# Questions
- When I install software with a package manager like apt-get, brew, easy-install, and pip, where do these programs get installed? How can I remove them? Is all this software safe?
- When I clone a git repo, how do I turn it into usable software?
- Can I use symbolic links to mirror folders to the cloud?


# Filesystem hierarchy
Linux usually organizes software the other way Windows does. But first some words about filesystem
structure in general. For most of Linux distributives the structure follows the [**Filesystem Hierarchy Standard**](http://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html) maintained by the Linux Foundation. It changes from time to time.
Another quick way to quickly look up this information is `man hier` command.

But let's make a brief overview of basic directories.

- `/etc` system wide configuration files (as well as of system as of applications)
- `/home` root directory where all users home folders are stored by default
- `/var` here one would find various files often changing it's size. Particularly logs, apt cache, 'lock' files of different processes
- `/usr`
- `/dev`
- `/bin`
- `/mnt`
- `/proc`
- `/opt`

One cool feature of Linux is that here _"Everything is a file"_.

## Resources and info command
- [**Filesystem Hierarchy Standard**](http://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)

