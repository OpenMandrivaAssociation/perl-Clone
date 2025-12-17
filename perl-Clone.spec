%bcond_with test
%define upstream_name Clone
%undefine _debugsource_packages

Summary:	Recursively copy Perl datatypes
Name:		perl-%{upstream_name}
Version:	0.47
Release:	2
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Clone
Source0:	https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/Clone-%{version}.tar.gz
Source100:	%{name}.rpmlintrc
%if %{with test}
BuildRequires:	perl(Test::More)
BuildRequires:	perl(B::COW)
%endif
BuildRequires:	perl-devel

%description
This module provides a clone() method which makes recursive
copies of nested hash, array, scalar and reference types, 
including tied variables and objects.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%if %{with test}
%check
%make test
%endif

%install
%make_install

%files
%doc Changes
%{perl_vendorarch}/Clone.pm
%{perl_vendorarch}/auto/Clone
%doc %{_mandir}/man3/*
