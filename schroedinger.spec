# TODO: CUDA (as bcond)
#
# Conditional build:
%bcond_with	opengl	# OpenGL rendering backend (disabled by default) [missing files as of 1.0.11]
#
Summary:	Library for decoding and encoding video in the Dirac format
Summary(pl.UTF-8):	Biblioteka do dekodowania i kodowania obrazu w formacie Dirac
Name:		schroedinger
Version:	1.0.11
Release:	3
License:	MPL 1.1 or LGPL v2 or GPL v2 or MIT
Group:		Libraries
Source0:	http://diracvideo.org/download/schroedinger/%{name}-%{version}.tar.gz
# Source0-md5:	da6af08e564ca1157348fb8d92efc891
Patch0:		%{name}-opt.patch
URL:		http://www.diracvideo.org/
%{?with_opengl:BuildRequires:	OpenGL-devel}
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake >= 1.6
%{?with_opengl:BuildRequires:	glew-devel >= 1.5}
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	orc-devel >= 0.4.16
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.98
%{?with_opengl:Requires:	glew >= 1.5}
Requires:	orc >= 0.4.16
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
%{?with_opengl:Requires:	glew-devel >= 1.5}
Requires:	libstdc++-devel
Requires:	orc-devel >= 0.4.16

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

%package apidocs
Summary:	API documentation for Schroedinger library
Summary(pl.UTF-8):	Dokumentacja API biblioteki Schroedinger
Group:		Documentation

%description apidocs
API documentation for Schroedinger library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Schroedinger.

%prep
%setup -q
%patch0 -p1

%{__rm} m4/libtool.m4 m4/lt*.m4

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir} \
	%{?with_opengl:--with-opengl}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libschroedinger-1.0.la

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
%{_includedir}/schroedinger-1.0
%{_pkgconfigdir}/schroedinger-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libschroedinger-1.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/schroedinger
