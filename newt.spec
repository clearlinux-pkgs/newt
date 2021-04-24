#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : newt
Version  : 0.52.21
Release  : 14
URL      : https://releases.pagure.org/newt/newt-0.52.21.tar.gz
Source0  : https://releases.pagure.org/newt/newt-0.52.21.tar.gz
Summary  : A development library for text mode user interfaces
Group    : Development/Tools
License  : LGPL-2.0
Requires: newt-bin = %{version}-%{release}
Requires: newt-lib = %{version}-%{release}
Requires: newt-license = %{version}-%{release}
Requires: newt-locales = %{version}-%{release}
Requires: newt-man = %{version}-%{release}
Requires: newt-python = %{version}-%{release}
Requires: newt-python3 = %{version}-%{release}
BuildRequires : grep
BuildRequires : popt-dev
BuildRequires : python3-dev
BuildRequires : slang-dev
Patch1: fix-python-path.patch

%description
Newt
----
Newt is a programming library for color text mode, widget based user
interfaces.  Newt can be used to add stacked windows, entry widgets,
checkboxes, radio buttons, labels, plain text fields, scrollbars,
etc., to text mode user interfaces.  Newt is based on the slang library.

%package bin
Summary: bin components for the newt package.
Group: Binaries
Requires: newt-license = %{version}-%{release}

%description bin
bin components for the newt package.


%package dev
Summary: dev components for the newt package.
Group: Development
Requires: newt-lib = %{version}-%{release}
Requires: newt-bin = %{version}-%{release}
Provides: newt-devel = %{version}-%{release}
Requires: newt = %{version}-%{release}
Requires: newt = %{version}-%{release}

%description dev
dev components for the newt package.


%package lib
Summary: lib components for the newt package.
Group: Libraries
Requires: newt-license = %{version}-%{release}

%description lib
lib components for the newt package.


%package license
Summary: license components for the newt package.
Group: Default

%description license
license components for the newt package.


%package locales
Summary: locales components for the newt package.
Group: Default

%description locales
locales components for the newt package.


%package man
Summary: man components for the newt package.
Group: Default

%description man
man components for the newt package.


%package python
Summary: python components for the newt package.
Group: Default
Requires: newt-python3 = %{version}-%{release}

%description python
python components for the newt package.


%package python3
Summary: python3 components for the newt package.
Group: Default
Requires: python3-core

%description python3
python3 components for the newt package.


%prep
%setup -q -n newt-0.52.21
cd %{_builddir}/newt-0.52.21
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583186647
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --with-python=python$(python3 -V | awk '{print $2}' | sed 's/\.[0-9]*$//g')
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
export SOURCE_DATE_EPOCH=1583186647
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/newt
cp %{_builddir}/newt-0.52.21/COPYING %{buildroot}/usr/share/package-licenses/newt/ba8966e2473a9969bdcab3dc82274c817cfd98a1
%make_install
%find_lang newt

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/whiptail

%files dev
%defattr(-,root,root,-)
/usr/include/newt.h
/usr/lib64/libnewt.so
/usr/lib64/pkgconfig/libnewt.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnewt.so.0.52
/usr/lib64/libnewt.so.0.52.21

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/newt/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/whiptail.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f newt.lang
%defattr(-,root,root,-)

