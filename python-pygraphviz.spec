# TODO:
# - summary, desc, some setuptools needed
# NFY
%define 	module	pygraphviz
Summary:	Python package for 
Summary(pl):	Pakiet dla Pythona
Name:		python-%{module}
Version:	0.21
Release:	0.1
License:	GPL v2+
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/networkx/%{module}-%{version}.tar.gz
# Source0-md5:	ea2a1f28dd64f616ba8d3e3080e042be
Source1:	http://cheeseshop.python.org/packages/2.4/s/setuptools/setuptools-0.6a7-py2.4.egg
# Source1-md5:	c6d62dab4461f71aed943caea89e6f20
URL:		http://networkx.sourceforge.net/
BuildRequires:	rpm-pythonprov
BuildRequires:	graphviz-devel
BuildRequires:	graphviz-python
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q -n %{module}-%{version}
install %{SOURCE1} ./

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

#broken!
python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT


find $RPM_BUILD_ROOT%{py_scriptdir} -type f -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%{py_sitescriptdir}/%{module}
%dir %{_datadir}/%{module}
%{_datadir}/%{module}/*.lfs
%{_datadir}/%{module}/pyx.def
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pyxrc
