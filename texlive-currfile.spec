Name:		texlive-currfile
Version:	0.5
Release:	1
Summary:	Macros for file name and path of input files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/currfile
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/currfile.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/currfile.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/currfile.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides macros holding file name information
(directory, base name, extension, full name and full path) for
files read by LaTeX \input and \include macros; it uses the
file hooks provided by the author's filehook. In particular, it
restores the parent file name after the trailing \clearpage of
an \included file; as a result, the macros may be usefully
employed in the page header and footer of the last printed page
of such a file. The package supersedes FiNK.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
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
