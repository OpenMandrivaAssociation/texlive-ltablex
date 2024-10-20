Name:		texlive-ltablex
Version:	34923
Release:	2
Summary:	Table package extensions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ltablex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltablex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltablex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Modifies the tabularx environment to combine the features of
the tabularx package (auto-sized columns in a fixed width
table) with those of the longtable package (multi-page tables).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ltablex
%doc %{_texmfdistdir}/doc/latex/ltablex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
