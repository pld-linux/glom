Summary:	A user-friendly database environment.
Summary(pl):	Przyjazne u¿ytkownikowi ¶rodowisko bazodanowe
Name:		glom
Version:	1.0.4
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/glom/1.0/%{name}-%{version}.tar.bz2
# Source0-md5:	1bb06562bf52a66747b4ac4a2aefa3a7
Patch0:		%{name}-desktop.patch
URL:		http://www.glom.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bakery-devel >= 2.3.18
BuildRequires:	gnome-doc-utils
BuildRequires:	gnome-vfsmm-devel >= 2.11.1
BuildRequires:	gtkmm-devel >= 2.6.1
BuildRequires:	intltool
BuildRequires:	iso-codes
BuildRequires:	libgdamm-devel >= 1.3.7
BuildRequires:	libgnome-devel >= 2.6.0
BuildRequires:	libgnomecanvasmm-devel >= 2.10.0
BuildRequires:	libtool
BuildRequires:	libxslt-devel >= 1.1.10
BuildRequires:	python-gnome-extras-gda-devel
BuildRequires:	python-pygtk-devel >= 2.6.0
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gtk+2
Requires(post,postun):	shared-mime-info
Requires:	python-gnome-extras-gda
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

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__gnome_doc_prepare}
%{__aclocal} -I macros
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
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
