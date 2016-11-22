#%define app_version %(cat %{sourcedir}/VERSION)
%define app_user  %{name}
%define app_group %{name}
%define app_data  %{_localstatedir}/lib/%{name}

Summary: Shell script and conf files example
Name: app
Version: %{_app_version}
Release: 1
URL:     http://github.com/bernardovale/my-rpm-examples
License: MIT
Group: Applications/Internet
BuildRoot: %{_tmppath}/%{name}-root
Requires: bash
Source0: app-%{version}.tar.gz
BuildArch: noarch

%description
Shell script app example with user/group increment

%prep
%setup -q

%build

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/usr/bin
mkdir -p ${RPM_BUILD_ROOT}/etc/app
mkdir -p ${RPM_BUILD_ROOT}/%{app_data}
cp conf/simple.conf ${RPM_BUILD_ROOT}/%{_sysconfdir}/app
install -m 755 bin/%{name} ${RPM_BUILD_ROOT}%{_bindir}

%clean
rm -rf ${RPM_BUILD_ROOT}

%pre
getent group %{app_group} >/dev/null || groupadd -r %{app_group}
getent passwd %{app_user} >/dev/null || /usr/sbin/useradd --comment "App User" --shell /bin/bash -M -r -g %{app_group} --home %{app_data} %{app_user}

%files
%defattr(-,%{app_user},%{app_group})
%attr(755,%{app_user},%{app_group}) %{_bindir}/app
%config(noreplace) %{_sysconfdir}/app/*.conf
%attr(0755,%{app_user},%{app_group}) %dir %{_localstatedir}/lib/%{name}

%post
echo "*/1 * * * * date" > mycrontab
crontab -u %{app_user} mycrontab
rm mycrontab