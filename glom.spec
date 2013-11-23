Summary:	A user-friendly database environment
Summary(pl.UTF-8):	Przyjazne użytkownikowi środowisko bazodanowe
Name:		glom
Version:	1.24.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/glom/1.24/%{name}-%{version}.tar.xz
# Source0-md5:	27cdba1fb3b24ee9a7561980b889ca18
URL:		http://www.glom.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	boost-devel
BuildRequires:	evince-devel >= 3.0
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	glibmm-devel >= 2.32.0
BuildRequires:	gnome-doc-utils >= 0.10.0
BuildRequires:	goocanvas2-devel >= 2.0.1
BuildRequires:	goocanvasmm2-devel >= 1.90.8
BuildRequires:	gtkmm3-devel >= 3.4.0
BuildRequires:	gtksourceviewmm3-devel >= 3.0.0
BuildRequires:	intltool >= 0.36.0
BuildRequires:	iso-codes
BuildRequires:	libepc-devel >= 0.4.0
BuildRequires:	libgda5-devel >= 5.0.3
BuildRequires:	libgdamm5-devel >= 4.99.6
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.2.0
BuildRequires:	libxml++-devel >= 2.23.1
BuildRequires:	libxslt-devel >= 1.1.17
BuildRequires:	mm-common >= 0.9.5
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(libgda-mysql-5.0)
BuildRequires:	pkgconfig(libgda-postgres-5.0)
BuildRequires:	pkgconfig(libgda-sqlite-5.0)
BuildRequires:	python-devel
BuildRequires:	python-pygobject3-devel >= 2.29.0
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sphinx-pdg
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,postun):	shared-mime-info
%pyrequires_eq	python-modules
Requires:	evince >= 3.0
Requires:	glibmm >= 2.32.0
Requires:	goocanvas2 >= 2.0.1
Requires:	goocanvasmm2 >= 1.90.8
Requires:	gtkmm3 >= 3.4.0
Requires:	gtksourceviewmm3 >= 3.0.0
Requires:	iso-codes
Requires:	libepc >= 0.4.0
Requires:	libgda5 >= 5.0.3
Requires:	libgdamm5 >= 4.99.6
Requires:	libxml++ >= 2.23.1
Requires:	libxslt >= 1.1.17
Requires:	python-pygobject3 >= 2.29.0
Suggests:	libgda5-provider-mysql >= 5.0.3
Suggests:	libgda5-provider-postgres >= 5.0.3
Suggests:	libgda5-provider-sqlite >= 5.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glom is an easy-to-use database designer and user interface.

%description -l pl.UTF-8
Glom jest łatwym w użyciu programem do projektowania baz danych oraz
interfejsem użytkownika.

%package devel
Summary:	Header files for Glom library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Glom
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Glom library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Glom.

%package apidocs
Summary:	API documentation for Glom library and its Python binding
Summary(pl.UTF-8):	Dokumentacja API biblioteki Glom i jej wiązań do Pythona
Group:		Documentation

%description apidocs
API documentation for Glom library and its Python binding.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Glom i jej wiązań do Pythona.

%package examples
Summary:	Examples for Glom
Summary(pl.UTF-8):	Przykłady dla Gloma
Group:		Documentation

%description examples
Examples for Glom.

%description examples -l pl.UTF-8
Przykłady dla Gloma.

%prep
%setup -q

%build
%{__gnome_doc_prepare}
%{__gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-scrollkeeper \
	--disable-silent-rules \
	--disable-static \
	--disable-update-mime-database \
	--with-postgres-utils=%{_bindir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/*.la

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
%attr(755,root,root) %{_bindir}/glom_export_po
%attr(755,root,root) %{_bindir}/glom_export_po_all
%attr(755,root,root) %{_bindir}/glom_import_po_all
%attr(755,root,root) %{_bindir}/glom_test_connection
%attr(755,root,root) %{_libdir}/libglom-1.24.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libglom-1.24.so.0
%attr(755,root,root) %{py_sitedir}/glom_1_24.so
%{_datadir}/%{name}
%{_datadir}/appdata/glom.appdata.xml
%{_datadir}/mime/packages/glom.xml
%{_desktopdir}/glom.desktop
%{_iconsdir}/hicolor/*/apps/glom.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglom-1.24.so
%{_includedir}/glom-1.24
%{_pkgconfigdir}/glom-1.24.pc

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/libglom-1.24
%{_docdir}/pyglom_1_24
%{_datadir}/devhelp/books/libglom-1.24

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/glom_create_from_example
%dir %{_docdir}/glom
%{_docdir}/glom/examples
