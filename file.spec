%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%define __libtoolize :

Summary: A utility for determining file types
Name: file
Version: 5.14
Release: 4
License: BSD
Group: Applications/File
Source0: ftp://ftp.astron.com/pub/file/file-%{version}.tar.gz
Patch0: file-aarch64.patch
Patch4: file-5.14-CVE-2014-1943.patch
Patch5: file-5.14-CVE-2014-2270.patch
Patch6: file-5.14-CVE-2013-7345.patch
Patch7: file-5.14-CVE-2014-0207.patch
Patch8: file-5.14-CVE-2014-3478.patch
Patch9: file-5.14-CVE-2014-3479.patch
Patch10: file-5.14-CVE-2014-3480.patch
Patch11: file-5.14-CVE-2014-3487.patch
Patch12: file-5.14-CVE-2014-3538.patch
Patch13: file-5.14-CVE-2014-3587.patch
Patch14: file-5.14-CVE-2014-3710.patch
Patch15: CVE-2014-8117.1.0de3251.patch
Patch16: TEMP-0000000-B67840.2.9b5bdd7.patch
Patch17: TEMP-0000000-B67840.3.c8451af.patch
Patch18: TEMP-0000000-C482B4.59e6383.patch
Patch19: CVE-2014-8116.1.b4c0114.patch
Patch20: CVE-2014-8116.2.d7cdad0.patch
Patch21: CVE-2014-8117.3.6f737dd.patch
Patch22: TEMP-0000000-B67840.4.8a90571.patch
Patch23: CVE-2014-8117.4.90018fe.patch
Patch24: CVE-2014-8117.5.5063ca3.patch
Patch25: TEMP-0000000-B67840.5.6ce24f3.patch
Patch26: TEMP-0000000-B67840.6.0056ec3.patch
Patch27: TEMP-0000000-B67840.7.09e4162.patch
Patch28: TEMP-0000000-B67840.8.af444af.patch
Patch29: CVE-2014-8117.6.6bf4527.patch
Patch30: TEMP-0000000-B67840.9.68bd843.patch
Patch31: TEMP-0000000-B67840.10.dddd3cd.patch
Patch32: TEMP-0000000-B67840.11.445c8fb.patch
Patch33: TEMP-0000000-B67840.12.ce90e05.patch
Patch34: TEMP-0000000-E110B2.65437ce.patch
Patch35: fix_case_file_use.patch
URL: http://www.darwinsys.com/file/

Requires: file-libs = %{version}-%{release}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
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
Group:   Applications/File

%description libs

Libraries for applications using libmagic.

%package devel
Summary:  Libraries and header files for file development
Group:    Applications/File
Requires: %{name} = %{version}-%{release}

%description devel
The file-devel package contains the header files and libmagic library
necessary for developing programs using libmagic.


%prep
# Don't use -b -- it will lead to poblems when compiling magic file
%setup -q
# file-aarch64.patch
%patch0 -p1
# file-5.14-CVE-2014-1943.patch
%patch4 -p1
# file-5.14-CVE-2014-2270.patch
%patch5 -p1
# file-5.14-CVE-2013-7345.patch
%patch6 -p1
# file-5.14-CVE-2014-0207.patch
%patch7 -p1
# file-5.14-CVE-2014-3478.patch
%patch8 -p1
# file-5.14-CVE-2014-3479.patch
%patch9 -p1
# file-5.14-CVE-2014-3480.patch
%patch10 -p1
# file-5.14-CVE-2014-3487.patch
%patch11 -p1
# file-5.14-CVE-2014-3538.patch
%patch12 -p1
# file-5.14-CVE-2014-3587.patch
%patch13 -p1
# file-5.14-CVE-2014-3710.patch
%patch14 -p1
#CVE-2014-8117.1.0de3251.patch
%patch15 -p1
#TEMP-0000000-B67840.2.9b5bdd7.patch
%patch16 -p1
#TEMP-0000000-B67840.3.c8451af.patch
%patch17 -p1
#TEMP-0000000-C482B4.59e6383.patch
%patch18 -p1
#CVE-2014-8116.1.b4c0114.patch
%patch19 -p1
#CVE-2014-8116.2.d7cdad0.patch
%patch20 -p1
#CVE-2014-8117.3.6f737dd.patch
%patch21 -p1
#TEMP-0000000-B67840.4.8a90571.patch
%patch22 -p1
#CVE-2014-8117.4.90018fe.patch
%patch23 -p1
#CVE-2014-8117.5.5063ca3.patch
%patch24 -p1
#TEMP-0000000-B67840.5.6ce24f3.patch
%patch25 -p1
#TEMP-0000000-B67840.6.0056ec3.patch
%patch26 -p1
#TEMP-0000000-B67840.7.09e4162.patch
%patch27 -p1
#TEMP-0000000-B67840.8.af444af.patch
%patch28 -p1
#CVE-2014-8117.6.6bf4527.patch
%patch29 -p1
#TEMP-0000000-B67840.9.68bd843.patch
%patch30 -p1
#TEMP-0000000-B67840.10.dddd3cd.patch
%patch31 -p1
#TEMP-0000000-B67840.11.445c8fb.patch
%patch32 -p1
#TEMP-0000000-B67840.12.ce90e05.patch
%patch33 -p1
#TEMP-0000000-E110B2.65437ce.patch
%patch34 -p1
#fix_case_file_use.patch
%patch35 -p1

%build
CFLAGS="%{optflags} -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE" \
%configure --enable-fsect-man5 --disable-rpath
# remove hardcoded library paths from local libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
export LD_LIBRARY_PATH=%{_builddir}/%{name}-%{version}/src/.libs
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man5
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/misc
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/file

make DESTDIR=${RPM_BUILD_ROOT} install
rm -f ${RPM_BUILD_ROOT}%{_libdir}/*.la

cat magic/Magdir/* > ${RPM_BUILD_ROOT}%{_datadir}/file/magic
ln -s file/magic ${RPM_BUILD_ROOT}%{_datadir}/magic
ln -s ../magic ${RPM_BUILD_ROOT}%{_datadir}/misc/magic


%clean
rm -rf $RPM_BUILD_ROOT

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog README
%{_bindir}/*
%{_mandir}/man1/*

%files libs
%defattr(-,root,root,-)
%{_libdir}/*so.*
%{_datadir}/magic*
%{_mandir}/man5/*
%{_datadir}/file
%{_datadir}/misc/*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_includedir}/magic.h
%{_mandir}/man3/*
