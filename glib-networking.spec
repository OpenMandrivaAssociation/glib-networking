%define name glib-networking
%define version 2.30.2
%define release 1
%define libname %mklibname %name

Summary: Network-related GIO modules
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
License: LGPLv2+
Group:System/Libraries
Url: http://www.gnome.org/
BuildRequires: glib2-devel >= 2.27.90
BuildRequires: libproxy-devel >= 0.3.1
BuildRequires: gnutls-devel >= 2.1.7
BuildRequires: libgcrypt-devel
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: intltool
Requires: %libname = %version

%description
This package contains the network-related GIO modules for Glib.

%package -n %libname
Summary: Network-related GIO modules
Group: System/Libraries
Requires: %name >= %version-%release

%description -n %libname
This package contains the network-related GIO modules for Glib.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std
rm -f %buildroot%_libdir/gio/modules/*.la
%find_lang %name

%files -f %name.lang
%doc README
%_libexecdir/glib-pacrunner
%_datadir/dbus-1/services/*.service

%files -n %libname
%_libdir/gio/modules/*.so
