%define module	Crypt-DES
%define name	perl-%{module}
%define version 2.05
%define release %mkrel 14

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Perl DES encryption module
Source0:	http://search.cpan.org/CPAN/authors/id/D/DP/DPARIS/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}/
BuildRequires:	perl-devel
# avoid build dependency on perl-Crypt-CBC to avoid dependency cycles
# https://qa.mandriva.com/show_bug.cgi?id=43033
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The module implements the Crypt::CBC interface.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="$RPM_OPT_FLAGS"

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYRIGHT
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/auto/Crypt
%{_mandir}/man3/*



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.05-14mdv2012.0
+ Revision: 765639
- bump release
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.05-12
+ Revision: 763627
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.05-11
+ Revision: 667058
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 2.05-10mdv2011.0
+ Revision: 564389
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.05-9mdv2011.0
+ Revision: 555710
- rebuild

* Tue Sep 01 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.05-8mdv2010.1
+ Revision: 423708
- rebuild

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.05-7mdv2009.0
+ Revision: 279118
- drop build dependency on perl-Crypt-CBC to avoid dependency cycles (fix #43033)

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 2.05-6mdv2009.0
+ Revision: 256208
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 2.05-4mdv2008.1
+ Revision: 151385
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.05-3mdv2008.0
+ Revision: 86238
- rebuild


* Tue Aug 15 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/15/06 01:28:19 (56120)
- rebuild

* Tue Aug 15 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/15/06 01:26:45 (56119)
Import perl-Crypt-DES

* Fri Dec 30 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.05-1mdk
- New release 2.05
- %%mkrel
- spec cleanup
- better summary and description
- better URL
- fix sources URL

* Fri Nov 19 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.03-9mdk
- Rebuild for new perl

* Thu Feb 12 2004 Michael Scherer <misc@mandrake.org> 2.03-8mdk
- do not own standard dir
- enable test

