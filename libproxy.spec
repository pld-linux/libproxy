Summary:	Library for automatic proxy configuration management
Summary(pl.UTF-8):	Biblioteka do automatycznego zarządzania konfiguracją proxy
Name:		libproxy
Version:	0.2.3
Release:	5
License:	LGPL v2
Group:		Libraries
Source0:	http://libproxy.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	86b635e1eb2d665cfbef4c6134fe6604
Patch0:		%{name}-dbus.patch
Patch1:		%{name}-asneeded.patch
URL:		http://code.google.com/p/libproxy/
BuildRequires:	GConf2-devel
BuildRequires:	NetworkManager-devel
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	gtk-webkit-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xulrunner-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for automatic proxy configuration management.

%description -l pl.UTF-8
Biblioteka do automatycznego zarządzania konfiguracją proxy.

%package devel
Summary:	Header files for libproxy library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libproxy
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libproxy library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libproxy.

%package static
Summary:	Static libproxy library
Summary(pl.UTF-8):	Statyczna biblioteka libproxy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libproxy library.

%description static -l pl.UTF-8
Statyczna biblioteka libproxy.

%package -n python-libproxy
Summary:	libproxy Python bindings
Summary(pl.UTF-8):	Wiązania libproxy dla Pythona
Group:		Libraries/Python
# uses libproxy shared library
Requires:	%{name} = %{version}-%{release}

%description -n python-libproxy
libproxy Python bindings.

%description -n python-libproxy -l pl.UTF-8
Wiązania libproxy dla Pythona.


%package gnome
Summary:	Plugin for libproxy and gnome
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gnome
The libproxy-gnome package contains the libproxy plugin for gnome.


%package kde
Summary:	Plugin for libproxy and kde
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description kde
The libproxy-kde package contains the libproxy plugin for kde.


%package mozjs
Summary:	Plugin for %{name} and mozjs
Group:		Libraries
Requires:	%{name} = %{version}

%description mozjs
The libproxy-mozjs package contains the libproxy plugin for mozjs.


%package webkit
Summary:	Plugin for %{name} and webkit
Group:		Libraries
Requires:	%{name} = %{version}

%description webkit
The libproxy-webkit package contains the libproxy plugin for webkit.


%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/proxy
%attr(755,root,root) %{_libdir}/libproxy.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libproxy.so.0
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/%{version}
%dir %{_libdir}/%{name}/%{version}/plugins
%attr(755,root,root) %{_libdir}/%{name}/%{version}/plugins/envvar.so
%attr(755,root,root) %{_libdir}/%{name}/%{version}/plugins/file.so
%attr(755,root,root) %{_libdir}/%{name}/%{version}/plugins/networkmanager.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libproxy.so
%{_libdir}/libproxy.la
%{_includedir}/*.h
%{_pkgconfigdir}/libproxy-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libproxy.a

%files -n python-libproxy
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.py[co]

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/%{version}/plugins/gnome.so

%files kde
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/%{version}/plugins/kde.so

%files mozjs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/%{version}/plugins/mozjs.so

%files webkit
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/%{version}/plugins/webkit.so
