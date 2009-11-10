Summary:	Small applications which embed themselves in the GNOME panel
Summary(pl.UTF-8):	Aplety GNOME - małe aplikacje osadzające się w panelu
Summary(ru.UTF-8):	Маленькие программы, встраивающиеся в панель GNOME
Summary(uk.UTF-8):	Маленькі програми, що вбудовуються в панель GNOME
Name:		gnome-applets
Version:	2.28.0
Release:	3
Epoch:		1
License:	GPL v2, FDL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-applets/2.28/%{name}-%{version}.tar.bz2
# Source0-md5:	9eb00e9dc468d2c5c71b70c9fb2b751c
# check paths in Makefile before removing it!
Patch0:		%{name}-m4_fix.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.26.0
BuildRequires:	NetworkManager-devel >= 0.7
BuildRequires:	PolicyKit-gnome-devel >= 0.7
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	cpufrequtils-devel >= 0.3
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.20.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-desktop-devel >= 2.26.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gnome-icon-theme >= 2.26.0
BuildRequires:	gnome-panel-devel >= 2.26.0
BuildRequires:	gnome-settings-daemon-devel >= 2.26.0
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.10
BuildRequires:	gtk+2-devel >= 2:2.16.0
BuildRequires:	gucharmap-devel >= 2.26.0
BuildRequires:	hal-devel >= 0.5.10
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgnomekbd-devel >= 2.24.0
BuildRequires:	libgtop-devel >= 1:2.22.0
BuildRequires:	libgweather-devel >= 2.26.0
BuildRequires:	libnotify-devel >= 0.4.4
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.26.0
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	libxslt-progs >= 1.1.20
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-gnome-desktop-devel
BuildRequires:	python-gnome-devel >= 2.22.0
BuildRequires:	python-pygtk-devel >= 2:2.14.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper >= 0.3.11-4
Requires:	gnome-icon-theme >= 2.26.0
Requires:	gnome-panel >= 2.26.0
Requires:	hicolor-icon-theme
Obsoletes:	gnome-applets-modemlights
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package accessx-status
Summary:	Keyboard Accessibility Status applet
Summary(pl.UTF-8):	Aplet stanu dostepności klawiatury
Group:		X11/Applications
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Suggests:	gnome-control-center >= 2.26.0
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
Requires:	dbus(org.freedesktop.Notifications)
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
Suggests:	gnome-media-volume-control >= 2.22.0
Conflicts:	gnome-applets <= 0:2.10.0-5

%description mixer
Volume Control applet.

%description mixer -l pl.UTF-8
Aplet regulacji głośności.

%package multiload
Summary:	System Monitor applet
Summary(pl.UTF-8):	Aplet monitora systemu
Group:		X11/Applications
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Suggests:	gnome-system-monitor >= 2.24.0
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
	--enable-mixer-applet
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
%find_lang accessx-status --with-gnome --with-omf
%find_lang battstat --with-gnome --with-omf
%find_lang char-palette --with-gnome --with-omf
%find_lang command-line --with-gnome --with-omf
%find_lang cpufreq-applet --with-gnome --with-omf
%find_lang drivemount --with-gnome --with-omf
%find_lang geyes --with-gnome --with-omf
%find_lang gswitchit --with-gnome --with-omf
%find_lang gweather --with-gnome --with-omf
%find_lang invest-applet --with-gnome --with-omf
%find_lang mixer_applet2 --with-gnome --with-omf
%find_lang multiload --with-gnome --with-omf
%find_lang stickynotes_applet --with-gnome --with-omf
%find_lang trashapplet --with-gnome --with-omf

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

%postun gweather
/sbin/ldconfig
%scrollkeeper_update_postun

%post invest
%scrollkeeper_update_post
%update_icon_cache hicolor

%postun invest
%scrollkeeper_update_postun
%update_icon_cache hicolor

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
%dir %{_datadir}/%{name}/builder
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

%files accessx-status -f accessx-status.lang
%defattr(644,root,root,755)
#%doc accessx-status/ChangeLog
%attr(755,root,root) %{_libdir}/accessx-status-applet
%{_libdir}/bonobo/servers/GNOME_AccessxStatusApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_AccessxApplet.xml
%{_pixmapsdir}/accessx-status-applet
%{_iconsdir}/hicolor/48x48/apps/ax-applet.png

%files battstat -f battstat.lang
%defattr(644,root,root,755)
#%doc battstat/ChangeLog
%attr(755,root,root) %{_libdir}/battstat-applet-2
%{_libdir}/bonobo/servers/GNOME_BattstatApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_BattstatApplet.xml
%{_datadir}/%{name}/builder/battstat_applet.ui
%{_sysconfdir}/gconf/schemas/battstat.schemas
%{_sysconfdir}/sound/events/battstat_applet.soundlist

%files charpicker -f char-palette.lang
%defattr(644,root,root,755)
#%doc charpick/ChangeLog
%attr(755,root,root) %{_libdir}/charpick_applet2
%{_libdir}/bonobo/servers/GNOME_CharpickerApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_CharpickerApplet.xml
%{_sysconfdir}/gconf/schemas/charpick.schemas

%files cpufreq -f cpufreq-applet.lang
%defattr(644,root,root,755)
#%doc cpufreq/ChangeLog
%attr(755,root,root) %{_bindir}/cpufreq-selector
%attr(755,root,root) %{_libdir}/cpufreq-applet
%{_libdir}/bonobo/servers/GNOME_CPUFreqApplet.server
#%{_datadir}/PolicyKit/policy/org.gnome.cpufreqselector.policy
%{_datadir}/dbus-1/system-services/org.gnome.CPUFreqSelector.service
%{_datadir}/gnome-2.0/ui/GNOME_CPUFreqApplet.xml
%{_datadir}/%{name}/builder/cpufreq-preferences.ui
%{_sysconfdir}/dbus-1/system.d/org.gnome.CPUFreqSelector.conf
%{_sysconfdir}/gconf/schemas/cpufreq-applet.schemas
%{_pixmapsdir}/cpufreq-applet
%{_iconsdir}/hicolor/*/apps/gnome-cpu-frequency-applet.*

%files drivemount -f drivemount.lang
%defattr(644,root,root,755)
#%doc drivemount/ChangeLog
%attr(755,root,root) %{_libdir}/drivemount_applet2
%{_libdir}/bonobo/servers/GNOME_DriveMountApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_DriveMountApplet.xml
%{_sysconfdir}/gconf/schemas/drivemount.schemas

%files geyes -f geyes.lang
%defattr(644,root,root,755)
#%doc geyes/ChangeLog
%attr(755,root,root) %{_libdir}/geyes_applet2
%{_libdir}/bonobo/servers/GNOME_GeyesApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_GeyesApplet.xml
%{_datadir}/%{name}/geyes
%{_iconsdir}/hicolor/*/apps/gnome-eyes-applet.*
%{_sysconfdir}/gconf/schemas/geyes.schemas

%files gweather -f gweather.lang
%defattr(644,root,root,755)
#%doc gweather/ChangeLog
%attr(755,root,root) %{_libdir}/gweather-applet-2
%{_libdir}/bonobo/servers/GNOME_GWeatherApplet_Factory.server
%{_datadir}/gnome-2.0/ui/GNOME_GWeatherApplet.xml

%files invest -f invest-applet.lang
%defattr(644,root,root,755)
#%doc invest-applet/ChangeLog
%attr(755,root,root) %{_bindir}/invest-chart
%attr(755,root,root) %{_libdir}/invest-applet
%{_libdir}/bonobo/servers/GNOME_GtikApplet.server
%{_libdir}/bonobo/servers/Invest_Applet.server
%{_datadir}/gnome-2.0/ui/Invest_Applet.xml
%{_datadir}/%{name}/builder/financialchart.ui
%{_datadir}/%{name}/builder/prefs-dialog.ui
%{_datadir}/%{name}/invest-applet
%{_iconsdir}/hicolor/*/apps/invest-applet.*
%dir %{py_sitedir}/invest
%{py_sitedir}/invest/*.py[co]

%files keyboard -f gswitchit.lang
%defattr(644,root,root,755)
#%doc gswitchit/ChangeLog
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
%{_datadir}/%{name}/builder/gswitchit*.ui

%files minicommander -f command-line.lang
%defattr(644,root,root,755)
#%doc mini-commander/ChangeLog
%attr(755,root,root) %{_libdir}/mini_commander_applet
%attr(755,root,root) %{_libdir}/%{name}/mc-install-default-macros
%{_libdir}/bonobo/servers/GNOME_MiniCommanderApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_MiniCommanderApplet.xml
%{_datadir}/%{name}/builder/mini-commander.ui
%{_iconsdir}/hicolor/48x48/apps/gnome-mini-commander.png
%{_sysconfdir}/gconf/schemas/mini-commander-global.schemas
%{_sysconfdir}/gconf/schemas/mini-commander.schemas

%files mixer -f mixer_applet2.lang
%defattr(644,root,root,755)
#%doc mixer/ChangeLog
%attr(755,root,root) %{_libdir}/mixer_applet2
%{_libdir}/bonobo/servers/GNOME_MixerApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_MixerApplet.xml
%{_sysconfdir}/gconf/schemas/mixer.schemas

%files multiload -f multiload.lang
%defattr(644,root,root,755)
#%doc multiload/ChangeLog
%attr(755,root,root) %{_libdir}/multiload-applet-2
%{_libdir}/bonobo/servers/GNOME_MultiLoadApplet_Factory.server
%{_datadir}/gnome-2.0/ui/GNOME_MultiloadApplet.xml
%{_sysconfdir}/gconf/schemas/multiload.schemas

%files stickynotes -f stickynotes_applet.lang
%defattr(644,root,root,755)
#%doc stickynotes/ChangeLog
%attr(755,root,root) %{_libdir}/stickynotes_applet
%{_libdir}/bonobo/servers/GNOME_StickyNotesApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_StickyNotesApplet.xml
%{_datadir}/%{name}/builder/stickynotes.ui
%{_pixmapsdir}/stickynotes
%{_iconsdir}/hicolor/*/apps/gnome-sticky-notes-applet.*
%{_sysconfdir}/gconf/schemas/stickynotes.schemas

%files trash -f trashapplet.lang
%defattr(644,root,root,755)
#%doc trashapplet/ChangeLog
%attr(755,root,root) %{_libdir}/trashapplet
%{_libdir}/bonobo/servers/GNOME_Panel_TrashApplet.server
%{_datadir}/%{name}/builder/trashapplet-empty-progress.ui
%{_datadir}/gnome-2.0/ui/GNOME_Panel_TrashApplet.xml
