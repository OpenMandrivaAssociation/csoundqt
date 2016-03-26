%global optflags %{optflags} -Wstrict-aliasing=0 
%define debug_package	%{nil}
#define distsuffix mrb
%define oname CsoundQt
Name:			csoundqt
Version:		0.9.1
Release:		2
Summary:		Frontend for the csound sound processor
License:		LGPLv2.1
Group:			Sound
URL:			http://csoundqt.github.io
Source0:		http://garr.dl.sourceforge.net/project/qutecsound/CsoundQt/%{version}/%{oname}-%{version}.tar.gz
Source1:		csoundqt.desktop
BuildRequires:		desktop-file-utils
BuildRequires:		qt4-devel
BuildRequires:      	doxygen
BuildRequires:     	imagemagick
BuildRequires:     	csound-devel
BuildRequires:     	PyQt4
BuildRequires:     	csound
BuildRequires:     	pkgconfig(sndfile)
BuildRequires:     	pkgconfig(python)
%rename			qutecsound


Requires:     	csound

%description
CsoundQt is a frontend for Csound featuring 
a highlighting editor with autocomplete, 
interactive widgets and integrated help. 
It is a cross-platform and aims to be a simple 
yet powerful and complete development environment 
for Csound. It can open files created by MacCsound. 
Csound is a musical programming 
language with a very long history,
with roots in the origins of computer music.
It is still being maintained by an active 
community and despite its age, is still one of 
the most powerful tools for sound processing and synthesis. 
CsoundQt hopes to bring the power of 
Csound to a larger group of people, by reducing 
Csound's intial learning curve, and by giving 
users more immediate control of their sound. 
It hopes to be both a simple tool for 
the beginner, as well as a powerful tool for experienced users.

%prep
%setup -qn %{oname}-%{version}

%build
%qmake_qt4 qcs.pro CSOUND_LIBRARY_DIR=%_libdir
%make

%install
# Prepare folders no install provided
install -d %{buildroot}/usr/{bin,share/{applications,{,doc}/%{name}}}

# Bin file
install -Dm755 bin/CsoundQt-d-cs6 "%{buildroot}%{_bindir}/%{name}"

# Examples docs and data
cp -a examples %{buildroot}%{_datadir}/%{name}
cp -a images %{buildroot}%{_datadir}/%{name}


# Desktop file and pixmaps
install -Dm644 %{SOURCE1} "%{buildroot}%{_datadir}/applications"
install -Dm644 images/qtcs.png "%{buildroot}%{_datadir}/pixmaps/%{name}.png"

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%doc ChangeLog BUILDING COPYING doc/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png




