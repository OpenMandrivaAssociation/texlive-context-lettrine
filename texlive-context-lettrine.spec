# revision 23167
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-lettrine
# catalog-date 2009-01-30 23:54:25 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-context-lettrine
Version:	20090130
Release:	1
Summary:	A ConTeXt implementation of lettrines
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-lettrine
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-lettrine.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-lettrine.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
This is a re-implementation of the LaTeX package lettrine.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/interface/third/lettrine.xml
%{_texmfdistdir}/tex/context/third/lettrine/t-lettrine.tex
%doc %{_texmfdistdir}/doc/context/third/lettrine/W.pdf
%doc %{_texmfdistdir}/doc/context/third/lettrine/lettrine-doc.pdf
%doc %{_texmfdistdir}/doc/context/third/lettrine/lettrine-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
