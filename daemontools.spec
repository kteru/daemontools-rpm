%define _name	daemontools
%define _ver	0.76
%define _dist	%(sh /usr/lib/rpm/redhat/dist.sh)
%define _rel	1%{?_dist}


Name:		%{_name}
Version:	%{_ver}
Release:	%{_rel}
Summary:	Service Monitoring and Logging Utilities
Group:		Unspecified
License:	Public Domain
URL:		http://cr.yp.to/daemontools.html
Source0:	http://cr.yp.to/daemontools/%{_name}-%{_ver}.tar.gz
Patch0:		daemontools-error.h.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root


%description
daemontools is a collection of tools for managing UNIX services.

supervise monitors a service. It starts the service and restarts the service
if it dies. Setting up a new service is easy: all supervise needs is a directory
with a run script that runs the service.

multilog saves error messages to one or more logs. It optionally timestamps each
line and, for each log, includes or excludes lines matching specified patterns.
It automatically rotates logs to limit the amount of disk space used.
If the disk fills up, it pauses and tries again, without losing any data.


%prep
%setup -q -n admin/%{_name}-%{_ver}
%patch0 -p0


%build
./package/compile


%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/usr/bin
cp -p command/* ${RPM_BUILD_ROOT}/usr/bin
cp -fp ${RPM_SOURCE_DIR}/svscanboot ${RPM_BUILD_ROOT}/usr/bin

%if "%{_dist}" == ".el7"
mkdir -p ${RPM_BUILD_ROOT}/usr/lib/systemd/system
cp -p ${RPM_SOURCE_DIR}/daemontools.service ${RPM_BUILD_ROOT}/usr/lib/systemd/system
%endif
%if "%{_dist}" == ".el6"
mkdir -p ${RPM_BUILD_ROOT}/etc/init
cp -p ${RPM_SOURCE_DIR}/daemontools.conf ${RPM_BUILD_ROOT}/etc/init
%endif


%clean
rm -rf ${RPM_BUILD_ROOT}


%post
[ -d /service ] || mkdir /service

%if "%{_dist}" == ".el6"
initctl reload-configuration
%endif
%if "%{_dist}" == ".el5" || "%{_dist}" == ".el4"
echo 'SV:123456:respawn:/usr/bin/svscanboot' >> /etc/inittab
%endif


%preun
%if "%{_dist}" == ".el7"
systemctl stop daemontools.service
systemctl disable daemontools.service 2> /dev/null
%endif
%if "%{_dist}" == ".el6"
initctl stop daemontools > /dev/null 2>&1 ||:
%endif
%if "%{_dist}" == ".el5" || "%{_dist}" == ".el4"
pkill svscan ||:
pkill svscanboot ||:
%endif


%postun
%if "%{_dist}" == ".el6"
initctl reload-configuration
%endif
%if "%{_dist}" == ".el5" || "%{_dist}" == ".el4"
sed -i '/svscanboot/d' /etc/inittab
%endif

rmdir /service 2> /dev/null ||:


%files
%attr(0755,root,root) /usr/bin/envdir
%attr(0755,root,root) /usr/bin/envuidgid
%attr(0755,root,root) /usr/bin/fghack
%attr(0755,root,root) /usr/bin/multilog
%attr(0755,root,root) /usr/bin/pgrphack
%attr(0755,root,root) /usr/bin/readproctitle
%attr(0755,root,root) /usr/bin/setlock
%attr(0755,root,root) /usr/bin/setuidgid
%attr(0755,root,root) /usr/bin/softlimit
%attr(0755,root,root) /usr/bin/supervise
%attr(0755,root,root) /usr/bin/svc
%attr(0755,root,root) /usr/bin/svok
%attr(0755,root,root) /usr/bin/svscan
%attr(0555,root,root) /usr/bin/svscanboot
%attr(0755,root,root) /usr/bin/svstat
%attr(0755,root,root) /usr/bin/tai64n
%attr(0755,root,root) /usr/bin/tai64nlocal
%if "%{_dist}" == ".el7"
%attr(0644,root,root) /usr/lib/systemd/system/daemontools.service
%endif
%if "%{_dist}" == ".el6"
%attr(0644,root,root) /etc/init/daemontools.conf
%endif


%changelog
* Sun Jul 20 2014 teru <teru@kteru.net>
- Added startup script for el7
* Fri Sep 16 2011 teru <teru@kteru.net>
- Added startup script for el6
* Wed Mar 2 2011 teru <teru@kteru.net>
- Initial version

