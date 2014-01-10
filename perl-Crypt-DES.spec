%define module	Crypt-DES
%define version	2.05

Summary:	Perl DES encryption module
Name:		perl-%{module}
Version:	%perl_convert_version 2.07
Release:	1
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source0:	http://www.cpan.org/authors/id/D/DP/DPARIS/Crypt-DES-2.07.tar.gz
BuildRequires:	perl-devel
# avoid build dependency on perl-Crypt-CBC to avoid dependency cycles
# https://qa.mandriva.com/show_bug.cgi?id=43033

%description
The module implements the Crypt::CBC interface.

%prep
%setup -qn %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%make test

%install
%makeinstall_std

%files
%doc README COPYRIGHT
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/auto/Crypt
%{_mandir}/man3/*


