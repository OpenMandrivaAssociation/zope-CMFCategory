%define Product CMFCategory
%define product cmfcategory
%define name    zope-%{Product}
%define version 0.8
%define release %mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    All algorithms related to categories and relations in CMF
License:    GPL
Group:      System/Servers
URL:        https://www.erp5.org
Source:     %{Product}-%{version}.tar.bz2
Requires:   zope
Obsoletes:  %{Product}
BuildRoot:  %{_tmppath}/%{name}

%description
Category objects allow to define classification categories
in an ERP5 portal. For example, a document may be assigned a color
attribute (red, blue, green). Rather than assigning an attribute
with a pop-up menu (which is still a possibility), we can prefer
in certain cases to associate to the object a category. In this
example, the category will be named color/red, color/blue or color/green

%prep
%setup -q -n %{Product}-%{version}

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_libdir}/zope/lib/python/Products/%{Product}
cp -pr * %{buildroot}%{_libdir}/zope/lib/python/Products/%{Product}

%files
%defattr(-,root,root)
%doc VERSION.txt
%{_libdir}/zope/lib/python/Products/%{Product}


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.8-6mdv2010.0
+ Revision: 435479
- rebuild
- rebuild

* Sat Aug 09 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.8-4mdv2009.0
+ Revision: 269876
- rebuild early 2009.0 package (before pixel changes)

* Sun May 11 2008 Nicolas Lécureuil <neoclust@mandriva.org> 0.8-3mdv2009.0
+ Revision: 205682
- Should not be noarch ed

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.8-2mdv2008.1
+ Revision: 136633
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.8-2mdv2008.0
+ Revision: 91830
- new version
  package renaming
- package renaming
- import CMFCategory

