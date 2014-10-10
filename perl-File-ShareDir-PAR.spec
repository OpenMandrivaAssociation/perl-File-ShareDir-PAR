%define upstream_name    File-ShareDir-PAR
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	File::ShareDir with PAR support
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Class::Inspector)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::ShareDir)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
'File::ShareDir::PAR' provides the same functionality as the File::ShareDir
manpage but tries hard to be compatible with the PAR manpage packaged
applications.

The problem is, that the concept of having a distribution or module
specific _share_ directory becomes a little hazy when you're loading
everything from a single file. the PAR manpage uses an '@INC' hook to
intercept any attempt to load a module. the File::ShareDir manpage uses the
directory structure that is typically found in the directories that are
listed in '@INC' for storing the shared data. In a 'PAR' enviroment, this
is not necessarily possible.

When you call one of the functions that this module provides, it will take
care to search in any of the currently loaded '.par' files before scanning
'@INC'. This is the same order of preference you get for loading modules
when PAR is in effect. If the path or file you are asking for is found in
one of the loaded '.par' files, that containing '.par' file is extracted
and the path returned will point to the extracted copy on disk.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc LICENSE Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.60.0-2mdv2011.0
+ Revision: 656915
- rebuild for updated spec-helper

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 595970
- update to new version 0.06

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 401661
- rebuild using %%perl_convert_version
- fixed license field

* Fri May 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.05-1mdv2010.0
+ Revision: 369686
- update to new version 0.05

* Tue Mar 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2009.1
+ Revision: 347688
- update to new version 0.04

* Sun Nov 16 2008 Jérôme Quelin <jquelin@mandriva.org> 0.03-1mdv2009.1
+ Revision: 303648
- update to new version 0.03

* Tue Nov 04 2008 Jérôme Quelin <jquelin@mandriva.org> 0.02-1mdv2009.1
+ Revision: 299764
- import perl-File-ShareDir-PAR


* Tue Nov 04 2008 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist

