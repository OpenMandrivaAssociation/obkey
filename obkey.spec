Summary:	Openbox Key Editor
Name:		obkey
Version:	1.0
Release:	2
License:	MIT
Group:		Editors
URL:		https://code.google.com/p/obkey/
Source0:	http://obkey.googlecode.com/files/%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	python
Requires:	pygtk2.0

%description
ObKey is the Openbox Key Editor, written in Python + PyGTK.

Current version is a development version. It means it wasn't tested a lot. And
there is a code for making backup of rc.xml (just in case).

You can specify other config file:

obkey mycustomrc.xml

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --skip-build --prefix=%{buildroot}%_prefix

mkdir -p %{buildroot}%{_datadir}/applications
install -m 0755 misc/obkey.desktop %{buildroot}%{_datadir}/applications/

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}/icons/*png
%{_datadir}/applications/%{name}.desktop
%{py_puresitedir}/obkey-1.0-py2.7.egg-info
%{py_puresitedir}/obkey_classes.py



%changelog
* Tue May 29 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.0-1
+ Revision: 801167
- imported package obkey

