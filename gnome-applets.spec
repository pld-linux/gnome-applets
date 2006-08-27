#
# Conditional build:
%bcond_without	modemlights	# don't build modemlights applet
#
Summary:	Small applications which embed themselves in the GNOME panel
Summary(pl):	Aplety GNOME - ma³e aplikacje osadzaj±ce siê w panelu
Summary(ru):	íÁÌÅÎØËÉÅ ÐÒÏÇÒÁÍÍÙ, ×ÓÔÒÁÉ×ÁÀÝÉÅÓÑ × ÐÁÎÅÌØ GNOME
Summary(uk):	íÁÌÅÎØË¦ ÐÒÏÇÒÁÍÉ, ÝÏ ×ÂÕÄÏ×ÕÀÔØÓÑ × ÐÁÎÅÌØ GNOME
Name:		gnome-applets
Version:	2.15.90
Release:	2
Epoch:		1
License:	GPL v2, FDL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-applets/2.15/%{name}-%{version}.tar.bz2
# Source0-md5:	421eda161541b42d42ea04c59b9ee4f1
Patch0:		%{name}-stickynotes-title-size.patch
Patch1:		%{name}-m4_fix.patch
Patch2:		%{name}-desktop.patch
Patch3:		%{name}-modemlights-conditional.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	control-center-devel >= 2.15.92
BuildRequires:	cpufrequtils-devel >= 0.3
BuildRequires:	dbus-glib-devel >= 0.71-2
BuildRequires:	gail-devel >= 1.9.2
BuildRequires:	gdbm-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnome-desktop-devel >= 2.15.92
BuildRequires:	gnome-doc-utils >= 0.7.2
BuildRequires:	gnome-panel-devel >= 2.15.92
BuildRequires:	gnome-vfs2-devel >= 2.15.92
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.9
BuildRequires:	gtk+2-devel >= 2:2.10.2
BuildRequires:	gucharmap-devel >= 1.7.0
BuildRequires:	hal-devel >= 0.5.7.1
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libgnomeui-devel >= 2.15.91
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgtop-devel >= 1:2.14.2
BuildRequires:	libnotify-devel >= 0.4.2
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.15.92
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	libxklavier-devel >= 2.91
BuildRequires:	libxslt-progs >= 1.1.17
BuildRequires:	pkgconfig
BuildRequires:	python-gnome-desktop-devel >= 2.15.90
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper >= 0.3.11-4
%if %{with modemlights}
BuildRequires:	system-tools-backends >= 1.4.0
BuildRequires:	system-tools-backends < 1.9.0
%endif
Requires:	gnome-icon-theme >= 2.15.92
Requires:	gnome-panel >= 2.15.92
Requires:	gnome-vfs2 >= 2.15.92
Requires:	hicolor-icon-theme
Requires:	libgnomeui >= 2.15.91
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
Requires:	GConf2-devel >= 2.14.0
Requires:	gtk+2-devel >= 2:2.10.2

%description devel
Header files for gnome-applets.

%description devel -l pl
Pliki nag³ówkowe gnome-applets.

%package accessx-status
Summary:	Keyboard Accessibility Status applet
Summary(pl):	Aplet stanu dostepno¶ci klawiatury
Group:		X11/Applications
Requires(post,postun):	gtk+2 >= 2.10.2
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
Requires(post,postun):	gtk+2 >= 2.10.2
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
Requires(post,postun):	gtk+2 >= 2.10.2
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
Requires(post,postun):	gtk+2 >= 2.10.2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets <= 0:2.10.0-5

%description geyes
Geyes applet.

%description geyes -l pl
Aplet geyes.

%package gweather
Summary:	Weather Report applet
Summary(pl):	Aplet raportu pogodowego
Group:		X11/Applications
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	notification-daemon
Conflicts:	gnome-applets <= 0:2.10.0-5

%description gweather
Weather Report applet.

%description gweather -l pl
Aplet raportu pogodowego.

%package invest
Summary:	Stock Ticker applet
Summary(pl):	Aplet wska¼nika gie³dowego
Group:		X11/Applications
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	python-gnome-extras-egg >= 2.14.2
Conflicts:	gnome-applets <= 0:2.10.0-5
Obsoletes:	gnome-applets-gtik

%description invest
Stock Ticker applet.

%description invest -l pl
Aplet wska¼nika gie³dowego.

%package keyboard
Summary:	Keyboard Indicator applet
Summary(pl):	Aplet wska¼nika klawiatury
Group:		X11/Applications
Requires(post,preun):	GConf2
Requires(post,postun):	gtk+2 >= 2.10.2
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
Requires(post,postun):	gtk+2 >= 2.10.2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gstreamer-audio-effects-base >= 0.10
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
Requires(post,postun):	gtk+2 >= 2.10.2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	system-tools-backends >= 1.4.0
Requires:	susyem-tools-backends < 1.9.0
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
Requires(post,postun):	gtk+2 >= 2.10.2
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
%patch3 -p1

%build
%{__gnome_doc_prepare}
%{__libtoolize}
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__gnome_doc_common}
%{__automake}
%{__autoconf}
%configure \
	--disable-static \
	--disable-schemas-install \
	--enable-mini-commander \
	--enable-stickynotes \
	%{!?with_modemlights:--disable-modemlights}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 \
	pythondir=%{py_sitedir}

rm -f $RPM_BUILD_ROOT%{_libdir}/libgweather.la
rm -f $RPM_BUILD_ROOT%{py_sitedir}/invest/*.py
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{es_*,no}

%find_lang %{name} --all-name --with-gnome
%find_lang accessx-status --with-gnome
%find_lang battstat --with-gnome
%find_lang char-palette --with-gnome
%find_lang command-line --with-gnome
%find_lang cpufreq-applet --with-gnome
%find_lang drivemount --with-gnome
%find_lang geyes --with-gnome
%find_lang gswitchit --with-gnome
%find_lang gweather --with-gnome
%find_lang mixer_applet2 --with-gnome
%find_lang multiload --with-gnome
%find_lang stickynotes_applet --with-gnome
%find_lang trashapplet --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post accessx-status
%scrollkeeper_update_post
%banner %{name} -e << EOF
For full functionality, you need to install control-center.
EOF
%update_icon_cache hicolor

%postun accessx-status
%scrollkeeper_update_postun
%update_icon_cache hicolor

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
%update_icon_cache hicolor

%preun charpicker
%gconf_schema_uninstall charpick.schemas

%postun charpicker
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post cpufreq
%scrollkeeper_update_post
%gconf_schema_install cpufreq-applet.schemas
%banner %{name} -e << EOF
For full functionality, set SUID /usr/bin/cpufreq-selector binary.
EOF
%update_icon_cache hicolor

%preun cpufreq
%gconf_schema_uninstall cpufreq-applet.schemas

%postun cpufreq
%scrollkeeper_update_postun
%update_icon_cache hicolor

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
%update_icon_cache hicolor

%preun geyes
%gconf_schema_uninstall geyes.schemas

%postun geyes 
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post gweather
/sbin/ldconfig
%scrollkeeper_update_post
%gconf_schema_install gweather.schemas

%preun gweather
%gconf_schema_uninstall gweather.schemas

%postun gweather
/sbin/ldconfig
%scrollkeeper_update_postun

%post invest
%scrollkeeper_update_post

%postun invest
%scrollkeeper_update_postun

%post keyboard
%scrollkeeper_update_post
%gconf_schema_install gswitchit.schemas
%update_icon_cache hicolor

%preun keyboard
%gconf_schema_uninstall gswitchit.schemas

%postun keyboard
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post minicommander
%scrollkeeper_update_post
%gconf_schema_install mini-commander-global.schemas
%gconf_schema_install mini-commander.schemas
GCONF_CONFIG_SOURCE="`%{_bindir}/gconftool-2 --get-default-source`" %{_libdir}/%{name}/mc-install-default-macros
%update_icon_cache hicolor

%preun minicommander
%gconf_schema_uninstall mini-commander-global.schemas
%gconf_schema_uninstall mini-commander.schemas

%postun minicommander
%scrollkeeper_update_postun
%update_icon_cache hicolor

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
%update_icon_cache hicolor

%postun modemlights
%update_icon_cache hicolor

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
%update_icon_cache hicolor

%preun stickynotes
%gconf_schema_uninstall stickynotes.schemas

%postun stickynotes
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post trash
%scrollkeeper_update_post

%postun trash
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/null_applet
%{_libdir}/bonobo/servers/GNOME_CDPlayerApplet.server
%{_libdir}/bonobo/servers/GNOME_MailcheckApplet_Factory.server
%{_libdir}/bonobo/servers/GNOME_NullApplet_Factory.server
%{_libdir}/bonobo/servers/GNOME_Panel_WirelessApplet.server
%dir %{_libdir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/glade

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_pkgconfigdir}/*.pc

%files accessx-status -f accessx-status.lang
%defattr(644,root,root,755)
%doc accessx-status/ChangeLog
%attr(755,root,root) %{_libdir}/accessx-status-applet
%{_libdir}/bonobo/servers/GNOME_AccessxStatusApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_AccessxApplet.xml
%{_pixmapsdir}/accessx-status-applet
%{_iconsdir}/hicolor/48x48/apps/ax-applet.png
%dir %{_omf_dest_dir}/accessx-status
%{_omf_dest_dir}/accessx-status/accessx-status-C.omf
%lang(bg) %{_omf_dest_dir}/accessx-status/accessx-status-bg.omf
%lang(es) %{_omf_dest_dir}/accessx-status/accessx-status-es.omf
%lang(fr) %{_omf_dest_dir}/accessx-status/accessx-status-fr.omf
%lang(it) %{_omf_dest_dir}/accessx-status/accessx-status-it.omf
%lang(nl) %{_omf_dest_dir}/accessx-status/accessx-status-nl.omf
%lang(sv) %{_omf_dest_dir}/accessx-status/accessx-status-sv.omf
%lang(uk) %{_omf_dest_dir}/accessx-status/accessx-status-uk.omf

%files battstat -f battstat.lang
%defattr(644,root,root,755)
%doc battstat/ChangeLog
%attr(755,root,root) %{_libdir}/battstat-applet-2
%{_libdir}/bonobo/servers/GNOME_BattstatApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_BattstatApplet.xml
%{_datadir}/%{name}/glade/battstat_applet.glade
%{_sysconfdir}/gconf/schemas/battstat.schemas
%{_sysconfdir}/sound/events/battstat_applet.soundlist
%dir %{_omf_dest_dir}/battstat
%{_omf_dest_dir}/battstat/battstat-C.omf
%lang(bg) %{_omf_dest_dir}/battstat/battstat-bg.omf
%lang(es) %{_omf_dest_dir}/battstat/battstat-es.omf
%lang(fr) %{_omf_dest_dir}/battstat/battstat-fr.omf
%lang(sv) %{_omf_dest_dir}/battstat/battstat-sv.omf
%lang(uk) %{_omf_dest_dir}/battstat/battstat-uk.omf

%files charpicker -f char-palette.lang
%defattr(644,root,root,755)
%doc charpick/ChangeLog
%attr(755,root,root) %{_libdir}/charpick_applet2
%{_libdir}/bonobo/servers/GNOME_CharpickerApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_CharpickerApplet.xml
%{_iconsdir}/hicolor/48x48/apps/charpick.png
%{_sysconfdir}/gconf/schemas/charpick.schemas
%dir %{_omf_dest_dir}/char-palette
%{_omf_dest_dir}/char-palette/char-palette-C.omf
%lang(bg) %{_omf_dest_dir}/char-palette/char-palette-bg.omf
%lang(es) %{_omf_dest_dir}/char-palette/char-palette-es.omf
%lang(fr) %{_omf_dest_dir}/char-palette/char-palette-fr.omf
%lang(it) %{_omf_dest_dir}/char-palette/char-palette-it.omf
%lang(nl) %{_omf_dest_dir}/char-palette/char-palette-nl.omf
%lang(pt_BR) %{_omf_dest_dir}/char-palette/char-palette-pt_BR.omf
%lang(sv) %{_omf_dest_dir}/char-palette/char-palette-sv.omf
%lang(uk) %{_omf_dest_dir}/char-palette/char-palette-uk.omf

%files cpufreq -f cpufreq-applet.lang
%defattr(644,root,root,755)
%doc cpufreq/ChangeLog
%attr(755,root,root) %{_bindir}/cpufreq-selector
%attr(755,root,root) %{_libdir}/cpufreq-applet
%{_libdir}/bonobo/servers/GNOME_CPUFreqApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_CPUFreqApplet.xml
%{_datadir}/%{name}/glade/cpufreq-preferences.glade
%{_sysconfdir}/gconf/schemas/cpufreq-applet.schemas
%{_pixmapsdir}/cpufreq-applet
%{_iconsdir}/hicolor/*/apps/gnome-cpu-frequency-applet.*
%dir %{_omf_dest_dir}/cpufreq-applet
%{_omf_dest_dir}/cpufreq-applet/cpufreq-applet-C.omf
%lang(es) %{_omf_dest_dir}/cpufreq-applet/cpufreq-applet-es.omf
%lang(fr) %{_omf_dest_dir}/cpufreq-applet/cpufreq-applet-fr.omf
%lang(nl) %{_omf_dest_dir}/cpufreq-applet/cpufreq-applet-nl.omf
%lang(sv) %{_omf_dest_dir}/cpufreq-applet/cpufreq-applet-sv.omf
%lang(uk) %{_omf_dest_dir}/cpufreq-applet/cpufreq-applet-uk.omf
%lang(zh_CN) %{_omf_dest_dir}/cpufreq-applet/cpufreq-applet-zh_CN.omf

%files drivemount -f drivemount.lang
%defattr(644,root,root,755)
%doc drivemount/ChangeLog
%attr(755,root,root) %{_libdir}/drivemount_applet2
%{_libdir}/bonobo/servers/GNOME_DriveMountApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_DriveMountApplet.xml
%{_sysconfdir}/gconf/schemas/drivemount.schemas
%dir %{_omf_dest_dir}/drivemount
%{_omf_dest_dir}/drivemount/drivemount-C.omf
%lang(es) %{_omf_dest_dir}/drivemount/drivemount-es.omf
%lang(fr) %{_omf_dest_dir}/drivemount/drivemount-fr.omf
%lang(it) %{_omf_dest_dir}/drivemount/drivemount-it.omf
%lang(pa) %{_omf_dest_dir}/drivemount/drivemount-pa.omf
%lang(sv) %{_omf_dest_dir}/drivemount/drivemount-sv.omf
%lang(uk) %{_omf_dest_dir}/drivemount/drivemount-uk.omf
%lang(zh_CN) %{_omf_dest_dir}/drivemount/drivemount-zh_CN.omf

%files geyes -f geyes.lang
%defattr(644,root,root,755)
%doc geyes/ChangeLog
%attr(755,root,root) %{_libdir}/geyes_applet2
%{_libdir}/bonobo/servers/GNOME_GeyesApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_GeyesApplet.xml
%{_datadir}/%{name}/geyes
%{_iconsdir}/hicolor/*/apps/gnome-eyes-applet.*
%{_sysconfdir}/gconf/schemas/geyes.schemas
%dir %{_omf_dest_dir}/geyes
%{_omf_dest_dir}/geyes/geyes-C.omf
%lang(bg) %{_omf_dest_dir}/geyes/geyes-bg.omf
%lang(es) %{_omf_dest_dir}/geyes/geyes-es.omf
%lang(fr) %{_omf_dest_dir}/geyes/geyes-fr.omf
%lang(it) %{_omf_dest_dir}/geyes/geyes-it.omf
%lang(ru) %{_omf_dest_dir}/geyes/geyes-ru.omf
%lang(sv) %{_omf_dest_dir}/geyes/geyes-sv.omf
%lang(uk) %{_omf_dest_dir}/geyes/geyes-uk.omf

%files gweather -f gweather.lang
%defattr(644,root,root,755)
%doc gweather/ChangeLog
%attr(755,root,root) %{_libdir}/gweather-applet-2
%attr(755,root,root) %{_libdir}/libgweather.so*
%{_libdir}/bonobo/servers/GNOME_GWeatherApplet_Factory.server
%{_datadir}/gnome-2.0/ui/GNOME_GWeatherApplet.xml
%{_datadir}/%{name}/gweather
%{_sysconfdir}/gconf/schemas/gweather.schemas
%dir %{_omf_dest_dir}/gweather
%{_omf_dest_dir}/gweather/gweather-C.omf
%lang(es) %{_omf_dest_dir}/gweather/gweather-es.omf
%lang(fr) %{_omf_dest_dir}/gweather/gweather-fr.omf
%lang(nl) %{_omf_dest_dir}/gweather/gweather-nl.omf
%lang(sv) %{_omf_dest_dir}/gweather/gweather-sv.omf
%lang(uk) %{_omf_dest_dir}/gweather/gweather-uk.omf

%files invest
%defattr(644,root,root,755)
%doc invest-applet/ChangeLog
%attr(755,root,root) %{_bindir}/invest-chart
%attr(755,root,root) %{_libdir}/invest-applet
%{_libdir}/bonobo/servers/GNOME_GtikApplet.server
%{_libdir}/bonobo/servers/Invest_Applet.server
%{_datadir}/gnome-2.0/ui/Invest_Applet.xml
%{_datadir}/%{name}/invest-applet
%{_datadir}/%{name}/glade/financialchart.glade
%{_datadir}/%{name}/glade/prefs-dialog.glade
%{_desktopdir}/invest-chart.desktop
%{_pixmapsdir}/invest-big.png
%dir %{py_sitedir}/invest
%{py_sitedir}/invest/*.py[co]

%files keyboard -f gswitchit.lang
%defattr(644,root,root,755)
%doc gswitchit/ChangeLog
%attr(755,root,root) %{_libdir}/gnome-keyboard-applet
%{_libdir}/bonobo/servers/GNOME_KeyboardApplet.server
%{_desktopdir}/gswitchit-plugins.desktop
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
%dir %{_omf_dest_dir}/gswitchit
%{_omf_dest_dir}/gswitchit/gswitchit-C.omf
%lang(es) %{_omf_dest_dir}/gswitchit/gswitchit-es.omf
%lang(fr) %{_omf_dest_dir}/gswitchit/gswitchit-fr.omf
%lang(sv) %{_omf_dest_dir}/gswitchit/gswitchit-sv.omf
%lang(uk) %{_omf_dest_dir}/gswitchit/gswitchit-uk.omf

%files minicommander -f command-line.lang
%defattr(644,root,root,755)
%doc mini-commander/ChangeLog
%attr(755,root,root) %{_libdir}/mini_commander_applet
%attr(755,root,root) %{_libdir}/%{name}/mc-install-default-macros
%{_libdir}/bonobo/servers/GNOME_MiniCommanderApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_MiniCommanderApplet.xml
%{_datadir}/%{name}/glade/mini-commander.glade
%{_iconsdir}/hicolor/48x48/apps/gnome-mini-commander.png
%{_sysconfdir}/gconf/schemas/mini-commander-global.schemas
%{_sysconfdir}/gconf/schemas/mini-commander.schemas
%dir %{_omf_dest_dir}/command-line
%{_omf_dest_dir}/command-line/command-line-C.omf
%lang(es) %{_omf_dest_dir}/command-line/command-line-es.omf
%lang(fr) %{_omf_dest_dir}/command-line/command-line-fr.omf
%lang(pt_BR) %{_omf_dest_dir}/command-line/command-line-pt_BR.omf
%lang(sv) %{_omf_dest_dir}/command-line/command-line-sv.omf
%lang(uk) %{_omf_dest_dir}/command-line/command-line-uk.omf

%files mixer
%defattr(644,root,root,755)
%doc mixer/ChangeLog
%attr(755,root,root) %{_libdir}/mixer_applet2
%{_libdir}/bonobo/servers/GNOME_MixerApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_MixerApplet.xml
%{_sysconfdir}/gconf/schemas/mixer.schemas
%dir %{_omf_dest_dir}/mixer_applet2
%{_omf_dest_dir}/mixer_applet2/mixer_applet2-C.omf
%lang(es) %{_omf_dest_dir}/mixer_applet2/mixer_applet2-es.omf
%lang(it) %{_omf_dest_dir}/mixer_applet2/mixer_applet2-it.omf
%lang(fr) %{_omf_dest_dir}/mixer_applet2/mixer_applet2-fr.omf
%lang(sv) %{_omf_dest_dir}/mixer_applet2/mixer_applet2-sv.omf
%lang(uk) %{_omf_dest_dir}/mixer_applet2/mixer_applet2-uk.omf

%if %{with modemlights}
%files modemlights
%defattr(644,root,root,755)
%doc modemlights/ChangeLog
%attr(755,root,root) %{_libdir}/modem_applet
%{_libdir}/bonobo/servers/GNOME_ModemLights.server
%{_datadir}/gnome-2.0/ui/GNOME_ModemLights.xml
%{_datadir}/%{name}/glade/modemlights.glade
%{_iconsdir}/hicolor/*/apps/gnome-modem-monitor-applet.*
%endif

%files multiload -f multiload.lang
%defattr(644,root,root,755)
%doc multiload/ChangeLog
%attr(755,root,root) %{_libdir}/multiload-applet-2
%{_libdir}/bonobo/servers/GNOME_MultiLoadApplet_Factory.server
%{_datadir}/gnome-2.0/ui/GNOME_MultiloadApplet.xml
%{_sysconfdir}/gconf/schemas/multiload.schemas
%dir %{_omf_dest_dir}/multiload
%{_omf_dest_dir}/multiload/multiload-C.omf
%lang(es) %{_omf_dest_dir}/multiload/multiload-es.omf
%lang(fr) %{_omf_dest_dir}/multiload/multiload-fr.omf
%lang(sv) %{_omf_dest_dir}/multiload/multiload-sv.omf
%lang(uk) %{_omf_dest_dir}/multiload/multiload-uk.omf

%files stickynotes -f stickynotes_applet.lang
%defattr(644,root,root,755)
%doc stickynotes/ChangeLog
%attr(755,root,root) %{_libdir}/stickynotes_applet
%{_libdir}/bonobo/servers/GNOME_StickyNotesApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_StickyNotesApplet.xml
%{_datadir}/%{name}/glade/stickynotes.glade
%{_pixmapsdir}/stickynotes
%{_iconsdir}/hicolor/*/apps/gnome-sticky-notes-applet.*
%{_sysconfdir}/gconf/schemas/stickynotes.schemas
%dir %{_omf_dest_dir}/stickynotes_applet
%{_omf_dest_dir}/stickynotes_applet/stickynotes_applet-C.omf
%lang(es) %{_omf_dest_dir}/stickynotes_applet/stickynotes_applet-es.omf
%lang(fr) %{_omf_dest_dir}/stickynotes_applet/stickynotes_applet-fr.omf
%lang(sv) %{_omf_dest_dir}/stickynotes_applet/stickynotes_applet-sv.omf
%lang(uk) %{_omf_dest_dir}/stickynotes_applet/stickynotes_applet-uk.omf

%files trash -f trashapplet.lang
%defattr(644,root,root,755)
%doc trashapplet/ChangeLog
%attr(755,root,root) %{_libdir}/trashapplet
%{_libdir}/bonobo/servers/GNOME_Panel_TrashApplet.server
%{_datadir}/%{name}/glade/trashapplet.glade
%{_datadir}/gnome-2.0/ui/GNOME_Panel_TrashApplet.xml
%dir %{_omf_dest_dir}/trashapplet
%{_omf_dest_dir}/trashapplet/trashapplet-C.omf
%lang(es) %{_omf_dest_dir}/trashapplet/trashapplet-es.omf
%lang(fr) %{_omf_dest_dir}/trashapplet/trashapplet-fr.omf
%lang(it) %{_omf_dest_dir}/trashapplet/trashapplet-it.omf
%lang(nl) %{_omf_dest_dir}/trashapplet/trashapplet-nl.omf
%lang(pa) %{_omf_dest_dir}/trashapplet/trashapplet-pa.omf
%lang(ru) %{_omf_dest_dir}/trashapplet/trashapplet-ru.omf
%lang(sv) %{_omf_dest_dir}/trashapplet/trashapplet-sv.omf
%lang(uk) %{_omf_dest_dir}/trashapplet/trashapplet-uk.omf
