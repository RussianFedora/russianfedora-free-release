%define repo free
#define repo nonfree
#define repo fixes

Name:           russianfedora-%{repo}-release
Version:        14
Release:        1
Summary:        Russian Fedora (%{repo}) Repository Configuration

Group:          System Environment/Base
License:        BSD
URL:            http://russianfedora.org
Source0:        RPM-GPG-KEY-russianfedora-%{repo}-fedora
Source1:        russianfedora-%{repo}.repo
Source2:        russianfedora-%{repo}-updates.repo
Source3:        russianfedora-%{repo}-updates-testing.repo
Source4:        russianfedora-%{repo}-rawhide.repo
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       system-release >= 14

# If apt is around, it needs to be a version with repomd support
Conflicts:      apt < 0.5.15lorg3

%if %{repo} == "nonfree"
Requires:       russianfedora-free-release >= %{version}

%description
Russian Fedora repository contains open source and other distributable software for
Fedora. It based on Tigro repository.

This package contains the Russian Fedora GPG key as well as Yum package manager
configuration files for Russian Fedora's "nonfree" repository, which holds
software that is not considered as Open Source Software according to the
Fedora packaging guidelines. 
%endif

%if %{repo} == "fixes"
%description
Russian Fedora repository contains open source and other distributable software for
Fedora. It based on Tigro repository.

This package contains the Russian Fedora GPG key as well as Yum package manager
configuration files for Russian Fedora's "fixes" repository, which holds
fixes for software that already is in Fedora Everything or updates.
Fedora packaging guidelines.
%endif

%if %{repo} == "free"
%description
Russian Fedora repository contains open source and other distributable software for
Fedora. It based on Tigro repository.

This package contains the Russian Fedora GPG key as well as Yum package manager
configuration files for Russian Fedora's "free" repository, which holds only
software that is considered as Open Source Software according to the Fedora
packaging guidelines. 
%endif

%prep
echo "Nothing to prep"

%build
echo "Nothing to build"

%install
rm -rf $RPM_BUILD_ROOT

# Create dirs
install -d -m755 \
  $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg  \
  $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

# GPG Key
%{__install} -Dp -m644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg

# Yum .repo files
%{__install} -p -m644 %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d


%clean
rm -rf $RPM_BUILD_ROOT


#%pre
#if [ -f /etc/yum.repos.d/russianfedora-%{repo}-pre-rawhide.repo ]; then
#    sed -i 's!enabled=1!enabled=0!g' /etc/yum.repos.d/russianfedora-%{repo}-pre-rawhide.repo
#fi


%files
%defattr(-,root,root,-)
%{_sysconfdir}/pki/rpm-gpg/*
%config(noreplace) %{_sysconfdir}/yum.repos.d/*


%changelog
* Thu Oct 14 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 14-1
- stable release

* Wed May 19 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 13-1
- enable stable repos disable unstable

* Mon Mar 15 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 13-0.1
- bump to 13

* Mon Nov  9 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 12-2
- fix updates repo

* Mon Nov  9 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 12-1
- update for RFRemix 12

* Sun Jan 11 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10-2
- add obsoletes for tigro-release
- fix repos files

* Fri Jan  9 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10-1
- initial build for Fedora 10
