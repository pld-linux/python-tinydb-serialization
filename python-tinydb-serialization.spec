# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		tinydb_serialization
%define		pypi_name	tinydb-serialization

Summary:	Serialization for objects that TinyDB otherwise couldn't handle
Name:		python-tinydb-serialization
Version:	1.0.4
Release:	3
License:	MIT
Group:		Development/Languages/Python
Source0:	https://files.pythonhosted.org/packages/source/t/tinydb-serialization/%{pypi_name}-%{version}.zip
# Source0-md5:	702447e3f5f70ec07a160f4cff95e1fd
URL:		https://pypi.python.org/project/tinydb-serialization
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	unzip
%if %{with python2}
BuildRequires:	python >= 1:2.6
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.3
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Serialization for objects that TinyDB otherwise couldn't handle.

%package -n python3-tinydb-serialization
Summary:	Serialization for objects that TinyDB otherwise couldn't handle
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-tinydb-serialization
Serialization for objects that TinyDB otherwise couldn't handle.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-tinydb-serialization
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
