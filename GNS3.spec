Summary:	A graphical frontend for dynamips Cisco 7200 Simulator
Summary(pl.UTF-8):	Graficzny interfejs do dynamips - symulatora Cisco 7200
Name:		GNS3
Version:	0.6.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/gns-3/%{name}-%{version}-src.tar.bz2
# Source0-md5:	355c38a008e7efc208ceffef535d9fb6
Source1:	http://pfe.epitech.net/frs/download.php/599/%{name}-%{version}_documentation.pdf
# Source1-md5:	449f80038960f121a26cd83af148c51f
Source2:	%{name}.desktop
Source3:	%{name}.png
URL:		http://www.gns3.net/
BuildRequires:	rpmbuild(macros) >= 1.231
BuildRequires:	rpm-pythonprov
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

%description -l pl.UTF-8
GNS-3 to graficzny symulator sieci umożliwiający projektowanie
złożonych topologii sieci. Pozwala uruchamiać symulacje lub
konfigurować urządzenia od prostych stacji roboczych do potężnych
routerów Cisco. Jest oparty na NS-3 - symulatorze sieci ze zdarzeniami
dyskretnymi do systemów internetowych oraz Dynamisie - emulatorze
IOS-a pozwalającym użytkownikom uruchamiać binarne obrazy IOS-a z
Cisco Systems.

%prep
%setup -q -n %{name}-%{version}-src
install %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

# remove .py files, leave just compiled ones.
%{py_postclean}

install -D %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install -D %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
install -D docs/man/gns3.1 $RPM_BUILD_ROOT%{_mandir}/man1/gns3.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG README %{name}-%{version}_documentation.pdf
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitescriptdir}/%{name}
%dir %{py_sitescriptdir}/%{name}/Config 
%dir %{py_sitescriptdir}/%{name}/Defaults 
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
%{py_sitescriptdir}/%{name}-%{version}-*.egg-info
%{py_sitescriptdir}/%{name}/Dynagen/configspec
%{_mandir}/man1/gns3.1*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%lang(ar) %{py_sitescriptdir}/%{name}/Langs/Lang_ar.qm
%lang(zh_CN) %{py_sitescriptdir}/%{name}/Langs/Lang_cn.qm
%lang(de) %{py_sitescriptdir}/%{name}/Langs/Lang_de.qm
%lang(en) %{py_sitescriptdir}/%{name}/Langs/Lang_en.qm
%lang(es) %{py_sitescriptdir}/%{name}/Langs/Lang_es.qm
%lang(fr) %{py_sitescriptdir}/%{name}/Langs/Lang_fr.qm
%lang(ja) %{py_sitescriptdir}/%{name}/Langs/Lang_jp.qm
%lang(ko) %{py_sitescriptdir}/%{name}/Langs/Lang_kr.qm
%lang(pl) %{py_sitescriptdir}/%{name}/Langs/Lang_pl.qm
%lang(pt_BR) %{py_sitescriptdir}/%{name}/Langs/Lang_pt_br.qm
%lang(ru) %{py_sitescriptdir}/%{name}/Langs/Lang_ru.qm
%lang(sk) %{py_sitescriptdir}/%{name}/Langs/Lang_sk.qm
%lang(sr) %{py_sitescriptdir}/%{name}/Langs/Lang_sr.qm
%lang(tr) %{py_sitescriptdir}/%{name}/Langs/Lang_tr.qm
%lang(ar) %{py_sitescriptdir}/%{name}/Langs/qt_ar.qm
%lang(zh_CN) %{py_sitescriptdir}/%{name}/Langs/qt_cn.qm
%lang(de) %{py_sitescriptdir}/%{name}/Langs/qt_de.qm
%lang(es) %{py_sitescriptdir}/%{name}/Langs/qt_es.qm
%lang(fr) %{py_sitescriptdir}/%{name}/Langs/qt_fr.qm
%lang(ja) %{py_sitescriptdir}/%{name}/Langs/qt_jp.qm
%lang(pl) %{py_sitescriptdir}/%{name}/Langs/qt_pl.qm
%lang(pt_BR) %{py_sitescriptdir}/%{name}/Langs/qt_pt_br.qm
%lang(ru) %{py_sitescriptdir}/%{name}/Langs/qt_ru.qm
%lang(sk) %{py_sitescriptdir}/%{name}/Langs/qt_sk.qm
%lang(sr) %{py_sitescriptdir}/%{name}/Langs/qt_sr.qm
