%define		pname	cairo-java
Summary:	Java interface for Cairo library
Summary(pl):	Wrapper Javy dla biblioteki Cairo
Name:		java-cairo
Version:	1.0.8
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/cairo-java/1.0/%{pname}-%{version}.tar.bz2
# Source0-md5:	857c194452f6762f17e352a21b33046f
URL:		http://java-gnome.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.2.4
BuildRequires:	fontconfig-devel >= 1:2.4.1
BuildRequires:	gcc-java >= 5:3.3.2
BuildRequires:	java-glib-devel >= 0.4.2
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		macros	%{_datadir}/glib-java/macros

%description
Java interface for the Cairo library.

%description -l pl
Wrapper Javy dla biblioteki Cairo.

%package devel
Summary:	Header files for java-cairo library
Summary(pl):	Pliki nag³ówkowe biblioteki java-cairo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 1.2.4
Requires:	fontconfig-devel >= 1:2.4.1
Requires:	java-glib-devel >= 0.4.2

%description devel
Header files for java-cairo library.

%description devel -l pl
Pliki nag³ówkowe biblioteki java-cairo.

%prep
%setup -q -n %{pname}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I %{macros}
%{__automake}
%{__autoconf}
%configure \
	GCJFLAGS="%{rpmcflags}" \
	JAR=%{_bindir}/fastjar \
	--without-javadocs \
	--enable-pdf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{pname}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README 
%attr(755,root,root) %{_libdir}/libcairo*-1.0.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcairojava.so
%attr(755,root,root) %{_libdir}/libcairojni.so
%{_javadir}/*.jar
%{_libdir}/*.la
%{_pkgconfigdir}/*.pc
