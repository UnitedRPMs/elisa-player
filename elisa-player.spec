#
# spec file for package elisa-player
#
# Copyright (c) 2021 UnitedRPMs.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://goo.gl/zqFJft
#

# elisa-player
%global commit0 761c696bb46a1d3afd4fc09a2f6aaca1d5b5fb77
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# upnp-lib-qt
%global commit1 df9e77c1471e2ae0eba1516bb9632dd1015f9a87
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

%global debug_package %{nil}
%global realname elisa
# 
#define _legacy_common_support 1

Name:           elisa-player
Version:        21.08.0
Release:        7%{dist}
Summary:        A simple music player aiming to provide a nice experience for its users
License:        LGPLv3+
Group:		Applications/Multimedia
URL:            https://community.kde.org/Elisa

Source0:	https://github.com/KDE/elisa/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
#Source1:	https://github.com/KDE/upnp-lib-qt/archive/%{commit1}.tar.gz#/upnp-lib-qt-%{shortcommit1}.tar.gz
Patch:		fixes.patch
BuildRequires:  cmake
	
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickTest)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Baloo)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5FileMetaData)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Package)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  qt5-qtbase-private-devel

BuildRequires:	vlc-devel
BuildRequires:	desktop-file-utils

# Not yet ready
#BuildRequires:	upnp-player-qt-devel
#BuildRequires:	kdsoap-devel
	
Requires:       hicolor-icon-theme
Requires:       kde-filesystem
Requires:       qt5-qtquickcontrols
Recommends:	elementary-theme
Recommends:	elementary-icon-theme
Recommends:	humanity-icon-theme


%description
Elisa is a music player with a library where music can be browsed by
album, artist or all tracks. It is indexed using either a private
indexer or an indexer using Baloo. The private one can be configured
to scan music on chosen paths. The Baloo one is faster because Baloo
is providing all needed data from its own database. Play-lists can be
built and played.


%prep
%autosetup -n %{realname}-%{commit0}  -p1
#rm -rf src/upnp/
#mv -f upnp-lib-qt-%{commit1}/src src/upnp


%build
mkdir -p build
%cmake -B build -DCMAKE_INSTALL_LIBDIR=lib64 -DBUILD_TESTING=OFF 

%make_build -C build

%install
%make_install -C build

#find_lang --all-name --with-kde --with-html


%post
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi



%files 
#-f %{realname}.lang
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
%{_kf5_libdir}/qt5/qml/org/kde/elisa/plugins.qmltypes
%{_kf5_datadir}/qlogging-categories5/elisa.categories

%changelog

* Mon Aug 16 2021 David Va <davidva AT tuta DOT io> 21.07.80-7
- Updated to 21.08.0

* Wed Jul 28 2021 David Va <davidva AT tuta DOT io> 21.07.80-7
- Updated to 21.07.80

* Mon Jun 28 2021 David Va <davidva AT tuta DOT io> 21.04.2-7
- Updated to 21.04.2

* Sat May 22 2021 David Va <davidva AT tuta DOT io> 21.04.1-7
- Updated to 21.04.1

* Mon Apr 26 2021 David Va <davidva AT tuta DOT io> 21.04.0-7
- Updated to 21.04.0

* Sat Mar 20 2021 David Va <davidva AT tuta DOT io> 20.12.3-7
- Updated to 20.12.3

* Mon Feb 15 2021 David Va <davidva AT tuta DOT io> 20.12.2-7
- Updated to 20.12.2

* Mon Jan 25 2021 David Va <davidva AT tuta DOT io> 20.12.1-7
- Updated to 20.12.1

* Sun Dec 20 2020 David Va <davidva AT tuta DOT io> 20.12.0-7
- Updated to 20.12.0

* Sat Oct 10 2020 David Va <davidva AT tuta DOT io> 20.08.2-7
- Updated to 20.08.2

* Mon Sep 14 2020 David Va <davidva AT tuta DOT io> 20.08.1-7
- Updated to 20.08.1

* Thu Aug 27 2020 David Va <davidva AT tuta DOT io> 20.08.0-7
- Updated to 20.08.0

* Sat Aug 08 2020 David Va <davidva AT tuta DOT io> 20.07.90-7
- Updated to 20.07.90

* Thu Jul 09 2020 David Va <davidva AT tuta DOT io> 20.04.3-7
- Updated to 20.04.3

* Thu Jun 11 2020 David Va <davidva AT tuta DOT io> 20.04.2-7
- Updated to 20.04.2

* Sat May 16 2020 David Va <davidva AT tuta DOT io> 20.04.1-7
- Added recommends humanity-icon-theme
- Updated to 20.04.1

* Sat May 02 2020 David Va <davidva AT tuta DOT io> 20.04.0-7
- Updated to 20.04.0

* Wed Mar 11 2020 David Va <davidva AT tuta DOT io> 19.12.3-7
- Updated to 19.12.3

* Fri Feb 07 2020 David Va <davidva AT tuta DOT io> 19.12.2-7
- Updated to 19.12.2

* Sat Jan 25 2020 David Va <davidva AT tuta DOT io> 19.12.1-7
- Updated to 19.12.1

* Fri Nov 22 2019 David Va <davidva AT tuta DOT io> 19.11.80-7
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
