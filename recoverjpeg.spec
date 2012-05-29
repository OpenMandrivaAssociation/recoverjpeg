Name:		recoverjpeg
Version:	2.1.1
Release:	1
Summary:	JFIF/JPEG File Recovery Tool
Source0:	https://github.com/downloads/samueltardieu/recoverjpeg/%{name}-%{version}.tar.gz
URL:		http://www.rfc1149.net/devel/recoverjpeg
Group:		Graphics
License:	GPL
Requires:	ImageMagick
BuildRequires:	make gcc
BuildRequires:	autoconf automake libtool 

%description
recoverjpeg tries to recover JFIF (JPEG) pictures from a peripheral. This may
be useful if you mistakenly overwrite a partition or if a device such as a
digital camera memory card is bogus.

%prep
%setup -q

%build
autoreconf -fiv
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_bindir}/recoverjpeg
%{_bindir}/recovermov
%{_bindir}/remove-duplicates
%{_bindir}/sort-pictures
%doc %{_mandir}/man1/recoverjpeg.1*
%doc %{_mandir}/man1/sort-pictures.1*
%doc %{_mandir}/man1/recovermov.1*
