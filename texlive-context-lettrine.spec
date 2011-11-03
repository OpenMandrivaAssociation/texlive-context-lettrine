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
Requires(post):	texlive-tlpkg
Requires:	texlive-context
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Requires(post):	texlive-context.bin

%description
This is a re-implementation of the LaTeX package lettrine.

%pre
    %_texmf_mtxrun_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mtxrun_post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_post
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/interface/third/lettrine.xml
%{_texmfdistdir}/tex/context/third/lettrine/t-lettrine.tex
%doc %{_texmfdistdir}/doc/context/third/lettrine/W.pdf
%doc %{_texmfdistdir}/doc/context/third/lettrine/lettrine-doc.pdf
%doc %{_texmfdistdir}/doc/context/third/lettrine/lettrine-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
