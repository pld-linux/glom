Summary:	A user-friendly database environment
Summary(pl.UTF-8):	Przyjazne użytkownikowi środowisko bazodanowe
Name:		glom
Version:	1.6.13
Release:	4
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/glom/1.6/%{name}-%{version}.tar.bz2
# Source0-md5:	827eb7927b4b1e764772e40bf3a77cc4
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-postgres-utils.patch
URL:		http://www.glom.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avahi-glib-devel
BuildRequires:	bakery-devel >= 2.4.3-2
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils >= 0.10.0
BuildRequires:	gnome-vfsmm-devel >= 2.16.0
BuildRequires:	goocanvas-devel
BuildRequires:	gtkmm-devel >= 2.10.5
BuildRequires:	intltool >= 0.36.0
BuildRequires:	iso-codes
BuildRequires:	libgdamm3-devel
BuildRequires:	libgnome-devel >= 2.16.0
BuildRequires:	libgtksourceviewmm-devel
BuildRequires:	libtool
BuildRequires:	libxslt-devel >= 1.1.17
BuildRequires:	pkgconfig
BuildRequires:	python-gnome-extras-gda-devel >= 2.19.1
BuildRequires:	python-pygtk-devel >= 2:2.12.0
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,postun):	shared-mime-info
Requires:	libgda3-provider-postgres
Requires:	python-gnome-extras-gda >= 2.19.1
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glom is an easy-to-use database designer and user interface.

%description -l pl.UTF-8
Glom jest łatwym w użyciu programem do projektowania baz danych oraz
interfejsem użytkownika.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gnome_doc_prepare}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--disable-update-mime-database \
	--disable-scrollkeeper \
	--with-postgres-utils=%{_bindir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/mime-info

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_desktop_database_post
%update_mime_database
%update_icon_cache hicolor
%scrollkeeper_update_post

%postun
/sbin/ldconfig
%update_desktop_database_postun
%update_mime_database
%update_icon_cache hicolor
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/glom
%attr(755,root,root) %{_libdir}/libglom.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libglom.so.0
%attr(755,root,root) %{py_sitedir}/glom.so
%{_datadir}/%{name}
%{_datadir}/mime/packages/glom.xml
%{_desktopdir}/glom.desktop
%{_iconsdir}/hicolor/*/apps/*
