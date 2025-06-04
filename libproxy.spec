#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	duktape		# Duktape pacrunner plugin
%bcond_without	kde		# KDE 4/5 config plugin

Summary:	Library for automatic proxy configuration management
Summary(pl.UTF-8):	Biblioteka do automatycznego zarządzania konfiguracją proxy
Name:		libproxy
Version:	0.5.9
Release:	2
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/libproxy/libproxy/releases
Source0:	https://github.com/libproxy/libproxy/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	11fd35c17e0ae017bae764fae1651973
URL:		https://libproxy.github.io/libproxy/
BuildRequires:	curl-devel
%{?with_duktape:BuildRequires:	duktape-devel}
%{?with_apidocs:BuildRequires:	gi-docgen}
BuildRequires:	glib2-devel >= 1:2.71.3
BuildRequires:	gobject-introspection-devel
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	sed >= 4.0
BuildRequires:	vala
Requires:	glib2 >= 1:2.71.3
Obsoletes:	dotnet-libproxy-sharp < 0.5.9
Obsoletes:	dotnet-libproxy-sharp-devel < 0.5.9
Obsoletes:	libproxy-duktape < 0.5.9
Obsoletes:	libproxy-gnome < 0.5.9
Obsoletes:	libproxy-kde < 0.5.9
Obsoletes:	libproxy-mozjs < 0.5.9
Obsoletes:	libproxy-networkmanager < 0.5.9
Obsoletes:	libproxy-pacrunner < 0.5.9
Obsoletes:	libproxy-webkit < 0.5.9
Obsoletes:	perl-Net-Libproxy < 0.5.9
Obsoletes:	python-libproxy < 0.5.9
Obsoletes:	python3-libproxy < 0.5.9
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
Requires:	glib2-devel >= 1:2.71.3
Requires:	libstdc++-devel
Obsoletes:	libproxy-static < 0.4

%description devel
Header files for libproxy library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libproxy.

%package -n vala-libproxy
Summary:	Vala bindings for libproxy API
Summary(pl.UTF-8):	Wiązania API libproxy dla języka Vala
Group:		Development/Languages
Requires:	%{name}-devel = %{version}-%{release}
BuildArch:	noarch

%description -n vala-libproxy
Vala bindings for libproxy API.

%description -n vala-libproxy -l pl.UTF-8
Wiązania API libproxy dla języka Vala.

%package apidocs
Summary:	API documentation for libproxy library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libproxy
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for libproxy library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libproxy.

%prep
%setup -q

%build
%meson \
	%{!?with_kde:-Dconfig-kde=false} \
	%{!?with_apidocs:-Ddocs=false} \
	%{!?with_duktape:-Dpacrunner-duktape=false} \
	-Drelease=true \
	-Dvapi=true

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%if %{with apidocs}
install -d $RPM_BUILD_ROOT%{_gidocdir}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/libproxy-1.0 $RPM_BUILD_ROOT%{_gidocdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/proxy
%attr(755,root,root) %{_libdir}/libproxy.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libproxy.so.1
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libpxbackend-1.0.so
%{_libdir}/girepository-1.0/Libproxy-1.0.typelib
%{_mandir}/man8/proxy.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libproxy.so
%{_includedir}/libproxy
%{_pkgconfigdir}/libproxy-1.0.pc
%{_datadir}/gir-1.0/Libproxy-1.0.gir

%files -n vala-libproxy
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libproxy-1.0.vapi
%{_datadir}/vala/vapi/libproxy-1.0.deps

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gidocdir}/libproxy-1.0
%endif
