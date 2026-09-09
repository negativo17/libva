Name:       libva
Epoch:      1
Version:    2.24.1
Release:    1%{?dist}
Summary:    Implementation for VA-API (Video Acceleration API)
License:    MIT
URL:        https://01.org/linuxmedia/vaapi

Source0:    https://github.com/intel/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  meson >= 0.53.0
BuildRequires:  pkgconfig(libdrm) >= 2.4.75
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(wayland-client) >= 1.11.0
BuildRequires:  pkgconfig(wayland-scanner) >= 1.15.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-dri3)
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

%build
%meson \
  -D with_x11=yes \
  -D with_glx=yes \
  -D with_wayland=yes \
  -D enable_docs=true \
  -D with_legacy=nvctrl

%meson_build

%install
%meson_install

# Let RPM pick up docs
rm -fr %{buildroot}%{_docdir}/%{name}

%files
%doc NEWS
%license COPYING
%ghost %{_sysconfdir}/libva.conf
%{_libdir}/libva-drm.so.2.*
%{_libdir}/libva-drm.so.2
%{_libdir}/libva-glx.so.2.*
%{_libdir}/libva-glx.so.2
%{_libdir}/libva.so.2.*
%{_libdir}/libva.so.2
%{_libdir}/libva-wayland.so.2.*
%{_libdir}/libva-wayland.so.2
%{_libdir}/libva-x11.so.2.*
%{_libdir}/libva-x11.so.2

%files devel
%doc %_vpath_builddir/doc/html-out
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
* Wed Sep 09 2026 Simone Caronni <negativo17@gmail.com> - 1:2.24.1-1
- Update to 2.24.1.

* Fri Dec 19 2025 Simone Caronni <negativo17@gmail.com> - 1:2.23.0-1
- Update to 2.23.0.

* Tue Jun 25 2024 Simone Caronni <negativo17@gmail.com> - 1:2.22.0-1
- Update to 2.22.0.

* Tue Mar 12 2024 Simone Caronni <negativo17@gmail.com> - 1:2.21.0-1
- Update to 2.21.0.

* Thu Sep 28 2023 Simone Caronni <negativo17@gmail.com> - 1:2.20.0-1
- Update to 2.20.0.

* Tue Jul 11 2023 Simone Caronni <negativo17@gmail.com> - 1:2.19.0-1
- Update to 2.19.0.

* Tue Apr 11 2023 Simone Caronni <negativo17@gmail.com> - 1:2.18.0-1
- Update to 2.18.0.

* Wed Feb 08 2023 Simone Caronni <negativo17@gmail.com> - 1:2.17.0-2
- Backport patch to disable DRI3 (LIBVA_DRI3_DISABLE=1).
- Enable nvctrl support to fix nvidia-vaapi-driver.

* Thu Jan 26 2023 Simone Caronni <negativo17@gmail.com> - 1:2.17.0-1
- Update to 2.17.0.
