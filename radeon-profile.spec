Name:           radeon-profile
Version:        20190311
Release:        1
Summary:        Application to read current clocks of ATi Radeon cards (xf86-video-ati, xf86-video-amdgpu) 
License:        GPL2.0
Group:          System/Configuration/Hardware
URL:            https://github.com/marazmista/radeon-profile
Source0:        https://github.com/marazmista/radeon-profile/archive/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  qmake5
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Charts)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5QuickWidgets)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ninja

Requires:       glxinfo
Requires:       xdriinfo
Requires:       xrandr


%description
Application to read current clocks of ATi Radeon cards (xf86-video-ati, xf86-video-amdgpu) 

%prep
%setup -q

%build
mkdir -p build
cd build
qmake-qt5 "../radeon-profile/"
make

#make_build

%install
#mkdir -p $RPM_BUILD_ROOT/%{_bindir}
#install  ./build/radeon-profile $RPM_BUILD_ROOT/%{_bindir}
#cd radeon-profile
#make install INSTALL_ROOT="%{buildroot}"
cd radeon-profile
install -Dm755 "radeon-profile" "%{buildroot}%{_bindir}/radeon-profile"
install -Dm644 "extra/radeon-profile.png" "%{buildroot}%{_datadir}/pixmaps/radeon-profile.png"
install -Dm644 "extra/radeon-profile.desktop" "%{buildroot}%{_datadir}/applications/radeon-profile.desktop"
cd translations
for t in $(ls *.qm); do install -Dm644 "$t" "%{buildroot}%{_datadir}/radeon-profile/$t"; done

%files
%license LICENSE
%{_bindir}/radeon-profile
%{_datadir}/applications/radeon-profile.desktop
%{_datadir}/icons/hicolor/512x512/apps/radeon-profile.png
