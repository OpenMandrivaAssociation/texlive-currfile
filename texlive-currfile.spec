# revision 26259
# category Package
# catalog-ctan /macros/latex/contrib/currfile
# catalog-date 2012-05-07 19:24:22 +0200
# catalog-license lppl1.3
# catalog-version 0.6
Name:		texlive-currfile
Version:	0.6
Release:	2
Summary:	Macros for file name and path of input files
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
of such a file. The package supersedes FiNK.

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


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.6-1
+ Revision: 804565
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.5-2
+ Revision: 750748
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.5-1
+ Revision: 718185
- texlive-currfile
- texlive-currfile
- texlive-currfile
- texlive-currfile

