# MAYBE TODO: default codecs (aom, libde265, x265, jpeg) as plugins, package plugins in subpackages?
#
# Conditional build:
%bcond_with	golang		# Go examples
%bcond_with	static_libs	# static library
%bcond_with	tests		# testing
# AVIF
%bcond_without	aom		# aom AVIF decoder/encoder
%bcond_with	dav1d		# dav1d AVIF decoder
%bcond_with	svtav1		# SVT-AV1 AVIF encoder
%bcond_with	rav1e		# rav1e AVIF encoder
# HEVC
%bcond_with	ffmpeg		# FFmpeg HEVC decoder (hw accelerated)
%bcond_with	kvazaar		# kvazaar HEVC encoder
%bcond_without	libde265	# libde265 HEVC decoder
%bcond_without	x265		# x265 HEVC encoder
# JPEG
%bcond_without	jpeg		# JPEG codecs support
# JPEG-2000
%bcond_without	openjpeg	# OpenJPEG (J2K) codecs support
# JPEG-2000-HT
%bcond_without	openjph		# OpenJPH (HTJ2K) encoder support
# VVC
%bcond_with	uvg266		# uvg266 VVC encoder (experimental)
%bcond_with	vvdec		# vvdec VVC decoder (experimental)
%bcond_with	vvenc		# vvenc VVC decoder (experimental)

%ifnarch %{ix86} %{x8664} aarch64
%undefine	with_rav1e
%endif
Summary:	ISO/IEC 23008-12:2017 HEIF file format decoder and encoder
Summary(pl.UTF-8):	Koder i dekoder formatu plików HEIF zgodnego z ISO/IEC 23008-12:2017
Name:		libheif
Version:	1.19.7
Release:	3
License:	LGPL v3+ (library), GPL v3+ (tools)
Group:		Libraries
#Source0Download: https://github.com/strukturag/libheif/releases/
Source0:	https://github.com/strukturag/libheif/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	cbb49df3d35360d228bac47f4287f2b8
URL:		https://github.com/strukturag/libheif
%{?with_aom:BuildRequires:	aom-devel}
BuildRequires:	cmake >= 3.16.3
%{?with_dav1d:BuildRequires:	dav1d-devel}
# libavcodec
%{?with_ffmpeg:BuildRequires:	ffmpeg-devel}
BuildRequires:	gdk-pixbuf2-devel >= 2.0
%{?with_golang:BuildRequires:	golang >= 1.6}
%{?with_kvazaar:BuildRequires:	kvazaar-devel}
%{?with_libde265:BuildRequires:	libde265-devel >= 1.0.7}
%{?with_jpeg:BuildRequires:	libjpeg-devel}
BuildRequires:	libpng-devel
BuildRequires:	libsharpyuv-devel
# C++20
BuildRequires:	libstdc++-devel >= 6:8
%{?with_x265:BuildRequires:	libx265-devel}
%{?with_openjpeg:BuildRequires:	openjpeg2-devel >= 2}
%{?with_openjph:BuildRequires:	openjph-devel}
BuildRequires:	pkgconfig
%{?with_rav1e:BuildRequires:	rav1e-devel}
%{?with_svtav1:BuildRequires:	svt-av1-devel}
BuildRequires:	rpmbuild(macros) >= 1.734
%{?with_uvg266:BuildRequires:	uvg266-devel}
%{?with_vvdec:BuildRequires:	vvdec-devel >= 2.3.0}
%{?with_vvdec:BuildRequires:	vvdec-devel < 3}
%{?with_vvenc:BuildRequires:	vvenc-devel >= 1.12.0}
%{?with_vvenc:BuildRequires:	vvenc-devel < 1.13}
%{?with_libde265:Requires:	libde265 >= 1.0.7}
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
%{?with_aom:Requires:	aom-devel}
Requires:	libde265-devel >= 1.0.7
Requires:	libsharpyuv-devel
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

%build
%if %{with static_libs}
%cmake -B build-static \
	-DBUILD_SHARED_LIBS=OFF \
	-DENABLE_PLUGIN_LOADING=OFF \
	-DCMAKE_COMPILE_WARNING_AS_ERROR=OFF \
	%{!?with_aom:-DWITH_AOM_DECODER=OFF} \
	%{!?with_aom:-DWITH_AOM_ENCODER=OFF} \
	%{?with_dav1d:-DWITH_DAV1D=ON} \
	%{?with_ffmpeg:-DWITH_FFMPEG_DECODER=ON} \
	%{?with_jpeg:-DWITH_JPEG_DECODER=ON} \
	%{?with_jpeg:-DWITH_JPEG_ENCODER=ON} \
	%{?with_kvazaar:-DWITH_KVAZAAR=ON} \
	%{!?with_libde265:-DWITH_LIBDE265=OFF} \
	%{?with_openjph:-DWITH_OPENJPH_ENCODER=ON} \
	%{?with_openjpeg:-DWITH_OpenJPEG_DECODER=ON} \
	%{?with_openjpeg:-DWITH_OpenJPEG_ENCODER=ON} \
	%{?with_rav1e:-DWITH_RAV1E=ON} \
	%{?with_svtav1:-DWITH_SvtEnc=ON} \
	%{?with_uvg266:-DWITH_UVG266=ON} \
	%{?with_vvdec:-DWITH_VVDEC=ON} \
	%{?with_vvenc:-DWITH_VVENC=ON} \
	%{!?with_x265:-DWITH_X265=OFF}

%{__make} -C build-static
%endif

%cmake -B build \
	-DCMAKE_COMPILE_WARNING_AS_ERROR=OFF \
	%{?with_tests:-DBUILD_TESTING=ON} \
	%{!?with_aom:-DWITH_AOM_DECODER=OFF} \
	%{!?with_aom:-DWITH_AOM_ENCODER=OFF} \
	%{?with_dav1d:-DWITH_DAV1D=ON} \
	%{?with_ffmpeg:-DWITH_FFMPEG_DECODER=ON} \
	%{?with_ffmpeg:-DWITH_FFMPEG_DECODER_PLUGIN=ON} \
	%{?with_jpeg:-DWITH_JPEG_DECODER=ON} \
	%{?with_jpeg:-DWITH_JPEG_ENCODER=ON} \
	%{?with_kvazaar:-DWITH_KVAZAAR=ON} \
	%{?with_kvazaar:-DWITH_KVAZAAR_PLUGIN=ON} \
	%{!?with_libde265:-DWITH_LIBDE265=OFF} \
	%{?with_openjpeg:-DWITH_OpenJPEG_DECODER=ON} \
	%{?with_openjpeg:-DWITH_OpenJPEG_ENCODER=ON} \
	%{?with_rav1e:-DWITH_RAV1E=ON} \
	%{?with_svtav1:-DWITH_SvtEnc=ON} \
	%{?with_uvg266:-DWITH_UVG266=ON} \
	%{?with_vvdec:-DWITH_VVDEC=ON} \
	%{?with_vvenc:-DWITH_VVENC=ON} \
	%{!?with_x265:-DWITH_X265=OFF}

%{__make} -C build

%{?with_tests:%{__make} -C build check}

%install
rm -rf $RPM_BUILD_ROOT

%if %{with static_libs}
%{__make} -C build-static install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libheif.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libheif.so.1
%dir %{_libdir}/libheif
# TODO: subpackages with plugins?
%if %{with dav1d}
%attr(755,root,root) %{_libdir}/libheif/libheif-dav1d.so
%endif
%if %{with ffmpeg}
%attr(755,root,root) %{_libdir}/libheif/libheif-ffmpegdec.so
%endif
%if %{with openjpeg}
%attr(755,root,root) %{_libdir}/libheif/libheif-j2kdec.so
%attr(755,root,root) %{_libdir}/libheif/libheif-j2kenc.so
%endif
%if %{with kvazaar}
%attr(755,root,root) %{_libdir}/libheif/libheif-kvazaar.so
%endif
%if %{with rav1e}
%attr(755,root,root) %{_libdir}/libheif/libheif-rav1e.so
%endif
%if %{with svtav1}
%attr(755,root,root) %{_libdir}/libheif/libheif-svtenc.so
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libheif.so
%{_includedir}/libheif
%{_pkgconfigdir}/libheif.pc
%{_libdir}/cmake/libheif

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libheif.a
%endif

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/heif-dec
%attr(755,root,root) %{_bindir}/heif-enc
%attr(755,root,root) %{_bindir}/heif-info
%attr(755,root,root) %{_bindir}/heif-thumbnailer
%{_datadir}/thumbnailers/heif.thumbnailer
%{_mandir}/man1/heif-dec.1*
%{_mandir}/man1/heif-enc.1*
%{_mandir}/man1/heif-info.1*
%{_mandir}/man1/heif-thumbnailer.1*

%files -n gdk-pixbuf2-loader-heif
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gdk-pixbuf-2.0/2.*/loaders/libpixbufloader-heif.so
