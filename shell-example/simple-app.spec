Summary: The do it all script. (Enterprise quality)
Name: app
Version: 0.2
Release: 1
URL:     http://github.com/bernardovale
License: GPL
Group: Applications/Internet
BuildRoot: %{_tmppath}/%{name}-root
Requires: bash
Source0: app-%{version}.tar.gz
BuildArch: noarch

%description
A shell script.

%prep
%setup -q

%build

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/usr/bin
mkdir -p ${RPM_BUILD_ROOT}/etc/app
cp conf/simple.conf ${RPM_BUILD_ROOT}/%{_sysconfdir}/app
install -m 755 bin/app ${RPM_BUILD_ROOT}%{_bindir}

%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/app
%config(noreplace) %{_sysconfdir}/app/*.conf