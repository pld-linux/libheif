#
# Conditional build:
%bcond_without	tests		# don't perform "make check"
#
Summary:	ISO/IEC 23008-12:2017 HEIF file format decoder and encoder
Summary(pl.UTF-8):	Koder i dekoder formatu plików HEIF zgodnego z ISO/IEC 23008-12:2017
Name:		libheif
Version:	1.3.2
Release:	4
License:	LGPL v3+ (library), GPL v3+ (tools)
Group:		Libraries
#Source0Download: https://github.com/strukturag/libheif/releases/
Source0:	https://github.com/strukturag/libheif/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	634b0d33db07c85eea2f56c1d8cb87b1
Patch0:		%{name}-pc.patch
URL:		https://github.com/strukturag/libheif
BuildRequires:	libde265-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libx265-devel
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
Requires:	libde265-devel
Requires:	libstdc++-devel
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

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_datadir}/mime/packages/heif.xml
%{_datadir}/thumbnailers/heif.thumbnailer
