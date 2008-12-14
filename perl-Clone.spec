%define module Clone
%define name perl-%{module}
%define version 0.30
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Recursively copy Perl datatypes
License: 	GPL or Artistic
Group: 		Development/Perl
Source: 	http://search.cpan.org/CPAN/authors/id/R/RD/RDF/%{module}-%{version}.tar.gz
Url: 		http://search.cpan.org/dist/%{module}
BuildRequires:	perl-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
This module provides a clone() method which makes recursive
copies of nested hash, array, scalar and reference types, 
including tied variables and objects.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorarch}/Clone.pm
%{perl_vendorarch}/auto/Clone
%{_mandir}/*/*

