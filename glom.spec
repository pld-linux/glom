Summary:	A user-friendly database environment
Summary(pl):	Przyjazne użytkownikowi środowisko bazodanowe
Name:		glom
Version:	1.0.5
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/glom/1.0/%{name}-%{version}.tar.bz2
# Source0-md5:	55e5b35d268e342ed5305e9c798856a4
Patch0:		%{name}-desktop.patch
URL:		http://www.glom.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bakery-devel >= 2.4.0
BuildRequires:	gnome-doc-utils >= 0.7.2
BuildRequires:	gnome-vfsmm-devel >= 2.16.0
BuildRequires:	gtkmm-devel >= 2.10.1
BuildRequires:	intltool
BuildRequires:	iso-codes
BuildRequires:	libgdamm-devel >= 1.3.7
BuildRequires:	libgnome-devel >= 2.16.0
BuildRequires:	libgnomecanvasmm-devel >= 2.16.0
BuildRequires:	libtool
BuildRequires:	libxslt-devel >= 1.1.17
BuildRequires:	python-gnome-extras-gda-devel >= 2.14.2-4
BuildRequires:	python-pygtk-devel >= 2:2.10.1
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gtk+2
Requires(post,postun):	shared-mime-info
Requires:	python-gnome-extras-gda >= 2.14.2-4
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glom is an easy-to-use database designer and user interface.

%description -l pl
Glom jest łatwym w użyciu programem do projektowania baz danych oraz
interfejsem użytkownika.

%prep
%setup -q
%patch0 -p1

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
	--disable-update-mime-database
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

%postun
/sbin/ldconfig
%update_mime_database
%update_icon_cache hicolor

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
