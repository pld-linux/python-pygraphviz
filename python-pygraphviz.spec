%define 	module	pygraphviz
Summary:	pygraphviz - wrapper to graphviz's graph data structure
Summary(pl.UTF-8):	pygraphviz - wrapper dla struktury danych grafów graphviza
Name:		python-%{module}
Version:	0.21
Release:	0.1
License:	GPL v2+
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/networkx/%{module}-%{version}.tar.gz
# Source0-md5:	ea2a1f28dd64f616ba8d3e3080e042be
Source1:	http://cheeseshop.python.org/packages/2.4/s/setuptools/setuptools-0.6a7-py2.4.egg
# Source1-md5:	c6d62dab4461f71aed943caea89e6f20
Patch0:		%{name}-install.patch
URL:		http://networkx.sourceforge.net/
BuildRequires:	graphviz-devel
BuildRequires:	graphviz-python
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pygraphviz is a wrapper to the graph data structure of the graphviz
graph layout and visualization package.

%description -l pl.UTF-8
pygraphviz to wrapper dla struktury danych grafów pakietu do opisu i
wizualizacji grafów graphviz.

%prep
%setup -q -n %{module}-%{version}
install %{SOURCE1} .
%patch0 -p1

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

#broken!
python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_scriptdir} -type f -name "*.py" | xargs rm
mv $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}-%{version}-py2.4.egg/%{module} $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/%{module}
