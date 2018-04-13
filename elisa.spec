Name:           elisa
Version:        0.1
Release:        1%{dist}
Summary:        A simple music player aiming to provide a nice experience for its users
License:        LGPLv3+
Group:		Applications/Multimedia
URL:            https://community.kde.org/Elisa

Source0:	https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
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
%autosetup 

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5}  \
    -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=OFF -DKDE_INSTALL_USE_QT_SYS_PATHS=ON ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang %{name} --with-kde
%find_lang kcm_elisa_local_file

%check
desktop-file-validate %{buildroot}/%{_kf5_datadir}/applications/org.kde.elisa.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_kf5_datadir}/metainfo/org.kde.elisa.appdata.xml

%post
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :

%files -f %{name}.lang -f kcm_elisa_local_file.lang
%doc README*
%license COPYING* LICENSE*
%{_kf5_bindir}/elisa
%{_kf5_qtplugindir}/kcms/kcm_elisa_local_file.so
%{_kf5_datadir}/applications/org.kde.elisa.desktop
%{_kf5_docdir}/HTML/*/elisa/
%{_kf5_datadir}/icons/hicolor/*/apps/elisa.png
%{_kf5_datadir}/icons/hicolor/scalable/apps/elisa.svg
%{_kf5_datadir}/kpackage/kcms/kcm_elisa_local_file/
%{_kf5_datadir}/kservices5/kcm_elisa_local_file.desktop
%{_kf5_datadir}/metainfo/org.kde.elisa.appdata.xml


%changelog

* Fri Apr 13 2018 David Vásquez <davidva AT tutanota DOT com> 0.1-1
- Initial packaging of elisa
