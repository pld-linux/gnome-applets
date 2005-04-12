Summary:	Small applications which embed themselves in the GNOME panel
Summary(pl):	Aplety GNOME - ma³e aplikacje osadzaj±ce siê w panelu
Summary(ru):	íÁÌÅÎØËÉÅ ÐÒÏÇÒÁÍÍÙ, ×ÓÔÒÁÉ×ÁÀÝÉÅÓÑ × ÐÁÎÅÌØ GNOME
Summary(uk):	íÁÌÅÎØË¦ ÐÒÏÇÒÁÍÉ, ÝÏ ×ÂÕÄÏ×ÕÀÔØÓÑ × ÐÁÎÅÌØ GNOME
Name:		gnome-applets
Version:	2.10.1
Release:	2
Epoch:		1
License:	GPL v2, FDL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-applets/2.10/%{name}-%{version}.tar.bz2
# Source0-md5:	da9cd75f77972c96eec9551d41878a7f
Patch0:		%{name}-stickynotes-title-size.patch
Patch1:		%{name}-m4_fix.patch
Patch2:		%{name}-doc_typos.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.10.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gail-devel >= 1.8.2
BuildRequires:	gdbm-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.8.0-2
BuildRequires:	gnome-panel-devel >= 2.10.0-2
BuildRequires:	gnome-vfs2-devel >= 2.10.0-2
BuildRequires:	gstreamer-plugins-devel >= 0.8.8
BuildRequires:	gtk+2-devel >= 2:2.6.4
BuildRequires:	gucharmap-devel >= 1.4.0
BuildRequires:	intltool >= 0.33
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgtop-devel >= 1:2.10.0
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.10.0
BuildRequires:	libxml2-devel >= 1:2.6.19
BuildRequires:	libxklavier-devel >= 2.0
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.3.11-4
BuildRequires:	system-tools-backends >= 1.2.0
Requires:	gnome-icon-theme >= 2.10.0
Requires:	gnome-panel >= 2.10.0-2
Requires:	gnome-vfs2 >= 2.10.0-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gnomehelpdir	%{_datadir}/gnome/help

%description
The gnome-applets package provides Panel applets which enhance your
GNOME experience.

%description -l pl
Pakiet gnome-applets udostêpnia aplety Panelu, które usprawniaj± pracê
z GNOME.

%description -l uk
ðÁËÅÔ gnome-applets Í¦ÓÔÉÔØ ÁÐÌÅÔÉ ðÁÎÅÌ¦ GNOME, ÝÏ ÚÂ¦ÌØÛÕÀÔØ
ËÏÍÆÏÒÔÎ¦ÓÔØ ÒÏÂÏÔÉ × ÓÅÒÅÄÏ×ÉÝ¦ GNOME.

%description -l ru
ðÁËÅÔ gnome-applets ÓÏÄÅÒÖÉÔ ÁÐÐÌÅÔÙ ðÁÎÅÌÉ GNOME, Õ×ÅÌÉÞÉ×ÁÀÝÉÅ
ËÏÍÆÏÒÔÎÏÓÔØ ÒÁÂÏÔÙ × ÓÒÅÄÅ GNOME.

%package devel
Summary:	Header files for gnome-applets
Summary(pl):	Pliki nag³ówkowe gnome-applets
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	GConf2-devel >= 2.10.0
Requires:	gtk+2-devel >= 2:2.6.4

%description devel
Header files for gnome-applets.

%description devel -l pl
Pliki nag³ówkowe gnome-applets.

%package accessx-status
Summary:	Keyboard Accessibility Status applet
Summary(pl):	Aplet stanu dostepno¶ci klawiatury
Group:		X11/Applications
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets <= 0:2.10.0-5

%description accessx-status
Keyboard Accessibility Status applet.

%description accessx-status -l pl
Aplet stanu dostepno¶ci klawiatury.

%package battstat
Summary:	Battery Charge Monitor applet
Summary(pl):	Aplet monitora stanu na³adowania akumulatora
Group:		X11/Applications
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets <= 0:2.10.0-5

%description battstat
Battery Charge Monitor applet.

%description battstat -l pl
Aplet monitora stanu na³adowania akumulatora.

%package charpicker
Summary:	Character Palette applet
Summary(pl):	Aplet palety znaków
Group:		X11/Applications
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets <= 0:2.10.0-5

%description charpicker
Character Palette applet.

%description charpicker -l pl
Aplet palety znaków.

%package cpufreq
Summary:	CPU Frequency Scaling Monitor applet
Summary(pl):	Aplet monitora czêstotliwo¶ci procesora
Group:		X11/Applications
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets <= 0:2.10.0-5
Obsoletes:	gnome-applet-cpufreq

%description cpufreq
CPU Frequency Scaling Monitor applet.

%description cpufreq -l pl
Aplet monitora czêstotliwo¶ci procesora.

%package drivemount
Summary:	Disk Mounter applet
Summary(pl):	Aplet do montowania dysków
Group:		X11/Applications
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets <= 0:2.10.0-5

%description drivemount
Disk Mounter applet.

%description drivemount -l pl
Aplet do monotwania dysków.

%package geyes
Summary:	Geyes applet
Summary(pl):	Aplet geyes
Group:		X11/Applications
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets <= 0:2.10.0-5

%description geyes
Geyes applet.

%description geyes -l pl
Aplet geyes.

%package gtik
Summary:	Stock Ticker applet
Summary(pl):	Aplet wska¼nika gie³dowego
Group:		X11/Applications
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets <= 0:2.10.0-5

%description gtik
Stock Ticker applet.

%description gtik -l pl
Aplet wska¼nika gie³dowego.

%package gweather
Summary:	Weather Report applet
Summary(pl):	Aplet raportu pogodowego
Group:		X11/Applications
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets <= 0:2.10.0-5

%description gweather
Weather Report applet.

%description gweather -l pl
Aplet raportu pogodowego.

%package keyboard
Summary:	Keyboard Indicator applet
Summary(pl):	Aplet wska¼nika klawiatury
Group:		X11/Applications
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets <= 0:2.10.0-5

%description keyboard
Keyboard Indicator applet.

%description keyboard -l pl
Aplet wska¼nika klawiatury.

%package minicommander
Summary:	Command Line applet
Summary(pl):	Aplet wiersza poleceñ
Group:		X11/Applications
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets <= 0:2.10.0-5

%description minicommander
Command Line applet.

%description minicommander -l pl
Aplet wiersza poleceñ.

%package mixer
Summary:	Volume Control applet
Summary(pl):	Aplet regulacji g³o¶no¶ci
Group:		X11/Applications
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gstreamer-audiosink
Conflicts:	gnome-applets <= 0:2.10.0-5

%description mixer
Volume Control applet.

%description mixer -l pl
Aplet regulacji g³o¶no¶ci.

%package modemlights
Summary:	Modem Lights applet
Summary(pl):	Aplet kontrolek modemu
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	system-tools-backends >= 1.2.0
Conflicts:	gnome-applets <= 0:2.10.0-5

%description modemlights
Modem Lights applet.

%description modemlights -l pl
Aplet kontrolek modemu.

%package multiload
Summary:	System Monitor applet
Summary(pl):	Aplet monitora systemu
Group:		X11/Applications
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets <= 0:2.10.0-5

%description multiload
System Monitor applet.

%description multiload -l pl
Aplet monitora systemu.

%package stickynotes
Summary:	Sticky Notes applet
Summary(pl):	Aplet notatek
Group:		X11/Applications
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets <= 0:2.10.0-5
Obsoletes:	gnotes_applet

%description stickynotes
Sticky Notes applet.

%description stickynotes -l pl
Aplet notatek.

%package trash
Summary:	Trash applet
Summary(pl):	Aplet ¶mietnika
Group:		X11/Applications
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets <= 0:2.10.0-5

%description trash
Trash applet.

%description trash -l pl
Aplet ¶mietnika.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal} -I m4
%{__libtoolize}
%{__glib_gettextize}
%{__intltoolize}
%{__autoheader}
%{__gnome_doc_common}
%{__automake}
%{__autoconf}
%configure \
	--disable-static \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --all-name

find $RPM_BUILD_ROOT/%{_pixmapsdir}/gkb/|grep '/..\.png$'|sed "s=$RPM_BUILD_ROOT\(/%{_pixmapsdir}/gkb/\)\(..\)\(.png\)=%lang(\2) \1\2\3=" >> %{name}.lang
find . 	-name ChangeLog -o \
	-name TODO -o \
	-name NEWS -o \
	-name AUTHORS \
	-o -name README | \
awk '{src=$0; dst=$0;sub("^./","",dst);gsub("/","-",dst);
	print "cp " src " " dst}  END {print "exit 0"}' | sh

%clean
rm -rf $RPM_BUILD_ROOT

%post accessx-status
%scrollkeeper_update_post
%banner %{name} -e << EOF
For full functionality, you need to install control-center.
EOF

%postun accessx-status
%scrollkeeper_update_postun

%post battstat
%scrollkeeper_update_post
%gconf_schema_install battstat.schemas

%preun battstat
%gconf_schema_uninstall battstat.schemas

%postun battstat
%scrollkeeper_update_postun

%post charpicker
%scrollkeeper_update_post
%gconf_schema_install charpick.schemas

%preun charpicker
%gconf_schema_uninstall charpick.schemas

%postun charpicker
%scrollkeeper_update_postun

%post cpufreq
%scrollkeeper_update_post
%gconf_schema_install cpufreq-applet.schemas
%banner %{name} -e << EOF
For full functionality, set SUID /usr/bin/cpufreq-selector binary.
EOF

%preun cpufreq
%gconf_schema_uninstall cpufreq-applet.schemas

%postun cpufreq
%scrollkeeper_update_postun

%post drivemount
%scrollkeeper_update_post
%gconf_schema_install drivemount.schemas

%preun drivemount
%gconf_schema_uninstall drivemount.schemas

%postun drivemount 
%scrollkeeper_update_postun

%post geyes
%scrollkeeper_update_post
%gconf_schema_install geyes.schemas

%preun geyes
%gconf_schema_uninstall geyes.schemas

%postun geyes 
%scrollkeeper_update_postun

%post gtik
%scrollkeeper_update_post
%gconf_schema_install gtik.schemas

%preun gtik
%gconf_schema_uninstall gtik.schemas

%postun gtik
%scrollkeeper_update_postun

%post gweather
%scrollkeeper_update_post
%gconf_schema_install gweather.schemas

%preun gweather
%gconf_schema_uninstall gweather.schemas

%postun gweather
%scrollkeeper_update_postun

%post keyboard
%scrollkeeper_update_post
%gconf_schema_install gswitchit.schemas

%preun keyboard
%gconf_schema_uninstall gswitchit.schemas

%postun keyboard
%scrollkeeper_update_postun

%post minicommander
%scrollkeeper_update_post
%gconf_schema_install mini-commander-global.schemas
%gconf_schema_install mini-commander.schemas
GCONF_CONFIG_SOURCE="`%{_bindir}/gconftool-2 --get-default-source`" %{_libdir}/%{name}/mc-install-default-macros

%preun minicommander
%gconf_schema_uninstall mini-commander-global.schemas
%gconf_schema_uninstall mini-commander.schemas

%postun minicommander
%scrollkeeper_update_postun

%post mixer
%scrollkeeper_update_post
%gconf_schema_install mixer.schemas
%banner %{name} -e << EOF
For full functionality, you need to install gnome-media-volume-control.
EOF

%preun mixer
%gconf_schema_uninstall mixer.schemas

%postun mixer
%scrollkeeper_update_postun

%post modemlights
%scrollkeeper_update_post

%postun modemlights
%scrollkeeper_update_postun

%post multiload
%scrollkeeper_update_post
%gconf_schema_install multiload.schemas
%banner %{name} -e << EOF
For full functionality, you need to install gnome-system-monitor.
EOF

%preun multiload
%gconf_schema_uninstall multiload.schemas

%postun multiload
%scrollkeeper_update_postun

%post stickynotes
%scrollkeeper_update_post
%gconf_schema_install stickynotes.schemas

%preun stickynotes
%gconf_schema_uninstall stickynotes.schemas

%postun stickynotes
%scrollkeeper_update_postun

%post trash
%scrollkeeper_update_post

%postun trash
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *AUTHORS *ChangeLog *NEWS *README *TODO
%attr(755,root,root) %{_libdir}/null_applet
%{_libdir}/bonobo/servers/GNOME_CDPlayerApplet.server
%{_libdir}/bonobo/servers/GNOME_MailcheckApplet_Factory.server
%{_libdir}/bonobo/servers/GNOME_NullApplet_Factory.server
%{_libdir}/bonobo/servers/GNOME_Panel_WirelessApplet.server
%dir %{_datadir}/%{name}/glade
%dir %{_libdir}/%{name}
%dir %{_omf_dest_dir}/%{name}

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_pkgconfigdir}/*.pc

%files accessx-status
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/accessx-status-applet
%{_libdir}/bonobo/servers/GNOME_AccessxStatusApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_AccessxApplet.xml
%{_pixmapsdir}/accessx-status-applet
%{_iconsdir}/hicolor/48x48/apps/ax-applet.png
%{_omf_dest_dir}/%{name}/accessx-status-C.omf
%lang(eu) %{_omf_dest_dir}/%{name}/accessx-status-eu.omf
%lang(uk) %{_omf_dest_dir}/%{name}/accessx-status-uk.omf
%dir %{_gnomehelpdir}/accessx-status
%{_gnomehelpdir}/accessx-status/C
%lang(eu) %{_gnomehelpdir}/accessx-status/eu
%lang(uk) %{_gnomehelpdir}/accessx-status/uk

%files battstat
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/battstat-applet-2
%{_libdir}/bonobo/servers/GNOME_BattstatApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_BattstatApplet.xml
%{_datadir}/%{name}/glade/battstat_applet.glade
%{_sysconfdir}/gconf/schemas/battstat.schemas
%{_sysconfdir}/sound/events/battstat_applet.soundlist
%{_omf_dest_dir}/%{name}/battstat-C.omf
%lang(de) %{_omf_dest_dir}/%{name}/battstat-de.omf
%lang(es) %{_omf_dest_dir}/%{name}/battstat-es.omf
%lang(eu) %{_omf_dest_dir}/%{name}/battstat-eu.omf
%lang(fr) %{_omf_dest_dir}/%{name}/battstat-fr.omf
%lang(it) %{_omf_dest_dir}/%{name}/battstat-it.omf
%lang(ja) %{_omf_dest_dir}/%{name}/battstat-ja.omf
%lang(ko) %{_omf_dest_dir}/%{name}/battstat-ko.omf
%lang(sv) %{_omf_dest_dir}/%{name}/battstat-sv.omf
%lang(uk) %{_omf_dest_dir}/%{name}/battstat-uk.omf
%lang(zh_CN) %{_omf_dest_dir}/%{name}/battstat-zh_CN.omf
%lang(zh_HK) %{_omf_dest_dir}/%{name}/battstat-zh_HK.omf
%lang(zh_TW) %{_omf_dest_dir}/%{name}/battstat-zh_TW.omf
%dir %{_gnomehelpdir}/battstat
%{_gnomehelpdir}/battstat/C
%lang(de) %{_gnomehelpdir}/battstat/de
%lang(es) %{_gnomehelpdir}/battstat/es
%lang(eu) %{_gnomehelpdir}/battstat/eu
%lang(fr) %{_gnomehelpdir}/battstat/fr
%lang(it) %{_gnomehelpdir}/battstat/it
%lang(ja) %{_gnomehelpdir}/battstat/ja
%lang(ko) %{_gnomehelpdir}/battstat/ko
%lang(sv) %{_gnomehelpdir}/battstat/sv
%lang(uk) %{_gnomehelpdir}/battstat/uk
%lang(zh_CN) %{_gnomehelpdir}/battstat/zh_CN
%lang(zh_HK) %{_gnomehelpdir}/battstat/zh_HK
%lang(zh_TW) %{_gnomehelpdir}/battstat/zh_TW

%files charpicker
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/charpick_applet2
%{_libdir}/bonobo/servers/GNOME_CharpickerApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_CharpickerApplet.xml
%{_iconsdir}/hicolor/48x48/apps/charpick.png
%{_sysconfdir}/gconf/schemas/charpick.schemas
%{_omf_dest_dir}/%{name}/char-palette-C.omf
%lang(de) %{_omf_dest_dir}/%{name}/char-palette-de.omf
%lang(es) %{_omf_dest_dir}/%{name}/char-palette-es.omf
%lang(eu) %{_omf_dest_dir}/%{name}/char-palette-eu.omf
%lang(fr) %{_omf_dest_dir}/%{name}/char-palette-fr.omf
%lang(it) %{_omf_dest_dir}/%{name}/char-palette-it.omf
%lang(ja) %{_omf_dest_dir}/%{name}/char-palette-ja.omf
%lang(ko) %{_omf_dest_dir}/%{name}/char-palette-ko.omf
%lang(sv) %{_omf_dest_dir}/%{name}/char-palette-sv.omf
%lang(uk) %{_omf_dest_dir}/%{name}/char-palette-uk.omf
%lang(zh_CN) %{_omf_dest_dir}/%{name}/char-palette-zh_CN.omf
%lang(zh_HK) %{_omf_dest_dir}/%{name}/char-palette-zh_HK.omf
%lang(zh_TW) %{_omf_dest_dir}/%{name}/char-palette-zh_TW.omf
%dir %{_gnomehelpdir}/char-palette
%{_gnomehelpdir}/char-palette/C
%lang(de) %{_gnomehelpdir}/char-palette/de
%lang(es) %{_gnomehelpdir}/char-palette/es
%lang(eu) %{_gnomehelpdir}/char-palette/eu
%lang(fr) %{_gnomehelpdir}/char-palette/fr
%lang(it) %{_gnomehelpdir}/char-palette/it
%lang(ja) %{_gnomehelpdir}/char-palette/ja
%lang(ko) %{_gnomehelpdir}/char-palette/ko
%lang(sv) %{_gnomehelpdir}/char-palette/sv
%lang(uk) %{_gnomehelpdir}/char-palette/uk
%lang(zh_CN) %{_gnomehelpdir}/char-palette/zh_CN
%lang(zh_HK) %{_gnomehelpdir}/char-palette/zh_HK
%lang(zh_TW) %{_gnomehelpdir}/char-palette/zh_TW

%files cpufreq
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cpufreq-selector
%attr(755,root,root) %{_libdir}/cpufreq-applet
%{_libdir}/bonobo/servers/GNOME_CPUFreqApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_CPUFreqApplet.xml
%{_datadir}/%{name}/glade/cpufreq-preferences.glade
%{_sysconfdir}/gconf/schemas/cpufreq-applet.schemas
%{_pixmapsdir}/cpufreq-applet
%{_iconsdir}/hicolor/48x48/apps/gnome-cpu.png
%{_omf_dest_dir}/%{name}/cpufreq-applet-C.omf
%lang(uk) %{_omf_dest_dir}/%{name}/cpufreq-applet-uk.omf
%dir %{_gnomehelpdir}/cpufreq-applet
%{_gnomehelpdir}/cpufreq-applet/C
%lang(uk) %{_gnomehelpdir}/cpufreq-applet/uk

%files drivemount
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/drivemount_applet2
%{_libdir}/bonobo/servers/GNOME_DriveMountApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_DriveMountApplet.xml
%{_sysconfdir}/gconf/schemas/drivemount.schemas
%{_omf_dest_dir}/%{name}/drivemount-C.omf
%lang(de) %{_omf_dest_dir}/%{name}/drivemount-de.omf
%lang(es) %{_omf_dest_dir}/%{name}/drivemount-es.omf
%lang(eu) %{_omf_dest_dir}/%{name}/drivemount-eu.omf
%lang(fr) %{_omf_dest_dir}/%{name}/drivemount-fr.omf
%lang(it) %{_omf_dest_dir}/%{name}/drivemount-it.omf
%lang(ja) %{_omf_dest_dir}/%{name}/drivemount-ja.omf
%lang(ko) %{_omf_dest_dir}/%{name}/drivemount-ko.omf
%lang(sv) %{_omf_dest_dir}/%{name}/drivemount-sv.omf
%lang(uk) %{_omf_dest_dir}/%{name}/drivemount-uk.omf
%lang(zh_CN) %{_omf_dest_dir}/%{name}/drivemount-zh_CN.omf
%lang(zh_HK) %{_omf_dest_dir}/%{name}/drivemount-zh_HK.omf
%lang(zh_TW) %{_omf_dest_dir}/%{name}/drivemount-zh_TW.omf
%dir %{_gnomehelpdir}/drivemount
%{_gnomehelpdir}/drivemount/C
%lang(de) %{_gnomehelpdir}/drivemount/de
%lang(es) %{_gnomehelpdir}/drivemount/es
%lang(eu) %{_gnomehelpdir}/drivemount/eu
%lang(fr) %{_gnomehelpdir}/drivemount/fr
%lang(it) %{_gnomehelpdir}/drivemount/it
%lang(ja) %{_gnomehelpdir}/drivemount/ja
%lang(ko) %{_gnomehelpdir}/drivemount/ko
%lang(sv) %{_gnomehelpdir}/drivemount/sv
%lang(uk) %{_gnomehelpdir}/drivemount/uk
%lang(zh_CN) %{_gnomehelpdir}/drivemount/zh_CN
%lang(zh_HK) %{_gnomehelpdir}/drivemount/zh_HK
%lang(zh_TW) %{_gnomehelpdir}/drivemount/zh_TW

%files geyes
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/geyes_applet2
%{_libdir}/bonobo/servers/GNOME_GeyesApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_GeyesApplet.xml
%{_datadir}/%{name}/geyes
%{_iconsdir}/hicolor/48x48/apps/gnome-eyes.png
%{_sysconfdir}/gconf/schemas/geyes.schemas
%{_omf_dest_dir}/%{name}/geyes-C.omf
%lang(de) %{_omf_dest_dir}/%{name}/geyes-de.omf
%lang(es) %{_omf_dest_dir}/%{name}/geyes-es.omf
%lang(eu) %{_omf_dest_dir}/%{name}/geyes-eu.omf
%lang(fr) %{_omf_dest_dir}/%{name}/geyes-fr.omf
%lang(it) %{_omf_dest_dir}/%{name}/geyes-it.omf
%lang(ja) %{_omf_dest_dir}/%{name}/geyes-ja.omf
%lang(ko) %{_omf_dest_dir}/%{name}/geyes-ko.omf
%lang(sv) %{_omf_dest_dir}/%{name}/geyes-sv.omf
%lang(uk) %{_omf_dest_dir}/%{name}/geyes-uk.omf
%lang(zh_CN) %{_omf_dest_dir}/%{name}/geyes-zh_CN.omf
%lang(zh_HK) %{_omf_dest_dir}/%{name}/geyes-zh_HK.omf
%lang(zh_TW) %{_omf_dest_dir}/%{name}/geyes-zh_TW.omf
%dir %{_gnomehelpdir}/geyes
%{_gnomehelpdir}/geyes/C
%lang(de) %{_gnomehelpdir}/geyes/de
%lang(es) %{_gnomehelpdir}/geyes/es
%lang(eu) %{_gnomehelpdir}/geyes/eu
%lang(fr) %{_gnomehelpdir}/geyes/fr
%lang(it) %{_gnomehelpdir}/geyes/it
%lang(ja) %{_gnomehelpdir}/geyes/ja
%lang(ko) %{_gnomehelpdir}/geyes/ko
%lang(sv) %{_gnomehelpdir}/geyes/sv
%lang(uk) %{_gnomehelpdir}/geyes/uk
%lang(zh_CN) %{_gnomehelpdir}/geyes/zh_CN
%lang(zh_HK) %{_gnomehelpdir}/geyes/zh_HK
%lang(zh_TW) %{_gnomehelpdir}/geyes/zh_TW

%files gtik
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtik2_applet2
%{_libdir}/bonobo/servers/GNOME_GtikApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_GtikApplet.xml
%{_iconsdir}/hicolor/48x48/apps/gnome-money.png
%{_sysconfdir}/gconf/schemas/gtik.schemas
%{_omf_dest_dir}/%{name}/gtik2_applet2-C.omf
%lang(de) %{_omf_dest_dir}/%{name}/gtik2_applet2-de.omf
%lang(es) %{_omf_dest_dir}/%{name}/gtik2_applet2-es.omf
%lang(eu) %{_omf_dest_dir}/%{name}/gtik2_applet2-eu.omf
%lang(fr) %{_omf_dest_dir}/%{name}/gtik2_applet2-fr.omf
%lang(it) %{_omf_dest_dir}/%{name}/gtik2_applet2-it.omf
%lang(ja) %{_omf_dest_dir}/%{name}/gtik2_applet2-ja.omf
%lang(ko) %{_omf_dest_dir}/%{name}/gtik2_applet2-ko.omf
%lang(sv) %{_omf_dest_dir}/%{name}/gtik2_applet2-sv.omf
%lang(uk) %{_omf_dest_dir}/%{name}/gtik2_applet2-uk.omf
%lang(zh_CN) %{_omf_dest_dir}/%{name}/gtik2_applet2-zh_CN.omf
%lang(zh_HK) %{_omf_dest_dir}/%{name}/gtik2_applet2-zh_HK.omf
%lang(zh_TW) %{_omf_dest_dir}/%{name}/gtik2_applet2-zh_TW.omf
%dir %{_gnomehelpdir}/gtik2_applet2
%{_gnomehelpdir}/gtik2_applet2/C
%lang(de) %{_gnomehelpdir}/gtik2_applet2/de
%lang(es) %{_gnomehelpdir}/gtik2_applet2/es
%lang(eu) %{_gnomehelpdir}/gtik2_applet2/eu
%lang(fr) %{_gnomehelpdir}/gtik2_applet2/fr
%lang(it) %{_gnomehelpdir}/gtik2_applet2/it
%lang(ja) %{_gnomehelpdir}/gtik2_applet2/ja
%lang(ko) %{_gnomehelpdir}/gtik2_applet2/ko
%lang(sv) %{_gnomehelpdir}/gtik2_applet2/sv
%lang(uk) %{_gnomehelpdir}/gtik2_applet2/uk
%lang(zh_CN) %{_gnomehelpdir}/gtik2_applet2/zh_CN
%lang(zh_HK) %{_gnomehelpdir}/gtik2_applet2/zh_HK
%lang(zh_TW) %{_gnomehelpdir}/gtik2_applet2/zh_TW

%files gweather
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gweather-applet-2
%{_libdir}/bonobo/servers/GNOME_GWeatherApplet_Factory.server
%{_datadir}/gnome-2.0/ui/GNOME_GWeatherApplet.xml
%{_datadir}/%{name}/gweather
%{_sysconfdir}/gconf/schemas/gweather.schemas
%{_omf_dest_dir}/%{name}/gweather-C.omf
%lang(de) %{_omf_dest_dir}/%{name}/gweather-de.omf
%lang(es) %{_omf_dest_dir}/%{name}/gweather-es.omf
%lang(eu) %{_omf_dest_dir}/%{name}/gweather-eu.omf
%lang(fr) %{_omf_dest_dir}/%{name}/gweather-fr.omf
%lang(it) %{_omf_dest_dir}/%{name}/gweather-it.omf
%lang(ja) %{_omf_dest_dir}/%{name}/gweather-ja.omf
%lang(ko) %{_omf_dest_dir}/%{name}/gweather-ko.omf
%lang(sv) %{_omf_dest_dir}/%{name}/gweather-sv.omf
%lang(uk) %{_omf_dest_dir}/%{name}/gweather-uk.omf
%lang(zh_CN) %{_omf_dest_dir}/%{name}/gweather-zh_CN.omf
%lang(zh_HK) %{_omf_dest_dir}/%{name}/gweather-zh_HK.omf
%lang(zh_TW) %{_omf_dest_dir}/%{name}/gweather-zh_TW.omf
%dir %{_gnomehelpdir}/gweather
%{_gnomehelpdir}/gweather/C
%lang(de) %{_gnomehelpdir}/gweather/de
%lang(es) %{_gnomehelpdir}/gweather/es
%lang(eu) %{_gnomehelpdir}/gweather/eu
%lang(fr) %{_gnomehelpdir}/gweather/fr
%lang(it) %{_gnomehelpdir}/gweather/it
%lang(ja) %{_gnomehelpdir}/gweather/ja
%lang(ko) %{_gnomehelpdir}/gweather/ko
%lang(sv) %{_gnomehelpdir}/gweather/sv
%lang(uk) %{_gnomehelpdir}/gweather/uk
%lang(zh_CN) %{_gnomehelpdir}/gweather/zh_CN
%lang(zh_HK) %{_gnomehelpdir}/gweather/zh_HK
%lang(zh_TW) %{_gnomehelpdir}/gweather/zh_TW

%files keyboard
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gnome-keyboard-applet
%{_libdir}/bonobo/servers/GNOME_KeyboardApplet.server
%dir %{_datadir}/xmodmap
%{_datadir}/xmodmap/base.xml
%lang(hy) %{_datadir}/xmodmap/xmodmap.am*
%lang(ar) %{_datadir}/xmodmap/xmodmap.ar*
%lang(fr,nl,wa) %{_datadir}/xmodmap/xmodmap.be*
%lang(bg) %{_datadir}/xmodmap/xmodmap.bg*
%lang(pt_BR) %{_datadir}/xmodmap/xmodmap.br*
%lang(de,fr) %{_datadir}/xmodmap/xmodmap.ch*
%lang(cs) %{_datadir}/xmodmap/xmodmap.cz*
%lang(de) %{_datadir}/xmodmap/xmodmap.de*
%lang(da) %{_datadir}/xmodmap/xmodmap.dk*
%{_datadir}/xmodmap/xmodmap.dvorak
%lang(et) %{_datadir}/xmodmap/xmodmap.ee*
%lang(es) %{_datadir}/xmodmap/xmodmap.es*
%lang(fi) %{_datadir}/xmodmap/xmodmap.fi*
%lang(fr) %{_datadir}/xmodmap/xmodmap.fr*
%{_datadir}/xmodmap/xmodmap.gb*
%lang(ka) %{_datadir}/xmodmap/xmodmap.ge*
%lang(el) %{_datadir}/xmodmap/xmodmap.gr*
%lang(hu) %{_datadir}/xmodmap/xmodmap.hu*
%lang(he,yi) %{_datadir}/xmodmap/xmodmap.il*
%lang(is) %{_datadir}/xmodmap/xmodmap.is*
%lang(it) %{_datadir}/xmodmap/xmodmap.it*
%lang(ja) %{_datadir}/xmodmap/xmodmap.jp*
%lang(ko) %{_datadir}/xmodmap/xmodmap.kr*
%lang(lo) %{_datadir}/xmodmap/xmodmap.la*
%lang(lt) %{_datadir}/xmodmap/xmodmap.lt*
%lang(mk) %{_datadir}/xmodmap/xmodmap.mk*
%lang(mn) %{_datadir}/xmodmap/xmodmap.mn*
%lang(nl) %{_datadir}/xmodmap/xmodmap.nl*
%lang(nn,no) %{_datadir}/xmodmap/xmodmap.no*
%lang(pl) %{_datadir}/xmodmap/xmodmap.pl*
%lang(pt) %{_datadir}/xmodmap/xmodmap.pt*
%lang(fr) %{_datadir}/xmodmap/xmodmap.qc*
%lang(ro) %{_datadir}/xmodmap/xmodmap.ro*
%lang(ru) %{_datadir}/xmodmap/xmodmap.ru*
%lang(sv) %{_datadir}/xmodmap/xmodmap.se*
%lang(fr) %{_datadir}/xmodmap/xmodmap.sf*
%lang(de) %{_datadir}/xmodmap/xmodmap.sg*
%lang(sl) %{_datadir}/xmodmap/xmodmap.si*
%lang(sk) %{_datadir}/xmodmap/xmodmap.sk*
%lang(th) %{_datadir}/xmodmap/xmodmap.th*
%lang(tr) %{_datadir}/xmodmap/xmodmap.tr*
%lang(uk) %{_datadir}/xmodmap/xmodmap.uk*
%{_datadir}/xmodmap/xmodmap.us*
%lang(hr,mk,sl,sr) %{_datadir}/xmodmap/xmodmap.yu*
%attr(755,root,root) %{_bindir}/gswitchit-plugins-capplet
%{_datadir}/gnome-2.0/ui/GNOME_GSwitchItApplet.xml
%{_datadir}/%{name}/glade/gswitchit*.glade
%{_iconsdir}/hicolor/48x48/apps/gswitchit*.png
%{_sysconfdir}/gconf/schemas/gswitchit.schemas
%{_omf_dest_dir}/%{name}/gswitchit-C.omf
%lang(uk) %{_omf_dest_dir}/%{name}/gswitchit-uk.omf
%dir %{_gnomehelpdir}/gswitchit
%{_gnomehelpdir}/gswitchit/C
%lang(uk) %{_gnomehelpdir}/gswitchit/uk

%files minicommander
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mini_commander_applet
%attr(755,root,root) %{_libdir}/%{name}/mc-install-default-macros
%{_libdir}/bonobo/servers/GNOME_MiniCommanderApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_MiniCommanderApplet.xml
%{_datadir}/%{name}/glade/mini-commander.glade
%{_iconsdir}/hicolor/48x48/apps/gnome-mini-commander.png
%{_sysconfdir}/gconf/schemas/mini-commander-global.schemas
%{_sysconfdir}/gconf/schemas/mini-commander.schemas
%{_omf_dest_dir}/%{name}/command-line-C.omf
%lang(de) %{_omf_dest_dir}/%{name}/command-line-de.omf
%lang(es) %{_omf_dest_dir}/%{name}/command-line-es.omf
%lang(eu) %{_omf_dest_dir}/%{name}/command-line-eu.omf
%lang(fr) %{_omf_dest_dir}/%{name}/command-line-fr.omf
%lang(it) %{_omf_dest_dir}/%{name}/command-line-it.omf
%lang(ja) %{_omf_dest_dir}/%{name}/command-line-ja.omf
%lang(ko) %{_omf_dest_dir}/%{name}/command-line-ko.omf
%lang(sv) %{_omf_dest_dir}/%{name}/command-line-sv.omf
%lang(uk) %{_omf_dest_dir}/%{name}/command-line-uk.omf
%lang(zh_CN) %{_omf_dest_dir}/%{name}/command-line-zh_CN.omf
%lang(zh_HK) %{_omf_dest_dir}/%{name}/command-line-zh_HK.omf
%lang(zh_TW) %{_omf_dest_dir}/%{name}/command-line-zh_TW.omf
%dir %{_gnomehelpdir}/command-line
%{_gnomehelpdir}/command-line/C
%lang(de) %{_gnomehelpdir}/command-line/de
%lang(es) %{_gnomehelpdir}/command-line/es
%lang(eu) %{_gnomehelpdir}/command-line/eu
%lang(fr) %{_gnomehelpdir}/command-line/fr
%lang(it) %{_gnomehelpdir}/command-line/it
%lang(ja) %{_gnomehelpdir}/command-line/ja
%lang(ko) %{_gnomehelpdir}/command-line/ko
%lang(sv) %{_gnomehelpdir}/command-line/sv
%lang(uk) %{_gnomehelpdir}/command-line/uk
%lang(zh_CN) %{_gnomehelpdir}/command-line/zh_CN
%lang(zh_HK) %{_gnomehelpdir}/command-line/zh_HK
%lang(zh_TW) %{_gnomehelpdir}/command-line/zh_TW

%files mixer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mixer_applet2
%{_libdir}/bonobo/servers/GNOME_MixerApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_MixerApplet.xml
%{_sysconfdir}/gconf/schemas/mixer.schemas
%{_omf_dest_dir}/%{name}/mixer_applet2-C.omf
%lang(de) %{_omf_dest_dir}/%{name}/mixer_applet2-de.omf
%lang(es) %{_omf_dest_dir}/%{name}/mixer_applet2-es.omf
%lang(eu) %{_omf_dest_dir}/%{name}/mixer_applet2-eu.omf
%lang(fr) %{_omf_dest_dir}/%{name}/mixer_applet2-fr.omf
%lang(it) %{_omf_dest_dir}/%{name}/mixer_applet2-it.omf
%lang(ja) %{_omf_dest_dir}/%{name}/mixer_applet2-ja.omf
%lang(ko) %{_omf_dest_dir}/%{name}/mixer_applet2-ko.omf
%lang(sv) %{_omf_dest_dir}/%{name}/mixer_applet2-sv.omf
%lang(uk) %{_omf_dest_dir}/%{name}/mixer_applet2-uk.omf
%lang(zh_CN) %{_omf_dest_dir}/%{name}/mixer_applet2-zh_CN.omf
%lang(zh_HK) %{_omf_dest_dir}/%{name}/mixer_applet2-zh_HK.omf
%lang(zh_TW) %{_omf_dest_dir}/%{name}/mixer_applet2-zh_TW.omf
%dir %{_gnomehelpdir}/mixer_applet2
%{_gnomehelpdir}/mixer_applet2/C
%lang(de) %{_gnomehelpdir}/mixer_applet2/de
%lang(es) %{_gnomehelpdir}/mixer_applet2/es
%lang(eu) %{_gnomehelpdir}/mixer_applet2/eu
%lang(fr) %{_gnomehelpdir}/mixer_applet2/fr
%lang(it) %{_gnomehelpdir}/mixer_applet2/it
%lang(ja) %{_gnomehelpdir}/mixer_applet2/ja
%lang(ko) %{_gnomehelpdir}/mixer_applet2/ko
%lang(sv) %{_gnomehelpdir}/mixer_applet2/sv
%lang(uk) %{_gnomehelpdir}/mixer_applet2/uk
%lang(zh_CN) %{_gnomehelpdir}/mixer_applet2/zh_CN
%lang(zh_HK) %{_gnomehelpdir}/mixer_applet2/zh_HK
%lang(zh_TW) %{_gnomehelpdir}/mixer_applet2/zh_TW

%files modemlights
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modem_applet
%{_libdir}/bonobo/servers/GNOME_ModemLights.server
%{_datadir}/gnome-2.0/ui/GNOME_ModemLights.xml
%{_datadir}/%{name}/glade/modemlights.glade
%{_iconsdir}/hicolor/48x48/apps/gnome-modem.png

%files multiload
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/multiload-applet-2
%{_libdir}/bonobo/servers/GNOME_MultiLoadApplet_Factory.server
%{_datadir}/gnome-2.0/ui/GNOME_MultiloadApplet.xml
%{_sysconfdir}/gconf/schemas/multiload.schemas
%{_omf_dest_dir}/%{name}/multiload-C.omf
%lang(de) %{_omf_dest_dir}/%{name}/multiload-de.omf
%lang(es) %{_omf_dest_dir}/%{name}/multiload-es.omf
%lang(eu) %{_omf_dest_dir}/%{name}/multiload-eu.omf
%lang(fr) %{_omf_dest_dir}/%{name}/multiload-fr.omf
%lang(it) %{_omf_dest_dir}/%{name}/multiload-it.omf
%lang(ja) %{_omf_dest_dir}/%{name}/multiload-ja.omf
%lang(ko) %{_omf_dest_dir}/%{name}/multiload-ko.omf
%lang(sv) %{_omf_dest_dir}/%{name}/multiload-sv.omf
%lang(uk) %{_omf_dest_dir}/%{name}/multiload-uk.omf
%lang(zh_CN) %{_omf_dest_dir}/%{name}/multiload-zh_CN.omf
%lang(zh_HK) %{_omf_dest_dir}/%{name}/multiload-zh_HK.omf
%lang(zh_TW) %{_omf_dest_dir}/%{name}/multiload-zh_TW.omf
%dir %{_gnomehelpdir}/multiload
%{_gnomehelpdir}/multiload/C
%lang(de) %{_gnomehelpdir}/multiload/de
%lang(es) %{_gnomehelpdir}/multiload/es
%lang(eu) %{_gnomehelpdir}/multiload/eu
%lang(fr) %{_gnomehelpdir}/multiload/fr
%lang(it) %{_gnomehelpdir}/multiload/it
%lang(ja) %{_gnomehelpdir}/multiload/ja
%lang(ko) %{_gnomehelpdir}/multiload/ko
%lang(sv) %{_gnomehelpdir}/multiload/sv
%lang(uk) %{_gnomehelpdir}/multiload/uk
%lang(zh_CN) %{_gnomehelpdir}/multiload/zh_CN
%lang(zh_HK) %{_gnomehelpdir}/multiload/zh_HK
%lang(zh_TW) %{_gnomehelpdir}/multiload/zh_TW

%files stickynotes
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/stickynotes_applet
%{_libdir}/bonobo/servers/GNOME_StickyNotesApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_StickyNotesApplet.xml
%{_datadir}/%{name}/glade/stickynotes.glade
%{_pixmapsdir}/stickynotes
%{_sysconfdir}/gconf/schemas/stickynotes.schemas
%{_omf_dest_dir}/%{name}/stickynotes_applet-C.omf
%lang(de) %{_omf_dest_dir}/%{name}/stickynotes_applet-de.omf
%lang(es) %{_omf_dest_dir}/%{name}/stickynotes_applet-es.omf
%lang(eu) %{_omf_dest_dir}/%{name}/stickynotes_applet-eu.omf
%lang(fr) %{_omf_dest_dir}/%{name}/stickynotes_applet-fr.omf
%lang(it) %{_omf_dest_dir}/%{name}/stickynotes_applet-it.omf
%lang(ja) %{_omf_dest_dir}/%{name}/stickynotes_applet-ja.omf
%lang(ko) %{_omf_dest_dir}/%{name}/stickynotes_applet-ko.omf
%lang(sv) %{_omf_dest_dir}/%{name}/stickynotes_applet-sv.omf
%lang(uk) %{_omf_dest_dir}/%{name}/stickynotes_applet-uk.omf
%lang(zh_CN) %{_omf_dest_dir}/%{name}/stickynotes_applet-zh_CN.omf
%lang(zh_HK) %{_omf_dest_dir}/%{name}/stickynotes_applet-zh_HK.omf
%lang(zh_TW) %{_omf_dest_dir}/%{name}/stickynotes_applet-zh_TW.omf
%dir %{_gnomehelpdir}/stickynotes_applet
%{_gnomehelpdir}/stickynotes_applet/C
%lang(de) %{_gnomehelpdir}/stickynotes_applet/de
%lang(es) %{_gnomehelpdir}/stickynotes_applet/es
%lang(eu) %{_gnomehelpdir}/stickynotes_applet/eu
%lang(fr) %{_gnomehelpdir}/stickynotes_applet/fr
%lang(it) %{_gnomehelpdir}/stickynotes_applet/it
%lang(ja) %{_gnomehelpdir}/stickynotes_applet/ja
%lang(ko) %{_gnomehelpdir}/stickynotes_applet/ko
%lang(sv) %{_gnomehelpdir}/stickynotes_applet/sv
%lang(uk) %{_gnomehelpdir}/stickynotes_applet/uk
%lang(zh_CN) %{_gnomehelpdir}/stickynotes_applet/zh_CN
%lang(zh_HK) %{_gnomehelpdir}/stickynotes_applet/zh_HK
%lang(zh_TW) %{_gnomehelpdir}/stickynotes_applet/zh_TW

%files trash
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/trashapplet
%{_libdir}/bonobo/servers/GNOME_Panel_TrashApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_Panel_TrashApplet.xml
%{_omf_dest_dir}/%{name}/trashapplet-C.omf
%lang(uk) %{_omf_dest_dir}/%{name}/trashapplet-uk.omf
%dir %{_gnomehelpdir}/trashapplet
%{_gnomehelpdir}/trashapplet/C
%lang(uk) %{_gnomehelpdir}/trashapplet/uk
