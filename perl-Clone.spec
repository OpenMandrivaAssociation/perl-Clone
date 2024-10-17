# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

%define upstream_name Clone
%define upstream_version 0.34

Summary:	Recursively copy Perl datatypes
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	16
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/G/GA/GARU/%{upstream_name}-%{upstream_version}.tar.gz
Source100:	%{name}.rpmlintrc
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
This module provides a clone() method which makes recursive
copies of nested hash, array, scalar and reference types, 
including tied variables and objects.

%prep
%autosetup -p1 -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make test

%install
%make_install

%files
%doc Changes
%{perl_vendorarch}/Clone.pm
%{perl_vendorarch}/auto/Clone
%doc %{_mandir}/man3/*
