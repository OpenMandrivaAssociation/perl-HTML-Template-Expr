%define upstream_name    HTML-Template-Expr
Name:		perl-%{upstream_name}
Version:	0.07
Release:	6

Summary:	HTML::Template extension adding expression support
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/HTML-Template-Expr
Source0:	https://cpan.metacpan.org/authors/id/S/SA/SAMTREGAR/HTML-Template-Expr-%{version}.tar.gz

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

%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 403261
- rebuild using %0.07 Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.07-3mdv2009.0
+ Revision: 257208
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.07-1mdv2008.1
+ Revision: 122695
- kill re-definition of %%buildroot on Pixel's request


* Wed Apr 19 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdk
- New release 0.07
- better source URL
- better buildrequires syntax

* Mon Mar 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdk
- New release 0.06

* Tue Dec 27 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdk
- New release 0.05
- spec cleanup
- drop explicit requires
- drop useless buildrequires versionning
- fix sources URL
- better summary and description
- %%mkrel

* Wed Sep 15 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.04-4mdk
- rebuild

* Tue Aug 12 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.04-3mdk
- rebuild
- rm -rf /home/guillomovitch/rpm/tmp/perl-HTML-Template-Expr-0.07 in %%install, not %%build
- use %%makeinstall_std macro
- drop $RPM_OPT_FLAGS, noarch..

