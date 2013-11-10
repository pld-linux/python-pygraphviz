%define 	module	pygraphviz
Summary:	pygraphviz - Python interface to the Graphviz graph layout and visualization package
Summary(pl.UTF-8):	pygraphviz - pythonowy interfejs do pakietu struktur i wizualizacji grafów Graphviz
Name:		python-%{module}
Version:	1.1
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://networkx.lanl.gov/download/pygraphviz/%{module}-%{version}.tar.gz
# Source0-md5:	f0b8b8e9dde1b0ef8bbdc84eb6246ab8
URL:		http://networkx.lanl.gov/pygraphviz/
BuildRequires:	graphviz-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pygraphviz is a Python wrapper to the graph data structure of the
graphviz graph layout and visualization package.

%description -l pl.UTF-8
pygraphviz to pythonowy interfejs do struktury danych grafów pakietu
do opisu i wizualizacji grafów graphviz.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/pygraphviz-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%dir %{py_sitedir}/pygraphviz
%dir %{py_sitedir}/pygraphviz/tests
%attr(755,root,root) %{py_sitedir}/pygraphviz/_graphviz.so
%{py_sitedir}/pygraphviz/*.py[co]
%{py_sitedir}/pygraphviz-*.egg-info
%{py_sitedir}/pygraphviz/tests/*.py[co]
%{py_sitedir}/pygraphviz/tests/*.txt
