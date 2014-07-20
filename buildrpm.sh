#!/usr/bin/env bash
DIR_BASE=$(cd ${BASH_SOURCE[0]%/*} && pwd)
set -e

DIR_RPMBUILD=`rpm --eval %{_topdir}`
mkdir -p ${DIR_RPMBUILD}/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

cd ${DIR_RPMBUILD}/SOURCES
cp -af ${DIR_BASE}/daemontools-0.76.tar.gz .
cp -af ${DIR_BASE}/daemontools-error.h.patch .
cp -af ${DIR_BASE}/daemontools.conf .
cp -af ${DIR_BASE}/daemontools.service .
cp -af ${DIR_BASE}/svscanboot .
cd - > /dev/null

cd ${DIR_RPMBUILD}/SPECS
cp -af ${DIR_BASE}/daemontools.spec .
cd - > /dev/null

rpmbuild -ba --clean ${DIR_RPMBUILD}/SPECS/daemontools.spec

