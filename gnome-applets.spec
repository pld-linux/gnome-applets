Summary:	Small applications which embed themselves in the GNOME panel
Summary(pl):	GNOME - Applety
Name:		gnome-applets
Version:	1.1.5
Release:	1
License:	GPL
Group:		X11/GNOME
Group(pl):	X11/GNOME
Source:		ftp://ftp.gnome.org/pub/GNOME/unstable/sources/gnome-applets/%{name}-%{version}.tar.gz
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	gnome-core-devel >= 1.1.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	esound-devel >= 0.2.7
BuildRequires:	libgtop-devel >= 1.0.0
BuildRequires:	libghttp-devel
BuildRequires:	xmms-devel
BuildRequires:	gdbm-devel
URL:		http://www.gnome.org/
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	gnotes_applet
Obsoletes:	gnome-applets-gumma-gqmpeg
Obsoletes:	gnome-applets-gumma-xmms

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var

%description
The gnome-applets package provides Panel applets which
enhance your GNOME experience.

%description -l pl
Applety pod GNOME.

%package gumma-gqmpeg
Summary:	Gqmpe sound plug-in for gumma GNOME applet
Summary(pl):	Wtyczka do apletu gumma GNOME do odtwarzania d¼wiêku z u¿yciem gqmpeg
Group:		X11/GNOME
Group(pl):	X11/GNOME
Requires:	%{name} = %{version}
Requires:	gqmpeg

%description gumma-gqmpeg
Gqmpe sound plug-in for gumma GNOME applet.

%description -l pl gumma-gqmpeg
Wtyczka do apletu gumma GNOME do odtwarzania d¼wiêku z u¿yciem gqmpeg.

%package gumma-xmms
Summary:	Xmms sound plug-in for gumma GNOME applet
Summary(pl):	Wtyczka do apletu gumma GNOME do odtwarzania d¼wiêku z u¿yciem xmms
Group:		X11/GNOME
Group(pl):	X11/GNOME
Requires:	%{name} = %{version}
Requires:	xmms

%description gumma-xmms
Xmms sound plug-in for gumma GNOME applet.

%description -l pl gumma-xmms
Wtyczka do apletu gumma GNOME do odtwarzania d¼wiêku z u¿yciem xmms.

%prep
%setup -q

%build
gettextize --copy --force
automake
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure \
	--disable-static
make
#make -C gumma

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT -C gumma

#strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/gumma/lib*.so

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS.gz ChangeLog.gz NEWS.gz README.gz

%{_sysconfdir}/CORBA/servers/*
%attr(755,root,root) %{_bindir}/*
#%dir %{_libdir}/gumma
#%attr(755,root,root) %{_libdir}/gumma/libgumma-cd*
%{_datadir}/applets/*/*
%{_datadir}/asclock
%{_datadir}/clockmail
%{_datadir}/geyes
%{_datadir}/gweather
%{_datadir}/odometer
%{_datadir}/sound-monitor
%{_datadir}/tickastat
%{_datadir}/pixmaps/gweather
%{_datadir}/pixmaps/mini-commander
%{_datadir}/pixmaps/*.png
%{_datadir}/pixmaps/*.xpm
%{_datadir}/gnome/help/gweather
%{_datadir}/gnome/help/mini-commander_applet

%dir %{_datadir}/pixmaps/gkb
%lang(at) %{_datadir}/pixmaps/gkb/at.xpm
%lang(be) %{_datadir}/pixmaps/gkb/be.xpm
%lang(bg) %{_datadir}/pixmaps/gkb/bg.xpm
%lang(br) %{_datadir}/pixmaps/gkb/br.xpm
%lang(ca) %{_datadir}/pixmaps/gkb/ca.xpm
%lang(ch) %{_datadir}/pixmaps/gkb/ch.xpm
%lang(cz) %{_datadir}/pixmaps/gkb/cz.xpm
%lang(de) %{_datadir}/pixmaps/gkb/de.xpm
%lang(dk) %{_datadir}/pixmaps/gkb/dk.xpm
%lang(ee) %{_datadir}/pixmaps/gkb/ee.xpm
%lang(es) %{_datadir}/pixmaps/gkb/es.xpm
%lang(fi) %{_datadir}/pixmaps/gkb/fi.xpm
%lang(fr) %{_datadir}/pixmaps/gkb/fr.xpm
%lang(gb) %{_datadir}/pixmaps/gkb/gb.xpm
%lang(gr) %{_datadir}/pixmaps/gkb/gr.xpm
%lang(hu) %{_datadir}/pixmaps/gkb/hu.xpm
%lang(il) %{_datadir}/pixmaps/gkb/il.xpm
%lang(is) %{_datadir}/pixmaps/gkb/is.xpm
%lang(it) %{_datadir}/pixmaps/gkb/it.xpm
%lang(jp) %{_datadir}/pixmaps/gkb/jp.xpm
%lang(mx) %{_datadir}/pixmaps/gkb/mx.xpm
%lang(nl) %{_datadir}/pixmaps/gkb/nl.xpm
%lang(no) %{_datadir}/pixmaps/gkb/no.xpm
%lang(pl) %{_datadir}/pixmaps/gkb/pl.xpm
%lang(pt) %{_datadir}/pixmaps/gkb/pt.xpm
%lang(qc) %{_datadir}/pixmaps/gkb/qc.xpm
%lang(ru) %{_datadir}/pixmaps/gkb/ru.xpm
%lang(se) %{_datadir}/pixmaps/gkb/se.xpm
%lang(si) %{_datadir}/pixmaps/gkb/si.xpm
%lang(sk) %{_datadir}/pixmaps/gkb/sk.xpm
%lang(th) %{_datadir}/pixmaps/gkb/th.xpm
%lang(tr) %{_datadir}/pixmaps/gkb/tr.xpm
%lang(un) %{_datadir}/pixmaps/gkb/un.xpm
%lang(us) %{_datadir}/pixmaps/gkb/us.xpm
%lang(uy) %{_datadir}/pixmaps/gkb/uy.xpm
%lang(yu) %{_datadir}/pixmaps/gkb/yu.xpm

%dir %{_datadir}/xmodmap
%{_datadir}/xmodmap/xmodmap.dvorak
%lang(be) %{_datadir}/xmodmap/xmodmap.be
%lang(bg) %{_datadir}/xmodmap/xmodmap.bg
%lang(ch) %{_datadir}/xmodmap/xmodmap.ch
%lang(cz) %{_datadir}/xmodmap/xmodmap.cz
%lang(de) %{_datadir}/xmodmap/xmodmap.de
%lang(dk) %{_datadir}/xmodmap/xmodmap.dk
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

#%files gumma-gqmpeg
#%attr(755,root,root) %{_libdir}/gumma/libgumma-gqmpeg*

#%files gumma-xmms
#%attr(755,root,root) %{_libdir}/gumma/libgumma-xmms*
