Summary:	Small applications which embed themselves in the GNOME panel
Summary(pl):	Aplety GNOME - ma³e aplikacje osadzaj±ce siê w panelu
Summary(ru):	íÁÌÅÎØËÉÅ ÐÒÏÇÒÁÍÍÙ, ×ÓÔÒÁÉ×ÁÀÝÉÅÓÑ × ÐÁÎÅÌØ GNOME
Summary(uk):	íÁÌÅÎØË¦ ÐÒÏÇÒÁÍÉ, ÝÏ ×ÂÕÄÏ×ÕÀÔØÓÑ × ÐÁÎÅÌØ GNOME
Name:		gnome-applets
Version:	2.6.0
Release:	3
Epoch:		1
License:	GPL v2, FDL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.6/%{name}-%{version}.tar.bz2
# Source0-md5:	9c2dcde8fc94dd43f8aa7be52ca9c103
Patch0:		%{name}-stickynotes-title-size.patch
Patch1:		%{name}-locale-names.patch
Patch2:		%{name}-battstat-ppc.patch
Patch3:		%{name}-gweather-sunny.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gail-devel >= 1.5.8
BuildRequires:	gdbm-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.4.0
BuildRequires:	gnome-panel-devel >= 2.5.93
BuildRequires:	gnome-vfs2-devel >= 2.5.91
BuildRequires:	gstreamer-plugins-devel >= 0.8.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	intltool >= 0.29
BuildRequires:	libgnome-devel >= 2.5.92
BuildRequires:	libgnomecanvas-devel >= 2.5.92
BuildRequires:	libgnomeui-devel >= 2.5.92
BuildRequires:	libglade2-devel >= 1:2.3.6
BuildRequires:	libgtop-devel >= 2.5.2
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.5.90
BuildRequires:	libxml2-devel >= 2.6.7
BuildRequires:	libxklavier-devel >= 0.97
BuildRequires:	scrollkeeper >= 0.3.11-4
Requires(post):	GConf2 >= 2.5.90
Requires(post):	scrollkeeper
Requires:	gnome-vfs2 >= 2.5.91
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
Requires:	GConf2-devel >= 2.5.90
Requires:	gtk+2-devel >= 2:2.4.0

%description devel
Header files for gnome-applets.

%description devel -l pl
Pliki nag³ówkowe gnome-applets.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0

mv po/{no,nb}.po

%build
%{__aclocal}
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
%attr(755,root,root) %{_libdir}/cdplayer_applet2
%attr(755,root,root) %{_libdir}/charpick_applet2
%attr(755,root,root) %{_libdir}/drivemount_applet2
%attr(755,root,root) %{_libdir}/geyes_applet2
%attr(755,root,root) %{_libdir}/gnome-keyboard-applet
%attr(755,root,root) %{_libdir}/gtik2_applet2
%attr(755,root,root) %{_libdir}/gweather-applet-2
%attr(755,root,root) %{_libdir}/mailcheck-applet
%attr(755,root,root) %{_libdir}/mini_commander_applet
%attr(755,root,root) %{_libdir}/mixer_applet2
%attr(755,root,root) %{_libdir}/modemlights_applet2
%attr(755,root,root) %{_libdir}/multiload-applet-2
%attr(755,root,root) %{_libdir}/stickynotes_applet
%attr(755,root,root) %{_libdir}/wireless-applet
%attr(755,root,root) %{_libdir}/%{name}
%{_libdir}/bonobo/servers/*
%{_datadir}/battstat_applet
%{_datadir}/geyes
%{_datadir}/gnome/gkb/presets.xml
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/gen_util
%{_datadir}/gswitchit
%{_datadir}/gweather
%{_datadir}/stickynotes
%{_datadir}/wireless-applet
%{_pixmapsdir}/accessx-status-applet
%{_pixmapsdir}/mailcheck
%{_pixmapsdir}/mini-commander
%{_pixmapsdir}/mixer
%{_pixmapsdir}/stickynotes
%{_pixmapsdir}/wireless-applet
%{_pixmapsdir}/*.png
%{_omf_dest_dir}/%{name}

%dir %{_datadir}/gnome/gkb
%{_datadir}/gnome/gkb/Dvorak.keyprop
%{_datadir}/gnome/gkb/Default.keyprop
%lang(hy) %{_datadir}/gnome/gkb/AM_Armenian.keyprop
%lang(ar) %{_datadir}/gnome/gkb/AR_*
%lang(hy) %{_datadir}/gnome/gkb/Armenian.keyprop
%lang(az) %{_datadir}/gnome/gkb/AZ_Azerbaidjani_Turkic.keyprop
%lang(eu) %{_datadir}/gnome/gkb/Basque.keyprop
%lang(nl) %{_datadir}/gnome/gkb/BE_Dutch.keyprop
%lang(fr,nl,wa) %{_datadir}/gnome/gkb/Belgian.keyprop
%lang(bg) %{_datadir}/gnome/gkb/BG_*
%lang(pt_BR) %{_datadir}/gnome/gkb/BR_*
%lang(bg) %{_datadir}/gnome/gkb/BulgarianCyril.keyprop
%lang(be) %{_datadir}/gnome/gkb/BY_Belarussian.keyprop
%lang(en_CA) %{_datadir}/gnome/gkb/CA_English.keyprop
%lang(de) %{_datadir}/gnome/gkb/CH_German_x.keyprop
%lang(cs) %{_datadir}/gnome/gkb/CZ_Czech.keyprop
%lang(cs) %{_datadir}/gnome/gkb/CZ_Czech_x.keyprop
%lang(cs,sk) %{_datadir}/gnome/gkb/CZ_Czech_Slovak.keyprop
%lang(de) %{_datadir}/gnome/gkb/DE_*
%lang(da) %{_datadir}/gnome/gkb/DK_*
%lang(et) %{_datadir}/gnome/gkb/EE_*
%lang(es) %{_datadir}/gnome/gkb/ES_*
%lang(fi) %{_datadir}/gnome/gkb/FI_*
%lang(fr) %{_datadir}/gnome/gkb/FrenchCanadian2.keyprop
%lang(fr) %{_datadir}/gnome/gkb/FrenchCanadian.keyprop
%lang(fr) %{_datadir}/gnome/gkb/FrenchSwiss.keyprop
%lang(fr) %{_datadir}/gnome/gkb/FR_*
%lang(ka) %{_datadir}/gnome/gkb/GE_Georgian_x.keyprop
%lang(ka) %{_datadir}/gnome/gkb/GeorgianLatin.keyprop
%lang(de) %{_datadir}/gnome/gkb/German.keyprop
%lang(de) %{_datadir}/gnome/gkb/GermanSwiss.keyprop
%lang(el) %{_datadir}/gnome/gkb/GR_*
%lang(hr) %{_datadir}/gnome/gkb/HR_*
%lang(hu) %{_datadir}/gnome/gkb/HU_*
%lang(hu) %{_datadir}/gnome/gkb/Hungarian*
%lang(he,yi) %{_datadir}/gnome/gkb/IL_*
%lang(is) %{_datadir}/gnome/gkb/IS_*
%lang(it) %{_datadir}/gnome/gkb/IT_*
%lang(ja) %{_datadir}/gnome/gkb/JP_*
%lang(ko) %{_datadir}/gnome/gkb/KR_Korean.keyprop
%lang(lo) %{_datadir}/gnome/gkb/LA_Lao_x.keyprop
%lang(lt) %{_datadir}/gnome/gkb/LT_*
%lang(mk) %{_datadir}/gnome/gkb/M*acedonian.keyprop
%lang(mn) %{_datadir}/gnome/gkb/MN_Mongolian*.keyprop
%lang(nl) %{_datadir}/gnome/gkb/NL_Dutch_x.keyprop
%lang(nn,no) %{_datadir}/gnome/gkb/NO_Norwegian.keyprop
%lang(nn,no) %{_datadir}/gnome/gkb/Norwegian.keyprop
%lang(pl) %{_datadir}/gnome/gkb/*olish*
%lang(pt) %{_datadir}/gnome/gkb/Portug*
%lang(pt) %{_datadir}/gnome/gkb/PT_*
%lang(ro) %{_datadir}/gnome/gkb/RO_Romanian.keyprop
%lang(ru) %{_datadir}/gnome/gkb/*Russian*
%lang(sv) %{_datadir}/gnome/gkb/SE_Swedish*.keyprop
%lang(sl) %{_datadir}/gnome/gkb/SI_Slovenian*.keyprop
%lang(sk) %{_datadir}/gnome/gkb/Slovak.keyprop
%lang(sl) %{_datadir}/gnome/gkb/Sloven*.keyprop
%lang(sr) %{_datadir}/gnome/gkb/SR_Dutch.keyprop
%lang(sv) %{_datadir}/gnome/gkb/Swedish.keyprop
# does (sy) really exist?
%lang(ar) %{_datadir}/gnome/gkb/Syriac*.keyprop
%lang(th) %{_datadir}/gnome/gkb/Thai2.keyprop
%lang(th) %{_datadir}/gnome/gkb/Thai.keyprop
%lang(th) %{_datadir}/gnome/gkb/TH_Thai.keyprop
%lang(th) %{_datadir}/gnome/gkb/TH_Thai_x.keyprop
%lang(tr) %{_datadir}/gnome/gkb/TR*
%lang(uk) %{_datadir}/gnome/gkb/UA_Ukrainian.keyprop
%{_datadir}/gnome/gkb/UK*
%{_datadir}/gnome/gkb/US*
%lang(vi) %{_datadir}/gnome/gkb/VN_Vietnamese.keyprop
%lang(hr,mk,sl,sr) %{_datadir}/gnome/gkb/Yugoslav.keyprop
%lang(sr) %{_datadir}/gnome/gkb/YU_Serb*.keyprop

%dir %{_pixmapsdir}/gkb
%{_pixmapsdir}/gkb/gkb.png
%{_pixmapsdir}/gkb/lam.png

%dir %{_datadir}/xmodmap
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
