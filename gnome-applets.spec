%define	glib2_ver	1:2.44.0
%define	gtk3_ver	3.15.2
Summary:	Small applications which embed themselves in the GNOME panel
Summary(pl.UTF-8):	Aplety GNOME - małe aplikacje osadzające się w panelu
Summary(ru.UTF-8):	Маленькие программы, встраивающиеся в панель GNOME
Summary(uk.UTF-8):	Маленькі програми, що вбудовуються в панель GNOME
Name:		gnome-applets
Version:	3.18.2
Release:	1
Epoch:		1
License:	GPL v2, FDL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-applets/3.18/%{name}-%{version}.tar.xz
# Source0-md5:	5d4e85d820abefd4298a7470f1234682
URL:		http://www.gnome.org/
BuildRequires:	adwaita-icon-theme >= 3.14.0
%ifarch %{ix86} arm mips ppc sh
BuildRequires:	apmd-devel
%endif
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.13
BuildRequires:	cpupowerutils-devel
BuildRequires:	dbus-devel >= 1.1.2
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-dtd43-xml
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= %{glib2_ver}
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-panel-devel >= 3.18.0
BuildRequires:	gnome-settings-daemon-devel >= 3.0.0
BuildRequires:	gtk+3-devel >= %{gtk3_ver}
BuildRequires:	gucharmap-devel >= 3.2.1
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgtop-devel >= 1:2.22.0
BuildRequires:	libgweather-devel >= 3.17.1
BuildRequires:	libiw-devel >= 28
BuildRequires:	libnotify-devel >= 0.7
BuildRequires:	libtool >= 2:2
BuildRequires:	libwnck-devel >= 3.0.0
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	libxslt-progs >= 1.1.20
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	polkit-devel >= 0.92
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-pygobject3-devel >= 3.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
BuildRequires:	tracker-devel >= 1.0
BuildRequires:	upower-devel >= 0.9.4
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires:	adwaita-icon-theme >= 3.14.0
Requires:	gnome-panel >= 3.18.0
Obsoletes:	gnome-applets-keyboard
Obsoletes:	gnome-applets-mixer
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
URL:		https://help.gnome.org/users/accessx-status/stable/
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2 >= %{glib2_ver}
Requires:	gtk+3 >= %{gtk3_ver}
Requires:	hicolor-icon-theme
Suggests:	gnome-control-center >= 2.26.0

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
URL:		https://help.gnome.org/users/battstat/stable/
Requires(post,postun):	glib2 >= %{glib2_ver}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2 >= %{glib2_ver}
Requires:	gtk+3 >= %{gtk3_ver}
Requires:	libnotify >= 0.7
Requires:	upower >= 0.9.4

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

%package brightness
Summary:	Brightness applet
Summary(pl.UTF-8):	Aplet jasności
Group:		X11/Applications
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2 >= %{glib2_ver}
Requires:	gtk+3 >= %{gtk3_ver}
Requires:	hicolor-icon-theme

%description brightness
Brightness applet adjusts laptop panel brightness.

%description brightness -l pl.UTF-8
Aplet jasności dopasowuje jasność wyświetlacza laptopa.

%package charpicker
Summary:	Character Palette applet
Summary(pl.UTF-8):	Aplet palety znaków
Group:		X11/Applications
URL:		https://help.gnome.org/users/char-palette/stable/
Requires(post,postun):	glib2 >= %{glib2_ver}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2 >= %{glib2_ver}
Requires:	gtk+3 >= %{gtk3_ver}
Requires:	gucharmap >= 3.2.1

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
URL:		https://help.gnome.org/users/cpufreq-applet/stable/
Requires(post,postun):	glib2 >= %{glib2_ver}
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	dbus-glib >= 0.74
Requires:	glib2 >= %{glib2_ver}
Requires:	gtk+3 >= %{gtk3_ver}
Requires:	hicolor-icon-theme
Requires:	polkit >= 0.92
Obsoletes:	gnome-applet-cpufreq

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
URL:		https://help.gnome.org/users/drivemount/stable/
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2 >= %{glib2_ver}
Requires:	gtk+3 >= %{gtk3_ver}

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
URL:		https://help.gnome.org/users/geyes/stable/
Requires(post,postun):	glib2 >= %{glib2_ver}
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2 >= %{glib2_ver}
Requires:	gtk+3 >= %{gtk3_ver}
Requires:	hicolor-icon-theme

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
URL:		https://help.gnome.org/users/gweather/stable/
Requires(post,postun):	glib2 >= %{glib2_ver}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	dbus(org.freedesktop.Notifications)
Requires:	glib2 >= %{glib2_ver}
Requires:	gtk+3 >= %{gtk3_ver}
Requires:	libgweather >= 3.17.1
Requires:	libnotify >= 0.7

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

%package inhibit
Summary:	Inhibit applet
Summary(pl.UTF-8):	Aplet wyłączania
Group:		X11/Applications
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2 >= %{glib2_ver}
Requires:	gtk+3 >= %{gtk3_ver}
Requires:	hicolor-icon-theme

%description inhibit
Inhibit applet allows user to inhibit automatic power saving.

%description inhibit -l pl.UTF-8
Aplet wyłączania pozwala użytkownikowi na wyłączenie automatycznego
oszczędzania zasilania.

%package invest
Summary:	Stock Ticker applet
Summary(pl.UTF-8):	Aplet wskaźnika giełdowego
Group:		X11/Applications
URL:		https://help.gnome.org/users/invest-applet/stable/
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2 >= %{glib2_ver}
Requires:	gobject-introspection
Requires:	gtk+3 >= %{gtk3_ver}
Requires:	hicolor-icon-theme
Requires:	python3-dbus
Requires:	python3-pygobject3 >= 3.0
Obsoletes:	gnome-applets-gtik

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
URL:		https://help.gnome.org/users/command-line/stable/
Requires(post,postun):	glib2 >= %{glib2_ver}
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2 >= %{glib2_ver}
Requires:	gtk+3 >= %{gtk3_ver}
Requires:	hicolor-icon-theme

%description minicommander
The Command Line provides a command line that you can use within any
panel on the desktop.

%description minicommander -l pl.UTF-8
Aplet wiersza poleceń udostępnia linię poleceń z poziomu każdego
panelu na pulpicie.

%package modemlights
Summary:	Modem Lights applet
Summary(pl.UTF-8):	Aplet kontrolek modemu
Group:		X11/Applications
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2 >= %{glib2_ver}
Requires:	gtk+3 >= %{gtk3_ver}
Requires:	hicolor-icon-theme
Requires:	libxml2 >= 1:2.6.30

%description modemlights
Modem Lights applet.

%description modemlights -l pl.UTF-8
Aplet kontrolek modemu.

%package multiload
Summary:	System Monitor applet
Summary(pl.UTF-8):	Aplet monitora systemu
Group:		X11/Applications
URL:		https://help.gnome.org/users/multiload/stable/
Requires(post,postun):	glib2 >= %{glib2_ver}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2 >= %{glib2_ver}
Requires:	gtk+3 >= %{gtk3_ver}
Requires:	libgtop >= 1:2.22.0
Suggests:	gnome-system-monitor >= 2.24.0

%description multiload
The System Monitor displays system load information in graphical
format in a panel.

%description multiload -l pl.UTF-8
Aplet monitora systemu wyświetla w panelu informacje o obciążeniu
systemu w postaci graficznej.

%package netspeed
Summary:	Applet to show how much traffic occurs on a network device
Summary(pl.UTF-8):	Aplet pokazujący wielkość ruchu występującego na urządzeniu sieciowym
Group:		X11/Applications
Requires(post,postun):	glib2 >= %{glib2_ver}
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2 >= %{glib2_ver}
Requires:	gtk+3 >= %{gtk3_ver}
Requires:	hicolor-icon-theme
Requires:	libiw >= 28
Obsoletes:	gnome-applet-netspeed

%description netspeed
Netspeed applet is just a little applet that shows how much traffic
occurs on a specified network device.

%description netspeed -l pl.UTF-8
Netspeed to mały aplet pokazujący, jak duży ruch występuje na
określonym urządzeniu sieciowym.

%package search
Summary:	Tracker Search Bar
Summary(pl.UTF-8):	Pasek wyszukiwania Tracker
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2 >= %{glib2_ver}
Requires:	gtk+3 >= %{gtk3_ver}
Requires:	tracker >= 1.0

%description search
Tracker Search Bar allows to find your data quickly using Tracker.

%description search -l pl.UTF-8
Pasek wyszukiwania pozwala na szybkie wyszukiwanie danych za pomocą
usługi Tracker.

%package stickynotes
Summary:	Sticky Notes applet
Summary(pl.UTF-8):	Aplet notatek
Group:		X11/Applications
URL:		https://help.gnome.org/users/stickynotes_applet/stable/
Requires(post,postun):	glib2 >= %{glib2_ver}
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2 >= %{glib2_ver}
Requires:	gtk+3 >= %{gtk3_ver}
Requires:	hicolor-icon-theme
Requires:	libwnck >= 3.0.0
Requires:	libxml2 >= 1:2.6.30
Obsoletes:	gnotes_applet

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
URL:		https://help.gnome.org/users/trashapplet/stable/
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2 >= %{glib2_ver}
Requires:	gtk+3 >= %{gtk3_ver}

%description trash
The Panel Trash applet lets you manage your Trash from the panel.

The trash on your panel acts identically to the trash on your desktop,
however it is useful because your panels are always visible.

%description trash -l pl.UTF-8
Aplet śmietnika pozwala na zarządzanie śmietnikiem z poziomu panelu.

Śmietnik w panelu zachowuje się tak samo, jak śmietnik na pulpicie,
ale jest przydatny o tyle, że panele są zawsze widoczne.

%package windowpicker
Summary:	Window Picker applet
Summary(pl.UTF-8):	Aplet do wybierania okien
Group:		X11/Applications
Requires(post,postun):	glib2 >= %{glib2_ver}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2 >= %{glib2_ver}
Requires:	gtk+3 >= %{gtk3_ver}
Requires:	libwnck >= 3.0.0

%description windowpicker
Window Picker is a port of the initial window-picker-applet made by
Cannonical to GNOME 3 and GTK+ 3. It give you a task list that only
contains the icons of each open window, but not the title. This saves
a lot of space, especially if you have many open windows. You can use
the mouse to reorder icons by drag and drop. Also on there are
preferences to set additional options, such as greying out inactive
icons.

%description windowpicker -l pl.UTF-8
Window Picket to port programu window-picker-applet napisanego przez
Cannonical do środowiska GNOME 3 i GTK+ 3. Aplet podaje listę zadań
zawierającą tylko ikony każdego otwartego okna, bez tytułu - oszczędza
to dużo miejsca, zwłaszcza w przypadku wielu otwartych okien. Można
zmieniać kolejność ikon myszką przez przeciąganie i upuszczanie.
Dostępne są także ustawienia dla dodatkowych opcji, takich jak
wyszarzanie nieaktywnych ikon.

%prep
%setup -q

%build
%{__libtoolize}
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-mini-commander \
	--with-cpufreq-lib=cpupower

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-applets/5.0/lib*.la

# es is more recent
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/es_ES

%find_lang %{name}-3.0
%find_lang accessx-status --with-gnome
%find_lang battstat --with-gnome
%find_lang char-palette --with-gnome
%find_lang command-line --with-gnome
%find_lang cpufreq-applet --with-gnome
%find_lang drivemount --with-gnome
%find_lang geyes --with-gnome
%find_lang gweather --with-gnome
%find_lang invest-applet --with-gnome
%find_lang multiload --with-gnome
%find_lang netspeed_applet --with-gnome
%find_lang stickynotes_applet --with-gnome
%find_lang trashapplet --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post accessx-status
%update_icon_cache hicolor

%postun accessx-status
%update_icon_cache hicolor

%post battstat
%glib_compile_schemas

%postun battstat
%glib_compile_schemas

%post brightness
%update_icon_cache hicolor

%postun brightness
%update_icon_cache hicolor

%post charpicker
%glib_compile_schemas

%postun charpicker
%glib_compile_schemas

%post cpufreq
%glib_compile_schemas
%update_icon_cache hicolor

%postun cpufreq
%glib_compile_schemas
%update_icon_cache hicolor

%post geyes
%glib_compile_schemas
%update_icon_cache hicolor

%postun geyes
%glib_compile_schemas
%update_icon_cache hicolor

%post gweather
%glib_compile_schemas

%postun gweather
%glib_compile_schemas

%post inhibit
%update_icon_cache hicolor

%postun inhibit
%update_icon_cache hicolor

%post invest
%update_icon_cache hicolor

%postun invest
%update_icon_cache hicolor

%post minicommander
%glib_compile_schemas
%update_icon_cache hicolor

%postun minicommander
%glib_compile_schemas
%update_icon_cache hicolor

%post modemlights
%update_icon_cache hicolor

%postun modemlights
%update_icon_cache hicolor

%post multiload
%glib_compile_schemas

%postun multiload
%glib_compile_schemas

%post netspeed
%glib_compile_schemas
%update_icon_cache hicolor

%postun netspeed
%glib_compile_schemas
%update_icon_cache hicolor

%post stickynotes
%glib_compile_schemas
%update_icon_cache hicolor

%postun stickynotes
%glib_compile_schemas
%update_icon_cache hicolor

%post windowpicker
%glib_compile_schemas

%postun windowpicker
%glib_compile_schemas

%files -f %{name}-3.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%dir %{_datadir}/gnome-applets
%dir %{_datadir}/gnome-applets/builder
%dir %{_datadir}/gnome-applets/ui

%files accessx-status -f accessx-status.lang
%defattr(644,root,root,755)
%doc accessx-status/AUTHORS
%attr(755,root,root) %{_libexecdir}/accessx-status-applet
%{_datadir}/dbus-1/services/org.gnome.panel.applet.AccessxStatusAppletFactory.service
%{_datadir}/gnome-applets/accessx-status-applet
%{_datadir}/gnome-applets/ui/accessx-status-applet-menu.xml
%{_datadir}/gnome-panel/5.0/applets/org.gnome.applets.AccessxStatusApplet.panel-applet
%{_iconsdir}/hicolor/48x48/apps/ax-applet.png

%files battstat -f battstat.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/battstat-applet-2
%{_datadir}/dbus-1/services/org.gnome.panel.applet.BattstatAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.battstat.gschema.xml
%{_datadir}/gnome-applets/builder/battstat_applet.ui
%{_datadir}/gnome-applets/ui/battstat-applet-menu.xml
%{_datadir}/gnome-panel/5.0/applets/org.gnome.applets.BattstatApplet.panel-applet
%{_sysconfdir}/sound/events/battstat_applet.soundlist

%files brightness
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gnome-brightness-applet
%{_datadir}/dbus-1/services/org.gnome.panel.applet.BrightnessAppletFactory.service
%{_datadir}/gnome-applets/ui/brightness-applet-menu.xml
%{_datadir}/gnome-panel/5.0/applets/org.gnome.BrightnessApplet.panel-applet
%{_datadir}/icons/hicolor/*x*/apps/gnome-brightness-applet.png
%{_datadir}/icons/hicolor/scalable/apps/gnome-brightness-applet.svg

%files charpicker -f char-palette.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/charpick_applet2
%{_datadir}/dbus-1/services/org.gnome.panel.applet.CharpickerAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.charpick.gschema.xml
%{_datadir}/gnome-applets/ui/charpick-applet-menu.xml
%{_datadir}/gnome-panel/5.0/applets/org.gnome.applets.CharpickerApplet.panel-applet

%files cpufreq -f cpufreq-applet.lang
%defattr(644,root,root,755)
%doc cpufreq/{AUTHORS,README}
%attr(755,root,root) %{_bindir}/cpufreq-selector
%attr(755,root,root) %{_libexecdir}/cpufreq-applet
%{_datadir}/dbus-1/services/org.gnome.panel.applet.CPUFreqAppletFactory.service
%{_datadir}/dbus-1/system-services/org.gnome.CPUFreqSelector.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.cpufreq.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.cpufreq.gschema.xml
%{_datadir}/gnome-applets/builder/cpufreq-preferences.ui
%{_datadir}/gnome-applets/cpufreq-applet
%{_datadir}/gnome-applets/ui/cpufreq-applet-menu.xml
%{_datadir}/gnome-panel/5.0/applets/org.gnome.applets.CPUFreqApplet.panel-applet
%{_datadir}/polkit-1/actions/org.gnome.cpufreqselector.policy
/etc/dbus-1/system.d/org.gnome.CPUFreqSelector.conf
%{_iconsdir}/hicolor/*x*/apps/gnome-cpu-frequency-applet.png
%{_iconsdir}/hicolor/scalable/apps/gnome-cpu-frequency-applet.svg

%files drivemount -f drivemount.lang
%defattr(644,root,root,755)
%doc drivemount/AUTHORS
%attr(755,root,root) %{_libexecdir}/drivemount_applet2
%{_datadir}/dbus-1/services/org.gnome.panel.applet.DriveMountAppletFactory.service
%{_datadir}/gnome-applets/ui/drivemount-applet-menu.xml
%{_datadir}/gnome-panel/5.0/applets/org.gnome.applets.DriveMountApplet.panel-applet

%files geyes -f geyes.lang
%defattr(644,root,root,755)
%doc geyes/{AUTHORS,README.themes}
%attr(755,root,root) %{_libexecdir}/geyes_applet2
%{_datadir}/dbus-1/services/org.gnome.panel.applet.GeyesAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.geyes.gschema.xml
%{_datadir}/gnome-applets/geyes
%{_datadir}/gnome-applets/ui/geyes-applet-menu.xml
%{_datadir}/gnome-panel/5.0/applets/org.gnome.applets.GeyesApplet.panel-applet
%{_iconsdir}/hicolor/*x*/apps/gnome-eyes-applet.png
%{_iconsdir}/hicolor/scalable/apps/gnome-eyes-applet.svg

%files gweather -f gweather.lang
%defattr(644,root,root,755)
%doc gweather/AUTHORS
%attr(755,root,root) %{_libexecdir}/gweather-applet-2
%{_datadir}/dbus-1/services/org.gnome.panel.applet.GWeatherAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.gweather.gschema.xml
%{_datadir}/gnome-applets/ui/gweather-applet-menu.xml
%{_datadir}/gnome-panel/5.0/applets/org.gnome.applets.GWeatherApplet.panel-applet

%files inhibit
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gnome-inhibit-applet
%{_datadir}/dbus-1/services/org.gnome.panel.applet.InhibitAppletFactory.service
%{_datadir}/gnome-applets/ui/inhibit-applet-menu.xml
%{_datadir}/gnome-panel/5.0/applets/org.gnome.InhibitApplet.panel-applet
%{_datadir}/icons/hicolor/*x*/apps/gnome-inhibit-applet.png
%{_datadir}/icons/hicolor/scalable/apps/gnome-inhibit-applet.svg

%files invest -f invest-applet.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/invest-chart
%attr(755,root,root) %{_libexecdir}/invest-applet
%{_datadir}/dbus-1/services/org.gnome.panel.applet.InvestAppletFactory.service
%{_datadir}/gnome-applets/builder/financialchart.ui
%{_datadir}/gnome-applets/builder/prefs-dialog.ui
%{_datadir}/gnome-applets/invest-applet
%{_datadir}/gnome-applets/ui/invest-applet-menu.xml
%{_datadir}/gnome-panel/5.0/applets/org.gnome.applets.InvestApplet.panel-applet
%{_iconsdir}/hicolor/*x*/apps/invest-applet.png
%{_iconsdir}/hicolor/scalable/apps/invest-applet.svg
%{py3_sitescriptdir}/invest

%files minicommander -f command-line.lang
%defattr(644,root,root,755)
%doc mini-commander/{AUTHORS,README,TODO}
%attr(755,root,root) %{_libdir}/mini_commander_applet
%{_datadir}/dbus-1/services/org.gnome.panel.applet.MiniCommanderAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.mini-commander.gschema.xml
%{_datadir}/gnome-applets/builder/mini-commander.ui
%{_datadir}/gnome-applets/ui/mini-commander-applet-menu.xml
%{_datadir}/gnome-panel/5.0/applets/org.gnome.applets.MiniCommanderApplet.panel-applet
%{_iconsdir}/hicolor/48x48/apps/gnome-mini-commander.png

%files modemlights
%defattr(644,root,root,755)
%doc modemlights/AUTHORS
%attr(755,root,root) %{_libexecdir}/modem_applet
%{_datadir}/dbus-1/services/org.gnome.panel.applet.ModemAppletFactory.service
%{_datadir}/gnome-applets/builder/modemlights.ui
%{_datadir}/gnome-applets/ui/modem-applet-menu.xml
%{_datadir}/gnome-panel/5.0/applets/org.gnome.applets.ModemApplet.panel-applet
%{_iconsdir}/hicolor/*x*/apps/gnome-modem-monitor-applet.png
%{_iconsdir}/hicolor/scalable/apps/gnome-modem-monitor-applet.svg

%files multiload -f multiload.lang
%defattr(644,root,root,755)
%doc multiload/AUTHORS
%attr(755,root,root) %{_libexecdir}/multiload-applet-2
%{_datadir}/dbus-1/services/org.gnome.panel.applet.MultiLoadAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.multiload.gschema.xml
%{_datadir}/gnome-applets/ui/multiload-applet-menu.xml
%{_datadir}/gnome-panel/5.0/applets/org.gnome.applets.MultiLoadApplet.panel-applet

%files netspeed -f netspeed_applet.lang
%defattr(644,root,root,755)
%doc netspeed/{AUTHORS,TODO}
%attr(755,root,root) %{_libexecdir}/netspeed_applet2
%{_datadir}/dbus-1/services/org.gnome.panel.applet.NetspeedAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.netspeed.gschema.xml
%{_datadir}/gnome-applets/ui/netspeed-menu.xml
%{_datadir}/gnome-panel/5.0/applets/org.gnome.panel.Netspeed.panel-applet
%{_iconsdir}/hicolor/*x*/apps/netspeed-applet.png
%{_iconsdir}/hicolor/scalable/apps/netspeed-applet.svg
%{_iconsdir}/hicolor/16x16/devices/netspeed-*.png
%{_iconsdir}/hicolor/24x24/status/netspeed-*.png

%files search
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/tracker-search-bar
%{_datadir}/dbus-1/services/org.gnome.panel.applet.SearchBarFactory.service
%{_datadir}/gnome-applets/ui/tracker-search-bar-menu.xml
%{_datadir}/gnome-applets/ui/tracker-search-bar.ui
%{_datadir}/gnome-panel/5.0/applets/org.gnome.panel.SearchBar.panel-applet

%files stickynotes -f stickynotes_applet.lang
%defattr(644,root,root,755)
%doc stickynotes/{README,TODO}
%attr(755,root,root) %{_libexecdir}/stickynotes_applet
%{_datadir}/dbus-1/services/org.gnome.panel.applet.StickyNotesAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.stickynotes.gschema.xml
%{_datadir}/gnome-applets/builder/stickynotes-*.ui
%{_datadir}/gnome-applets/icons
%{_datadir}/gnome-applets/ui/stickynotes-*-menu.xml
%{_datadir}/gnome-panel/5.0/applets/org.gnome.applets.StickyNotesApplet.panel-applet
%{_iconsdir}/hicolor/*x*/apps/gnome-sticky-notes-applet.png
%{_iconsdir}/hicolor/scalable/apps/gnome-sticky-notes-applet.svg

%files trash -f trashapplet.lang
%defattr(644,root,root,755)
%doc trashapplet/README
%attr(755,root,root) %{_libexecdir}/trashapplet
%{_datadir}/dbus-1/services/org.gnome.panel.applet.TrashAppletFactory.service
%{_datadir}/gnome-applets/builder/trashapplet-empty-progress.ui
%{_datadir}/gnome-applets/ui/trashapplet-menu.xml
%{_datadir}/gnome-panel/5.0/applets/org.gnome.applets.TrashApplet.panel-applet

%files windowpicker
%defattr(644,root,root,755)
%doc windowpicker/{AUTHORS,TODO}
%dir %{_libdir}/gnome-applets
%dir %{_libdir}/gnome-applets/5.0
%attr(755,root,root) %{_libdir}/gnome-applets/5.0/libwindow-picker-applet.so
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.window-picker-applet.gschema.xml
%{_datadir}/gnome-panel/5.0/applets/org.gnome.applets.WindowPicker.panel-applet
