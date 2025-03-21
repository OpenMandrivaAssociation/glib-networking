%define url_ver %(echo %{version}|cut -d. -f1,2)
%define libname %mklibname %{name}

Summary:	Network-related GIO modules
Name:		glib-networking
Version:	2.80.1
Release:	2
License:	LGPLv2+
Group:		System/Libraries
Url:		https://www.gnome.org/
Source0:	https://ftp.gnome.org/pub/GNOME/sources/glib-networking/%{url_ver}/%{name}-%{version}.tar.xz
#Patch0:		glib-networking-2.64.0-try-harder-to-set-gnutls-priorities.patch

BuildRequires:	intltool
BuildRequires:	meson
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  glib-gir
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(libproxy-1.0)
BuildRequires:	pkgconfig(p11-kit-1)
Requires:	%{libname} = %{version}-%{release}
Requires:	gsettings-desktop-schemas
Requires:	ca-certificates

%description
This package contains the network-related GIO modules for Glib.

%package -n %{libname}
Summary:	Network-related GIO modules
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}

%description -n %{libname}
This package contains the network-related GIO modules for Glib.

%prep
%autosetup -p1
%meson

%build
%meson_build

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
%doc README
%{_libexecdir}/glib-pacrunner
%{_datadir}/dbus-1/services/*.service
%{_userunitdir}/glib-pacrunner.service

%files -n %{libname}
%{_libdir}/gio/modules/*.so
