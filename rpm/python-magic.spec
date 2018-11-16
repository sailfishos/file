%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%define __libtoolize :

Summary: Python bindings for the libmagic API
Name: python-magic
Version: 5.14
Release: 5
License: BSD
Group: System/Libraries
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
Patch36: CVE-2014-9653.2.445c8fb.patch

URL: http://www.darwinsys.com/file/

Requires: file >= %{version}
BuildRequires: zlib-devel
BuildRequires: python-devel, file-devel

%description
This package contains the Python bindings to allow access to the
libmagic API. The libmagic library is also used by the familiar
file(1) command.

%prep
# Don't use -b -- it will lead to poblems when compiling magic file
%setup -q -n file-%{version}
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
#CVE-2014-9653.2.445c8fb.patch
%patch36 -p1

%build
CFLAGS="%{optflags} -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE" \
cd python
CFLAGS="%{optflags}" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
cd python
%{__python} setup.py install  --root ${RPM_BUILD_ROOT}
%{__install} -d ${RPM_BUILD_ROOT}%{_datadir}/%{name}
%{__install} -d ${RPM_BUILD_ROOT}/%{_docdir}/%{name}-%{version}
%{__install} -D example.py ${RPM_BUILD_ROOT}/%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc python/README COPYING python/example.py
%{python_sitearch}/magic.py*
%{python_sitearch}/*egg-info

