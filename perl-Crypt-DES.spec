%define module	Crypt-DES
%define upstream_version 2.07

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	7
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Perl DES encryption module
Source0:	http://www.cpan.org/authors/id/D/DP/DPARIS/Crypt-DES-2.07.tar.gz
Url:            http://search.cpan.org/dist/%{module}/
BuildRequires:	perl-devel
# avoid build dependency on perl-Crypt-CBC to avoid dependency cycles
# https://qa.mandriva.com/show_bug.cgi?id=43033

%description
The module implements the Crypt::CBC interface.

%prep
%setup -q -n %{module}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%make test

%install
%makeinstall_std

%clean

%files
%doc README COPYRIGHT
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/auto/Crypt
%{_mandir}/man3/*

