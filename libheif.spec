#
# Conditional build:
%bcond_without	tests	# don't perform "make check"
#
Summary:	ISO/IEC 23008-12:2017 HEIF file format decoder and encoder
Summary(pl.UTF-8):	Koder i dekoder formatu plików HEIF zgodnego z ISO/IEC 23008-12:2017
Name:		libheif
Version:	1.9.0
Release:	1
License:	LGPL v3+ (library), GPL v3+ (tools)
Group:		Libraries
#Source0Download: https://github.com/strukturag/libheif/releases/
Source0:	https://github.com/strukturag/libheif/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8a03d009e521653654ec78ea34bd96e8
Patch0:		%{name}-pc.patch
Patch1:		%{name}-gdkpixbuf.patch
URL:		https://github.com/strukturag/libheif
BuildRequires:	aom-devel
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake >= 1:1.13
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	libde265-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:2
BuildRequires:	libx265-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.734
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libheif is an ISO/IEC 23008-12:2017 HEIF file format decoder and
encoder.

HEIF is a new image file format employing HEVC (h.265) image coding
for the best compression ratios currently possible.

libheif makes use of libde265 for the actual image decoding and x265
for encoding. Alternative codecs for, e.g., AVC and JPEG can be
provided as plugins.

%description -l pl.UTF-8
libheif to koder i dekoder formatu plików HEIF, zgodnego z ISO/IEC
23008-12:2017.

HEIF to nowy format plików obrazów wykorzystujący kodowanie obrazu
HEVC (h.265) w celu osiągnięcia najwyższych dostepnych obecnie
współczynników kompresji.

libheif wykorzystuje libde265 do właściwego procesu dekodowania obrazu
oraz x265 do kodowania. Alternatywne kodeki do np. AVC czy JPEG mogą
być dostarczone jako wtyczki.

%package devel
Summary:	Header files for libheif
Summary(de.UTF-8):	libheif Headers
Summary(pl.UTF-8):	Pliki nagłówkowe libheif
License:	LGPL v3+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	aom-devel
Requires:	libde265-devel
Requires:	libstdc++-devel >= 6:4.7
Requires:	libx265-devel

%description devel
The header files are only needed for development of programs using the
libheif library.

%description devel -l pl.UTF-8
Pliki nagłówkowe, potrzebne jedynie do rozwijania oprogramowania
wykorzystującego bibliotekę libheif.

%package static
Summary:	Static libheif library
Summary(pl.UTF-8):	Statyczna biblioteka libheif
License:	LGPL v3+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libheif library.

%description static -l pl.UTF-8
Statyczna biblioteka libheif.

%package progs
Summary:	libheif utility programs
Summary(pl.UTF-8):	Programy narzędziowe libheif
License:	GPL v3+
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
This package contains utility programs to convert HEIF files.

%description progs -l pl.UTF-8
Ten pakiet zawiera programy narzędziowe do konwersji plików HEIF.

%package -n gdk-pixbuf2-loader-heif
Summary:	gdk-pixbuf plugin to handle HEIF files
Summary(pl.UTF-8):	Wtyczka gdk-pixbuf do obsługi plików HEIF
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n gdk-pixbuf2-loader-heif
gdk-pixbuf plugin to handle HEIF files.

%description -n gdk-pixbuf2-loader-heif -l pl.UTF-8
Wtyczka gdk-pixbuf do obsługi plików HEIF.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
%ifarch x32
	--disable-go
%endif

%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# module loaded via gmodule
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gdk-pixbuf-2.0/2.*/loaders/*.la
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libheif.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libheif.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libheif.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libheif.so
%{_includedir}/libheif
%{_pkgconfigdir}/libheif.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libheif.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/heif-convert
%attr(755,root,root) %{_bindir}/heif-enc
%attr(755,root,root) %{_bindir}/heif-info
%attr(755,root,root) %{_bindir}/heif-thumbnailer
%{_datadir}/mime/packages/avif.xml
%{_datadir}/mime/packages/heif.xml
%{_datadir}/thumbnailers/heif.thumbnailer
%{_mandir}/man1/heif-convert.1*
%{_mandir}/man1/heif-enc.1*
%{_mandir}/man1/heif-info.1*
%{_mandir}/man1/heif-thumbnailer.1*

%files -n gdk-pixbuf2-loader-heif
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gdk-pixbuf-2.0/2.*/loaders/libpixbufloader-heif.so
