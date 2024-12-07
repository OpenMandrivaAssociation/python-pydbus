Name:		python-pydbus
Version:	0.6.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pydbus/pydbus-%{version}.tar.gz
Summary:	Pythonic DBus library
URL:		https://pypi.org/project/pydbus/
License:	LGPLv2+
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Pythonic DBus library

%prep
%autosetup -p1 -n pydbus-%{version}

%files
%{py_sitedir}/pydbus
%{py_sitedir}/pydbus-*.*-info
