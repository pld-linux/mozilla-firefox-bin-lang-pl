Summary:	Polish resources for Mozilla-firefox
Summary(pl.UTF-8):	Polskie pliki językowe dla Mozilli-firefox
Name:		mozilla-firefox-bin-lang-pl
Version:	3.5.2
Release:	1
License:	GPL
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pl.xpi
# Source0-md5:	30bae06c139893ced8103370db78e472
URL:		http://www.firefox.pl/
BuildRequires:	unzip
Requires(post,postun):	mozilla-firefox-bin >= %{version}
Requires(post,postun):	textutils
Requires:	mozilla-firefox-bin >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_firefoxdir	%{_libdir}/mozilla-firefox-bin
%define		_chromedir	%{_firefoxdir}/chrome

%description
Polish resources for Mozilla-firefox.

%description -l pl.UTF-8
Polskie pliki językowe dla Mozilli-firefox.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_chromedir},%{_firefoxdir}/defaults/profile}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_libdir}
sed -i -e 's,jar:chrome/,jar:,' $RPM_BUILD_ROOT%{_libdir}/chrome.manifest
mv $RPM_BUILD_ROOT%{_libdir}/chrome.manifest $RPM_BUILD_ROOT%{_chromedir}/pl.manifest
mv $RPM_BUILD_ROOT%{_libdir}/chrome/pl.jar $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_chromedir}/pl.jar
%{_chromedir}/pl.manifest
