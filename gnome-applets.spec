Summary:	Small applications which embed themselves in the GNOME panel
Summary(pl):	Aplety GNOME - ma³e aplikacje osadzaj±ce siê w panelu
Summary(ru):	íÁÌÅÎØËÉÅ ÐÒÏÇÒÁÍÍÙ, ×ÓÔÒÁÉ×ÁÀÝÉÅÓÑ × ÐÁÎÅÌØ GNOME
Summary(uk):	íÁÌÅÎØË¦ ÐÒÏÇÒÁÍÉ, ÝÏ ×ÂÕÄÏ×ÕÀÔØÓÑ × ÐÁÎÅÌØ GNOME
Name:		gnome-applets
Version:	2.10.0
Release:	4
Epoch:		1
License:	GPL v2, FDL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-applets/2.10/%{name}-%{version}.tar.bz2
# Source0-md5:	c230df43a21a0d788197b5b0f3e688f1
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
BuildRequires:	libxml2-devel >= 1:2.6.17
BuildRequires:	libxklavier-devel >= 2.0
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	scrollkeeper >= 0.3.11-4
BuildRequires:	system-tools-backends >= 1.2.0
Requires(post):	GConf2 >= 2.10.0
Requires(post):	scrollkeeper
Requires:	gnome-icon-theme >= 2.10.0
Requires:	gnome-vfs2 >= 2.10.0-2
Requires:	gstreamer-audiosink
Requires:	system-tools-backends >= 1.2.0
Obsoletes:	gnotes_applet
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal} -I m4
%{__libtoolize}
glib-gettextize --copy --force
intltoolize --copy --force
%{__autoheader}
gnome-doc-common
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

%find_lang %{name} --with-gnome --all-name

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

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install
GCONF_CONFIG_SOURCE="`%{_bindir}/gconftool-2 --get-default-source`" %{_libdir}/%{name}/mc-install-default-macros

%postun	-p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *AUTHORS *ChangeLog *NEWS *README *TODO
%{_sysconfdir}/gconf/schemas/*
%{_sysconfdir}/sound/events/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/accessx-status-applet
%attr(755,root,root) %{_libdir}/battstat-applet-2
%attr(755,root,root) %{_libdir}/charpick_applet2
%attr(755,root,root) %{_libdir}/cpufreq-applet
%attr(755,root,root) %{_libdir}/drivemount_applet2
%attr(755,root,root) %{_libdir}/geyes_applet2
%attr(755,root,root) %{_libdir}/gnome-keyboard-applet
%attr(755,root,root) %{_libdir}/gtik2_applet2
%attr(755,root,root) %{_libdir}/gweather-applet-2
%attr(755,root,root) %{_libdir}/mini_commander_applet
%attr(755,root,root) %{_libdir}/mixer_applet2
%attr(755,root,root) %{_libdir}/modem_applet
%attr(755,root,root) %{_libdir}/multiload-applet-2
%attr(755,root,root) %{_libdir}/null_applet
%attr(755,root,root) %{_libdir}/stickynotes_applet
%attr(755,root,root) %{_libdir}/trashapplet
%attr(755,root,root) %{_libdir}/%{name}
%{_libdir}/bonobo/servers/*
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/%{name}
%{_pixmapsdir}/accessx-status-applet
%{_pixmapsdir}/cpufreq-applet
%{_pixmapsdir}/stickynotes
%{_iconsdir}/hicolor/48x48/apps/*.png
%{_omf_dest_dir}/%{name}

%dir %{_datadir}/xmodmap
%{_datadir}/xmodmap/base.xml
%lang(hy) %{_datadir}/xmodmap/xmodmap.am*
# ?
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

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_pkgconfigdir}/*.pc
