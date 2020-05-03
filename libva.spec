%global     soname_version 2.700.0

Name:       libva
Epoch:      1
Version:    2.7.1
Release:    1%{?dist}
Summary:    Implementation for VA-API (Video Acceleration API)
License:    MIT
URL:        https://01.org/linuxmedia/vaapi

Source0:    https://github.com/intel/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(wayland-client) >= 1.11.0
BuildRequires:  pkgconfig(wayland-scanner) >= 1.11.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)

%description
VA-API is an open-source library and API specification, which provides access to
graphics hardware acceleration capabilities for video processing. It consists of
a main library and driver-specific acceleration backends for each supported
hardware vendor.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{_isa} = %{epoch}:%{version}-%{release}
Requires:	pkgconfig

%description	devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -p1
autoreconf -vif

%build
%configure \
    --disable-static \
    --enable-drm \
    --enable-glx \
    --enable-va-messaging \
    --enable-wayland \
    --enable-x11

%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete

%ldconfig_scriptlets

%files
%doc NEWS
%license COPYING
%ghost %{_sysconfdir}/libva.conf
%{_libdir}/libva-drm.so.%{soname_version}
%{_libdir}/libva-drm.so.2
%{_libdir}/libva-glx.so.%{soname_version}
%{_libdir}/libva-glx.so.2
%{_libdir}/libva.so.%{soname_version}
%{_libdir}/libva.so.2
%{_libdir}/libva-wayland.so.%{soname_version}
%{_libdir}/libva-wayland.so.2
%{_libdir}/libva-x11.so.%{soname_version}
%{_libdir}/libva-x11.so.2

%files devel
%{_includedir}/va
%{_libdir}/libva-drm.so
%{_libdir}/libva-glx.so
%{_libdir}/libva.so
%{_libdir}/libva-x11.so
%{_libdir}/libva-wayland.so
%{_libdir}/pkgconfig/libva-drm.pc
%{_libdir}/pkgconfig/libva-glx.pc
%{_libdir}/pkgconfig/libva.pc
%{_libdir}/pkgconfig/libva-x11.pc
%{_libdir}/pkgconfig/libva-wayland.pc

%changelog
* Sat May 02 2020 Simone Caronni <negativo17@gmail.com> - 1:2.7.1-1
- First build.