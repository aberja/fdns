Name:           fdns
Version:        0.9.69
Release:        1.git%{?dist}
Summary:        Firejail DNS-over-HTTPS Proxy Server

License:        GPLv3+
URL:            https://github.com/netblue30/fdns
Source0:        fdns-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  libseccomp-devel
BuildRequires:  openssl-devel
BuildRequires:  systemd-rpm-macros

%description
fdns is a DNS-over-HTTPS proxy server targeted at small networks and
Linux desktops. To speed up the name resolution fdns caches the responses,
and uses a configurable adblocker and privacy filter to cut down
unnecessary traffic. The software is written in C, and is licensed under GPLv3.


%prep
%autosetup -S git


%build
%configure --with-systemd=%{_unitdir}
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%license COPYING
%doc COPYING README RELNOTES
%{_bindir}/fdns
%{_bindir}/nxdomain
%config %{_sysconfdir}/fdns
%{_unitdir}/fdns.service
%{_datadir}/bash-completion/completions/fdns
%{_mandir}/man1/fdns.1.gz
%{_mandir}/man1/nxdomain.1.gz
