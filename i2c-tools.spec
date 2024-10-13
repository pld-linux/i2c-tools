#
# Conditional build:
%bcond_without	python	# (any) Python smbus module
%bcond_without	python2	# CPython 2.x smbus module
%bcond_without	python3	# CPython 3.x smbus module
#
Summary:	I2C tools for Linux
Summary(en.UTF-8):	I²C tools for Linux
Summary(pl.UTF-8):	Narzędzia I²C dla Linuksa
Name:		i2c-tools
Version:	4.3
Release:	2
License:	GPL v2+
Group:		Applications/System
Source0:	https://www.kernel.org/pub/software/utils/i2c-tools/%{name}-%{version}.tar.xz
# Source0-md5:	0c42800f746e064dc40a4dad44ed8a33
Patch0:		%{name}-python.patch
URL:		https://i2c.wiki.kernel.org/index.php/I2C_Tools
BuildRequires:	perl-modules >= 1:5.6
%if %{with python}
%{?with_python2:BuildRequires:	python-devel >= 2}
%{?with_python3:BuildRequires:	python3-devel >= 1:3.2}
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	rpm-pythonprov >= 1.714
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	dev >= 2.9.0-13
Requires:	libi2c = %{version}-%{release}
Requires:	uname(release) >= 2.6.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
I2C tools for Linux.

%description -l en.UTF-8
I²C tools for Linux.

%description -l pl.UTF-8
Narzędzia I²C dla Linuksa.

%package -n libi2c
Summary:	I2C/SMBus bus access library
Summary(pl.UTF-8):	Biblioteka dostępu do szyny I2C/SMBus
Group:		Libraries

%description -n libi2c
I2C/SMBus bus access library.

%description -n libi2c -l pl.UTF-8
Biblioteka dostępu do szyny I2C/SMBus.

%package -n libi2c-devel
Summary:	Header file for libi2c library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki libi2c
Group:		Development/Libraries
Requires:	libi2c = %{version}-%{release}

%description -n libi2c-devel
Header file for libi2c library.

%description -n libi2c-devel -l pl.UTF-8
Plik nagłówkowy biblioteki libi2c.

%package -n libi2c-static
Summary:	Static libi2c library
Summary(pl.UTF-8):	Statyczna biblioteka libi2c
Group:		Development/Libraries
Requires:	libi2c-devel = %{version}-%{release}

%description -n libi2c-static
Static libi2c library.

%description -n libi2c-static -l pl.UTF-8
Statyczna biblioteka libi2c.

%package -n python-smbus
Summary:	Python 2 SMBus module
Summary(pl.UTF-8):	Moduł Pythona 2 SMBus
Group:		Libraries/Python
Requires:	libi2c = %{version}-%{release}

%description -n python-smbus
Python 2 bindings for Linux SMBus access through i2c-dev.

%description -n python-smbus -l pl.UTF-8
Wiązania Pythona 2 służące do dostępu do szyny SMBus spod Linuksa
poprzez i2c-dev.

%package -n python3-smbus
Summary:	Python 3 SMBus module
Summary(pl.UTF-8):	Moduł Pythona 3 SMBus
Group:		Libraries/Python
Requires:	libi2c = %{version}-%{release}

%description -n python3-smbus
Python 3 bindings for Linux SMBus access through i2c-dev.

%description -n python3-smbus -l pl.UTF-8
Wiązania Pythona 3 służące do dostępu do szyny SMBus spod Linuksa
poprzez i2c-dev.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -j1 \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	EXTRA="eeprog"

%if %{with python}
cd py-smbus
%if %{with python2}
%py_build
%endif
%if %{with python3}
%py3_build
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	EXTRA="eeprog" \
	PREFIX=%{_prefix} \
	libdir=%{_libdir}

%if %{with python}
cd py-smbus
%if %{with python2}
%py_install
%endif
%if %{with python3}
%py3_install
%endif
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libi2c -p /sbin/ldconfig
%postun	-n libi2c -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES README eeprog/README.eeprog
%attr(755,root,root) %{_bindir}/ddcmon
%attr(755,root,root) %{_bindir}/decode-dimms
%attr(755,root,root) %{_bindir}/decode-edid
%attr(755,root,root) %{_bindir}/decode-vaio
%attr(755,root,root) %{_sbindir}/eeprog
%attr(755,root,root) %{_sbindir}/i2cdetect
%attr(755,root,root) %{_sbindir}/i2cdump
%attr(755,root,root) %{_sbindir}/i2cget
%attr(755,root,root) %{_sbindir}/i2cset
%attr(755,root,root) %{_sbindir}/i2ctransfer
%attr(755,root,root) %{_sbindir}/i2c-stub-from-dump
%{_mandir}/man1/decode-dimms.1*
%{_mandir}/man1/decode-vaio.1*
%{_mandir}/man8/i2cdetect.8*
%{_mandir}/man8/eeprog.8*
%{_mandir}/man8/i2cdump.8*
%{_mandir}/man8/i2cget.8*
%{_mandir}/man8/i2cset.8*
%{_mandir}/man8/i2ctransfer.8*
%{_mandir}/man8/i2c-stub-from-dump.8*

%files -n libi2c
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libi2c.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libi2c.so.0

%files -n libi2c-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libi2c.so
%dir %{_includedir}/i2c
%{_includedir}/i2c/smbus.h
%{_mandir}/man3/libi2c.3*

%files -n libi2c-static
%defattr(644,root,root,755)
%{_libdir}/libi2c.a

%if %{with python2}
%files -n python-smbus
%defattr(644,root,root,755)
%doc py-smbus/README
%attr(755,root,root) %{py_sitedir}/smbus.so
%{py_sitedir}/smbus-1.1-py*.egg-info
%endif

%if %{with python3}
%files -n python3-smbus
%defattr(644,root,root,755)
%doc py-smbus/README
%attr(755,root,root) %{py3_sitedir}/smbus.cpython-*.so
%{py3_sitedir}/smbus-1.1-py*.egg-info
%endif
