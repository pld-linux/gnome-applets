Summary:	Small applications which embed themselves in the GNOME panel
Summary(pl.UTF-8):	Aplety GNOME - małe aplikacje osadzające się w panelu
Summary(ru.UTF-8):	Маленькие программы, встраивающиеся в панель GNOME
Summary(uk.UTF-8):	Маленькі програми, що вбудовуються в панель GNOME
Name:		gnome-applets
Version:	3.2.1
Release:	2
Epoch:		1
License:	GPL v2, FDL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-applets/3.2/%{name}-%{version}.tar.xz
# Source0-md5:	bce6d49f3bb2caff8d91c78599ffcfd0
# check paths in Makefile before removing it!
Patch0:		%{name}-m4_fix.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.26.0
BuildRequires:	NetworkManager-devel >= 0.7
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	cpufrequtils-devel >= 0.3
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-dtd43-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.22.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gnome-icon-theme >= 3.0.0
BuildRequires:	gnome-panel-devel >= 3.2.1
BuildRequires:	gnome-settings-daemon-devel >= 3.0.0
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.10
BuildRequires:	gtk+3-devel
BuildRequires:	gucharmap-devel >= 3.2.1
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgtop-devel >= 1:2.22.0
BuildRequires:	libgweather-devel >= 3.0.0
BuildRequires:	libnotify-devel >= 0.7
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 3.0.0
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	libxslt-progs >= 1.1.20
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	polkit-devel >= 0.92
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-pygobject-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper >= 0.3.11-4
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires:	gnome-icon-theme >= 3.0.0
Requires:	gnome-panel >= 3.2.0
Requires:	hicolor-icon-theme
Obsoletes:	gnome-applets-keyboard
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
URL:		http://library.gnome.org/users/accessx-status/stable/
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Suggests:	gnome-control-center >= 2.26.0
Conflicts:	gnome-applets < 0:2.10.0-6

%description accessx-status
The Keyboard Accessibility Monitor shows you the status of the
keyboard accessibility features when these are in use. For example,
you can see which modifier keys are currently active, and which mouse
buttons are being pressed via the keyboard.

%description accessx-status -l pl.UTF-8
Aplet monitora dostępności klawiatury pokazuje stan funkcji
zwiększających dostępność klawiatury, kiedy są włączone. Pozwala
zobaczyć m.in. które klawisze modyfikatorów są aktywne albo które
przyciski myszy są wciskane z poziomu klawiatury.

%package battstat
Summary:	Battery Charge Monitor applet
Summary(pl.UTF-8):	Aplet monitora stanu naładowania akumulatora
Group:		X11/Applications
URL:		http://library.gnome.org/users/battstat/stable/
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets < 0:2.10.0-6

%description battstat
The Battery Charge Monitor shows the status of any batteries in your
laptop computer. The monitor can tell you the capacity remaining both
visually and as a percentage, as well as offer you an estimate of the
time remaining based off the current usage rate.

%description battstat -l pl.UTF-8
Aplet monitora stanu naładowania akumulatora pokazuje stan wszelkich
baterii w laptopie. Monitor informuje o pozostałej pojemności zarówno
w postaci graficznej, jak i procentowej, a także podaje przybliżony
pozostały czas pracy przy założeniu bieżącego użycia prądu.

%package charpicker
Summary:	Character Palette applet
Summary(pl.UTF-8):	Aplet palety znaków
Group:		X11/Applications
URL:		http://library.gnome.org/users/char-palette/stable/
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets < 0:2.10.0-6

%description charpicker
The Character Palette provides a convenient way to access characters
that are not on your keyboard, such as accented characters,
mathematical symbols, special symbols, and punctuation marks.

You can insert characters from the applet into text strings, for
example in text documents or at the command line. You can customize
the contents of the applet to suit your requirements.

Character Palette supports the UTF-8 character encoding so you can use
the palette to display or copy any Unicode character.

%description charpicker -l pl.UTF-8
Aplet palety znaków udostępnia wygodną metodę wprowadzania znaków nie
istniejących na klawiaturze, takich jak znaki akcentowane, symbole
matematyczne, symbole specjalne i znaki przestankowe.

Przy pomocy apletu można wprowadzać znaki do łańcuchów tekstowych, na
przykład w dokumentach tekstowych lub w linii poleceń. Zawartość
apletu można dostosowywać do własnych wymagań.

Paleta znaków obsługuje kodowanie znaków UTF-8, więc można jej używać
do wyświetlania lub kopiowania dowolnych znaków unikodowych.

%package cpufreq
Summary:	CPU Frequency Scaling Monitor applet
Summary(pl.UTF-8):	Aplet monitora częstotliwości procesora
Group:		X11/Applications
URL:		http://library.gnome.org/users/cpufreq-applet/stable/
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	polkit-gnome >= 0.92
Obsoletes:	gnome-applet-cpufreq
Conflicts:	gnome-applets < 0:2.10.0-6

%description cpufreq
The CPU Frequency Scaling Monitor provides a convenient way to monitor
the CPU Frequency Scaling for each CPU.

%description cpufreq -l pl.UTF-8
Aplet monitora częstotliwości procesora umożliwia wygodne
monitorowanie częstotliwości dla każdego procesora.

%package drivemount
Summary:	Disk Mounter applet
Summary(pl.UTF-8):	Aplet do montowania dysków
Group:		X11/Applications
URL:		http://library.gnome.org/users/drivemount/stable/
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets < 0:2.10.0-6

%description drivemount
The Disk Mounter enables you to quickly mount and unmount various
types of drives and file systems.

%description drivemount -l pl.UTF-8
Aplet do montowania dysków, pozwalający szybko montować i odmontowywać
różne rodzaje dysków i systemów plików.

%package geyes
Summary:	Geyes applet - tracking the mouse pointer
Summary(pl.UTF-8):	Aplet geyes - śledzenie wskaźnika myszy
Group:		X11/Applications
URL:		http://library.gnome.org/users/geyes/stable/
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets < 0:2.10.0-6

%description geyes
The Geyes applet provides an entertaining way to track the movement of
the mouse pointer around your screen. The applet is an image of one or
more eyes that follow the mouse pointer around the screen.

%description geyes -l pl.UTF-8
Aplet geyes to zabawny sposób śledzenia ruchu wskaźnika myszy po
ekranie. Aplet jest obrazem jednego lub większej liczby oczu
podążających za wskaźnikiem myszy.

%package gweather
Summary:	Weather Report applet
Summary(pl.UTF-8):	Aplet raportu pogodowego
Group:		X11/Applications
URL:		http://library.gnome.org/users/gweather/stable/
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	dbus(org.freedesktop.Notifications)
Conflicts:	gnome-applets < 0:2.10.0-6

%description gweather
The Weather Report downloads weather information from the U.S.
National Weather Service (NWS) servers, including the Interactive
Weather Information Network (IWIN) and other weather services. You can
use Weather Report to display current weather information and weather
forecasts on your computer.

%description gweather -l pl.UTF-8
Aplet raportu pogodowego ściąga informacje pogodowe z serwerów U.S.
National Weather Service (NWS), wraz z siecią Interactive Weather
Information Network (IWIN) oraz innych serwisów pogodowych. Apletu
można używać do wyświetlania aktualnych informacji pogodowych oraz
prognoz.

%package invest
Summary:	Stock Ticker applet
Summary(pl.UTF-8):	Aplet wskaźnika giełdowego
Group:		X11/Applications
URL:		http://library.gnome.org/users/invest-applet/stable/
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	GConf2-libs
Requires:	gnome-panel-libs >= 3.2.0
Requires:	gobject-introspection
Requires:	python-dbus
Requires:	python-pygobject
Requires:	python-pygtk-gtk
Obsoletes:	gnome-applets-gtik
Conflicts:	gnome-applets < 0:2.10.0-6

%description invest
The Invest GNOME panel applet downloads current stock quotes from
Yahoo! Finance and displays the quotes in a drop-down list.

%description invest -l pl.UTF-8
Aplet wskaźnika giełdowego, ściągający aktualne notowania z serwisu
Yahoo! Finance i wyświetlające je na rozwijanej liście.

%package minicommander
Summary:	Command Line applet
Summary(pl.UTF-8):	Aplet wiersza poleceń
Group:		X11/Applications
URL:		http://library.gnome.org/users/command-line/stable/
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets < 0:2.10.0-6

%description minicommander
The Command Line provides a command line that you can use within any
panel on the desktop.

%description minicommander -l pl.UTF-8
Aplet wiersza poleceń udostępnia linię poleceń z poziomu każdego
panelu na pulpicie.

%package mixer
Summary:	Volume Control applet
Summary(pl.UTF-8):	Aplet regulacji głośności
Group:		X11/Applications
URL:		http://library.gnome.org/users/mixer_applet2/stable/
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gnome-control-center >= 3.2.0
Requires:	gstreamer-audio-effects-base >= 0.10.10
Requires:	gstreamer-audiosink
Conflicts:	gnome-applets < 0:2.10.0-6

%description mixer
The Volume Control applet enables you to control the sound volume on
your system. The applet icon changes depending on the volume level
that you select. For example, if you select a low volume level, the
icon displays one sound wave emanating from the speaker in the applet
icon. As you increase the volume, the icon changes to display more
sound waves.

%description mixer -l pl.UTF-8
Aplet regulacji głośności pozwala sterować głośnością dźwięku. Ikona
apletu zmienia się w zależności od wybranego poziomu głośności. Na
przykład przy niskiej głośności pokazuje pojedynczą falę wydobywającą
się z głośnika; w miarę zwiększania głośności ikona wyświetla coraz
więcej fal.

%package multiload
Summary:	System Monitor applet
Summary(pl.UTF-8):	Aplet monitora systemu
Group:		X11/Applications
URL:		http://library.gnome.org/users/multiload/stable/
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Suggests:	gnome-system-monitor >= 2.24.0
Conflicts:	gnome-applets < 0:2.10.0-6

%description multiload
The System Monitor displays system load information in graphical
format in a panel.

%description multiload -l pl.UTF-8
Aplet monitora systemu wyświetla w panelu informacje o obciążeniu
systemu w postaci graficznej.

%package stickynotes
Summary:	Sticky Notes applet
Summary(pl.UTF-8):	Aplet notatek
Group:		X11/Applications
URL:		http://library.gnome.org/users/stickynotes_applet/stable/
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	gnotes_applet
Conflicts:	gnome-applets < 0:2.10.0-6

%description stickynotes
The Sticky Notes panel application enables you to create, view, and
manage sticky notes on your desktop. You can edit the title, contents,
dimensions, and style of sticky notes. When the panel is restarted,
for example when you log out and log in again, all sticky notes are
saved and reopened in the same position with the same dimensions and
style.

%description stickynotes -l pl.UTF-8
Aplet notatek pozwala na tworzenie, oglądanie i zarządzanie
przyczepianymi notatkami na pulpicie. Pozwala modyfikować tytuł,
treść, wymiary i styl notatek. Przy restarcie panelu, na przykład przy
wylogowaniu i ponownym zalogowaniu, wszystkie notatki są zapisywane, a
następnie otwierane ponownie w tym samym miejscu, z tymi samymi
wymiarami i stylem.

%package trash
Summary:	Trash applet
Summary(pl.UTF-8):	Aplet śmietnika
Group:		X11/Applications
URL:		http://library.gnome.org/users/trashapplet/stable/
Requires(post,postun):	scrollkeeper
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	gnome-applets < 0:2.10.0-6

%description trash
The Panel Trash applet lets you manage your Trash from the panel.

The trash on your panel acts identically to the trash on your desktop,
however it is useful because your panels are always visible.

%description trash -l pl.UTF-8
Aplet śmietnika pozwala na zarządzanie śmietnikiem z poziomu panelu.

Śmietnik w panelu zachowuje się tak samo, jak śmietnik na pulpicie,
ale jest przydatny o tyle, że panele są zawsze widoczne.

%prep
%setup -q
%patch0 -p1

%build
%{__gnome_doc_prepare}
%{__gnome_doc_common}
%{__libtoolize}
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--without-hal \
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

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/invest/*.py

# es_ES is more complete copy
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/es{_ES,}/LC_MESSAGES/*.mo
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/es_ES

# keyboard applet has been removed
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/xmodmap

%find_lang %{name}-3.0
%find_lang accessx-status --with-gnome --with-omf
%find_lang battstat --with-gnome --with-omf
%find_lang char-palette --with-gnome --with-omf
%find_lang command-line --with-gnome --with-omf
%find_lang cpufreq-applet --with-gnome --with-omf
%find_lang drivemount --with-gnome --with-omf
%find_lang geyes --with-gnome --with-omf
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

%files -f %{name}-3.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/null_applet
%{_datadir}/dbus-1/services/org.gnome.panel.applet.NullAppletFactory.service
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.NullApplet.panel-applet
%dir %{_libdir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/builder
%dir %{_datadir}/%{name}/ui
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
%attr(755,root,root) %{_libdir}/accessx-status-applet
%{_datadir}/dbus-1/services/org.gnome.panel.applet.AccessxStatusAppletFactory.service
%{_datadir}/gnome-applets/ui/accessx-status-applet-menu.xml
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.AccessxStatusApplet.panel-applet
%{_pixmapsdir}/accessx-status-applet
%{_iconsdir}/hicolor/48x48/apps/ax-applet.png

%files battstat -f battstat.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/battstat-applet-2
%{_datadir}/dbus-1/services/org.gnome.panel.applet.BattstatAppletFactory.service
%{_datadir}/gnome-applets/ui/battstat-applet-menu.xml
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.BattstatApplet.panel-applet
%{_datadir}/%{name}/builder/battstat_applet.ui
%{_sysconfdir}/gconf/schemas/battstat.schemas
%{_sysconfdir}/sound/events/battstat_applet.soundlist

%files charpicker -f char-palette.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/charpick_applet2
%{_datadir}/dbus-1/services/org.gnome.panel.applet.CharpickerAppletFactory.service
%{_datadir}/gnome-applets/ui/charpick-applet-menu.xml
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.CharpickerApplet.panel-applet
%{_sysconfdir}/gconf/schemas/charpick.schemas

%files cpufreq -f cpufreq-applet.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cpufreq-selector
%attr(755,root,root) %{_libdir}/cpufreq-applet
%{_datadir}/dbus-1/services/org.gnome.panel.applet.CPUFreqAppletFactory.service
%{_datadir}/dbus-1/system-services/org.gnome.CPUFreqSelector.service
%{_datadir}/gnome-applets/ui/cpufreq-applet-menu.xml
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.CPUFreqApplet.panel-applet
%{_datadir}/polkit-1/actions/org.gnome.cpufreqselector.policy
%{_datadir}/%{name}/builder/cpufreq-preferences.ui
/etc/dbus-1/system.d/org.gnome.CPUFreqSelector.conf
%{_sysconfdir}/gconf/schemas/cpufreq-applet.schemas
%{_pixmapsdir}/cpufreq-applet
%{_iconsdir}/hicolor/*/apps/gnome-cpu-frequency-applet.*

%files drivemount -f drivemount.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/drivemount_applet2
%{_datadir}/dbus-1/services/org.gnome.panel.applet.DriveMountAppletFactory.service
%{_datadir}/gnome-applets/ui/drivemount-applet-menu.xml
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.DriveMountApplet.panel-applet
%{_sysconfdir}/gconf/schemas/drivemount.schemas

%files geyes -f geyes.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/geyes_applet2
%{_datadir}/dbus-1/services/org.gnome.panel.applet.GeyesAppletFactory.service
%{_datadir}/gnome-applets/ui/geyes-applet-menu.xml
%{_datadir}/%{name}/geyes
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.GeyesApplet.panel-applet
%{_iconsdir}/hicolor/*/apps/gnome-eyes-applet.*
%{_sysconfdir}/gconf/schemas/geyes.schemas

%files gweather -f gweather.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gweather-applet-2
%{_datadir}/dbus-1/services/org.gnome.panel.applet.GWeatherAppletFactory.service
%{_datadir}/gnome-applets/ui/gweather-applet-menu.xml
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.GWeatherApplet.panel-applet

%files invest -f invest-applet.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/invest-chart
%attr(755,root,root) %{_libdir}/invest-applet
%{_datadir}/dbus-1/services/org.gnome.panel.applet.InvestAppletFactory.service
%{_datadir}/gnome-applets/ui/invest-applet-menu.xml
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.InvestApplet.panel-applet
%{_datadir}/%{name}/builder/financialchart.ui
%{_datadir}/%{name}/builder/prefs-dialog.ui
%{_datadir}/%{name}/invest-applet
%{_iconsdir}/hicolor/*/apps/invest-applet.*
%dir %{py_sitedir}/invest
%{py_sitedir}/invest/*.py[co]

%files minicommander -f command-line.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mini_commander_applet
%attr(755,root,root) %{_libdir}/%{name}/mc-install-default-macros
%{_datadir}/dbus-1/services/org.gnome.panel.applet.MiniCommanderAppletFactory.service
%{_datadir}/gnome-applets/ui/mini-commander-applet-menu.xml
%{_datadir}/%{name}/builder/mini-commander.ui
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.MiniCommanderApplet.panel-applet
%{_iconsdir}/hicolor/48x48/apps/gnome-mini-commander.png
%{_sysconfdir}/gconf/schemas/mini-commander-global.schemas
%{_sysconfdir}/gconf/schemas/mini-commander.schemas

%files mixer -f mixer_applet2.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mixer_applet2
%{_datadir}/dbus-1/services/org.gnome.panel.applet.MixerAppletFactory.service
%{_datadir}/gnome-applets/ui/mixer-applet-menu.xml
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.MixerApplet.panel-applet
%{_sysconfdir}/gconf/schemas/mixer.schemas

%files multiload -f multiload.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/multiload-applet-2
%{_datadir}/dbus-1/services/org.gnome.panel.applet.MultiLoadAppletFactory.service
%{_datadir}/gnome-applets/ui/multiload-applet-menu.xml
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.MultiLoadApplet.panel-applet
%{_sysconfdir}/gconf/schemas/multiload.schemas

%files stickynotes -f stickynotes_applet.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/stickynotes_applet
%{_datadir}/dbus-1/services/org.gnome.panel.applet.StickyNotesAppletFactory.service
%{_datadir}/gnome-applets/ui/stickynotes-applet-menu.xml
%{_datadir}/%{name}/builder/stickynotes.ui
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.StickyNotesApplet.panel-applet
%{_pixmapsdir}/stickynotes
%{_iconsdir}/hicolor/*/apps/gnome-sticky-notes-applet.*
%{_sysconfdir}/gconf/schemas/stickynotes.schemas

%files trash -f trashapplet.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/trashapplet
%{_datadir}/dbus-1/services/org.gnome.panel.applet.TrashAppletFactory.service
%{_datadir}/%{name}/builder/trashapplet-empty-progress.ui
%{_datadir}/gnome-applets/ui/trashapplet-menu.xml
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.TrashApplet.panel-applet
