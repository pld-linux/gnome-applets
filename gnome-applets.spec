Summary:	Small applications which embed themselves in the GNOME panel
Summary(pl):	GNOME - Applety
Name:		gnome-applets
Version:	1.4.0
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/gnome-applets/%{name}-%{version}.tar.gz
Patch0:		%{name}-applet-docs.make.patch
BuildRequires:	esound-devel >= 0.2.7
BuildRequires:	gdbm-devel
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	gnome-core-devel >= 1.1.0
BuildRequires:	gdk-pixbuf-devel >= 0.7.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libgtop-devel >= 1.0.0
BuildRequires:	libghttp-devel
URL:		http://www.gnome.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnotes_applet

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var

%description
The gnome-applets package provides Panel applets which enhance your
GNOME experience.

%description -l pl
Applety pod GNOME.

%prep
%setup -q
%patch0 -p1

%build
gettextize --copy --force
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name} --with-gnome --all-name

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS.gz ChangeLog.gz NEWS.gz README.gz

%{_sysconfdir}/CORBA/servers/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/applets
%{_datadir}/asclock
%{_datadir}/clockmail
%{_datadir}/geyes
%{_datadir}/gweather
%{_datadir}/odometer
%{_datadir}/sound-monitor
%{_datadir}/tickastat
%{_datadir}/omf/%{name}
%{_pixmapsdir}/gweather
%{_pixmapsdir}/mini-commander
%{_pixmapsdir}/*.png
%{_pixmapsdir}/*.xpm

%dir %{_datadir}/gnome/gkb
%lang(am) %{_datadir}/gnome/gkb/AM_Armenian.keyprop
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
%lang(si) %{_datadir}/gnome/gkb/Slovene.keyprop
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

%dir %{_datadir}/pixmaps/gkb
%lang(at) %{_datadir}/pixmaps/gkb/at.png
%lang(be) %{_datadir}/pixmaps/gkb/be.png
%lang(bg) %{_datadir}/pixmaps/gkb/bg.png
%lang(br) %{_datadir}/pixmaps/gkb/br.png
%lang(ca) %{_datadir}/pixmaps/gkb/ca.png
%lang(ch) %{_datadir}/pixmaps/gkb/ch.png
%lang(cu) %{_datadir}/pixmaps/gkb/cu.png
%lang(cz) %{_datadir}/pixmaps/gkb/cz.png
%lang(de) %{_datadir}/pixmaps/gkb/de.png
%lang(dk) %{_datadir}/pixmaps/gkb/dk.png
%lang(ee) %{_datadir}/pixmaps/gkb/ee.png
%lang(es) %{_datadir}/pixmaps/gkb/es.png
%lang(eu) %{_datadir}/pixmaps/gkb/eu.png
%lang(fi) %{_datadir}/pixmaps/gkb/fi.png
%lang(fr) %{_datadir}/pixmaps/gkb/fr.png
%lang(gb) %{_datadir}/pixmaps/gkb/gb.png
%{_datadir}/pixmaps/gkb/gkb-foot.png
%lang(gr) %{_datadir}/pixmaps/gkb/gr.png
%lang(hr) %{_datadir}/pixmaps/gkb/hr.png
%lang(hu) %{_datadir}/pixmaps/gkb/hu.png
%lang(il) %{_datadir}/pixmaps/gkb/il.png
%lang(is) %{_datadir}/pixmaps/gkb/is.png
%lang(it) %{_datadir}/pixmaps/gkb/it.png
%lang(jp) %{_datadir}/pixmaps/gkb/jp.png
%lang(lt) %{_datadir}/pixmaps/gkb/lt.png
%lang(mk) %{_datadir}/pixmaps/gkb/mk.png
%lang(mx) %{_datadir}/pixmaps/gkb/mx.png
%lang(nl) %{_datadir}/pixmaps/gkb/nl.png
%lang(no) %{_datadir}/pixmaps/gkb/no.png
%lang(pl) %{_datadir}/pixmaps/gkb/pl.png
%lang(pt) %{_datadir}/pixmaps/gkb/pt.png
%lang(qc) %{_datadir}/pixmaps/gkb/qc.png
%lang(ro) %{_datadir}/pixmaps/gkb/ro.png
%lang(ru) %{_datadir}/pixmaps/gkb/ru.png
%lang(se) %{_datadir}/pixmaps/gkb/se.png
%lang(si) %{_datadir}/pixmaps/gkb/si.png
%lang(sk) %{_datadir}/pixmaps/gkb/sk.png
%lang(th) %{_datadir}/pixmaps/gkb/th.png
%lang(tr) %{_datadir}/pixmaps/gkb/tr.png
%lang(un) %{_datadir}/pixmaps/gkb/un.png
%lang(us) %{_datadir}/pixmaps/gkb/us.png
%lang(uy) %{_datadir}/pixmaps/gkb/uy.png
%lang(yu) %{_datadir}/pixmaps/gkb/yu.png

%dir %{_datadir}/xmodmap
%lang(be) %{_datadir}/xmodmap/xmodmap.be
%lang(bg) %{_datadir}/xmodmap/xmodmap.bg
%lang(ch) %{_datadir}/xmodmap/xmodmap.ch
%lang(cz) %{_datadir}/xmodmap/xmodmap.cz
%lang(de) %{_datadir}/xmodmap/xmodmap.de
%lang(dk) %{_datadir}/xmodmap/xmodmap.dk
%{_datadir}/xmodmap/xmodmap.dvorak
%lang(ee) %{_datadir}/xmodmap/xmodmap.ee
%lang(es) %{_datadir}/xmodmap/xmodmap.es
%lang(fi) %{_datadir}/xmodmap/xmodmap.fi
%lang(fr) %{_datadir}/xmodmap/xmodmap.fr*
%lang(hu) %{_datadir}/xmodmap/xmodmap.hu*
%lang(gr) %{_datadir}/xmodmap/xmodmap.gr
%lang(il) %{_datadir}/xmodmap/xmodmap.il
%lang(is) %{_datadir}/xmodmap/xmodmap.is
%lang(it) %{_datadir}/xmodmap/xmodmap.it
%lang(la) %{_datadir}/xmodmap/xmodmap.la
%lang(nl) %{_datadir}/xmodmap/xmodmap.nl
%lang(no) %{_datadir}/xmodmap/xmodmap.no
%lang(pl) %{_datadir}/xmodmap/xmodmap.pl
%lang(pt) %{_datadir}/xmodmap/xmodmap.pt*
%lang(qc) %{_datadir}/xmodmap/xmodmap.qc
%lang(ru) %{_datadir}/xmodmap/xmodmap.ru*
%lang(se) %{_datadir}/xmodmap/xmodmap.se
%lang(sf) %{_datadir}/xmodmap/xmodmap.sf
%lang(sg) %{_datadir}/xmodmap/xmodmap.sg
%lang(si) %{_datadir}/xmodmap/xmodmap.si
%lang(sk) %{_datadir}/xmodmap/xmodmap.sk
%lang(th) %{_datadir}/xmodmap/xmodmap.th
%lang(tr) %{_datadir}/xmodmap/xmodmap.tr*
%lang(uk) %{_datadir}/xmodmap/xmodmap.uk
%lang(us) %{_datadir}/xmodmap/xmodmap.us*
%lang(yu) %{_datadir}/xmodmap/xmodmap.yu
