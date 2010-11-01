Summary:	Library for decoding and encoding video in the Dirac format
Summary(pl.UTF-8):	Biblioteka do dekodowania i kodowania obrazu w formacie Dirac
Name:		schroedinger
Version:	1.0.10
Release:	1
License:	MPL 1.1 or LGPL v2 or GPL v2 or MIT
Group:		Libraries
Source0:	http://diracvideo.org/download/schroedinger/%{name}-%{version}.tar.gz
# Source0-md5:	9de088ccc314bb9e766cb3aa6510a0ef
Patch0:		%{name}-opt.patch
URL:		http://www.diracvideo.org/
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake >= 1.6
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	orc-devel >= 0.4.10
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.98
Requires:	orc >= 0.4.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for decoding and encoding video in the Dirac format. It is
implemented in ANSI C and optimized through the use of liboil.
libschroedinger is written as a collaboration between the BBC Research
and Development, David Schleef and Fluendo.

%description -l pl.UTF-8
Biblioteka do dekodowania i kodowania obrazu w formacie Dirac. Jest
zaimplementowana w ANSI C i zoptymalizowana poprzez użycie liboil.
Jest pisana we współpracy między BBC Research and Development, Davidem
Schleefem i Fluendo.

%package devel
Summary:	Header files for Schroedinger library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Schroedinger
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	orc-devel >= 0.4.10

%description devel
Header files for Schroedinger library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Schroedinger.

%package static
Summary:	Static Schroedinger library
Summary(pl.UTF-8):	Statyczna biblioteka Schroedinger
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Schroedinger library.

%description static -l pl.UTF-8
Statyczna biblioteka Schroedinger.

%prep
%setup -q
%patch0 -p1

rm -f m4/libtool.m4 m4/lt*.m4

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING.MIT NEWS TODO
%attr(755,root,root) %{_libdir}/libschroedinger-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libschroedinger-1.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libschroedinger-1.0.so
%{_libdir}/libschroedinger-1.0.la
%{_includedir}/schroedinger-1.0
%{_pkgconfigdir}/schroedinger-1.0.pc
%{_gtkdocdir}/schroedinger

%files static
%defattr(644,root,root,755)
%{_libdir}/libschroedinger-1.0.a
