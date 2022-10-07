Name:		recoverjpeg
Version:	2.6.3
Release:	1
Summary:	JFIF/JPEG File Recovery Tool
Source0:	https://rfc1149.net/download/recoverjpeg/recoverjpeg-%{version}.tar.gz
URL:		http://www.rfc1149.net/devel/recoverjpeg
Group:		Graphics
License:	GPL
Requires:	imagemagick
BuildRequires:	make gcc
BuildRequires:	autoconf automake libtool 

%description
recoverjpeg tries to recover JFIF (JPEG) pictures from a peripheral. This may
be useful if you mistakenly overwrite a partition or if a device such as a
digital camera memory card is bogus.

%prep
%autosetup -p1
autoreconf -fiv
%configure

%build
%make_build

%install
%make_install

%files
%doc COPYING
%{_bindir}/recoverjpeg
%{_bindir}/recovermov
%{_bindir}/remove-duplicates
%{_bindir}/sort-pictures
%doc %{_mandir}/man1/recoverjpeg.1*
%doc %{_mandir}/man1/remove-duplicates.1*
%doc %{_mandir}/man1/sort-pictures.1*
%doc %{_mandir}/man1/recovermov.1*
