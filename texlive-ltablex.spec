# revision 29903
# category Package
# catalog-ctan /macros/latex/contrib/ltablex
# catalog-date 2013-04-12 10:31:24 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-ltablex
Version:	1.0
Release:	6
Summary:	Table package extensions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ltablex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltablex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltablex.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/ltablex/ltablex.sty
%doc %{_texmfdistdir}/doc/latex/ltablex/README
%doc %{_texmfdistdir}/doc/latex/ltablex/ltablex.pdf
%doc %{_texmfdistdir}/doc/latex/ltablex/ltablex.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
