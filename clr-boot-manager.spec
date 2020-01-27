#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-boot-manager
Version  : 3.2.4
Release  : 59
URL      : https://github.com/clearlinux/clr-boot-manager/releases/download/v3.2.4/clr-boot-manager-3.2.4.tar.xz
Source0  : https://github.com/clearlinux/clr-boot-manager/releases/download/v3.2.4/clr-boot-manager-3.2.4.tar.xz
Source1  : clr-boot-manager-motd.service
Summary  : Common C library functions
Group    : Development/Tools
License  : LGPL-2.1
Requires: clr-boot-manager-autostart = %{version}-%{release}
Requires: clr-boot-manager-bin = %{version}-%{release}
Requires: clr-boot-manager-data = %{version}-%{release}
Requires: clr-boot-manager-license = %{version}-%{release}
Requires: clr-boot-manager-man = %{version}-%{release}
Requires: clr-boot-manager-services = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : efivar-dev
BuildRequires : gnu-efi-dev
BuildRequires : pkgconfig(blkid)
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(systemd)
BuildRequires : valgrind
Patch1: 0001-Ease-performance-impact-of-kernel-booted-detection.patch
Patch2: 0002-Motd-updating-script-for-clearlinux.patch
Patch3: 0003-Don-t-set-root-for-Oracle-kernels.patch

%description
clr-boot-manager
----------------
![](https://github.com/clearlinux/clr-boot-manager/workflows/CI/badge.svg)

%package autostart
Summary: autostart components for the clr-boot-manager package.
Group: Default

%description autostart
autostart components for the clr-boot-manager package.


%package bin
Summary: bin components for the clr-boot-manager package.
Group: Binaries
Requires: clr-boot-manager-data = %{version}-%{release}
Requires: clr-boot-manager-license = %{version}-%{release}
Requires: clr-boot-manager-services = %{version}-%{release}

%description bin
bin components for the clr-boot-manager package.


%package data
Summary: data components for the clr-boot-manager package.
Group: Data

%description data
data components for the clr-boot-manager package.


%package license
Summary: license components for the clr-boot-manager package.
Group: Default

%description license
license components for the clr-boot-manager package.


%package man
Summary: man components for the clr-boot-manager package.
Group: Default

%description man
man components for the clr-boot-manager package.


%package services
Summary: services components for the clr-boot-manager package.
Group: Systemd services

%description services
services components for the clr-boot-manager package.


%prep
%setup -q -n clr-boot-manager-3.2.4
cd %{_builddir}/clr-boot-manager-3.2.4
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1580160397
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dwith-vendor-prefix=Clear-linux \
-Dwith-kernel-modules-dir=/usr/lib/modules \
-Dwith-kernel-namespace=org.clearlinux \
-Dwith-bootloader=shim-systemd-boot  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/clr-boot-manager
cp %{_builddir}/clr-boot-manager-3.2.4/LICENSE.LGPL2.1 %{buildroot}/usr/share/package-licenses/clr-boot-manager/01a6b4bf79aca9b556822601186afab86e8c4fbf
cp %{_builddir}/clr-boot-manager-3.2.4/src/libnica/LICENSE.LGPL2.1 %{buildroot}/usr/share/package-licenses/clr-boot-manager/01a6b4bf79aca9b556822601186afab86e8c4fbf
DESTDIR=%{buildroot} ninja -C builddir install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/clr-boot-manager-motd.service
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/
ln -s ../clr-boot-manager-booted.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/clr-boot-manager-booted.service
mkdir -p %{buildroot}/usr/bin
install -m0755 clr-boot-manager-motd.sh %{buildroot}/usr/bin/clr-boot-manager-motd.sh
mkdir -p %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants
ln -sf ../clr-boot-manager-motd.service %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants/clr-boot-manager-motd.service
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/clr-boot-manager-booted.service

%files bin
%defattr(-,root,root,-)
/usr/bin/clr-boot-manager
/usr/bin/clr-boot-manager-motd.sh

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/clr-boot-manager
/usr/share/zsh/site-functions/_clr-boot-manager

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-boot-manager/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/clr-boot-manager.1

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/clr-boot-manager-booted.service
/usr/lib/systemd/system/clr-boot-manager-booted.service
/usr/lib/systemd/system/clr-boot-manager-motd.service
/usr/lib/systemd/system/update-triggers.target.wants/clr-boot-manager-motd.service
