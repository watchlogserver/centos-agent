Name: watchlog-agent
Version: 1.0.0
Release: 1%{?dist}
Summary: Watchlog Agent for collecting system metrics
License: MIT
URL: https://watchlog.io
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch
Requires: nodejs >= 10.0.0

%description
Watchlog Agent is a tool for collecting system metrics and sending them to a Watchlog server.

%prep
# Nothing to do here as we are not compiling any code.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/watchlog-agent/src
cp -r src/* %{buildroot}/opt/watchlog-agent/src/
install -Dm644 watchlog-agent.service %{buildroot}/usr/lib/systemd/system/watchlog-agent.service

%post
# Post-installation script
systemctl daemon-reload
systemctl enable watchlog-agent
systemctl start watchlog-agent

%files
%license LICENSE
%doc README.md
/opt/watchlog-agent/src/*
/usr/lib/systemd/system/watchlog-agent.service

%changelog
* Tue Nov 19 2024 Mohammad Najm <mohammadnajm75@gmail.com> 1.0.0-1
- Initial RPM package for Watchlog Agent.
