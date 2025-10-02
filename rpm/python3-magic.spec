Summary: Python bindings for the libmagic API
Name: python3-magic
Version: 5.48
Release: 0
License: BSD
Source0: %{name}-%{version}.tar.gz

# revert upstream commits (rhbz#2167964)
# 1. https://github.com/file/file/commit/e1233247bbe4d2d66b891224336a23384a93cce1
# 2. https://github.com/file/file/commit/f7a65dbf1739a8f8671621e41c5648d1f7e9f6ae
Patch1: file-5.45-readelf-limit-revert.patch

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
pushd python
%py3_install
popd

rm -f ${RPM_BUILD_ROOT}%{_bindir}/realpython

%files
%license COPYING
%{python3_sitelib}/magic.py
%{python3_sitelib}/__pycache__/magic.cpython*.pyc
%{python3_sitelib}/*egg-info
