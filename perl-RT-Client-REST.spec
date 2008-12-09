#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl

%define	pdir	RT
%define	pnam	Client-REST
Summary:	RT::Client::REST - talk to RT installation using REST protocol
Name:		perl-RT-Client-REST
Version:	0.37
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/D/DM/DMITRI/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	383bf572afdb8040641d4d413ef96476
URL:		http://search.cpan.org/dist/RT-Client-REST/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RT::Client::REST is /usr/bin/rt converted to a Perl module. I needed
to implement some RT interactions from my application, but did not
feel that invoking a shell command is appropriate. Thus, I took rt
tool, written by Abhijit Menon-Sen, and converted it to an
object-oriented Perl module.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/RT
%{_mandir}/man3/*
