%define module	Crypt-DES
%define name	perl-%{module}
%define version 2.05
%define release %mkrel 9

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

