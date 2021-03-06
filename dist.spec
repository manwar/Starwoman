Name: <% $zilla->name %>
Version: <% (my $v = $zilla->version) =~ s/^v//; $v %>
Release: 1%{?_dist}

Summary: <% $zilla->abstract %>
License: <% $zilla->license->name %>
Group: System/Cluster
BuildArch: noarch
Vendor: <% $zilla->license->holder %>
Source: <% $archive %>

BuildRoot: %{_tmppath}/%{name}-%{version}-BUILD
BuildRequires: perl >= 0:5.01204

%description
<% $zilla->abstract %>

%prep
%setup -q

%build
PERL_MB_OPT="" PERL_MM_OPT="" CFLAGS="$RPM_OPT_FLAGS" perl Build.PL --installdirs vendor
./Build

%check
./Build test

%install
if [ "%{buildroot}" != "/" ] ; then
    rm -rf %{buildroot}
fi
./Build install --destdir %{buildroot}
#find %{buildroot} | sed -e 's#%{buildroot}##' > %{_tmppath}/filelist

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

find %{buildroot} \( -name perllocal.pod -o -name .packlist \) -exec rm -v {} \;

find %{buildroot}/usr -type f -print | \
        sed "s@^%{buildroot}@@g" | \
        grep -v perllocal.pod | \
        grep -v "\.packlist" > %{name}-%{version}-filelist
if [ "$(cat %{name}-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit -1
fi

%clean
if [ "%{buildroot}" != "/" ] ; then
    rm -rf %{buildroot}
fi

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%changelog
* %(date '+%a %b %d %Y') Ashley Willis <awillis@synacor.com> %{version}-1
- Initial Synacor build.
