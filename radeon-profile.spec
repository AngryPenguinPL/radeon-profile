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

mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install  ./build/radeon-profile $RPM_BUILD_ROOT/%{_bindir}

%files
%{_bindir}/%{name}
