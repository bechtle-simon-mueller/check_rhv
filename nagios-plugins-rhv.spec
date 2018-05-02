Name:		nagios-plugins-rhv
Version:	2.0
Release:	1%{?dist}
Summary:	RHV monitoring plugin for Nagios/Icinga

Group:		Applications/System
License:	GPLv2+
URL:		https://github.com/rk-it-at/check_rhv
Source0:	check_rhv-%{version}.tar.gz
BuildRoot:	%{_tmppath}/check_rhv-%{version}-%{release}-root

BuildRequires:	perl-Crypt-SSLeay
BuildRequires:	perl-libwww-perl
BuildRequires:	perl-XML-Simple

Requires:	perl-Crypt-SSLeay
Requires:	perl-libwww-perl
Requires:	perl-XML-Simple

%description
This plugin for Icinga/Nagios is used to monitor a variety of
a RHV environement including datacenters, clusters, hosts,
vms, vm pools and storage domains.

%prep
%setup -q -n check_rhv-%{version}

%build
%configure --prefix=%{_libdir}/nagios/plugins \
	   --with-nagios-user=nagios \
	   --with-nagios-group=nagios \
	   --with-pnp-dir=%{_datadir}/nagios/html/pnp4nagios

make all


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL_OPTS=""

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(0755,nagios,nagios)
%{_libdir}/nagios/plugins/check_rhv
%{_datadir}/nagios/html/pnp4nagios/templates/check_rhv.php
%doc README INSTALL NEWS ChangeLog COPYING



%changelog
* Fri Apr 20 2018 Rene Koch <rkoch@rk-it.at> 2.0-1
- Initial build of renamed package nagios-plugins-rhv

* Sun Nov 06 2016 Rene Koch <rkoch@rk-it.at> 1.6-1
- Initial build

* Fri Feb 19 2016 Rene Koch <rkoch@rk-it.at> 1.5-1
- Initial build

* Wed Apr 16 2014 Rene Koch <rkoch@linuxland.at> 1.4-1
- Initial build

* Thu Nov 07 2013 Rene Koch <r.koch@ovido.at> 1.3-1
- Initial build

* Tue Jul 23 2013 Rene Koch <r.koch@ovido.at> 1.2.1-1
- Initial build

* Thu May 16 2013 Rene Koch <r.koch@ovido.at> 1.2-1
- Initial build

* Wed Jan 30 2013 Rene Koch <r.koch@ovido.at> 1.1-1
- Initial build

* Thu Dec 27 2012 Rene Koch <r.koch@ovido.at> 1.0.1-1
- Initial build for bugfix release

* Fri Aug 31 2012 Rene Koch <r.koch@ovido.at> 1.0-2
- Removed BuildArch: noarch

* Mon Aug 27 2012 Rene Koch <r.koch@ovido.at> 1.0-1
- Initial build.

