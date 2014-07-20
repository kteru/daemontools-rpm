daemontools-rpm - A tools for building daemontools rpm package
==============================================================

Supported distribution
----------------------

- RHEL/CentOS 7.x x86_64
- RHEL/CentOS 6.x x86_64/i386
- RHEL/CentOS 5.x x86_64/i386
- CentOS 4.x x86_64/i386

How to use
----------

### Common

Clone daemontools-rpm

```
$ git clone https://github.com/kteru/daemontools-rpm.git
```

Get source code

```
$ cd /path/to/daemontools-rpm
$ wget http://cr.yp.to/daemontools/daemontools-0.76.tar.gz
```

### RHEL/CentOS 7.x

Install requirements

```
$ sudo yum -y install rpm-build redhat-rpm-config make gcc
```

Build/Install rpm

```
$ cd /path/to/daemontools-rpm
$ ./buildrpm.sh
$ sudo rpm -ivh /path/to/daemontools-<VER>-<REL>.<DIST>.<ARCH>.rpm
```

Launch

```
# systemctl enable daemontools.service
# systemctl start daemontools.service
```

### RHEL/CentOS 6.x

Install requirements

```
$ sudo yum -y install rpm-build redhat-rpm-config make gcc
```

Build/Install rpm

```
$ cd /path/to/daemontools-rpm
$ ./buildrpm.sh
$ sudo rpm -ivh /path/to/daemontools-<VER>-<REL>.<DIST>.<ARCH>.rpm
```

Launch

```
# initctl start daemontools
```

### RHEL/CentOS 5.x / CentOS 4.x

Install requirements

```
# yum -y install rpm-build redhat-rpm-config make gcc
```

Build/Install rpm

```
# cd /path/to/daemontools-rpm
# ./buildrpm.sh
# rpm -ivh /path/to/daemontools-<VER>-<REL>.<DIST>.<ARCH>.rpm
```

Launch

```
# /usr/bin/svscanboot &
# jobs
[1]+  Running                 /usr/bin/svscanboot &
# disown %1
```

