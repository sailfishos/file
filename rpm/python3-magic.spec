Summary: Python bindings for the libmagic API
Name: python3-magic
Version: 5.41
Release: 0
License: BSD
Source0: %{name}-%{version}.tar.gz
URL: https://github.com/sailfishos/file
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
%py3_build
popd

%install
rm -rf $RPM_BUILD_ROOT
pushd python
%py3_install
popd

%files
%defattr(-,root,root,-)
%license COPYING
%{python3_sitelib}/magic.py
%{python3_sitelib}/__pycache__/magic.cpython*.pyc
%{python3_sitelib}/*egg-info
