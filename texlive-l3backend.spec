Name:		texlive-l3backend
Version:	71991
Release:	1
Summary:	LaTeX3 backend drivers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/l3backend
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3backend.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3backend.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l3backend.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package forms parts of expl3, and contains the code used
to interface with backends (drivers) across the expl3 codebase.
The functions here are defined differently depending on the
engine in use. As such, these are distributed separately from
l3kernel to allow this code to be updated on an independent
schedule.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/l3backend
%{_texmfdistdir}/tex/latex/l3backend
%{_texmfdistdir}/dvips/l3backend
%doc %{_texmfdistdir}/doc/latex/l3backend

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
