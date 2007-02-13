Summary:	KBiff - Mail notification utility
Summary(pl.UTF-8):	Wskaźnik skrzynki pocztowej dla kde
Name:		kbiff
Version:	3.8
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kbiff/%{name}-%{version}.tar.bz2
# Source0-md5:	97d9f7e24d4928a602f1c89d7ff18755
Patch0:		%{name}.desktop.patch
URL:		http://kbiff.granroth.org/
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An "xbiff"-like mail notification utility. Has multiple pixmaps,
session management, and GUI configuration. Can "dock" into KDE panel.
Can display animated gifs, play system sounds, or run arbitrary shell
command when new mail arrives. Supports mbox, maildir, mh, POP3,
IMAP4, and NNTP mailboxes. Has capability to monitor multiple
mailboxes with one instance. Supports SSL.

%description -l pl.UTF-8
Kbiff jest podobnym do xbiff programem do informowania o nowej
poczcie. Posiada wiele obrazków i zarządcę sesji oraz jest
konfigurowalny przy użyciu GUI. Dodatkowo może być zadokowany w panelu
KDE oraz wyświetlać animowane gify, odgrywać dźwięki systemowe lub
uruchamiać odpowiednią komendę w powłoce, gdy nadejdzie nowa poczta.
Obsługuje skrzynki pocztowe w formatach: mbox, maildir, mh, POP3,
IMAP4 oraz NNTP. Ma możliwość monitorowania wielu kont na raz.
Dodatkowo obsługuje SSL.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
%configure \
	--disable-debug \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install-strip \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	appsdir=%{_desktopdir}

mv $RPM_BUILD_ROOT%{_iconsdir}/{l,L}ocolor
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{no,nb}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{no_NY,nn}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/zh_TW{.Big5,}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}.so
%{_libdir}/%{name}.la
%{_desktopdir}/%{name}.desktop
%{_datadir}/apps/%{name}
%{_iconsdir}/*/*/apps/%{name}.png
%{_mandir}/man1/*
