%define debug_package %{nil}

%global gh_user jc21

Name:           cloudflare-ddns
Version:        1.0.0
Release:        1%{?dist}
Summary:        A command to detect your public IP and update a Cloudflare A/AAAA record when changed
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
Source:         https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
BuildRequires:  git golang

%description
Sick of using Dynamic DNS services that are costly or annoying?
Already use Cloudflare for your domain DNS?
Do you have a dynamically assigned IP address?
This is the command for you.

%prep
%setup -qn %{name}-%{version}

%build
go build -o bin/%{name} cmd/%{name}/main.go

%install
install -Dm0755 bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Wed Jul 30 2025 Jamie Curnow <jc@jc21.com> 1.0.0-1
- v1.0.0
