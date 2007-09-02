Summary:	Small applications which embed themselves in the GNOME panel
Summary(pl.UTF-8):	Aplety GNOME - małe aplikacje osadzające się w panelu
Summary(ru.UTF-8):	Маленькие программы, встраивающиеся в панель GNOME
Summary(uk.UTF-8):	Маленькі програми, що вбудовуються в панель GNOME
Name:		gnome-applets
Version:	2.19.1
Release:	1
Epoch:		1
License:	GPL v2, FDL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-applets/2.19/%{name}-%{version}.tar.bz2
# Source0-md5:	9dc982c8df1eaa27fecd4e78675070ba
Patch0:		%{name}-stickynotes-title-size.patch
Patch1:		%{name}-m4_fix.patch
Patch2:		%{name}-use-liboobs.patch
URL:		http://www.gnome.org/
#BuildRequires:	GConf2-devel >= 2.18.0.1
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	gnome-control-center-devel >= 2.19.91
BuildRequires:	cpufrequtils-devel >= 0.3
BuildRequires:	dbus-glib-devel >= 0.73
BuildRequires:	gail-devel >= 1.19.6
BuildRequires:	gdbm-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.18.0
BuildRequires:	gnome-desktop-devel >= 2.19.90
BuildRequires:	gnome-doc-utils >= 0.11.2
BuildRequires:	gnome-icon-theme >= 2.19.91
BuildRequires:	gnome-panel-devel >= 2.19.6
BuildRequires:	gnome-vfs2-devel >= 2.19.91
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.10
BuildRequires:	gtk+2-devel >= 2:2.11.6
BuildRequires:	gucharmap-devel >= 1.10.0
BuildRequires:	hal-devel >= 0.5.9
BuildRequires:	intltool >= 0.36.1
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomekbd-devel >= 2.19.91
BuildRequires:	libgnomeui-devel >= 2.19.1
BuildRequires:	libgtop-devel >= 1:2.19.92
BuildRequires:	libnotify-devel >= 0.4.2
BuildRequires:	liboobs-devel >= 2.18.1
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.19.90
BuildRequires:	libxklavier-devel >= 3.0
BuildRequires:	libxml2-devel >= 1:2.6.29
BuildRequires:	libxslt-progs >= 1.1.20
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	python-gnome-desktop-devel >= 2.19.2
BuildRequires:	python-pygtk-devel >= 2:2.10.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper >= 0.3.11-4
Requires:	gnome-icon-theme >= 2.19.91
Requires:	gnome-panel >= 2.19.6
Requires:	gnome-vfs2 >= 2.19.91
Requires:	hicolor-icon-theme
Requires:	libgnomeui >= 2.19.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gnomehelpdir	%{_datadir}/gnome/help

%description
The gnome-applets package provides Panel applets which enhance your
GNOME experience.

%description -l pl.UTF-8
Pakiet gnome-applets udostępnia aplety Panelu, które usprawniają pracę
z GNOME.

%description -l uk.UTF-8
Пакет gnome-applets містить аплети Панелі GNOME, що збільшують
комфортність роботи в середовищі GNOME.

%description -l ru.UTF-8
Пакет gnome-applets содержит апплеты Панели GNOME, увеличивающие
комфортность работы в среде GNOME.

%package devel
Summary:	Header files for gnome-applets
Summary(pl.UTF-8):	Pliki nagłówkowe gnome-applets
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	GConf2-devel >= 2.19.1
Requires:	gtk+2-devel >= 2:2.11.6

%description devel
Header files for gnome-applets.

%description devel -l pl.UTF-8
Pliki nagłówkowe gnome-applets.

%package accessx-status
Summary:	Keyboard Accessibility Status applet
Summary(pl.UTF-8):	Aplet stanu dostepności klawiatury
Group:		X11/Applications
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Suggests:	gnome-control-center >= 2.19.91
Conflicts:	gnome-applets <= 0:2.10.0-5

%description accessx-status
Keyboard Accessibility Status applet.

%description accessx-status -l pl.UTF-8
Aplet stanu dostepności klawiatury.

%package battstat
Summary:	Battery Charge Monitor applet
Summary(pl.UTF-8):	Aplet monitora stanu naładowania akumulatora
Group:		X11/Applications
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets <= 0:2.10.0-5

%description battstat
Battery Charge Monitor applet.

%description battstat -l pl.UTF-8
Aplet monitora stanu naładowania akumulatora.

%package charpicker
Summary:	Character Palette applet
Summary(pl.UTF-8):	Aplet palety znaków
Group:		X11/Applications
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets <= 0:2.10.0-5

%description charpicker
Character Palette applet.

%description charpicker -l pl.UTF-8
Aplet palety znaków.

%package cpufreq
Summary:	CPU Frequency Scaling Monitor applet
Summary(pl.UTF-8):	Aplet monitora częstotliwości procesora
Group:		X11/Applications
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	gnome-applet-cpufreq
Conflicts:	gnome-applets <= 0:2.10.0-5

%description cpufreq
CPU Frequency Scaling Monitor applet.

%description cpufreq -l pl.UTF-8
Aplet monitora częstotliwości procesora.

%package drivemount
Summary:	Disk Mounter applet
Summary(pl.UTF-8):	Aplet do montowania dysków
Group:		X11/Applications
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets <= 0:2.10.0-5

%description drivemount
Disk Mounter applet.

%description drivemount -l pl.UTF-8
Aplet do monotwania dysków.

%package geyes
Summary:	Geyes applet
Summary(pl.UTF-8):	Aplet geyes
Group:		X11/Applications
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets <= 0:2.10.0-5

%description geyes
Geyes applet.

%description geyes -l pl.UTF-8
Aplet geyes.

%package gweather
Summary:	Weather Report applet
Summary(pl.UTF-8):	Aplet raportu pogodowego
Group:		X11/Applications
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	notification-daemon
Conflicts:	gnome-applets <= 0:2.10.0-5

%description gweather
Weather Report applet.

%description gweather -l pl.UTF-8
Aplet raportu pogodowego.

%package invest
Summary:	Stock Ticker applet
Summary(pl.UTF-8):	Aplet wskaźnika giełdowego
Group:		X11/Applications
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	python-gnome-extras-egg >= 2.14.2
Obsoletes:	gnome-applets-gtik
Conflicts:	gnome-applets <= 0:2.10.0-5

%description invest
Stock Ticker applet.

%description invest -l pl.UTF-8
Aplet wskaźnika giełdowego.

%package keyboard
Summary:	Keyboard Indicator applet
Summary(pl.UTF-8):	Aplet wskaźnika klawiatury
Group:		X11/Applications
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets <= 0:2.10.0-5

%description keyboard
Keyboard Indicator applet.

%description keyboard -l pl.UTF-8
Aplet wskaźnika klawiatury.

%package minicommander
Summary:	Command Line applet
Summary(pl.UTF-8):	Aplet wiersza poleceń
Group:		X11/Applications
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets <= 0:2.10.0-5

%description minicommander
Command Line applet.

%description minicommander -l pl.UTF-8
Aplet wiersza poleceń.

%package mixer
Summary:	Volume Control applet
Summary(pl.UTF-8):	Aplet regulacji głośności
Group:		X11/Applications
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gstreamer-audio-effects-base >= 0.10.10
Requires:	gstreamer-audiosink
Suggests:	gnome-media-volume-control >= 2.18.0
Conflicts:	gnome-applets <= 0:2.10.0-5

%description mixer
Volume Control applet.

%description mixer -l pl.UTF-8
Aplet regulacji głośności.

%package modemlights
Summary:	Modem Lights applet
Summary(pl.UTF-8):	Aplet kontrolek modemu
Group:		X11/Applications
Requires(post,postun):	gtk+2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	system-tools-backends
Conflicts:	gnome-applets <= 0:2.10.0-5

%description modemlights
Modem Lights applet.

%description modemlights -l pl.UTF-8
Aplet kontrolek modemu.

%package multiload
Summary:	System Monitor applet
Summary(pl.UTF-8):	Aplet monitora systemu
Group:		X11/Applications
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Suggests:	gnome-system-monitor >= 2.19.91
Conflicts:	gnome-applets <= 0:2.10.0-5

%description multiload
System Monitor applet.

%description multiload -l pl.UTF-8
Aplet monitora systemu.

%package stickynotes
Summary:	Sticky Notes applet
Summary(pl.UTF-8):	Aplet notatek
Group:		X11/Applications
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	gnotes_applet
Conflicts:	gnome-applets <= 0:2.10.0-5

%description stickynotes
Sticky Notes applet.

%description stickynotes -l pl.UTF-8
Aplet notatek.

%package trash
Summary:	Trash applet
Summary(pl.UTF-8):	Aplet śmietnika
Group:		X11/Applications
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets <= 0:2.10.0-5

%description trash
Trash applet.

%description trash -l pl.UTF-8
Aplet śmietnika.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
	--enable-stickynotes
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 \
	pythondir=%{py_sitedir}

rm -f $RPM_BUILD_ROOT%{_libdir}/libgweather.la
rm -f $RPM_BUILD_ROOT%{py_sitedir}/invest/*.py
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/es{_ES,}/LC_MESSAGES/*.mo
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/es_ES

%find_lang %{name}-2.0
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
%update_icon_cache hicolor

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

%files -f %{name}-2.0.lang
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
%lang(es_CL) %dir %{_datadir}/locale/es_CL
%lang(es_CL) %dir %{_datadir}/locale/es_CL/LC_MESSAGES
%lang(es_CO) %dir %{_datadir}/locale/es_CO
%lang(es_CO) %dir %{_datadir}/locale/es_CO/LC_MESSAGES
%lang(es_CR) %dir %{_datadir}/locale/es_CR
%lang(es_CR) %dir %{_datadir}/locale/es_CR/LC_MESSAGES
%lang(es_DO) %dir %{_datadir}/locale/es_DO
%lang(es_DO) %dir %{_datadir}/locale/es_DO/LC_MESSAGES
%lang(es_EC) %dir %{_datadir}/locale/es_EC
%lang(es_EC) %dir %{_datadir}/locale/es_EC/LC_MESSAGES
%lang(es_GT) %dir %{_datadir}/locale/es_GT
%lang(es_GT) %dir %{_datadir}/locale/es_GT/LC_MESSAGES
%lang(es_HN) %dir %{_datadir}/locale/es_HN
%lang(es_HN) %dir %{_datadir}/locale/es_HN/LC_MESSAGES
%lang(es_PA) %dir %{_datadir}/locale/es_PA
%lang(es_PA) %dir %{_datadir}/locale/es_PA/LC_MESSAGES
%lang(es_PE) %dir %{_datadir}/locale/es_PE
%lang(es_PE) %dir %{_datadir}/locale/es_PE/LC_MESSAGES
%lang(es_PR) %dir %{_datadir}/locale/es_PR
%lang(es_PR) %dir %{_datadir}/locale/es_PR/LC_MESSAGES
%lang(es_SV) %dir %{_datadir}/locale/es_SV
%lang(es_SV) %dir %{_datadir}/locale/es_SV/LC_MESSAGES
%lang(es_UY) %dir %{_datadir}/locale/es_UY
%lang(es_UY) %dir %{_datadir}/locale/es_UY/LC_MESSAGES
%lang(es_VE) %dir %{_datadir}/locale/es_VE
%lang(es_VE) %dir %{_datadir}/locale/es_VE/LC_MESSAGES

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
%lang(ca) %{_omf_dest_dir}/accessx-status/accessx-status-ca.omf
%lang(en_GB) %{_omf_dest_dir}/accessx-status/accessx-status-en_GB.omf
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
%lang(en_GB) %{_omf_dest_dir}/battstat/battstat-en_GB.omf
%lang(es) %{_omf_dest_dir}/battstat/battstat-es.omf
%lang(fr) %{_omf_dest_dir}/battstat/battstat-fr.omf
%lang(pa) %{_omf_dest_dir}/battstat/battstat-pa.omf
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
%lang(en_GB) %{_omf_dest_dir}/char-palette/char-palette-en_GB.omf
%lang(es) %{_omf_dest_dir}/char-palette/char-palette-es.omf
%lang(fr) %{_omf_dest_dir}/char-palette/char-palette-fr.omf
%lang(it) %{_omf_dest_dir}/char-palette/char-palette-it.omf
%lang(nl) %{_omf_dest_dir}/char-palette/char-palette-nl.omf
%lang(pt_BR) %{_omf_dest_dir}/char-palette/char-palette-pt_BR.omf
%lang(ru) %{_omf_dest_dir}/char-palette/char-palette-ru.omf
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
%lang(ca) %{_omf_dest_dir}/cpufreq-applet/cpufreq-applet-ca.omf
%lang(en_GB) %{_omf_dest_dir}/cpufreq-applet/cpufreq-applet-en_GB.omf
%lang(es) %{_omf_dest_dir}/cpufreq-applet/cpufreq-applet-es.omf
%lang(fr) %{_omf_dest_dir}/cpufreq-applet/cpufreq-applet-fr.omf
%lang(nl) %{_omf_dest_dir}/cpufreq-applet/cpufreq-applet-nl.omf
%lang(ru) %{_omf_dest_dir}/cpufreq-applet/cpufreq-applet-ru.omf
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
%lang(en_GB) %{_omf_dest_dir}/drivemount/drivemount-en_GB.omf
%lang(es) %{_omf_dest_dir}/drivemount/drivemount-es.omf
%lang(fr) %{_omf_dest_dir}/drivemount/drivemount-fr.omf
%lang(it) %{_omf_dest_dir}/drivemount/drivemount-it.omf
%lang(pa) %{_omf_dest_dir}/drivemount/drivemount-pa.omf
%lang(ru) %{_omf_dest_dir}/drivemount/drivemount-ru.omf
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
%lang(en_GB) %{_omf_dest_dir}/geyes/geyes-en_GB.omf
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
%lang(en_GB) %{_omf_dest_dir}/gweather/gweather-en_GB.omf
%lang(es) %{_omf_dest_dir}/gweather/gweather-es.omf
%lang(fr) %{_omf_dest_dir}/gweather/gweather-fr.omf
%lang(nl) %{_omf_dest_dir}/gweather/gweather-nl.omf
%lang(pa) %{_omf_dest_dir}/gweather/gweather-pa.omf
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
%{_pixmapsdir}/invest-big.png
%dir %{py_sitedir}/invest
%{py_sitedir}/invest/*.py[co]

%files keyboard -f gswitchit.lang
%defattr(644,root,root,755)
%doc gswitchit/ChangeLog
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
%{_datadir}/gnome-2.0/ui/GNOME_GSwitchItApplet.xml
%{_datadir}/%{name}/glade/gswitchit*.glade
%{_iconsdir}/hicolor/48x48/apps/gswitchit*.png
%dir %{_omf_dest_dir}/gswitchit
%{_omf_dest_dir}/gswitchit/gswitchit-C.omf
%lang(en_GB) %{_omf_dest_dir}/gswitchit/gswitchit-en_GB.omf
%lang(es) %{_omf_dest_dir}/gswitchit/gswitchit-es.omf
%lang(fr) %{_omf_dest_dir}/gswitchit/gswitchit-fr.omf
%lang(ru) %{_omf_dest_dir}/gswitchit/gswitchit-ru.omf
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
%lang(en_GB) %{_omf_dest_dir}/command-line/command-line-en_GB.omf
%lang(es) %{_omf_dest_dir}/command-line/command-line-es.omf
%lang(fr) %{_omf_dest_dir}/command-line/command-line-fr.omf
%lang(pt_BR) %{_omf_dest_dir}/command-line/command-line-pt_BR.omf
%lang(sv) %{_omf_dest_dir}/command-line/command-line-sv.omf
%lang(uk) %{_omf_dest_dir}/command-line/command-line-uk.omf

%files mixer -f mixer_applet2.lang
%defattr(644,root,root,755)
%doc mixer/ChangeLog
%attr(755,root,root) %{_libdir}/mixer_applet2
%{_libdir}/bonobo/servers/GNOME_MixerApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_MixerApplet.xml
%{_sysconfdir}/gconf/schemas/mixer.schemas
%dir %{_omf_dest_dir}/mixer_applet2
%{_omf_dest_dir}/mixer_applet2/mixer_applet2-C.omf
%lang(ca) %{_omf_dest_dir}//mixer_applet2/mixer_applet2-ca.omf
%lang(en_GB) %{_omf_dest_dir}/mixer_applet2/mixer_applet2-en_GB.omf
%lang(es) %{_omf_dest_dir}/mixer_applet2/mixer_applet2-es.omf
%lang(it) %{_omf_dest_dir}/mixer_applet2/mixer_applet2-it.omf
%lang(fr) %{_omf_dest_dir}/mixer_applet2/mixer_applet2-fr.omf
%lang(pa) %{_omf_dest_dir}/mixer_applet2/mixer_applet2-pa.omf
%lang(ru) %{_omf_dest_dir}/mixer_applet2/mixer_applet2-ru.omf
%lang(sv) %{_omf_dest_dir}/mixer_applet2/mixer_applet2-sv.omf
%lang(uk) %{_omf_dest_dir}/mixer_applet2/mixer_applet2-uk.omf

%files modemlights
%defattr(644,root,root,755)
%doc modemlights/ChangeLog
%attr(755,root,root) %{_libdir}/modem_applet
%{_libdir}/bonobo/servers/GNOME_ModemLights.server
%{_datadir}/gnome-2.0/ui/GNOME_ModemLights.xml
%{_datadir}/%{name}/glade/modemlights.glade
%{_iconsdir}/hicolor/*/apps/gnome-modem-monitor-applet.*

%files multiload -f multiload.lang
%defattr(644,root,root,755)
%doc multiload/ChangeLog
%attr(755,root,root) %{_libdir}/multiload-applet-2
%{_libdir}/bonobo/servers/GNOME_MultiLoadApplet_Factory.server
%{_datadir}/gnome-2.0/ui/GNOME_MultiloadApplet.xml
%{_sysconfdir}/gconf/schemas/multiload.schemas
%dir %{_omf_dest_dir}/multiload
%{_omf_dest_dir}/multiload/multiload-C.omf
%lang(ca) %{_omf_dest_dir}//multiload/multiload-ca.omf
%lang(en_GB) %{_omf_dest_dir}/multiload/multiload-en_GB.omf
%lang(es) %{_omf_dest_dir}/multiload/multiload-es.omf
%lang(fr) %{_omf_dest_dir}/multiload/multiload-fr.omf
%lang(pa) %{_omf_dest_dir}/multiload/multiload-pa.omf
%lang(ru) %{_omf_dest_dir}/multiload/multiload-ru.omf
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
%lang(en_GB) %{_omf_dest_dir}/stickynotes_applet/stickynotes_applet-en_GB.omf
%lang(es) %{_omf_dest_dir}/stickynotes_applet/stickynotes_applet-es.omf
%lang(fr) %{_omf_dest_dir}/stickynotes_applet/stickynotes_applet-fr.omf
%lang(pa) %{_omf_dest_dir}/stickynotes_applet/stickynotes_applet-pa.omf
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
%lang(en_GB) %{_omf_dest_dir}/trashapplet/trashapplet-en_GB.omf
%lang(es) %{_omf_dest_dir}/trashapplet/trashapplet-es.omf
%lang(fr) %{_omf_dest_dir}/trashapplet/trashapplet-fr.omf
%lang(it) %{_omf_dest_dir}/trashapplet/trashapplet-it.omf
%lang(nl) %{_omf_dest_dir}/trashapplet/trashapplet-nl.omf
%lang(pa) %{_omf_dest_dir}/trashapplet/trashapplet-pa.omf
%lang(ru) %{_omf_dest_dir}/trashapplet/trashapplet-ru.omf
%lang(sv) %{_omf_dest_dir}/trashapplet/trashapplet-sv.omf
%lang(uk) %{_omf_dest_dir}/trashapplet/trashapplet-uk.omf
