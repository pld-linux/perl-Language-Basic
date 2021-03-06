%define		pdir	Language
%define		pnam	Basic
Summary:	Language::Basic Perl module - BASIC language implementation
Summary(pl.UTF-8):	Moduł Perla Language::Basic - implementacja języka BASIC
Name:		perl-Language-Basic
Version:	1.44
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b3dac4979e9e61cded185df434eb4ffe
URL:		http://search.cpan.org/dist/Language-Basic/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Language::Basic is a Perl module implementation of the BASIC computer
language. It allows you to run BASIC programs or translate them to
Perl scripts. Note that it implements 80's-era BASIC. Think Applesoft
or GW-BASIC.

%description -l pl.UTF-8
Language::Basic to perlowa implementacja języka programowania BASIC.
Moduł ten pozwala na uruchamianie programów w BASIC-u lub tłumaczenie
ich na skrypty Perla. Jest to BASIC rodem z lat 80-tych - podobny do
Applesoft czy GW-Basic.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# get rid of pod documentation
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Language/Basic/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes NOTES README TODO wumpus.bas
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Language/Basic.pm
%{perl_vendorlib}/Language/Basic
%{_mandir}/man3/*
