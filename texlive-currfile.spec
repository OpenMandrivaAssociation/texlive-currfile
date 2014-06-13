# revision 29012
# category Package
# catalog-ctan /macros/latex/contrib/currfile
# catalog-date 2013-02-02 11:38:19 +0100
# catalog-license lppl1.3
# catalog-version 0.7b
Name:		texlive-currfile
Version:	0.7b
Release:	6
Summary:	Provide file name and path of input files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/currfile
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/currfile.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/currfile.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/currfile.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides macros holding file name information
(directory, base name, extension, full name and full path) for
files read by LaTeX \input and \include macros; it uses the
file hooks provided by the author's filehook. In particular, it
restores the parent file name after the trailing \clearpage of
an \included file; as a result, the macros may be usefully
employed in the page header and footer of the last printed page
of such a file. The depth of inclusion is made available,
together with the "parent" (including file) and "parents" (all
including files to the root of the tree). The package
supersedes FiNK.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/currfile/currfile-abspath.sty
%{_texmfdistdir}/tex/latex/currfile/currfile.sty
%doc %{_texmfdistdir}/doc/latex/currfile/README
%doc %{_texmfdistdir}/doc/latex/currfile/currfile.pdf
#- source
%doc %{_texmfdistdir}/source/latex/currfile/currfile.dtx
%doc %{_texmfdistdir}/source/latex/currfile/currfile.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
