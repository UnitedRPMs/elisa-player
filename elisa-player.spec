%global debug_package %{nil}
%global realname elisa

%bcond_without lang


Name:           elisa-player
Version:        19.12.1
Release:        7%{dist}
Summary:        A simple music player aiming to provide a nice experience for its users
License:        LGPLv3+
Group:		Applications/Multimedia
URL:            https://community.kde.org/Elisa

Source0:	https://github.com/KDE/elisa/archive/v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Baloo) >= 5.32.0
BuildRequires:  cmake(KF5Config) >= 5.32.0
BuildRequires:  cmake(KF5ConfigWidgets) >= 5.32.0
BuildRequires:  cmake(KF5CoreAddons) >= 5.32.0
BuildRequires:  cmake(KF5Crash) >= 5.32.0
BuildRequires:  cmake(KF5DBusAddons) >= 5.32.0
BuildRequires:  cmake(KF5Declarative) >= 5.32.0
BuildRequires:  cmake(KF5DocTools) >= 5.39.0
BuildRequires:  cmake(KF5FileMetaData) >= 5.32.0
BuildRequires:  cmake(KF5I18n) >= 5.32.0
BuildRequires:  cmake(KF5KCMUtils) >= 5.32.0
BuildRequires:  cmake(KF5Package) >= 5.32.0
BuildRequires:  cmake(KF5XmlGui) >= 5.32.0
BuildRequires:  pkgconfig(Qt5Core) >= 5.9.0
BuildRequires:  pkgconfig(Qt5DBus) >= 5.9.0
BuildRequires:  pkgconfig(Qt5Gui) >= 5.9.0
BuildRequires:  pkgconfig(Qt5Multimedia) >= 5.9.0
BuildRequires:  pkgconfig(Qt5Network) >= 5.9.0
BuildRequires:  pkgconfig(Qt5Qml) >= 5.9.0
BuildRequires:  pkgconfig(Qt5Quick) >= 5.9.0
BuildRequires:  pkgconfig(Qt5Sql) >= 5.9.0
BuildRequires:  pkgconfig(Qt5Svg) >= 5.9.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.9.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.9.0 
BuildRequires:	pkgconfig(Qt5QuickWidgets) >= 5.9.0
BuildRequires:  pkgconfig(Qt5QuickControls2) >= 5.9.0
BuildRequires:	vlc-devel
BuildRequires:	kf5-kirigami2-devel
BuildRequires:	qt5-qtbase-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib
Requires:	elementary-theme
Requires:	elementary-icon-theme

%description
Elisa is a music player with a library where music can be browsed by
album, artist or all tracks. It is indexed using either a private
indexer or an indexer using Baloo. The private one can be configured
to scan music on chosen paths. The Baloo one is faster because Baloo
is providing all needed data from its own database. Play-lists can be
built and played.


%prep
%autosetup -n %{realname}-%{version}

%build
mkdir %{_target_platform}
pushd %{_target_platform}
cmake \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib64 \
    -DBUILD_TESTING=OFF ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

  %if ! %{with lang}
    %find_lang %{realname} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif

%post
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi



%if ! %{with lang}
%files -f %{realname}.lang
%else
%files 
%endif
%doc README*
%license COPYING* 
%{_kf5_bindir}/elisa
%{_kf5_datadir}/applications/org.kde.elisa.desktop
%{_kf5_docdir}/HTML/*/elisa/
%{_kf5_datadir}/icons/hicolor/*/apps/elisa.png
%{_kf5_datadir}/icons/hicolor/scalable/apps/elisa.svg
%{_kf5_libdir}/elisa/libelisaLib.so.*
%{_kf5_datadir}/metainfo/*.appdata.xml
%{_kf5_libdir}/qt5/qml/org/kde/elisa/libelisaqmlplugin.so
%{_kf5_libdir}/qt5/qml/org/kde/elisa/qmldir
%{_kf5_datadir}/qlogging-categories5/elisa.categories

%changelog

* Sat Jan 25 2020 David Va <davidva AT tuta DOT io> 19.12.1-1
- Updated to 19.12.1

* Fri Nov 22 2019 David Va <davidva AT tuta DOT io> 19.11.80-1
- Updated to 19.11.80

* Thu Jul 11 2019 David Va <davidva AT tuta DOT io> 0.4.2-1
- Updated to 0.4.2

* Sat May 25 2019 David Va <davidva AT tuta DOT io> 0.4.0-1
- Updated to 0.4.0

* Thu May 16 2019 David Va <davidva AT tuta DOT io> 0.3.80-1
- Updated to 0.3.80

* Mon Oct 01 2018 David Va <davidva AT tuta DOT io> 0.3.0-1
- Updated to 0.3.0

* Sat Sep 08 2018 David Va <davidva AT tuta DOT io> 0.2.80-1
- Updated to 0.2.80

* Fri Jul 13 2018 David Va <davidva AT tuta DOT io> 0.2.1-1
- Updated to 0.2.1

* Wed Jul 04 2018 David Vásquez <davidva AT tuta DOT io> 0.2.0-1
- Updated to 0.2.0

* Thu Jun 14 2018 David Vásquez <davidva AT tuta DOT io> 0.1.80-1
- Updated to 0.1.80

* Wed Apr 18 2018 David Vásquez <davidva AT tutanota DOT com> 0.1.1-1
- Updated to 0.1.1

* Fri Apr 13 2018 David Vásquez <davidva AT tutanota DOT com> 0.1-1
- Initial packaging of elisa
