Summary:	Small applications which embed themselves in the GNOME panel
Summary(pl):	GNOME - Applety
Name:		gnome-applets
Version:	1.2.1
Release:	6
License:	GPL
Group:		X11/GNOME
Group(de):	X11/GNOME
Group(pl):	X11/GNOME
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnome-applets/%{name}-%{version}.tar.gz
Source1:	http://www.brendy.addr.com/linux/gnomesensors/GnomeSensors-0.2.0.tar.gz
Patch0:		%{name}-applet-docs.make.patch
Patch1:		%{name}-sensors.patch
BuildRequires:	esound-devel >= 0.2.7
BuildRequires:	gdbm-devel
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	gnome-core-devel >= 1.1.0
BuildRequires:	gdk-pixbuf-devel >= 0.7.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libgtop-devel >= 1.0.0
BuildRequires:	libghttp-devel
BuildRequires:	xmms-devel
BuildRequires:	lm_sensors-devel
URL:		http://www.gnome.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnotes_applet
Obsoletes:	gnome-applets-gumma-gqmpeg
Obsoletes:	gnome-applets-gumma-xmms

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var

%description
The gnome-applets package provides Panel applets which enhance your
GNOME experience.

%description -l pl
Applety pod GNOME.

%package gumma-gqmpeg
Summary:	Gqmpe sound plug-in for gumma GNOME applet
Summary(pl):	Wtyczka do apletu gumma GNOME do odtwarzania d¼wiêku z u¿yciem gqmpeg
Group:		X11/GNOME
Group(de):	X11/GNOME
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
Group(de):	X11/GNOME
Group(pl):	X11/GNOME
Requires:	%{name} = %{version}
Requires:	xmms

%description gumma-xmms
Xmms sound plug-in for gumma GNOME applet.

%description -l pl gumma-xmms
Wtyczka do apletu gumma GNOME do odtwarzania d¼wiêku z u¿yciem xmms.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1

%build
gettextize --copy --force
%configure \
	--disable-static
%{__make}
#make -C gumma

cd GnomeSensors-0.2.0
%configure \
	--disable-static
%{__make} gnorbadir=%{_sysconfdir}/CORBA/servers

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT \
	gnorbadir=%{_sysconfdir}/CORBA/servers -C GnomeSensors-0.2.0
#%{__make} install DESTDIR=$RPM_BUILD_ROOT -C gumma

#strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/gumma/lib*.so

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

%dir %{_datadir}/pixmaps/gkb
%lang(at) %{_datadir}/pixmaps/gkb/at.png
%lang(be) %{_datadir}/pixmaps/gkb/be.png
%lang(bg) %{_datadir}/pixmaps/gkb/bg.png
%lang(br) %{_datadir}/pixmaps/gkb/br.png
%lang(ca) %{_datadir}/pixmaps/gkb/ca.png
%lang(ch) %{_datadir}/pixmaps/gkb/ch.png
%lang(cz) %{_datadir}/pixmaps/gkb/cz.png
%lang(de) %{_datadir}/pixmaps/gkb/de.png
%lang(dk) %{_datadir}/pixmaps/gkb/dk.png
%lang(ee) %{_datadir}/pixmaps/gkb/ee.png
%lang(es) %{_datadir}/pixmaps/gkb/es.png
%lang(fi) %{_datadir}/pixmaps/gkb/fi.png
%lang(fr) %{_datadir}/pixmaps/gkb/fr.png
%lang(gb) %{_datadir}/pixmaps/gkb/gb.png
%lang(gr) %{_datadir}/pixmaps/gkb/gr.png
%lang(hu) %{_datadir}/pixmaps/gkb/hu.png
%lang(il) %{_datadir}/pixmaps/gkb/il.png
%lang(is) %{_datadir}/pixmaps/gkb/is.png
%lang(it) %{_datadir}/pixmaps/gkb/it.png
%lang(jp) %{_datadir}/pixmaps/gkb/jp.png
%lang(mx) %{_datadir}/pixmaps/gkb/mx.png
%lang(nl) %{_datadir}/pixmaps/gkb/nl.png
%lang(no) %{_datadir}/pixmaps/gkb/no.png
%lang(pl) %{_datadir}/pixmaps/gkb/pl.png
%lang(pt) %{_datadir}/pixmaps/gkb/pt.png
%lang(qc) %{_datadir}/pixmaps/gkb/qc.png
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
