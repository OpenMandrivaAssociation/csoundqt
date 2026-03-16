%global	debug_package %{nil}
%define	oname	CsoundQt

Summary:	Front-end for the csound sound processor
Name:	csoundqt
Version:	7.0.0
Release:	0.beta.2
License:	LGPLv2+
Group:	Sound
Url:			https://csoundqt.github.io/
#Source0:	https://github.com/%%{oname}/%%{oname}/archive/%%{oname}-%%{version}.tar.gz
Source0:	%{oname}-%{version}-beta2.tar.xz
BuildRequires:	byacc
BuildRequires:	cmake
BuildRequires:	csound >= 7.0.0
BuildRequires:	desktop-file-utils
BuildRequires:	doxygen
BuildRequires:	flex
BuildRequires:	make
BuildRequires:	qt6-qttools-linguist-tools
BuildRequires:	csound-devel >= 7.0.0
BuildRequires:	python-qt6-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(Qt6Concurrent)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Network)
BuildRequires:	pkgconfig(Qt6OpenGL)
BuildRequires:	pkgconfig(Qt6PrintSupport)
BuildRequires:	pkgconfig(Qt6Qml)
BuildRequires:	pkgconfig(Qt6QmlMeta)
BuildRequires:	pkgconfig(Qt6QmlModels)
BuildRequires:	pkgconfig(Qt6QmlWorkerScript)
BuildRequires:	pkgconfig(Qt6Quick)
BuildRequires:	pkgconfig(Qt6QuickWidgets)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Xml)
BuildRequires:	pkgconfig(rtmidi)
BuildRequires:	pkgconfig(sndfile)
Requires:	csound >= 7.0.0
Requires:	python3dist(pyqt6)
%rename	qutecsound

%description
This is a front-end for Csound featuring a highlighting editor with
auto-complete, interactive widgets and integrated help. It is a cross platform
and aims to be a simple yet powerful and complete development environment for
Csound. It can open files created by MacCsound. Csound is a musical
programming language with a very long history, with roots in the origins of
computer music. It is still being maintained by an active community and
despite its age, is still one of the most powerful tools for sound processing
and synthesis. This program  hopes to bring the power of Csound to a larger
group of people, by reducing Csound's initial learning curve, and by giving
users more immediate control of their sound. It hopes to be both a simple
tool for the beginner, as well as a powerful tool for experienced users.

%files
%doc ChangeLog COPYING README.md
%doc doc/*.pdf doc/images/* release_notes/*.md
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/x-csound-*.xml
%{_datadir}/icons/hicolor/*/mimetypes/csound.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{oname}-%{version}-beta2

# Fix paths
sed -i s,"/usr/lib","%{_libdir}",g qcs-unix.pro
sed -i s,"/usr/local/include","%{_includedir}",g qcs-unix.pro


%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export LDFLAGS="%{ldflags}"
%{_bindir}/qmake-qt6 qcs.pro CONFIG+=html_webengine CONFIG+=html_support CONFIG+=rtmidi \
											INSTALL_DIR="%{buildroot}%{_prefix}" SHARE_DIR="%{buildroot}%{_datadir}" \
%if "lib64" != "lib" 
	libsuff=64 \
%endif 
	QMAKE_CFLAGS="${CFLAGS:-$CFLAGS}" \
	QMAKE_CFLAGS_RELEASE="${CFLAGS:-$CFLAGS}" \
	QMAKE_CFLAGS_OPTIMIZE="${CFLAGS:-$CFLAGS}" \
	QMAKE_CFLAGS_OPTIMIZE_FULL="${CFLAGS:-$CFLAGS}" \
	QMAKE_CXXFLAGS="${CXXFLAGS:-$CXXFLAGS}" \
	QMAKE_CXXFLAGS_RELEASE="${CXXFLAGS:-$CXXFLAGS}" \
	QMAKE_LFLAGS="$LDFLAGS" \
	QMAKE_LFLAGS_RELEASE="$LDFLAGS"

%make_build


%install
%make_install INSTALL_DIR="%{buildroot}%{_prefix}" SHARE_DIR="%{buildroot}%{_datadir}"

# Install images data
cp -a images %{buildroot}%{_datadir}/%{name}

# Fix perms
chmod -x "%{buildroot}%{_datadir}/%{name}/Examples/McCurdy Collection/LiveAudioIn/pitchamdf.csd"
chmod -x "%{buildroot}%{_datadir}/%{name}/Examples/CsoundQt/K Miscellaneous/Pseudostereo.csd"
chmod -x %{buildroot}%{_datadir}/applications/%{name}.desktop 
