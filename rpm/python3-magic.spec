%define __libtoolize :

Summary: Python bindings for the libmagic API
Name: python3-magic
Version: 5.37
Release: 0
License: BSD
Source0: %{name}-%{version}.tar.gz
Patch0: 0001-Limit-the-number-of-elements-in-a-vector-found-by-os.patch
Patch1: 0002-Set-buffer-to-NULL-to-prevent-double-free-Kamil-Dudk.patch
Obsoletes: python-magic
URL: https://git.sailfishos.org/mer-core/file
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
Requires:  %{name} = %{version}-%{release}

%description doc
Documentation and an example %{name}.

%prep
# Don't use -b -- it will lead to problems when compiling magic file
%autosetup -p1 -n %{name}-%{version}/upstream

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
