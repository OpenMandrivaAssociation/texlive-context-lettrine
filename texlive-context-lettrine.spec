Name:		texlive-context-lettrine
Version:	47085
Release:	2
Summary:	A ConTeXt implementation of lettrines
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/context/contrib/context-lettrine
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-lettrine.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-lettrine.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/context/third/lettrine
%doc %{_texmfdistdir}/doc/context/third/lettrine

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
