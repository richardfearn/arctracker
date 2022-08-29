Name:           arctracker
Version:        0.2.0
Release:        2%{?dist}
Summary:        Plays Tracker and Desktop Tracker files from the Acorn Archimedes

License:        GPLv2+
URL:            http://sourceforge.net/projects/arctracker/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc

# enable ALSA sound output
BuildRequires:  alsa-lib-devel

Patch0:         arctracker-remove-inline.patch
Patch1:         arctracker-LDFLAGS-fix.patch

%description
This program is designed to play modfiles that have been created using the
Tracker and Desktop Tracker programs that run on the Acorn Archimedes and
compatible range of microcomputers.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure --prefix=%{buildroot}%{_prefix}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
%make_install

%files
%{_bindir}/arctracker
%doc COPYING README

%changelog
* Mon Aug 29 2022 Richard Fearn <richardfearn@gmail.com> - 0.2.0-2
- Fix compilation on Fedora 36

* Sun May  3 2015 Richard Fearn <richardfearn@gmail.com> - 0.2.0-1
- Initial package for Fedora
