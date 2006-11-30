Summary:	A user-friendly database environment
Summary(pl):	Przyjazne u¿ytkownikowi ¶rodowisko bazodanowe
Name:		glom
Version:	1.2.1
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/glom/1.2/%{name}-%{version}.tar.bz2
# Source0-md5:	690b14bea6086ada40764b7e878924fa
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-buildfix.patch
URL:		http://www.glom.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bakery-devel >= 2.4.0
BuildRequires:	gnome-doc-utils >= 0.8.0
BuildRequires:	gnome-vfsmm-devel >= 2.16.0
BuildRequires:	gtkmm-devel >= 2.10.5
BuildRequires:	intltool
BuildRequires:	iso-codes
BuildRequires:	libgdamm-devel >= 1.3.7
BuildRequires:	libgnome-devel >= 2.16.0
BuildRequires:	libgnomecanvasmm-devel >= 2.16.0
BuildRequires:	libtool
BuildRequires:	libxslt-devel >= 1.1.17
BuildRequires:	python-gnome-extras-gda-devel >= 2.14.2-4
BuildRequires:	python-pygtk-devel >= 2:2.10.3
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,postun):	shared-mime-info
Requires:	python-gnome-extras-gda >= 2.14.2-4
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glom is an easy-to-use database designer and user interface.

%description -l pl
Glom jest ³atwym w u¿yciu programem do projektowania baz danych oraz
interfejsem u¿ytkownika.

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
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-static \
	--disable-update-mime-database \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/mime-info

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_mime_database
%update_icon_cache hicolor
%scrollkeeper_update_post

%postun
/sbin/ldconfig
%update_mime_database
%update_icon_cache hicolor
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libglom.so*
%attr(755,root,root) %{py_sitedir}/glom.so
%{_datadir}/%{name}
%{_datadir}/mime/packages/*.xml
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%dir %{_omf_dest_dir}/%{name}
%{_omf_dest_dir}/%{name}/glom-C.omf
%lang(de) %{_omf_dest_dir}/%{name}/glom-de.omf
