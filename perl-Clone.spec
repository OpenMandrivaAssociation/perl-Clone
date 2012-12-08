%define upstream_name    Clone
%define upstream_version 0.31

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 8

Summary: 	Recursively copy Perl datatypes
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url: 		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/R/RD/RDF/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides a clone() method which makes recursive
copies of nested hash, array, scalar and reference types, 
including tied variables and objects.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.310.0-8mdv2012.0
+ Revision: 765094
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.310.0-7
+ Revision: 763559
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.310.0-6
+ Revision: 667047
- mass rebuild

* Sun Apr 03 2011 Funda Wang <fwang@mandriva.org> 0.310.0-5
+ Revision: 650028
- rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.310.0-4mdv2011.0
+ Revision: 564386
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.310.0-3mdv2011.0
+ Revision: 555458
- rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.310.0-2mdv2011.0
+ Revision: 555221
- rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.310.0-1mdv2010.1
+ Revision: 406316
- rebuild using %%perl_convert_version

* Wed Jan 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.31-1mdv2009.1
+ Revision: 332122
- update to new version 0.31

* Sun Dec 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.30-1mdv2009.1
+ Revision: 314243
- update to new version 0.30

* Sun Jul 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.29-1mdv2009.0
+ Revision: 234287
- update to new version 0.29

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.28-2mdv2008.1
+ Revision: 151389
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Oct 21 2007 Funda Wang <fwang@mandriva.org> 0.28-1mdv2008.1
+ Revision: 101001
- update to new version 0.28

* Sun Oct 21 2007 Funda Wang <fwang@mandriva.org> 0.27-2mdv2008.1
+ Revision: 101000
- rebuild

* Fri Jul 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.27-1mdv2008.0
+ Revision: 56126
- new version

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 0.23-1mdv2008.0
+ Revision: 19810
- 0.23


* Fri Mar 10 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.20-1mdk
- 0.20

* Wed Mar 08 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.19-1mdk
- 0.19

* Tue May 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.18-1mdk
- 0.18

* Tue Nov 16 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.15-2mdk
- rebuild for new perl

* Sun Feb 29 2004 Pascal Terjan <pterjan@mandrake.org> 0.15-1mdk
- First Mandrake package

