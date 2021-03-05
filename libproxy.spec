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
Summary:	Library for automatic proxy configuration management
Summary(pl.UTF-8):	Biblioteka do automatycznego zarządzania konfiguracją proxy
Name:		libproxy
Version:	0.4.17
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/libproxy/libproxy/releases
Source0:	https://github.com/libproxy/libproxy/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	74af4aa1e7920f3b6117203d55a9c524
Patch0:		%{name}-pac-modules.patch
URL:		https://libproxy.github.io/libproxy/
BuildRequires:	NetworkManager-devel
BuildRequires:	cmake >= 2.6
BuildRequires:	dbus-devel
BuildRequires:	glib2-devel >= 1:2.26
%{?with_webkit:BuildRequires:	gtk-webkit4-devel >= 2.6}
BuildRequires:	libstdc++-devel >= 6:7
%{?with_mono:BuildRequires:	mono-csharp}
%{?with_mozjs:BuildRequires:	mozjs68-devel}
%{?with_natus:BuildRequires:	natus-devel}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.752
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
Requires:	python-libs >= 1:2.5
BuildArch:	noarch

%description -n python-libproxy
libproxy Python bindings.

%description -n python-libproxy -l pl.UTF-8
Wiązania libproxy dla Pythona.

%package -n python3-libproxy
Summary:	libproxy Python 3 bindings
Summary(pl.UTF-8):	Wiązania libproxy dla Pythona 3
Group:		Libraries/Python
# uses libproxy shared library
Requires:	%{name} = %{version}-%{release}
Requires:	python3-libs >= 1:3.2
BuildArch:	noarch

%description -n python3-libproxy
libproxy Python 3 bindings.

%description -n python3-libproxy -l pl.UTF-8
Wiązania libproxy dla Pythona 3.

%package -n vala-libproxy
Summary:	Vala bindings for libproxy API
Summary(pl.UTF-8):	Wiązania API libproxy dla języka Vala
Group:		Development/Languages
Requires:	%{name}-devel = %{version}-%{release}
%{?noarchpackage}

%description -n vala-libproxy
Vala bindings for libproxy API.

%description -n vala-libproxy -l pl.UTF-8
Wiązania API libproxy dla języka Vala.

%package networkmanager
Summary:	NetworkManager network plugin for libproxy
Summary(pl.UTF-8):	Wtyczka sieci NetworkManager dla libproxy
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description networkmanager
NetworkManager network plugin for libproxy, to query NetworkManager
about network configuration changes.

%description networkmanager -l pl.UTF-8
Wtyczka sieci NetworkManager dla libproxy, do odpytywania
NetworkManagera o zmiany konfiguracji sieci.

%package gnome
Summary:	GNOME configuration plugin for libproxy
Summary(pl.UTF-8):	Wtyczka konfiguracji GNOME dla libproxy
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2 >= 1:2.26

%description gnome
GNOME (gsettings) configuration plugin for libproxy, to query GNOME
about proxy settings.

%description gnome -l pl.UTF-8
Wtyczka konfiguracji GNOME (gsettings) dla libproxy, do odczytu
ustawień proxy z GNOME.

%package kde
Summary:	KDE configuration plugin for libproxy
Summary(pl.UTF-8):	Wtyczka konfiguracji KDE dla libproxy
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
#Requires:	kreadconfig (KDE4) or kreadconfig5 (KF5)

%description kde
KDE configuration plugin for libproxy, to query KDE about proxy
settings.

%description kde -l pl.UTF-8
Wtyczka konfiguracji KDE dla libproxy, do odczytu ustawień proxy z
KDE.

%package pacrunner
Summary:	Pacrunner configuration plugin for libproxy
Summary(pl.UTF-8):	Wtyczka konfiguracji pacrunner dla libproxy
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description pacrunner
Pacrunner configuration plugin for libproxy, to query pacrunner about
proxy settings.

%description pacrunner -l pl.UTF-8
Wtyczka konfiguracji pacrunner dla libproxy, do odczytu ustawień proxy
z pacrunnera.

%package mozjs
Summary:	MozJS pacrunner plugin for libproxy
Summary(pl.UTF-8):	Wtyczka pacrunner MozJS dla libproxy
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description mozjs
MozJS (XULrunner/JavaScript) pacrunner plugin for libproxy, to get
proxy from WPAD/PAC script using MozJS engine.

%description mozjs -l pl.UTF-8
Wtyczka pacrunner MozJS (XULrunner/JavaScript) dla libproxy, do
pobierania proxy ze skryptu WPAD/PAC przy użyciu silnika MozJS.

%package webkit
Summary:	WebKit pacrunner plugin for libproxy
Summary(pl.UTF-8):	Wtyczka pacrunner WebKit dla libproxy
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk-webkit4 >= 2.6

%description webkit
WebKit (JavaScriptCore) pacrunner plugin for libproxy, to get proxy
from WPAD/PAC script using WebKit engine.

%description webkit -l pl.UTF-8
Wtyczka pacrunner WebKit (JavaScriptCore) dla libproxy, do pobierania
ustawień proxy ze skryptu WPAD/PAC, przy użyciu silnika WebKit.

%prep
%setup -q
%patch0 -p1

%if %{without natus}
echo 'set(NATUS_FOUND 0)' > libproxy/cmake/modules/pacrunner_natus.cmk
%endif

%build
install -d build
cd build
%cmake .. \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DLIBEXEC_INSTALL_DIR=%{_libdir}/libproxy \
	-DPERL_VENDORINSTALL=ON \
	-DPYTHON2_SITEPKG_DIR=%{py_sitescriptdir} \
	-DPYTHON3_SITEPKG_DIR=%{py3_sitescriptdir} \
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

%py3_comp $RPM_BUILD_ROOT%{py3_sitescriptdir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitescriptdir}

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

%files -n python3-libproxy
%defattr(644,root,root,755)
%{py3_sitescriptdir}/libproxy.py
%{py3_sitescriptdir}/__pycache__/libproxy.cpython-*.py[co]

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

%files pacrunner
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/%{version}/modules/config_pacrunner.so

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
