Summary: A utility for determining file types
Name: file
Version: 5.48
Release: 1
License: BSD
Source0: %{name}-%{version}.tar.gz

# revert upstream commits (rhbz#2167964)
# 1. https://github.com/file/file/commit/e1233247bbe4d2d66b891224336a23384a93cce1
# 2. https://github.com/file/file/commit/f7a65dbf1739a8f8671621e41c5648d1f7e9f6ae
Patch1: file-5.45-readelf-limit-revert.patch

URL: https://github.com/sailfishos/file

Requires: file-libs = %{version}-%{release}
BuildRequires: zlib-devel

%description
The file command is used to identify a particular file according to the
type of data contained by the file.  File can identify many different
file types, including ELF binaries, system libraries, RPM packages, and
different graphics formats.

You should install the file package, since the file command is such a
useful utility.

%package libs
Summary: Libraries for applications using libmagic

%description libs

Libraries for applications using libmagic.

%package devel
Summary:  Libraries and header files for file development
Requires: %{name} = %{version}-%{release}

%description devel
The file-devel package contains the header files and libmagic library
necessary for developing programs using libmagic.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}

%description doc
Man pages for %{name}.


%prep
# Don't use -b -- it will lead to problems when compiling magic file
%autosetup -n %{name}-%{version}/upstream -p1

%build
autoreconf -f -i
CFLAGS="%{optflags} -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE" \
%configure --disable-libseccomp --disable-silent-rules
%make_build

%check
make -C tests check

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/misc
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/file

%make_install
rm -f ${RPM_BUILD_ROOT}%{_libdir}/*.la

cat magic/Magdir/* > ${RPM_BUILD_ROOT}%{_datadir}/file/magic
ln -s file/magic ${RPM_BUILD_ROOT}%{_datadir}/magic
ln -s ../magic ${RPM_BUILD_ROOT}%{_datadir}/misc/magic

mkdir -p ${RPM_BUILD_ROOT}%{_docdir}/%{name}-%{version}
install -m0644 -t ${RPM_BUILD_ROOT}%{_docdir}/%{name}-%{version} \
        ChangeLog README.md


%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%license COPYING
%{_bindir}/*

%files libs
%{_libdir}/*so.*
%{_datadir}/magic*
%{_datadir}/file
%{_datadir}/misc/*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/libmagic.pc
%{_includedir}/magic.h

%files doc
%{_mandir}/man1/%{name}.*
%{_mandir}/man*/*magic.*
%{_docdir}/%{name}-%{version}
