# TODO:
# - natus-based pacrunner (doesn't build with natus 0.2.1)
# - ruby binding (not finished as of 0.4.8 - no buildsystem)
#
# Conditional build:
%bcond_without	kde		# KDE 4/5 config plugin
%bcond_without	mozjs		# MozJS pacrunner plugin
%bcond_with	natus		# Natus pacrunner plugin [doesn't build with natus 0.2.1]
%bcond_without	webkit		# WebKit pacrunner plugin
%bcond_without	mono		# Mono C# bindings

%ifarch x32
%undefine	with_mono
%endif
%include	/usr/lib/rpm/macros.perl
%include	/usr/lib/rpm/macros.mono
Summary:	Library for automatic proxy configuration management
Summary(pl.UTF-8):	Biblioteka do automatycznego zarządzania konfiguracją proxy
Name:		libproxy
Version:	0.4.13
Release:	2
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/libproxy/libproxy/releases
Source0:	https://github.com/libproxy/libproxy/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	de293bb311f185a2ffa3492700a694c2
Patch0:		%{name}-pac-modules.patch
Patch1:		%{name}-mozjs.patch
URL:		https://libproxy.github.io/libproxy/
BuildRequires:	NetworkManager-devel
BuildRequires:	cmake >= 2.6
BuildRequires:	glib2-devel >= 1:2.26
%{?with_webkit:BuildRequires:	gtk-webkit4-devel >= 2.6}
%{?with_mozjs:BuildRequires:	js187-devel}
BuildRequires:	libmodman-devel >= 2
BuildRequires:	libstdc++-devel
%{?with_mono:BuildRequires:	mono-csharp}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	rpmbuild(monoautodeps)
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXmu-devel
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
Requires:	libstdc++-devel
Obsoletes:	libproxy-static

%description devel
Header files for libproxy library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libproxy.

%package -n dotnet-libproxy-sharp
Summary:	Libproxy# - libproxy .NET bindings
Summary(pl.UTF-8):	Libproxy# - wiązania libproxy dla .NET
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n dotnet-libproxy-sharp
Libproxy# - libproxy .NET bindings.

%description -n dotnet-libproxy-sharp -l pl.UTF-8
Libproxy# - wiązania libproxy dla .NET.

%package -n dotnet-libproxy-sharp-devel
Summary:	libproxy .NET bindings - development files
Summary(pl.UTF-8):	Wiązania libproxy dla .NET - pliki programistyczne
Group:		Development/Libraries
Requires:	dotnet-libproxy-sharp = %{version}-%{release}

%description -n dotnet-libproxy-sharp-devel
Development files for libproxy .NET bindings.

%description -n dotnet-libproxy-sharp-devel -l pl.UTF-8
Pliki programistyczne wiązań libproxy dla .NET.

%package -n perl-Net-Libproxy
Summary:	libproxy Perl bindings
Summary(pl.UTF-8):	Wiązania libproxy dla Perla
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description -n perl-Net-Libproxy
libproxy Perl bindings.

%description -n perl-Net-Libproxy -l pl.UTF-8
Wiązania libproxy dla Perla.

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

%package -n vala-libproxy
Summary:	Vala bindings for libproxy API
Summary(pl.UTF-8):	Wiązania API libproxy dla języka Vala
Group:		Development/Languages
Requires:	%{name}-devel = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n vala-libproxy
Vala bindings for libproxy API.

%description -n vala-libproxy -l pl.UTF-8
Wiązania API libproxy dla języka Vala.

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
Requires:	glib2 >= 1:2.26

%description gnome
GNOME (GConf) configuration plugin for libproxy.

%description gnome -l pl.UTF-8
Wtyczka konfiguracji GNOME (GConf) dla libproxy.

%package kde
Summary:	KDE plugin for libproxy
Summary(pl.UTF-8):	Wtyczka KDE dla libproxy
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
#Requires:	kreadconfig (KDE4) or kreadconfig5 (KF5)

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
Requires:	gtk-webkit4 >= 2.6

%description webkit
WebKit (JavaScriptCore) configuration plugin for libproxy.

%description webkit -l pl.UTF-8
Wtyczka konfigracji WebKit (JavaScriptCore) dla libproxy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%if %{without natus}
echo 'set(NATUS_FOUND 0)' > libproxy/cmake/modules/pacrunner_natus.cmk
%endif

%build
install -d build
cd build
%cmake .. \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DLIBEXEC_INSTALL_DIR=%{_libdir}/libproxy \
	-DFORCE_SYSTEM_LIBMODMAN=ON \
	-DPERL_VENDORINSTALL=ON \
	-DPYTHON_SITEPKG_DIR=%{py_sitescriptdir} \
	%{?with_mono:-DWITH_DOTNET=ON -DGMCS_EXECUTABLE=/usr/bin/mcs} \
	%{!?with_kde:-DWITH_KDE=OFF} \
	%{!?with_mozjs:-DWITH_MOZJS=OFF} \
	-DWITH_VALA=ON \
	%{!?with_webkit:-DWITH_WEBKIT=OFF} \
	%{?with_webkit:-DWITH_WEBKIT3=ON}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/proxy
%attr(755,root,root) %{_libdir}/libproxy.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libproxy.so.1
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/%{version}
%dir %{_libdir}/%{name}/%{version}/modules

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libproxy.so
%{_includedir}/proxy.h
%{_pkgconfigdir}/libproxy-1.0.pc
%{_datadir}/cmake/Modules/Findlibproxy.cmake

%if %{with mono}
%files -n dotnet-libproxy-sharp
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/libproxy-sharp

%files -n dotnet-libproxy-sharp-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/libproxy-sharp
%{_pkgconfigdir}/libproxy-sharp-1.0.pc
%endif

%files -n perl-Net-Libproxy
%defattr(644,root,root,755)
%{perl_vendorarch}/Net/Libproxy.pm
%dir %{perl_vendorarch}/auto/Net/Libproxy
%attr(755,root,root) %{perl_vendorarch}/auto/Net/Libproxy/Libproxy.so

%files -n python-libproxy
%defattr(644,root,root,755)
%{py_sitescriptdir}/libproxy.py[co]

%files -n vala-libproxy
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libproxy-1.0.vapi

%files networkmanager
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/%{version}/modules/network_networkmanager.so

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/%{version}/modules/config_gnome3.so
%attr(755,root,root) %{_libdir}/%{name}/pxgsettings

%if %{with kde}
%files kde
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/%{version}/modules/config_kde.so
%endif

%if %{with mozjs}
%files mozjs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/%{version}/modules/pacrunner_mozjs.so
%endif

%if %{with webkit}
%files webkit
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/%{version}/modules/pacrunner_webkit.so
%endif
