%include	/usr/lib/rpm/macros.perl
Summary:	I2C tools for Linux
Summary(en.UTF-8):	I²C tools for Linux
Summary(pl.UTF-8):	Narzędzia I²C dla Linuksa
Name:		i2c-tools
Version:	3.0.2
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.lm-sensors.org/i2c-tools/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	b546345ac19db56719dea6b8199f11e0
URL:		http://www.lm-sensors.org/wiki/I2CTools
BuildRequires:	perl-modules >= 1:5.6
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

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	mandir=%{_mandir}

# enhanced (more 2.4-compatible) private copy; public header already in llh
rm $RPM_BUILD_ROOT%{_includedir}/linux/i2c-dev.h

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/ddcmon
%attr(755,root,root) %{_bindir}/decode-dimms
%attr(755,root,root) %{_bindir}/decode-edid
%attr(755,root,root) %{_bindir}/decode-vaio
%attr(755,root,root) %{_sbindir}/i2cdetect
%attr(755,root,root) %{_sbindir}/i2cdump
%attr(755,root,root) %{_sbindir}/i2cget
%attr(755,root,root) %{_sbindir}/i2cset
%attr(755,root,root) %{_sbindir}/i2c-stub-from-dump
%{_mandir}/man8/i2cdetect.8*
%{_mandir}/man8/i2cdump.8*
%{_mandir}/man8/i2cget.8*
%{_mandir}/man8/i2cset.8*
%{_mandir}/man8/i2c-stub-from-dump.8*
