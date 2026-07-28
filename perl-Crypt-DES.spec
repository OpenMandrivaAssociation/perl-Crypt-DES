# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

%define module Crypt-DES
Name:		perl-%{module}
Version:	2.07
Release:	13
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Perl DES encryption module
Source0:	https://cpan.metacpan.org/authors/id/D/DP/DPARIS/Crypt-DES-2.07.tar.gz
Url:            https://metacpan.org/dist/Crypt-DES
BuildRequires:	make
BuildRequires:	perl-devel
# avoid build dependency on perl-Crypt-CBC to avoid dependency cycles
# https://qa.mandriva.com/show_bug.cgi?id=43033

%description
The module implements the Crypt::CBC interface.

%prep
%autosetup -n %{module}-%{version} -p1

%build
# old XS: clang defaults to -Werror=implicit-function-declaration
export CFLAGS="${CFLAGS:-%{optflags}} -Wno-error=implicit-function-declaration -Wno-implicit-function-declaration"
export CXXFLAGS="${CXXFLAGS:-%{optflags}} -Wno-error=implicit-function-declaration -Wno-implicit-function-declaration"
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags} -Wno-error=implicit-function-declaration -Wno-implicit-function-declaration"
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
