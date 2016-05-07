#
# Conditional build:
%bcond_without	python	# Python smbus module
#
%include	/usr/lib/rpm/macros.perl
Summary:	I2C tools for Linux
Summary(en.UTF-8):	I²C tools for Linux
Summary(pl.UTF-8):	Narzędzia I²C dla Linuksa
Name:		i2c-tools
Version:	3.1.2
Release:	3
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.lm-sensors.org/i2c-tools/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	7104a1043d11a5e2c7b131614eb1b962
Patch0:		%{name}-python.patch
URL:		http://www.lm-sensors.org/wiki/I2CTools
BuildRequires:	perl-modules >= 1:5.6
%{?with_python:BuildRequires:	python-devel >= 2}
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	dev >= 2.9.0-13
Requires:	uname(release) >= 2.6.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
I2C tools for Linux.

%description -l en.UTF-8
I²C tools for Linux.

%description -l pl.UTF-8
Narzędzia I²C dla Linuksa.

%package -n python-smbus
Summary:	Python SMBus module
Summary(pl.UTF-8):	Moduł Pythona SMBus
Group:		Libraries/Python

%description -n python-smbus
Python bindings for Linux SMBus access through i2c-dev.

%description -n python-smbus -l pl.UTF-8
Wiązania Pythona służące do dostępu do szyny SMBus spod Linuksa
poprzez i2c-dev.

%prep
%setup -q
%patch0 -p1

%{__mv} eepromer/{README,README.eeproms}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	%{?with_python:EXTRA=py-smbus}

%{__make} -C eepromer \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I../include -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	%{?with_python:EXTRA=py-smbus} \
	prefix=%{_prefix} \
	mandir=%{_mandir}

install eepromer/{eeprog,eeprom,eepromer} $RPM_BUILD_ROOT%{_sbindir}
cp -p eepromer/{eeprog,eeprom,eepromer}.8 $RPM_BUILD_ROOT%{_mandir}/man8

# enhanced (more 2.4-compatible) private copy; public header already in llh
%{__rm} $RPM_BUILD_ROOT%{_includedir}/linux/i2c-dev.h

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README eepromer/README.ee*
%attr(755,root,root) %{_bindir}/ddcmon
%attr(755,root,root) %{_bindir}/decode-dimms
%attr(755,root,root) %{_bindir}/decode-edid
%attr(755,root,root) %{_bindir}/decode-vaio
%attr(755,root,root) %{_sbindir}/eeprog
%attr(755,root,root) %{_sbindir}/eeprom
%attr(755,root,root) %{_sbindir}/eepromer
%attr(755,root,root) %{_sbindir}/i2cdetect
%attr(755,root,root) %{_sbindir}/i2cdump
%attr(755,root,root) %{_sbindir}/i2cget
%attr(755,root,root) %{_sbindir}/i2cset
%attr(755,root,root) %{_sbindir}/i2c-stub-from-dump
%{_mandir}/man1/decode-dimms.1*
%{_mandir}/man1/decode-vaio.1*
%{_mandir}/man8/i2cdetect.8*
%{_mandir}/man8/eeprog.8*
%{_mandir}/man8/eeprom.8*
%{_mandir}/man8/eepromer.8*
%{_mandir}/man8/i2cdump.8*
%{_mandir}/man8/i2cget.8*
%{_mandir}/man8/i2cset.8*
%{_mandir}/man8/i2c-stub-from-dump.8*

%if %{with python}
%files -n python-smbus
%defattr(644,root,root,755)
%doc py-smbus/README
%attr(755,root,root) %{py_sitedir}/smbus.so
%{py_sitedir}/smbus-1.1-py*.egg-info
%endif
