# Conditional build:
%bcond_without	tests		# don't perform "make check"
#
Summary:	ISO/IEC 23008-12:2017 HEIF file format decoder and encoder
Name:		libheif
Version:	1.3.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	https://github.com/strukturag/libheif/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	634b0d33db07c85eea2f56c1d8cb87b1
URL:		https://github.com/strukturag/libheif
BuildRequires:	libde265-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
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

%package devel
Summary:	Header files for libheif
Summary(de.UTF-8):	libheif Headers
Summary(es.UTF-8):	Archivos de inclusión y bibliotecas estáticas
Summary(fr.UTF-8):	en-têtes et bibliothèques statiques
Summary(pl.UTF-8):	Pliki nagłówkowe libheif
Summary(pt_BR.UTF-8):	Arquivos de inclusão e bibliotecas estáticas
Summary(tr.UTF-8):	başlık dosyaları ve statik kitaplıklar
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
The header files are only needed for development of programs using the
libheif library.

%package static
Summary:	Static libheif library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libheif library.

%package progs
Summary:	libheif utility programs
Group:		Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description progs
This package contains utility programs to convert HEIF files.

%prep
%setup -q

%build
%configure
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libheif.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libheif.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libheif.so
%{_includedir}/libheif
%{_pkgconfigdir}/libheif.pc
%{_libdir}/libheif.la

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
