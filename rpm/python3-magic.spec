%define __libtoolize :

Summary: Python bindings for the libmagic API
Name: python3-magic
Version: 5.14
Release: 5
License: BSD
Group: System/Libraries
Source0: %{name}-%{version}.tar.gz
Obsoletes: python-magic

URL: http://www.darwinsys.com/file/

Requires: file >= %{version}
BuildRequires: zlib-devel
BuildRequires: file-devel
BuildRequires: python3-devel, python3-setuptools

%description
This package contains the Python bindings to allow access to the
libmagic API. The libmagic library is also used by the familiar
file(1) command.

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}

%description doc
Documentation and an example %{name}.

%prep
# Don't use -b -- it will lead to poblems when compiling magic file
%setup -q -n %{name}-%{version}/upstream

%build
autoreconf -f -i
pushd python
CFLAGS="%{optflags}" python3 setup.py build
popd

%install
rm -rf $RPM_BUILD_ROOT
pushd python
python3 setup.py install  --root ${RPM_BUILD_ROOT}
install -d ${RPM_BUILD_ROOT}%{_datadir}/%{name}
install -d ${RPM_BUILD_ROOT}/%{_docdir}/%{name}-%{version}
install -m 0644 -D README.md ${RPM_BUILD_ROOT}/%{_docdir}/%{name}-%{version}
install -D example.py ${RPM_BUILD_ROOT}/%{_docdir}/%{name}-%{version}
popd

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/python3*/site-packages/magic.py
%{_libdir}/python3*/site-packages/__pycache__/magic.cpython*.pyc
%{_libdir}/python3*/site-packages/*egg-info

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}
