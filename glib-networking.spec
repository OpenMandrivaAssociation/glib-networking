%define name glib-networking
%define version 2.28.4
%define release %mkrel 1
%define libname %mklibname %name
%define giolibname %mklibname gio2.0_ 0
Summary: Network-related GIO modules
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
License: LGPLv2+
Group:System/Libraries
Url: http://www.gnome.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: glib2-devel >= 2.27.90
BuildRequires: libproxy-devel >= 0.3.1
BuildRequires: gnutls-devel >= 2.1.7
BuildRequires: libgcrypt-devel
BuildRequires: intltool

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
rm -rf %{buildroot}
%makeinstall_std
rm -f %buildroot%_libdir/gio/modules/*.la
%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc README

%files -n %libname
%defattr(-,root,root)
%_libdir/gio/modules/*.so
%_libexecdir/glib-pacrunner
%_datadir/dbus-1/services/*.service
