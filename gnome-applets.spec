# TODO:
# - libnotify dependency (just a toy)
#
Summary:	Small applications which embed themselves in the GNOME panel
Summary(pl):	Aplety GNOME - ma³e aplikacje osadzaj±ce siê w panelu
Summary(ru):	íÁÌÅÎØËÉÅ ÐÒÏÇÒÁÍÍÙ, ×ÓÔÒÁÉ×ÁÀÝÉÅÓÑ × ÐÁÎÅÌØ GNOME
Summary(uk):	íÁÌÅÎØË¦ ÐÒÏÇÒÁÍÉ, ÝÏ ×ÂÕÄÏ×ÕÀÔØÓÑ × ÐÁÎÅÌØ GNOME
Name:		gnome-applets
Version:	2.11.92.1
Release:	1
Epoch:		1
License:	GPL v2, FDL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-applets/2.11/%{name}-%{version}.tar.bz2
# Source0-md5:	035684af82060eb19af881d70a822478
Patch0:		%{name}-stickynotes-title-size.patch
Patch1:		%{name}-m4_fix.patch
Patch2:		%{name}-pangoxft_fix.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.10.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gail-devel >= 1.8.2
BuildRequires:	gdbm-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.8.0-2
BuildRequires:	gnome-doc-utils >= 0.3.2
BuildRequires:	gnome-panel-devel >= 2.10.0-2
BuildRequires:	gnome-vfs2-devel >= 2.10.0-2
BuildRequires:	gstreamer-plugins-devel >= 0.8.8
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	gucharmap-devel >= 1.4.0
BuildRequires:	intltool >= 0.33
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgtop-devel >= 1:2.11.92
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.11.91
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
gnome-doc-prepare --copy --force
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
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --all-name --with-gnome
%find_lang char-palette --with-gnome
%find_lang drivemount --with-gnome
%find_lang geyes --with-gnome
%find_lang command-line --with-gnome
%find_lang stickynotes_applet --with-gnome
%find_lang mixer_applet2 --with-gnome
%find_lang multiload --with-gnome
%find_lang gtik2_applet2 --with-gnome
%find_lang gweather --with-gnome
%find_lang trashapplet --with-gnome
%find_lang battstat --with-gnome
%find_lang accessx-status --with-gnome
%find_lang gswitchit --with-gnome
%find_lang cpufreq-applet --with-gnome

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/null_applet
%{_libdir}/bonobo/servers/GNOME_CDPlayerApplet.server
%{_libdir}/bonobo/servers/GNOME_MailcheckApplet_Factory.server
%{_libdir}/bonobo/servers/GNOME_NullApplet_Factory.server
%{_libdir}/bonobo/servers/GNOME_Panel_WirelessApplet.server
%dir %{_datadir}/%{name}/glade
%dir %{_libdir}/%{name}
%dir %{_datadir}/%{name}

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
%{_omf_dest_dir}/accessx-status/accessx-status-C.omf
%lang(es) %{_omf_dest_dir}/accessx-status/accessx-status-es.omf

%files battstat -f battstat.lang
%defattr(644,root,root,755)
%doc battstat/ChangeLog
%attr(755,root,root) %{_libdir}/battstat-applet-2
%{_libdir}/bonobo/servers/GNOME_BattstatApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_BattstatApplet.xml
%{_datadir}/%{name}/glade/battstat_applet.glade
%{_sysconfdir}/gconf/schemas/battstat.schemas
%{_sysconfdir}/sound/events/battstat_applet.soundlist
%{_omf_dest_dir}/battstat/battstat-C.omf

%files charpicker -f char-palette.lang
%defattr(644,root,root,755)
%doc charpick/ChangeLog
%attr(755,root,root) %{_libdir}/charpick_applet2
%{_libdir}/bonobo/servers/GNOME_CharpickerApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_CharpickerApplet.xml
%{_iconsdir}/hicolor/48x48/apps/charpick.png
%{_sysconfdir}/gconf/schemas/charpick.schemas
%{_omf_dest_dir}/char-palette/char-palette-C.omf
%lang(es) %{_omf_dest_dir}/char-palette/char-palette-es.omf
%lang(nl) %{_omf_dest_dir}/char-palette/char-palette-nl.omf

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
%{_iconsdir}/hicolor/48x48/apps/gnome-cpu.png
%{_omf_dest_dir}/cpufreq-applet/cpufreq-applet-C.omf
%lang(es) %{_omf_dest_dir}/cpufreq-applet/cpufreq-applet-es.omf

%files drivemount -f drivemount.lang
%defattr(644,root,root,755)
%doc drivemount/ChangeLog
%attr(755,root,root) %{_libdir}/drivemount_applet2
%{_libdir}/bonobo/servers/GNOME_DriveMountApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_DriveMountApplet.xml
%{_sysconfdir}/gconf/schemas/drivemount.schemas
%{_omf_dest_dir}/drivemount/drivemount-C.omf
%lang(es) %{_omf_dest_dir}/drivemount/drivemount-es.omf

%files geyes -f geyes.lang
%defattr(644,root,root,755)
%doc geyes/ChangeLog
%attr(755,root,root) %{_libdir}/geyes_applet2
%{_libdir}/bonobo/servers/GNOME_GeyesApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_GeyesApplet.xml
%{_datadir}/%{name}/geyes
%{_iconsdir}/hicolor/48x48/apps/gnome-eyes.png
%{_sysconfdir}/gconf/schemas/geyes.schemas
%{_omf_dest_dir}/geyes/geyes-C.omf
%lang(es) %{_omf_dest_dir}/geyes/geyes-es.omf

%files gtik -f gtik2_applet2.lang
%defattr(644,root,root,755)
%doc gtik/ChangeLog
%attr(755,root,root) %{_libdir}/gtik2_applet2
%{_libdir}/bonobo/servers/GNOME_GtikApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_GtikApplet.xml
%{_iconsdir}/hicolor/48x48/apps/gnome-money.png
%{_sysconfdir}/gconf/schemas/gtik.schemas
%{_omf_dest_dir}/gtik2_applet2/gtik2_applet2-C.omf
%lang(es) %{_omf_dest_dir}/gtik2_applet2/gtik2_applet2-es.omf

%files gweather -f gweather.lang
%defattr(644,root,root,755)
%doc gweather/ChangeLog
%attr(755,root,root) %{_libdir}/gweather-applet-2
%{_libdir}/bonobo/servers/GNOME_GWeatherApplet_Factory.server
%{_datadir}/gnome-2.0/ui/GNOME_GWeatherApplet.xml
%{_datadir}/%{name}/gweather
%{_sysconfdir}/gconf/schemas/gweather.schemas
%{_omf_dest_dir}/gweather/gweather-C.omf
%lang(es) %{_omf_dest_dir}/gweather/gweather-es.omf

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
%attr(755,root,root) %{_bindir}/gswitchit-plugins-capplet
%{_datadir}/gnome-2.0/ui/GNOME_GSwitchItApplet.xml
%{_datadir}/%{name}/glade/gswitchit*.glade
%{_iconsdir}/hicolor/48x48/apps/gswitchit*.png
%{_sysconfdir}/gconf/schemas/gswitchit.schemas
%{_omf_dest_dir}/gswitchit/gswitchit-C.omf
%lang(es) %{_omf_dest_dir}/gswitchit/gswitchit-es.omf

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
%{_omf_dest_dir}/command-line/command-line-C.omf
%lang(es) %{_omf_dest_dir}/command-line/command-line-es.omf

%files mixer
%defattr(644,root,root,755)
%doc mixer/ChangeLog
%attr(755,root,root) %{_libdir}/mixer_applet2
%{_libdir}/bonobo/servers/GNOME_MixerApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_MixerApplet.xml
%{_sysconfdir}/gconf/schemas/mixer.schemas
%{_omf_dest_dir}/mixer_applet2/mixer_applet2-C.omf
%lang(es) %{_omf_dest_dir}/mixer_applet2/mixer_applet2-es.omf

%files modemlights
%defattr(644,root,root,755)
%doc modemlights/ChangeLog
%attr(755,root,root) %{_libdir}/modem_applet
%{_libdir}/bonobo/servers/GNOME_ModemLights.server
%{_datadir}/gnome-2.0/ui/GNOME_ModemLights.xml
%{_datadir}/%{name}/glade/modemlights.glade
%{_iconsdir}/hicolor/48x48/apps/gnome-modem.png

%files multiload -f multiload.lang
%defattr(644,root,root,755)
%doc multiload/ChangeLog
%attr(755,root,root) %{_libdir}/multiload-applet-2
%{_libdir}/bonobo/servers/GNOME_MultiLoadApplet_Factory.server
%{_datadir}/gnome-2.0/ui/GNOME_MultiloadApplet.xml
%{_sysconfdir}/gconf/schemas/multiload.schemas
%{_omf_dest_dir}/multiload/multiload-C.omf
%lang(es) %{_omf_dest_dir}/multiload/multiload-es.omf

%files stickynotes -f stickynotes_applet.lang
%defattr(644,root,root,755)
%doc stickynotes/ChangeLog
%attr(755,root,root) %{_libdir}/stickynotes_applet
%{_libdir}/bonobo/servers/GNOME_StickyNotesApplet.server
%{_datadir}/gnome-2.0/ui/GNOME_StickyNotesApplet.xml
%{_datadir}/%{name}/glade/stickynotes.glade
%{_pixmapsdir}/stickynotes
%{_sysconfdir}/gconf/schemas/stickynotes.schemas
%{_omf_dest_dir}/stickynotes_applet/stickynotes_applet-C.omf
%lang(es) %{_omf_dest_dir}/stickynotes_applet/stickynotes_applet-es.omf

%files trash -f trashapplet.lang
%defattr(644,root,root,755)
%doc trashapplet/ChangeLog
%attr(755,root,root) %{_libdir}/trashapplet
%{_libdir}/bonobo/servers/GNOME_Panel_TrashApplet.server
%{_datadir}/%{name}/glade/trashapplet.glade
%{_datadir}/gnome-2.0/ui/GNOME_Panel_TrashApplet.xml
%{_omf_dest_dir}/trashapplet/trashapplet-C.omf
%lang(es) %{_omf_dest_dir}/trashapplet/trashapplet-es.omf
%lang(pa) %{_omf_dest_dir}/trashapplet/trashapplet-pa.omf
