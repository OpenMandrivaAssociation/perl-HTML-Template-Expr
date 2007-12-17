%define module  HTML-Template-Expr
%define	name	perl-%{module}
%define version 0.07
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	HTML::Template extension adding expression support
License: 	GPL or Artistic
Group: 		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(HTML::Template)
BuildRequires:	perl(Parse::RecDescent)
BuildRequires:	perl(Test::Simple)
BuildArch: 	noarch

%description
This module provides an extension to HTML::Template which
allows expressions in the template syntax.  This is purely an addition
- all the normal HTML::Template options, syntax and behaviors will
still work.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README 
%{perl_vendorlib}/HTML
%{_mandir}/*/*

