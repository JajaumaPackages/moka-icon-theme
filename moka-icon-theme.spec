Name:           moka-icon-theme
Version:        5.3.2
Release:        1%{?dist}
Summary:        Moka Icon theme

License:        CC-BY-SA-4.0
URL:            https://snwh.org/moka
Source0:        https://github.com/snwh/moka-icon-theme/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  automake
BuildRequires:  icon-naming-utils
BuildRequires:  gtk2
Requires:       hicolor-icon-theme
Requires:       faba-icon-theme

%description


%prep
%setup -q
find -L . -type l -print -delete
chmod +x autogen.sh
./autogen.sh


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install


%files
%doc AUTHORS README.md
%license COPYING LICENSE_*
%{_datadir}/icons/Moka
%ghost %{_datadir}/icons/Moka/icon-theme.cache



%post
touch --no-create %{_datadir}/icons/Moka &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/Moka &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/Moka &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/Moka &>/dev/null || :


%changelog
* Tue Sep 27 2016 Jajauma's Packages <jajauma@yandex.ru> - 5.3.2-1
- Public release
