%define upstream_name    File-ShareDir-PAR
%define upstream_version 0.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    File::ShareDir with PAR support
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Class::Inspector)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::ShareDir)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Params::Util)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc LICENSE Changes
%{_mandir}/man3/*
%perl_vendorlib/*

