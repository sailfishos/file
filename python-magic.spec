%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%define __libtoolize :

Summary: Python bindings for the libmagic API
Name: python-magic
Version: 5.14
Release: 1
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

