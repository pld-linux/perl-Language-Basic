%include	/usr/lib/rpm/macros.perl
%define	pdir	Language
%define	pnam	Basic
Summary:	Language::Basic perl module - BASIC language implementation
Summary(pl):	Modu� perla Language::Basic - implementacja j�zyka BASIC
Name:		perl-Language-Basic
Version:	1.44
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Language::Basic is a Perl module implementation of the BASIC computer
language. It allows you to run BASIC programs or translate them to
Perl scripts. Note that it implements 80's-era BASIC. Think Applesoft
or GW-BASIC.

%description -l pl
Language::Basic to perlowa implementacja j�zyka programowania BASIC.
Modu� ten pozwala na uruchamianie program�w w BASIC-u lub t�umaczenie
ich na skrypty Perla. Jest to BASIC rodem z lat 80-tych - podobny do
Applesoft czy GW-Basic.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes NOTES README TODO wumpus.bas
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/Language/Basic.pm
%{perl_sitelib}/Language/Basic
%{_mandir}/man3/*
