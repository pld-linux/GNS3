Summary:	A graphical frontend for dynamips Cisco 7200 Simulator
#Summary(pl.UTF-8):	-
Name:		GNS3
Version:	0.3.2
Release:	0.2
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/gns-3/%{name}-%{version}-src.tar.bz2
# Source0-md5:	795d6082beaab80755f54890630e96a1
Source1:	http://pfe.epitech.net/frs/download.php/599/%{name}-%{version}_documentation.pdf
# Source1-md5:	0c9cd5c97d0f19f4c00f4e3abd316c87
Source2:	%{name}.desktop
Source3:	%{name}.png
Patch0:		%{name}-version.patch
URL:		http://www.gns3.net/
BuildRequires:	python >= 2.4
BuildRequires:	rpmbuild(macros) >= 1.231
Requires:	dynagen
Requires:	dynamips >= 0.2.8
Requires:	python-PyQt4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNS-3 is a graphical network simulator that allows you to design
complex network topologies. You may run simulations or configure
devices ranging from simple workstations to powerful Cisco routers. It
is based on NS-3, a discrete-event network simulator for Internet
systems, and Dynamips, an IOS emulator which allows users to run IOS
binary images from Cisco Systems.

#%%description -l pl.UTF-8

%prep
%setup -q
install %{SOURCE1} .

%build

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
	--root=$RPM_BUILD_ROOT

# compile the scripts
%{py_ocomp} $RPM_BUILD_ROOT%{py_sitescriptdir}

# remove .py files, leave just compiled ones.
%{py_postclean}

install -D %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install -D %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
install -D {docs/man,$RPM_BUILD_ROOT%{_mandir}/man1}/gns3.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG README %{name}-%{version}_documentation.pdf
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitescriptdir}/%{name}
%dir %{py_sitescriptdir}/%{name}/Config 
%dir %{py_sitescriptdir}/%{name}/Dynagen 
%dir %{py_sitescriptdir}/%{name}/External 
%dir %{py_sitescriptdir}/%{name}/Globals 
%dir %{py_sitescriptdir}/%{name}/Langs 
%dir %{py_sitescriptdir}/%{name}/Link 
%dir %{py_sitescriptdir}/%{name}/Node 
%dir %{py_sitescriptdir}/%{name}/Ui/ConfigurationPages 
%dir %{py_sitescriptdir}/%{name}/Ui 
%{py_sitescriptdir}/%{name}/*.py[co]
%{py_sitescriptdir}/%{name}/*/*.py[co]
%{py_sitescriptdir}/%{name}/*/*/*.py[co]
%{_mandir}/man1/gns3.1*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%lang(de) %{py_sitescriptdir}/%{name}/Langs/Lang_de.qm
%lang(en) %{py_sitescriptdir}/%{name}/Langs/Lang_en.qm
%lang(fr) %{py_sitescriptdir}/%{name}/Langs/Lang_fr.qm
