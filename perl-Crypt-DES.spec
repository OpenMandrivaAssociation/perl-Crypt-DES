# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

%define module Crypt-DES
%define upstream_version 2.07

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	9
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Perl DES encryption module
Source0:	http://www.cpan.org/authors/id/D/DP/DPARIS/Crypt-DES-2.07.tar.gz
Url:            https://search.cpan.org/dist/%{module}/
BuildRequires:	perl-devel
# avoid build dependency on perl-Crypt-CBC to avoid dependency cycles
# https://qa.mandriva.com/show_bug.cgi?id=43033

%description
The module implements the Crypt::CBC interface.

%prep
%autosetup -n %{module}-%{upstream_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build CFLAGS="%{optflags}"

%check
%make test

%install
%make_install

%files
%doc README COPYRIGHT
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/auto/Crypt
%doc %{_mandir}/man3/*
