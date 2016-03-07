# Questions
- When I install software with a package manager like apt-get, brew, easy-install, and pip, where do these programs get installed? How can I remove them? Is all this software safe?
- When I clone a git repo, how do I turn it into usable software?
- Can I use symbolic links to mirror folders to the cloud?


# Filesystem hierarchy
For most of Linux distributives filesystem structure follows the [**Filesystem Hierarchy Standard**](http://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html) maintained by the Linux Foundation. It changes from time to time.
Another way to quickly look up this information is `man hier` command.

But let's make a brief overview of basic directories.
- `/etc`: system wide configuration files (system and of applications)
- `/var`: here one would find various files often changing it's size. Particularly logs, apt cache, 'lock' files of different processes.
- `/home`: root directory where all users home folders are stored by default
- `/usr`: here are libraries, binaries, application's various stuff.
- `/mnt`: usually partitions mounted by user.
- `/media`: usually partitions automounted by system.
- `/opt`: applications 'installed` without package manager knowledge, all app files in one folder. 

One cool feature of Linux is that here _"Everything is a file"_. That's why, for example, one may work with devices as with files
- `/dev`: representations of various devices (and some other stuff): hard drives, plugged usb sticks, audio, video etc.

For example, when one plugs a usb stick it might appear as `/dev/sdc1`, and to manually mount it to `/mnt/usb` one could do

    mount /dev/sdc1 /mnt/usb

- `/proc`: contains information about running processes, and various system parameters.

In fact objects in `/dev` in `/proc` are not actual files, but special system objects which behave themselves like files, so that one could use regular file API to query and manage them.

# Packaging
Linux usually organizes software the other way Windows does.
Common way to install an application or library is to use a package manager.
It would spread application files over whole filesystem, putting various types of files in appropriate places.
Configuration files would usually go to
- `/etc`
- user's home as hidden files or folders
- `.config` in user's home.

Libraries and binaries usually go to `/usr`.
When user runs command from shell the shell searches for it in folders listed in `PATH` environmental variable. On my machine it looks like this

    PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games

Package manager saves information for every package about where it's files are located. To see this information for apt (there is a `dpkg` in it's core) one may use `dpkg -L <package_name>` command.

So applications installed by means of package manages must be removed the same way.

Packages installed by means of package managers in most cases should be considered safe. At least as long as these packages are more or less popular and there no warning about package repository authenticity.

But sometimes applications may also be distributed just like portable programs on Windows, all needed (more or less) files in one folder. For example if one would install PyCharm he would download a regular archive, extract it whenever he wants and run a binary file inside. In this case the `/opt` is a good place to store extracted application. In my case `/opt` looks this (the output is produced by `tree -L 1 /opt` command)

    /opt
    ├── echo-msk-downloader
    ├── google
    ├── pycharm-community-5.0.4
    ├── ranger
    └── Telegram


If one would like to run an application cloned from a git repo, he should follow specific instruction contained in this repo. But in general the recipe is as follows:

1. clone it to whereever you like
2. install all required dependencies
3. build the application (if it needs to be built)
4. prepare additional environment (for example, set some environmental variables)
5. run it. If you'd like to run it from command line, create a symbolic link to it in some binaries folder (`/usr/local/bin` for example)


# Links usages
- Mirror folders to the cloud is OK. I can't accurately remember at the moment why I decided so, but I usually do it contrariwise: store actual files in cloud folder and make links to them in appropriate places. In this case if I would eventually move files which are not in cloud folder, this action wouldn't spoil the links in cloud folder and the files wouldn't be deleted in the cloud unnoticeably for me.
