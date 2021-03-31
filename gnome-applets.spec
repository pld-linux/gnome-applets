%define	glib2_ver	1:2.44.0
%define	gtk3_ver	3.20.0
Summary:	Small applications which embed themselves in the GNOME panel
Summary(pl.UTF-8):	Aplety GNOME - małe aplikacje osadzające się w panelu
Summary(ru.UTF-8):	Маленькие программы, встраивающиеся в панель GNOME
Summary(uk.UTF-8):	Маленькі програми, що вбудовуються в панель GNOME
Name:		gnome-applets
Version:	3.40.0
Release:	1
Epoch:		1
License:	GPL v2+, FDL
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-applets/3.40/%{name}-%{version}.tar.xz
# Source0-md5:	2d749a807c7a2884621acd39ad913233
URL:		https://wiki.gnome.org/Projects/GnomeApplets
BuildRequires:	adwaita-icon-theme >= 3.14.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.13
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-dtd43-xml
BuildRequires:	docbook-utils
BuildRequires:	gettext-tools >= 0.19.6
BuildRequires:	glib2-devel >= %{glib2_ver}
BuildRequires:	gnome-panel-devel >= 3.37.0
BuildRequires:	gtk+3-devel >= %{gtk3_ver}
BuildRequires:	gucharmap-devel >= 3.2.1
BuildRequires:	itstool
BuildRequires:	kernel-tools-cpupower-libs-devel
BuildRequires:	libgtop-devel >= 1:2.22.0
BuildRequires:	libgweather-devel >= 3.28.0
BuildRequires:	libiw-devel >= 28
BuildRequires:	libnotify-devel >= 0.7
BuildRequires:	libtool >= 2:2
BuildRequires:	libwnck-devel >= 3.14.1
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	libxslt-progs >= 1.1.20
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	polkit-devel >= 0.97
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
BuildRequires:	tracker3-devel >= 3.0
BuildRequires:	upower-devel >= 0.99.8
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= %{glib2_ver}
Requires(post,postun):	gtk-update-icon-cache
Requires:	adwaita-icon-theme >= 3.14.0
Requires:	dbus(org.freedesktop.Notifications)
Requires:	glib2 >= %{glib2_ver}
Requires:	gnome-panel >= 3.37.0
Requires:	gtk+3 >= %{gtk3_ver}
Requires:	gucharmap >= 3.2.1
Requires:	hicolor-icon-theme
Requires:	libgtop >= 1:2.22.0
Requires:	libiw >= 28
Requires:	libnotify >= 0.7
Requires:	libwnck >= 3.14.1
Requires:	libxml2 >= 1:2.6.30
Requires:	polkit >= 0.97
Requires:	tracker3 >= 3.0
Requires:	upower >= 0.99.8
Suggests:	gnome-control-center >= 2.26.0
Suggests:	gnome-system-monitor >= 2.24.0
# applets merged into single org.gnome.gnome-applets module since 3.37.0
Provides:	gnome-applets-accessx-status = %{epoch}:%{version}
Provides:	gnome-applets-battstat = %{epoch}:%{version}
Provides:	gnome-applets-brightness = %{epoch}:%{version}
Provides:	gnome-applets-charpicker = %{epoch}:%{version}
Provides:	gnome-applets-command = %{epoch}:%{version}
Provides:	gnome-applets-cpufreq = %{epoch}:%{version}
Provides:	gnome-applets-drivemount = %{epoch}:%{version}
Provides:	gnome-applets-geyes = %{epoch}:%{version}
Provides:	gnome-applets-gweather = %{epoch}:%{version}
Provides:	gnome-applets-inhibit = %{epoch}:%{version}
Provides:	gnome-applets-minicommander = %{epoch}:%{version}
Provides:	gnome-applets-multiload = %{epoch}:%{version}
Provides:	gnome-applets-netspeed = %{epoch}:%{version}
Provides:	gnome-applets-search = %{epoch}:%{version}
Provides:	gnome-applets-stickynotes = %{epoch}:%{version}
Provides:	gnome-applets-timer = %{epoch}:%{version}
Provides:	gnome-applets-trash = %{epoch}:%{version}
Provides:	gnome-applets-windowpicker = %{epoch}:%{version}
Provides:	gnome-applets-window-buttons = %{epoch}:%{version}
Provides:	gnome-applets-window-title = %{epoch}:%{version}
Obsoletes:	gnome-applets-accessx-status < 1:3.37.0
Obsoletes:	gnome-applets-battstat < 1:3.37.0
Obsoletes:	gnome-applets-brightness < 1:3.37.0
Obsoletes:	gnome-applets-charpicker < 1:3.37.0
Obsoletes:	gnome-applets-command < 1:3.37.0
Obsoletes:	gnome-applets-cpufreq < 1:3.37.0
Obsoletes:	gnome-applets-drivemount < 1:3.37.0
Obsoletes:	gnome-applets-geyes < 1:3.37.0
Obsoletes:	gnome-applets-gweather < 1:3.37.0
Obsoletes:	gnome-applets-inhibit < 1:3.37.0
Obsoletes:	gnome-applets-minicommander < 1:3.37.0
Obsoletes:	gnome-applets-multiload < 1:3.37.0
Obsoletes:	gnome-applets-netspeed < 1:3.37.0
Obsoletes:	gnome-applets-search < 1:3.37.0
Obsoletes:	gnome-applets-stickynotes < 1:3.37.0
Obsoletes:	gnome-applets-timer < 1:3.37.0
Obsoletes:	gnome-applets-trash < 1:3.37.0
Obsoletes:	gnome-applets-windowpicker < 1:3.37.0
Obsoletes:	gnome-applets-window-buttons < 1:3.37.0
Obsoletes:	gnome-applets-window-title < 1:3.37.0
# old names
Obsoletes:	gnome-applet-cpufreq < 0.3.2
Obsoletes:	gnome-applet-netspeed < 0.15
Obsoletes:	gnotes_applet < 1.65
# withdrawn applets
Obsoletes:	gnome-applets-invest < 1:3.28.0
Obsoletes:	gnome-applets-keyboard < 1:2.30.0
Obsoletes:	gnome-applets-mixer < 1:3.16.0
Obsoletes:	gnome-applets-modemlights < 1:3.34.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The gnome-applets package provides Panel applets which enhance your
GNOME experience:
- accessx-status: Keyboard Accessibility Status
- battstat: Battery Charge Monitor
- brightness
- charpicker: Character Palette
- command: show the output of a command
- cpufreq: CPU Frequency Scaling Monitor
- drivemount: Disk Mounter
- geyes: tracking the mouse pointer
- gweather: Weather Report
- inhibit: inhibit automatic power saving
- minicommander: command line
- multiload: system monitor
- netspeed: show how much traffic occurs on a network device
- search: Tracker Search Bar
- stickynotes: Sticky Notes
- timer
- trash
- windowpicker: Window Picker
- window-buttons: Window buttons for GNOME Panel
- window-title: Window title for GNOME Panel

%description -l pl.UTF-8
Pakiet gnome-applets udostępnia aplety Panelu, które usprawniają pracę
z GNOME:
- accessx-status: stan dostepności klawiatury
- battstat: monitor stanu naładowania akumulatora
- brightness: jasność
- charpicker: paleta znaków
- command: pokazywanie wyjścia z polecenia
- cpufreq: monitor częstotliwości procesora
- drivemount: montowanie dysków
- geyes: śledzenie wskaźnika myszy
- gweather: raport pogodowy
- inhibit: wyłączanie automatycznego oszczędzania zasilania
- minicommander: wiersz poleceń
- multiload: monitor systemu
- netspeed: pokazywanie wielkości ruchu występującego na urządzeniu
  sieciowym
- search: Pasek wyszukiwania Trackera
- stickynotes: przyklejane notatki
- timer: minutnik
- trash: śmietnik
- windowpicker: wybieranie okien
- window-buttons: przyciski okien dla Panelu GNOME
- window-title: tytuł okien dla Panelu GNOME

%description -l uk.UTF-8
Пакет gnome-applets містить аплети Панелі GNOME, що збільшують
комфортність роботи в середовищі GNOME.

%description -l ru.UTF-8
Пакет gnome-applets содержит апплеты Панели GNOME, увеличивающие
комфортность работы в среде GNOME.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-panel/modules/*.la

# merged gnome-applets.mo, multiple help dirs
%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS
/etc/dbus-1/system.d/org.gnome.CPUFreqSelector.conf
%attr(755,root,root) %{_bindir}/cpufreq-selector
%attr(755,root,root) %{_libdir}/gnome-panel/modules/org.gnome.gnome-applets.so
%{_datadir}/dbus-1/system-services/org.gnome.CPUFreqSelector.service
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.battstat.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.charpick.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.command.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.cpufreq.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.geyes.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.gweather.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.mini-commander.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.multiload.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.netspeed.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.stickynotes.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.timer.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.window-picker-applet.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.window-buttons.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets.window-title.gschema.xml
%{_datadir}/gnome-applets
%{_datadir}/polkit-1/actions/org.gnome.cpufreqselector.policy
%{_iconsdir}/hicolor/*x*/apps/gnome-brightness-applet.png
%{_iconsdir}/hicolor/*x*/apps/gnome-cpu-frequency-applet.png
%{_iconsdir}/hicolor/*x*/apps/gnome-eyes-applet.png
%{_iconsdir}/hicolor/*x*/apps/gnome-inhibit-applet.png
%{_iconsdir}/hicolor/*x*/apps/gnome-sticky-notes-applet.png
%{_iconsdir}/hicolor/*x*/apps/netspeed-applet.png
%{_iconsdir}/hicolor/48x48/apps/ax-applet.png
%{_iconsdir}/hicolor/48x48/apps/gnome-mini-commander.png
%{_iconsdir}/hicolor/72x72/apps/windowtitle-applet.png
%{_iconsdir}/hicolor/96x96/apps/windowbuttons-applet.png
%{_iconsdir}/hicolor/scalable/apps/gnome-brightness-applet.svg
%{_iconsdir}/hicolor/scalable/apps/gnome-cpu-frequency-applet.svg
%{_iconsdir}/hicolor/scalable/apps/gnome-eyes-applet.svg
%{_iconsdir}/hicolor/scalable/apps/gnome-inhibit-applet.svg
%{_iconsdir}/hicolor/scalable/apps/gnome-sticky-notes-applet.svg
%{_iconsdir}/hicolor/scalable/apps/netspeed-applet.svg
