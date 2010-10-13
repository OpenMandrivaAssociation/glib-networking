%define name glib-networking
%define version 2.26.0
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
BuildRequires: glib2-devel >= 2.25
BuildRequires: libproxy-devel
BuildRequires: intltool

%description
This package contains the network-related GIO modules for Glib.

%package -n %libname
Summary: Network-related GIO modules
Group:System/Libraries
Requires: %name >= %version-%release
Requires(post): %giolibname >= 2.23.4-2mdv
Requires(postun): %giolibname >= 2.23.4-2mdv

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

%post -n %{libname}
%if %_lib != lib
 %{_bindir}/gio-querymodules-64 %{_libdir}/gio/modules 
%else
 %{_bindir}/gio-querymodules-32 %{_libdir}/gio/modules
%endif

%postun -n %{libname}
if [ "$1" = "0" ]; then
%if %_lib != lib
 %{_bindir}/gio-querymodules-64 %{_libdir}/gio/modules 
%else
 %{_bindir}/gio-querymodules-32 %{_libdir}/gio/modules
%endif
fi

%files -f %name.lang
%defattr(-,root,root)
%doc README


%files -n %libname
%defattr(-,root,root)
%_libdir/gio/modules/libgiolibproxy.so
