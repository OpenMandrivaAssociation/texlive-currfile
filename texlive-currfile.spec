Name:		texlive-currfile
Version:	64673
Release:	1
Summary:	Provide file name and path of input files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/currfile
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/currfile.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/currfile.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/currfile.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
