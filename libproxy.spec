#
# Conditional build:
%bcond_without	webkit	# WebKit plugin
#
Summary:	Library for automatic proxy configuration management
Summary(pl.UTF-8):	Biblioteka do automatycznego zarządzania konfiguracją proxy
Name:		libproxy
Version:	0.2.3
Release:	6
License:	LGPL v2
Group:		Libraries
#Source0Download: http://code.google.com/p/libproxy/downloads/list
Source0:	http://libproxy.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	86b635e1eb2d665cfbef4c6134fe6604
Patch0:		%{name}-dbus.patch
Patch1:		%{name}-asneeded.patch
URL:		http://code.google.com/p/libproxy/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	NetworkManager-devel
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
%{?with_webkit:BuildRequires:	gtk-webkit-devel}
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	xorg-lib-libX11-devel
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

%package networkmanager
Summary:	NetworkManager plugin for libproxy
Summary(pl.UTF-8):	Wtyczka NetworkManager dla libproxy
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description networkmanager
NetworkManager configuration plugin for libproxy.

%description networkmanager -l pl.UTF-8
Wtyczka konfiguracji NetworkManager dla libproxy.

%package gnome
Summary:	GNOME plugin for libproxy
Summary(pl.UTF-8):	Wtyczka GNOME dla libproxy
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gnome
GNOME (GConf) configuration plugin for libproxy.

%description gnome -l pl.UTF-8
Wtyczka konfiguracji GNOME (GConf) dla libproxy.

%package kde
Summary:	KDE plugin for libproxy
Summary(pl.UTF-8):	Wtyczka KDE dla libproxy
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description kde
KDE configuration plugin for libproxy.

%description kde -l pl.UTF-8
Wtyczka konfiguracji KDE dla libproxy

%package mozjs
Summary:	MozJS plugin for libproxy
Summary(pl.UTF-8):	Wtyczka MozJS dla libproxy
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description mozjs
MozJS (XULrunner/JavaScript) configuration plugin for libproxy.

%description mozjs -l pl.UTF-8
Wtyczka konfiguracji MozJS (XULrunner/JavaScript) dla libproxy.

%package webkit
Summary:	WebKit plugin for libproxy
Summary(pl.UTF-8):	Wtyczka WebKit dla libproxy
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description webkit
WebKit (JavaScriptCore) configuration plugin for libproxy.

%description webkit -l pl.UTF-8
Wtyczka konfigracji WebKit (JavaScriptCore) dla libproxy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_webkit:--without-webkit}
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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libproxy.so
%{_libdir}/libproxy.la
%{_includedir}/proxy.h
%{_pkgconfigdir}/libproxy-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libproxy.a

%files -n python-libproxy
%defattr(644,root,root,755)
%{py_sitescriptdir}/libproxy.py[co]

%files networkmanager
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/%{version}/plugins/networkmanager.so

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/%{version}/plugins/gnome.so

%files kde
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/%{version}/plugins/kde.so

%files mozjs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/%{version}/plugins/mozjs.so

%if %{with webkit}
%files webkit
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/%{version}/plugins/webkit.so
%endif
