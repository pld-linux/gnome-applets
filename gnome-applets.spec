Summary:	Small applications which embed themselves in the GNOME panel
Summary(pl):	GNOME - Applety
Summary(ru):	Маленькие программы, встраивающиеся в панель GNOME
Summary(uk):	Маленьк╕ програми, що вбудовуються в панель GNOME
Name:		gnome-applets
Version:	2.0.1
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-am.patch
Patch1:		%{name}-charpick.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gail-devel >= 0.17
BuildRequires:	gdbm-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-panel-devel >= 2.0.5
BuildRequires:	gnome-vfs2-devel >= 2.0.2
BuildRequires:	gtk+2-devel >= 2.0.6
BuildRequires:	intltool >= 0.22
BuildRequires:	libgnome-devel >= 2.0.2
BuildRequires:	libgnomecanvas-devel >= 2.0.2
BuildRequires:	libgnomeui-devel >= 2.0.3
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgtop-devel >= 2.0.0
BuildRequires:	libwnck-devel >= 0.16
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.23
BuildRequires:	scrollkeeper >= 0.3.6
Prereq:		/sbin/ldconfig
Prereq:		scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnotes_applet

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME2
%define		_localstatedir	/var
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

%description
The gnome-applets package provides Panel applets which enhance your
GNOME experience.

%description -l pl
Applety pod GNOME.

%description -l uk
Пакет gnome-applets м╕стить аплети Панел╕ GNOME, що зб╕льшують
комфортн╕сть роботи в середовищ╕ GNOME.

%description -l ru
Пакет gnome-applets содержит апплеты Панели GNOME, увеличивающие
комфортность работы в среде GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
libtoolize --copy --force
glib-gettextize --copy --force
intltoolize --copy --force
aclocal
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

for i in `find $RPM_BUILD_ROOT -name "*\.xml" | grep help`
do
        sed s@http://www.oasis-open.org/docbook/xml/4.1.2@/usr/share/sgml/docbook/xml-dtd-4.1.2@ $i > $i-
        mv -f $i- $i
done

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
GCONF_CONFIG_SOURCE="`%{_bindir}/gconftool-2 --get-default-source`" /usr/X11R6/bin/gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/*.schemas > /dev/null 

%postun	-p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *AUTHORS *ChangeLog *NEWS *README *TODO
%{_sysconfdir}/gconf/schemas/*
%{_sysconfdir}/sound/events/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/battstat-applet-2
%attr(755,root,root) %{_libdir}/cdplayer_applet2
%attr(755,root,root) %{_libdir}/charpick_applet2
%attr(755,root,root) %{_libdir}/drivemount_applet2
%attr(755,root,root) %{_libdir}/geyes_applet2
%attr(755,root,root) %{_libdir}/gkb-applet-2
%attr(755,root,root) %{_libdir}/gtik2_applet2
%attr(755,root,root) %{_libdir}/gweather-applet-2
%attr(755,root,root) %{_libdir}/mini_commander_applet
%attr(755,root,root) %{_libdir}/mixer_applet2
%attr(755,root,root) %{_libdir}/modemlights_applet2
%attr(755,root,root) %{_libdir}/multiload-applet-2
%{_libdir}/bonobo/servers/*
%{_datadir}/battstat_applet
%{_datadir}/geyes
%{_datadir}/gweather
%{_datadir}/gnome-2.0/ui/*
%{_pixmapsdir}/gweather
%{_pixmapsdir}/mini-commander
%{_pixmapsdir}/*.png
%{_omf_dest_dir}/%{name}

%dir %{_datadir}/gnome/gkb
%{_datadir}/gnome/gkb/Dvorak.keyprop
%{_datadir}/gnome/gkb/Default.keyprop
%lang(am) %{_datadir}/gnome/gkb/AM_Armenian.keyprop
%lang(ar) %{_datadir}/gnome/gkb/AR_Arabic.keyprop
%lang(am) %{_datadir}/gnome/gkb/Armenian.keyprop
%lang(az) %{_datadir}/gnome/gkb/AZ_Azerbaidjani_Turkic.keyprop
%lang(eu) %{_datadir}/gnome/gkb/Basque.keyprop
%lang(be) %{_datadir}/gnome/gkb/BE_Dutch.keyprop
%lang(be) %{_datadir}/gnome/gkb/Belgian.keyprop
%lang(bg) %{_datadir}/gnome/gkb/BG_*
%lang(br) %{_datadir}/gnome/gkb/BR_*
%lang(bg) %{_datadir}/gnome/gkb/BulgarianCyril.keyprop
%lang(by) %{_datadir}/gnome/gkb/BY_Belarussian.keyprop
%lang(ca) %{_datadir}/gnome/gkb/CA_English.keyprop
%lang(ch) %{_datadir}/gnome/gkb/CH_German_x.keyprop
%lang(cs) %{_datadir}/gnome/gkb/CS_Czech.keyprop
%lang(cz,sk) %{_datadir}/gnome/gkb/CZ_Czech_Slovak.keyprop
%lang(cz) %{_datadir}/gnome/gkb/CZ_Czech_x.keyprop
%lang(de) %{_datadir}/gnome/gkb/DE_*
%lang(dk) %{_datadir}/gnome/gkb/DK_*
%lang(ee) %{_datadir}/gnome/gkb/EE_*
%lang(es) %{_datadir}/gnome/gkb/ES_*
%lang(fi) %{_datadir}/gnome/gkb/FI_*
%lang(ch) %{_datadir}/gnome/gkb/FrenchCanadian2.keyprop
%lang(qc) %{_datadir}/gnome/gkb/FrenchCanadian.keyprop
%lang(ch) %{_datadir}/gnome/gkb/FrenchSwiss.keyprop
%lang(fr) %{_datadir}/gnome/gkb/FR_*
%lang(gb) %{_datadir}/gnome/gkb/GB*
%lang(ge) %{_datadir}/gnome/gkb/GE_Georgian_x.keyprop
%lang(ge-la) %{_datadir}/gnome/gkb/GeorgianLatin.keyprop
%lang(de,at,ch) %{_datadir}/gnome/gkb/German.keyprop
%lang(ch) %{_datadir}/gnome/gkb/GermanSwiss.keyprop
%lang(gr) %{_datadir}/gnome/gkb/GR_*
%lang(hu) %{_datadir}/gnome/gkb/HU_*
%lang(hu) %{_datadir}/gnome/gkb/Hungarian*
%lang(il) %{_datadir}/gnome/gkb/IL_*
%lang(is) %{_datadir}/gnome/gkb/IS_*
%lang(it) %{_datadir}/gnome/gkb/IT_*
%lang(jp) %{_datadir}/gnome/gkb/JP_*
%lang(la) %{_datadir}/gnome/gkb/LA_Lao_x.keyprop
%lang(lt) %{_datadir}/gnome/gkb/LT_*
%lang(mk) %{_datadir}/gnome/gkb/M*acedonian.keyprop
%lang(nl) %{_datadir}/gnome/gkb/NL_Dutch_x.keyprop
%lang(no) %{_datadir}/gnome/gkb/NO_Norwegian.keyprop
%lang(no) %{_datadir}/gnome/gkb/Norwegian.keyprop
%lang(pl) %{_datadir}/gnome/gkb/*olish*
%lang(pt) %{_datadir}/gnome/gkb/Portug*
%lang(pt) %{_datadir}/gnome/gkb/PT_*
%lang(ro) %{_datadir}/gnome/gkb/RO_Romanian.keyprop
%lang(ru) %{_datadir}/gnome/gkb/*Russian*
%lang(se) %{_datadir}/gnome/gkb/SE_Swedish.keyprop
%lang(si) %{_datadir}/gnome/gkb/SI_Slovenian.keyprop
%lang(sk) %{_datadir}/gnome/gkb/Slovak.keyprop
%lang(si) %{_datadir}/gnome/gkb/Slovenian.keyprop
%lang(yu) %{_datadir}/gnome/gkb/SR_Dutch.keyprop
%lang(sv) %{_datadir}/gnome/gkb/Swedish.keyprop
%lang(th) %{_datadir}/gnome/gkb/Thai2.keyprop
%lang(th) %{_datadir}/gnome/gkb/Thai.keyprop
%lang(th) %{_datadir}/gnome/gkb/TH_Thai.keyprop
%lang(th) %{_datadir}/gnome/gkb/TH_Thai_x.keyprop
%lang(tr) %{_datadir}/gnome/gkb/TR*
%lang(ua) %{_datadir}/gnome/gkb/UA_Ukrainian.keyprop
%lang(uk) %{_datadir}/gnome/gkb/UK.keyprop
%lang(us) %{_datadir}/gnome/gkb/US*
%lang(vn) %{_datadir}/gnome/gkb/VN_Vietnamese.keyprop
%lang(yu) %{_datadir}/gnome/gkb/Yugoslav.keyprop
%lang(yu) %{_datadir}/gnome/gkb/YU_Serbo-Croatian_x.keyprop

%dir %{_pixmapsdir}/gkb
%{_pixmapsdir}/gkb/gkb.png

%dir %{_datadir}/xmodmap
%lang(am) %{_datadir}/xmodmap/xmodmap.am*
%lang(be) %{_datadir}/xmodmap/xmodmap.be*
%lang(bg) %{_datadir}/xmodmap/xmodmap.bg*
%lang(br) %{_datadir}/xmodmap/xmodmap.br*
%lang(ch) %{_datadir}/xmodmap/xmodmap.ch*
%lang(cz) %{_datadir}/xmodmap/xmodmap.cz*
%lang(de) %{_datadir}/xmodmap/xmodmap.de*
%lang(dk) %{_datadir}/xmodmap/xmodmap.dk*
%{_datadir}/xmodmap/xmodmap.dvorak
%lang(ee) %{_datadir}/xmodmap/xmodmap.ee*
%lang(es) %{_datadir}/xmodmap/xmodmap.es*
%lang(fi) %{_datadir}/xmodmap/xmodmap.fi*
%lang(fr) %{_datadir}/xmodmap/xmodmap.fr*
%lang(gb) %{_datadir}/xmodmap/xmodmap.gb*
%lang(ge) %{_datadir}/xmodmap/xmodmap.ge*
%lang(gr) %{_datadir}/xmodmap/xmodmap.gr*
%lang(hu) %{_datadir}/xmodmap/xmodmap.hu*
%lang(il) %{_datadir}/xmodmap/xmodmap.il*
%lang(is) %{_datadir}/xmodmap/xmodmap.is*
%lang(it) %{_datadir}/xmodmap/xmodmap.it*
%lang(jp) %{_datadir}/xmodmap/xmodmap.jp*
%lang(la) %{_datadir}/xmodmap/xmodmap.la*
%lang(lt) %{_datadir}/xmodmap/xmodmap.lt*
%lang(mk) %{_datadir}/xmodmap/xmodmap.mk*
%lang(nl) %{_datadir}/xmodmap/xmodmap.nl*
%lang(no) %{_datadir}/xmodmap/xmodmap.no*
%lang(pl) %{_datadir}/xmodmap/xmodmap.pl*
%lang(pt) %{_datadir}/xmodmap/xmodmap.pt*
%lang(qc) %{_datadir}/xmodmap/xmodmap.qc*
%lang(ro) %{_datadir}/xmodmap/xmodmap.ro*
%lang(ru) %{_datadir}/xmodmap/xmodmap.ru*
%lang(se) %{_datadir}/xmodmap/xmodmap.se*
%lang(sf) %{_datadir}/xmodmap/xmodmap.sf*
%lang(sg) %{_datadir}/xmodmap/xmodmap.sg*
%lang(si) %{_datadir}/xmodmap/xmodmap.si*
%lang(sk) %{_datadir}/xmodmap/xmodmap.sk*
%lang(th) %{_datadir}/xmodmap/xmodmap.th*
%lang(tr) %{_datadir}/xmodmap/xmodmap.tr*
%lang(uk) %{_datadir}/xmodmap/xmodmap.uk*
%lang(us) %{_datadir}/xmodmap/xmodmap.us*
%lang(yu) %{_datadir}/xmodmap/xmodmap.yu*
