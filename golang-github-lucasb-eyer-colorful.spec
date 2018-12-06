%global goipath         github.com/lucasb-eyer/go-colorful
Version:                1.0

%gometa

Name:           %{goname}
Release:        2%{?dist}
Summary:        A library for playing with colors in Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(gopkg.in/DATA-DOG/go-sqlmock.v1)

Provides:      golang-github-lucasb-eyer-go-colorful-devel = %{version}-%{release}
Obsoletes:     golang-github-lucasb-eyer-go-colorful-devel < 1.0-1

%description devel
%{summary}

This package contains library source intended for building other packages
which use import path with %{goipath} prefix.


%prep
%gosetup -q


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%doc README.md
%license LICENSE


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 07 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0-1
- Update to latest version
- Re-template against More Go Packaging guidelines

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170710gitd1be5f1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.20170710gitd1be5f1
- Add commit date to revision

* Fri Aug 18 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.gitd1be5f1
- Initial package for Fedora
