Name:           arctracker
Version:        0.2.0
Release:        1%{?dist}
Summary:        Plays Tracker and Desktop Tracker files from the Acorn Archimedes

License:        GPLv2+
URL:            http://sourceforge.net/projects/arctracker/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

# enable ALSA sound output
BuildRequires:  alsa-lib-devel

%description
This program is designed to play modfiles that have been created using the
Tracker and Desktop Tracker programs that run on the Acorn Archimedes and
compatible range of microcomputers.

%prep
%setup -q

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
* Sun May  3 2015 Richard Fearn <richardfearn@gmail.com> - 0.2.0-1
- Initial package for Fedora
