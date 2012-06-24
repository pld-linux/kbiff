Name:		kbiff
Summary:	KBiff -- Mail notification utility
Summary(pl):	Wska�nik skrzynki pocztowej dla kde
Version:	3.8
Release:	1
License:	GPL
Group:		X11/Applications
URL:		http://kbiff.granroth.org
Source0:	http://dl.sourceforge.net/kbiff/%{name}-%{version}.tar.bz2
# Source0-md5:	97d9f7e24d4928a602f1c89d7ff18755
Patch0:		%{name}.desktop.patch
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An "xbiff"-like mail notification utility. Has multiple pixmaps,
session management, and GUI configuration. Can "dock" into KDE panel.
Can display animated gifs, play system sounds, or run arbitrary shell
command when new mail arrives. Supports mbox, maildir, mh, POP3,
IMAP4, and NNTP mailboxes. Has capability to monitor multiple
mailboxes with one instance. Supports SSL.

%description -l pl
Kbiff jest podobnym do xbiff programem do informowanie on nowej
poczcie. Posiada wiele obrazk�w, zarz�dc� sesji, oraz jest
konfigurowalny przy u�yciu GUI. Dodatkowo mo�e by� zadokowany w panelu
KDE, oraz wy�wietla� animowane gify, odgrywa� d�wi�ki systemowe, lub
uruchamia� odpowiedni� komend� w pow�oce, gdy nadejdzie nowa poczta.
Obs�uguje skrzynki pocztowe w formatach: mbox, maildir, mh, POP3,
IMAP4 oraz NNTP. Posiada mo�liwo�� monitorowania wielu kont na raz.
Dodatkowo obs�uguje SSL.

%prep
%setup -q
%patch0 -p0

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

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING INSTALL kbiff.lsm NEWS README
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_libdir}/%{name}.*
%{_desktopdir}/%{name}.desktop
%{_datadir}/apps/%{name}
%{_datadir}/icons/*/*/apps/%{name}.png
%{_mandir}/man1/*
