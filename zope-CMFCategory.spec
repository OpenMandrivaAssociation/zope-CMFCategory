%define Product CMFCategory
%define product cmfcategory
%define name    zope-%{Product}
%define version 0.8
%define release %mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    All algorithms related to categories and relations in CMF
License:    GPL
Group:      System/Servers
URL:        http://www.erp5.org
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
