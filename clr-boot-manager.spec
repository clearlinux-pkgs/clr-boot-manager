#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB8987752EC6A08C9 (ikey.doherty@gmail.com)
#
Name     : clr-boot-manager
Version  : 1.5.3
Release  : 19
URL      : https://github.com/clearlinux/clr-boot-manager/releases/download/v1.5.3/clr-boot-manager-1.5.3.tar.xz
Source0  : https://github.com/clearlinux/clr-boot-manager/releases/download/v1.5.3/clr-boot-manager-1.5.3.tar.xz
Source99 : https://github.com/clearlinux/clr-boot-manager/releases/download/v1.5.3/clr-boot-manager-1.5.3.tar.xz.asc
Summary  : Common C library functions
Group    : Development/Tools
License  : LGPL-2.1
Requires: clr-boot-manager-bin
Requires: clr-boot-manager-autostart
Requires: clr-boot-manager-config
Requires: clr-boot-manager-doc
BuildRequires : pkgconfig(blkid)
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(systemd)
BuildRequires : systemd-boot
BuildRequires : systemd-dev
BuildRequires : valgrind
Patch1: service-is-simple.patch

%description
clr-boot-manager
----------------
[![Build Status](https://travis-ci.org/ikeydoherty/clr-boot-manager.svg?branch=master)](https://travis-ci.org/ikeydoherty/clr-boot-manager)
[![Coverage Status](https://coveralls.io/repos/github/ikeydoherty/clr-boot-manager/badge.png?branch=master)](https://coveralls.io/github/ikeydoherty/clr-boot-manager?branch=master)

%package autostart
Summary: autostart components for the clr-boot-manager package.
Group: Default

%description autostart
autostart components for the clr-boot-manager package.


%package bin
Summary: bin components for the clr-boot-manager package.
Group: Binaries
Requires: clr-boot-manager-config

%description bin
bin components for the clr-boot-manager package.


%package config
Summary: config components for the clr-boot-manager package.
Group: Default

%description config
config components for the clr-boot-manager package.


%package doc
Summary: doc components for the clr-boot-manager package.
Group: Documentation

%description doc
doc components for the clr-boot-manager package.


%prep
%setup -q -n clr-boot-manager-1.5.3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1497538335
%configure --disable-static --with-vendor-prefix=Clear-linux \
--with-kernel-modules-dir=/usr/lib/modules \
--with-kernel-namespace=org.clearlinux \
--with-bootloader=systemd-boot
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1497538335
rm -rf %{buildroot}
%make_install
## make_install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/
ln -s ../clr-boot-manager-booted.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/clr-boot-manager-booted.service
## make_install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/clr-boot-manager-booted.service

%files bin
%defattr(-,root,root,-)
/usr/bin/clr-boot-manager

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/clr-boot-manager-booted.service
/usr/lib/systemd/system/clr-boot-manager-booted.service

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
