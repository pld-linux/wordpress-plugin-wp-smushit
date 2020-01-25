%define		plugin	wp-smushit
%define		php_min_version 5.2.0
Summary:	WP Smush.it
Name:		wordpress-plugin-%{plugin}
Version:	1.3.4
Release:	1
License:	GPL v3
Group:		Applications/WWW
Source0:	http://downloads.wordpress.org/plugin/wp-smushit.%{version}.zip
# Source0-md5:	49698b06c26cf5288370a80cd2e4b8cf
URL:		http://wordpress.org/extend/plugins/wp-smushit/
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-json
Requires:	php-pcre
Requires:	webapps
Requires:	webserver(php)
Requires:	wordpress >= 2.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		wp_root		%{_datadir}/wordpress
%define		wp_content	%{wp_root}/wp-content
%define		pluginsdir	%{wp_content}/plugins
%define		plugindir	%{pluginsdir}/%{plugin}

%define		_noautoreq	pear

%description
Reduce image file sizes and improve performance using the Smush.it API
within WordPress.

%prep
%setup -qn %{plugin}
%undos -f txt,php

# PEAR JSON copy, we depend on native ext
%{__rm} -r JSON

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm $RPM_BUILD_ROOT%{plugindir}/{readme,license}.txt
rm -f $RPM_BUILD_ROOT%{plugindir}/debug*.list

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.jpg
