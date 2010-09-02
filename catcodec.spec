Summary:	Tool for decode and encode sample catalogues for OpenTTD
Summary(pl.UTF-8):	Narzędzie do dekodowania oraz enkodowania katalogów dźwiękowych dla OpenTTD
Name:		catcodec
Version:	1.0.1
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://cz.binaries.openttd.org/openttd/binaries/extra/catcodec/%{version}/%{name}-%{version}-source.tar.bz2
# Source0-md5:	d5b90debd0761911a0d3a15607392c85
Patch0:		%{name}-flags.patch
URL:		http://www.openttd.org/en/download-catcodec
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
catcodec decodes and encodes sample catalogues for OpenTTD.

%description -l pl.UTF-8
catcodec to narzędzie do dekodowania i enkodowania katalogów
dźwiękowych dla OpenTTD.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	OPTFLAGS="%{rpmcxxflags}" \
	LDFLAGS="%{rpmldflags}" \
	VERBOSE="on"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install catcodec $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/readme.txt
%attr(755,root,root) %{_bindir}/catcodec
