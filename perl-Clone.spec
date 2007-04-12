%define real_name Clone
%define name perl-%{real_name}
%define version 0.20
%define release %mkrel 1

Summary: 	Clone module for Perl
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group: 		Development/Perl
Source: 	http://www.cpan.org/authors/id/GAAS/%{real_name}-%{version}.tar.bz2
Url: 		http://search.cpan.org/dist/%{real_name}
BuildRequires:	perl-devel
BuildRoot: 	%{_tmppath}/%{name}-buildroot/
Requires: 	perl

%description
This module provides a clone() method which makes recursive
copies of nested hash, array, scalar and reference types, 
including tied variables and objects.

%prep
%setup -q -n %{real_name}-%{version}
find -type f | xargs chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorarch}/Clone.pm
%{perl_vendorarch}/auto/Clone
%{_mandir}/*/*

