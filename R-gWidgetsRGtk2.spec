%global packname  gWidgetsRGtk2
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.0_78
Release:          1
Summary:          Toolkit implementation of gWidgets for RGtk2
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-78.tar.gz
Requires:         R-methods R-gWidgets 
Requires:         R-RGtk2 
Requires:         R-cairoDevice 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods R-gWidgets
BuildRequires:    R-RGtk2 
BuildRequires:    R-cairoDevice 
BuildRequires:    gtk2-devel

%description
Port of gWidgets API to RGtk2

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
if [ x$DISPLAY != x ];	then %{_bindir}/R CMD check %{packname}
else			true
fi

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/images
