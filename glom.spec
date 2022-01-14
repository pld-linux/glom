Summary:	A user-friendly database environment
Summary(pl.UTF-8):	Przyjazne użytkownikowi środowisko bazodanowe
Name:		glom
Version:	1.32.0
Release:	6
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/glom/1.32/%{name}-%{version}.tar.xz
# Source0-md5:	194d2dec2254f48c49f518935302992f
Patch0:		%{name}-build.patch
Patch1:		%{name}-pc.patch
URL:		http://www.glom.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	boost-devel
BuildRequires:	boost-python3-devel
BuildRequires:	evince-devel >= 3.0
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glibmm-devel >= 2.47.4
BuildRequires:	goocanvas2-devel >= 2.0.1
BuildRequires:	goocanvasmm2-devel >= 1.90.11
BuildRequires:	gtkmm3-devel >= 3.22.0
BuildRequires:	gtksourceviewmm3-devel >= 3.18.0
BuildRequires:	intltool >= 0.36.0
BuildRequires:	iso-codes
BuildRequires:	libarchive-devel >= 3.0
BuildRequires:	libepc-devel >= 0.4.0
BuildRequires:	libgda5-devel >= 5.2.9
BuildRequires:	libgdamm5-devel >= 4.99.10
BuildRequires:	libsigc++-devel >= 2.9.2
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	libtool >= 2:2.2.0
BuildRequires:	libxml++-devel >= 3.0.0
BuildRequires:	libxslt-devel >= 1.1.17
BuildRequires:	mm-common >= 0.9.5
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(libgda-mysql-5.0)
BuildRequires:	pkgconfig(libgda-postgres-5.0)
BuildRequires:	pkgconfig(libgda-sqlite-5.0)
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-pygobject3-devel >= 2.29.0
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sphinx-pdg
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	shared-mime-info
Requires:	evince >= 3.0
Requires:	glibmm >= 2.47.4
Requires:	goocanvas2 >= 2.0.1
Requires:	goocanvasmm2 >= 1.90.11
Requires:	gtkmm3 >= 3.22.0
Requires:	gtksourceviewmm3 >= 3.18.0
Requires:	iso-codes
Requires:	libepc >= 0.4.0
Requires:	libgda5 >= 5.2.9
Requires:	libgdamm5 >= 4.99.10
Requires:	libsigc++ >= 2.9.2
Requires:	libxml++ >= 3.0.0
Requires:	libxslt >= 1.1.17
Requires:	python3-modules >= 1:3.2
Requires:	python3-pygobject3 >= 2.29.0
Suggests:	libgda5-provider-mysql >= 5.2.9
Suggests:	libgda5-provider-postgres >= 5.2.9
Suggests:	libgda5-provider-sqlite >= 5.2.9
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
Requires:	glibmm-devel >= 2.47.4
Requires:	libgdamm5-devel >= 4.99.10
Requires:	libstdc++-devel >= 6:5
Requires:	libxml++-devel >= 3.0.0
Requires:	libxslt-devel >= 1.1.17

%description devel
Header files for Glom library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Glom.

%package apidocs
Summary:	API documentation for Glom library and its Python binding
Summary(pl.UTF-8):	Dokumentacja API biblioteki Glom i jej wiązań do Pythona
Group:		Documentation
BuildArch:	noarch

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
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PYTHON="%{__python3}" \
	--disable-silent-rules \
	--disable-static \
	--disable-update-mime-database \
	--enable-mysql \
	--enable-sqlite \
	--with-mysql-utils=%{_bindir} \
	--with-postgres-utils=%{_bindir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/*.la

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -pr examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_desktop_database_post
%update_mime_database
%update_icon_cache hicolor

%postun
/sbin/ldconfig
%update_desktop_database_postun
%update_mime_database
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/glom
%attr(755,root,root) %{_bindir}/glom_export_po
%attr(755,root,root) %{_bindir}/glom_export_po_all
%attr(755,root,root) %{_bindir}/glom_import_po_all
%attr(755,root,root) %{_bindir}/glom_test_connection
%attr(755,root,root) %{_libdir}/libglom-1.32.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libglom-1.32.so.0
%attr(755,root,root) %{py3_sitedir}/glom_1_32.so
%{_datadir}/%{name}
%{_datadir}/appdata/glom.appdata.xml
%{_datadir}/mime/packages/glom.xml
%{_desktopdir}/glom.desktop
%{_iconsdir}/hicolor/*x*/apps/glom.png
%{_iconsdir}/hicolor/scalable/apps/glom.svg

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglom-1.32.so
%{_includedir}/glom-1.32
%{_pkgconfigdir}/glom-1.32.pc

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/libglom-1.32
%{_docdir}/pyglom_1_32
%{_datadir}/devhelp/books/libglom-1.32

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/glom_create_from_example
%{_examplesdir}/%{name}-%{version}
