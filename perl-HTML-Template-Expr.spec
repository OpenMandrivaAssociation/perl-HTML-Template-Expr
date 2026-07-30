%define upstream_name    HTML-Template-Expr
%define upstream_version 0.07
Name:		perl-%{upstream_name}
Version:	0.07
Release:	1

Summary:	HTML::Template extension adding expression support
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/HTML-Template-Expr
Source0:	https://cpan.metacpan.org/authors/id/S/SA/SAMTREGAR/HTML-Template-Expr-0.07.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(HTML::Template)
BuildRequires:	perl(Parse::RecDescent)
BuildRequires:	perl(Test::Simple)
BuildArch:	noarch

%description
This module provides an extension to HTML::Template which
allows expressions in the template syntax.  This is purely an addition
- all the normal HTML::Template options, syntax and behaviors will
still work.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README 
%{perl_vendorlib}/HTML
%{_mandir}/*/*

