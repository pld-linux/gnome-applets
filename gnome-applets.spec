Summary:	Small applications which embed themselves in the GNOME panel
Summary(pl):	GNOME - Aplety
Summary(ru):	Маленькие программы, встраивающиеся в панель GNOME
Summary(uk):	Маленьк╕ програми, що вбудовуються в панель GNOME
Name:		gnome-applets
Version:	1.4.0.5
Release:	8
Epoch:		1
License:	GPL v2, FDL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnome-applets/%{name}-%{version}.tar.bz2
Patch0:		%{name}-applet-docs.make.patch
Patch1:		%{name}-ISDN.patch
Patch2:		%{name}-am_conditional.patch
Patch3:		%{name}-am15.patch
Patch4:		%{name}-ru_omf.patch
Patch5:		%{name}-am_cdplayer_linux_hack.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRequires:	esound-devel >= 0.2.7
BuildRequires:	gdbm-devel
BuildRequires:	gdk-pixbuf-devel >= 0.7.0
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	gnome-core-devel >= 1.1.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libgtop-devel >= 1.0.0
BuildRequires:	libghttp-devel
BuildRequires:	scrollkeeper
BuildRequires:	xml-i18n-tools
Prereq:		/sbin/ldconfig
Prereq:		scrollkeeper
URL:		http://www.gnome.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnotes_applet

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

%description
The gnome-applets package provides Panel applets which enhance your
GNOME experience.

%description -l pl
Aplety pod GNOME.

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
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing
libtoolize --copy --force
gettextize --copy --force
aclocal -I macros
%{__autoconf}
%{__automake}
%configure \
	--disable-static \
	--without-included-gettext
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%postun
/sbin/ldconfig
/usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README

%{_sysconfdir}/CORBA/servers/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/applets/*/*.desktop
%{_datadir}/asclock
%{_datadir}/clockmail
%{_datadir}/geyes
%{_datadir}/gweather
%{_datadir}/odometer
%{_datadir}/sound-monitor
%{_datadir}/tickastat
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/gweather
%{_pixmapsdir}/mini-commander
%{_pixmapsdir}/*.png
%{_pixmapsdir}/*.xpm

%dir %{_datadir}/gnome/gkb
%lang(am) %{_datadir}/gnome/gkb/AM_Armenian.keyprop
%lang(am) %{_datadir}/gnome/gkb/Armenian.keyprop
%lang(az) %{_datadir}/gnome/gkb/AZ_Azerbaidjani_Turkic.keyprop
%lang(eu) %{_datadir}/gnome/gkb/Basque.keyprop
%lang(nl) %{_datadir}/gnome/gkb/BE_Dutch.keyprop
%lang(fr,nl,wa) %{_datadir}/gnome/gkb/Belgian.keyprop
%lang(bg) %{_datadir}/gnome/gkb/BG_*
%lang(pt_BR) %{_datadir}/gnome/gkb/BR_*
%lang(bg) %{_datadir}/gnome/gkb/BulgarianCyril.keyprop
%lang(be) %{_datadir}/gnome/gkb/BY_Belarussian.keyprop
%{_datadir}/gnome/gkb/CA_English.keyprop
%lang(de) %{_datadir}/gnome/gkb/CH_German_x.keyprop
%lang(cs) %{_datadir}/gnome/gkb/CS_Czech.keyprop
%lang(cs,sk) %{_datadir}/gnome/gkb/CZ_Czech_Slovak.keyprop
%lang(cs) %{_datadir}/gnome/gkb/CZ_Czech_x.keyprop
%lang(de) %{_datadir}/gnome/gkb/DE_*
%lang(da) %{_datadir}/gnome/gkb/DK_*
%lang(et) %{_datadir}/gnome/gkb/EE_*
%lang(es) %{_datadir}/gnome/gkb/ES_*
%lang(fi) %{_datadir}/gnome/gkb/FI_*
%lang(fr) %{_datadir}/gnome/gkb/FrenchCanadian2.keyprop
%lang(fr) %{_datadir}/gnome/gkb/FrenchCanadian.keyprop
%lang(fr) %{_datadir}/gnome/gkb/FrenchSwiss.keyprop
%lang(fr) %{_datadir}/gnome/gkb/FR_*
%{_datadir}/gnome/gkb/GB*
%lang(ka) %{_datadir}/gnome/gkb/GE_Georgian_x.keyprop
%lang(ka) %{_datadir}/gnome/gkb/GeorgianLatin.keyprop
%lang(de) %{_datadir}/gnome/gkb/German.keyprop
%lang(de) %{_datadir}/gnome/gkb/GermanSwiss.keyprop
%lang(el) %{_datadir}/gnome/gkb/GR_*
%lang(hu) %{_datadir}/gnome/gkb/HU_*
%lang(hu) %{_datadir}/gnome/gkb/Hungarian*
%lang(he,iw) %{_datadir}/gnome/gkb/IL_*
%lang(is) %{_datadir}/gnome/gkb/IS_*
%lang(it) %{_datadir}/gnome/gkb/IT_*
%lang(jp) %{_datadir}/gnome/gkb/JP_*
%lang(lo) %{_datadir}/gnome/gkb/LA_Lao_x.keyprop
%lang(lt) %{_datadir}/gnome/gkb/LT_*
%lang(mk) %{_datadir}/gnome/gkb/M*acedonian.keyprop
%lang(nl) %{_datadir}/gnome/gkb/NL_Dutch_x.keyprop
%lang(no,nn) %{_datadir}/gnome/gkb/NO_Norwegian.keyprop
%lang(no,nn) %{_datadir}/gnome/gkb/Norwegian.keyprop
%lang(pl) %{_datadir}/gnome/gkb/*olish*
%lang(pt) %{_datadir}/gnome/gkb/Portug*
%lang(pt) %{_datadir}/gnome/gkb/PT_*
%lang(ro) %{_datadir}/gnome/gkb/RO_Romanian.keyprop
%lang(ru) %{_datadir}/gnome/gkb/*Russian*
%lang(sv) %{_datadir}/gnome/gkb/SE_Swedish.keyprop
%lang(sl) %{_datadir}/gnome/gkb/SI_Slovenian.keyprop
%lang(sk) %{_datadir}/gnome/gkb/Slovak.keyprop
%lang(sl) %{_datadir}/gnome/gkb/Slovene.keyprop
%lang(sr,sh) %{_datadir}/gnome/gkb/SR_Dutch.keyprop
%lang(sv) %{_datadir}/gnome/gkb/Swedish.keyprop
%lang(th) %{_datadir}/gnome/gkb/Thai2.keyprop
%lang(th) %{_datadir}/gnome/gkb/Thai.keyprop
%lang(th) %{_datadir}/gnome/gkb/TH_Thai.keyprop
%lang(th) %{_datadir}/gnome/gkb/TH_Thai_x.keyprop
%lang(tr) %{_datadir}/gnome/gkb/TR*
%lang(uk) %{_datadir}/gnome/gkb/UA_Ukrainian.keyprop
%{_datadir}/gnome/gkb/UK.keyprop
%{_datadir}/gnome/gkb/US*
%lang(vi) %{_datadir}/gnome/gkb/VN_Vietnamese.keyprop
%lang(sr,sh) %{_datadir}/gnome/gkb/Yugoslav.keyprop
%lang(sr,sh) %{_datadir}/gnome/gkb/YU_Serbo-Croatian_x.keyprop

%dir %{_datadir}/pixmaps/gkb
%{_datadir}/pixmaps/gkb/*.png
# %lang(ar) %{_datadir}/pixmaps/gkb/ar.png
# %lang(de) %{_datadir}/pixmaps/gkb/at.png
# %lang(fr,nl,wa,de) %{_datadir}/pixmaps/gkb/be.png
# %lang(bg) %{_datadir}/pixmaps/gkb/bg.png
# %lang(pt_BR) %{_datadir}/pixmaps/gkb/br.png
# %{_datadir}/pixmaps/gkb/ca.png
# %lang(de,it,fr) %{_datadir}/pixmaps/gkb/ch.png
# %lang(es) %{_datadir}/pixmaps/gkb/cu.png
# %lang(cs) %{_datadir}/pixmaps/gkb/cz.png
# %lang(de) %{_datadir}/pixmaps/gkb/de.png
# %lang(da) %{_datadir}/pixmaps/gkb/dk.png
# %lang(et) %{_datadir}/pixmaps/gkb/ee.png
# %lang(es) %{_datadir}/pixmaps/gkb/es.png
# %lang(eu) %{_datadir}/pixmaps/gkb/eu.png
# %lang(fi) %{_datadir}/pixmaps/gkb/fi.png
# %lang(fr) %{_datadir}/pixmaps/gkb/fr.png
# %{_datadir}/pixmaps/gkb/gb.png
# %{_datadir}/pixmaps/gkb/gkb-foot.png
# %lang(el) %{_datadir}/pixmaps/gkb/gr.png
# %lang(hr) %{_datadir}/pixmaps/gkb/hr.png
# %lang(hu) %{_datadir}/pixmaps/gkb/hu.png
# %lang(he,iw) %{_datadir}/pixmaps/gkb/il.png
# %lang(is) %{_datadir}/pixmaps/gkb/is.png
# %lang(it) %{_datadir}/pixmaps/gkb/it.png
# %lang(jp) %{_datadir}/pixmaps/gkb/jp.png
# %lang(lt) %{_datadir}/pixmaps/gkb/lt.png
# %lang(mk) %{_datadir}/pixmaps/gkb/mk.png
# %lang(es) %{_datadir}/pixmaps/gkb/mx.png
# %lang(nl) %{_datadir}/pixmaps/gkb/nl.png
# %lang(no,nn) %{_datadir}/pixmaps/gkb/no.png
# %lang(pl) %{_datadir}/pixmaps/gkb/pl.png
# %lang(pt) %{_datadir}/pixmaps/gkb/pt.png
# %lang(fr) %{_datadir}/pixmaps/gkb/qc.png
# %lang(ro) %{_datadir}/pixmaps/gkb/ro.png
# %lang(ru) %{_datadir}/pixmaps/gkb/ru.png
# %lang(sv) %{_datadir}/pixmaps/gkb/se.png
# %lang(sl) %{_datadir}/pixmaps/gkb/si.png
# %lang(sk) %{_datadir}/pixmaps/gkb/sk.png
# %lang(th) %{_datadir}/pixmaps/gkb/th.png
# %lang(tr) %{_datadir}/pixmaps/gkb/tr.png
# %{_datadir}/pixmaps/gkb/un.png
# %{_datadir}/pixmaps/gkb/us.png
# %lang(es) %{_datadir}/pixmaps/gkb/uy.png
# %lang(sr,sh) %{_datadir}/pixmaps/gkb/yu.png

%dir %{_datadir}/xmodmap
%lang(am) %{_datadir}/xmodmap/xmodmap.am*
%lang(fr,wa,de,nl) %{_datadir}/xmodmap/xmodmap.be*
%lang(bg) %{_datadir}/xmodmap/xmodmap.bg*
%lang(pt_BR) %{_datadir}/xmodmap/xmodmap.br*
%lang(de) %{_datadir}/xmodmap/xmodmap.ch*
%lang(cs) %{_datadir}/xmodmap/xmodmap.cz*
%lang(de) %{_datadir}/xmodmap/xmodmap.de*
%lang(da) %{_datadir}/xmodmap/xmodmap.dk*
%{_datadir}/xmodmap/xmodmap.dvorak
%lang(et) %{_datadir}/xmodmap/xmodmap.ee*
%lang(es) %{_datadir}/xmodmap/xmodmap.es*
%lang(fi) %{_datadir}/xmodmap/xmodmap.fi*
%lang(fr) %{_datadir}/xmodmap/xmodmap.fr*
%{_datadir}/xmodmap/xmodmap.gb*
%lang(el) %{_datadir}/xmodmap/xmodmap.gr*
%lang(hu) %{_datadir}/xmodmap/xmodmap.hu*
%lang(he,iw) %{_datadir}/xmodmap/xmodmap.il*
%lang(is) %{_datadir}/xmodmap/xmodmap.is*
%lang(it) %{_datadir}/xmodmap/xmodmap.it*
%lang(es,pt_BR) %{_datadir}/xmodmap/xmodmap.la*
%lang(lt) %{_datadir}/xmodmap/xmodmap.lt*
%lang(mk) %{_datadir}/xmodmap/xmodmap.mk*
%lang(nl) %{_datadir}/xmodmap/xmodmap.nl*
%lang(no,nn) %{_datadir}/xmodmap/xmodmap.no*
%lang(pl) %{_datadir}/xmodmap/xmodmap.pl*
%lang(pt) %{_datadir}/xmodmap/xmodmap.pt*
%lang(fr) %{_datadir}/xmodmap/xmodmap.qc*
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
%lang(sr,sh) %{_datadir}/xmodmap/xmodmap.yu*
