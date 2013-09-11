Summary:	PDF plugin
Name:		zathura-pdf-poppler
Version:	0.2.3
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	https://pwmt.org/projects/zathura/plugins/download/%{name}-%{version}.tar.gz
# Source0-md5:	1d8deb2d2ee5a6847267f977b8f2e542
BuildRequires:	pkg-config
BuildRequires:	poppler-glib-devel
BuildRequires:	zathura-devel
Requires(post,postun):	desktop-file-utils
Requires:	zathura
Provides:	zathura-plugin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The zathura-pdf-poppler plugin adds PDF support to zathura by using
the poppler rendering engine.

%prep
%setup -q

%{__sed} -i "s/^DFLAGS.*/DFLAGS=/" config.mk

%build
export CFLAGS="%{rpmcflags}"
export LDFLAGS="%{rpmldflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT	\
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE
%attr(755,root,root) %{_libdir}/zathura/pdf.so
%{_desktopdir}/zathura-pdf-poppler.desktop

