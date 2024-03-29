#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-spc
Version  : 0.6.7
Release  : 46
URL      : https://cran.r-project.org/src/contrib/spc_0.6.7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/spc_0.6.7.tar.gz
Summary  : Statistical Process Control -- Calculation of ARL and Other
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-spc-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
the zero-state, steady-state ARL (Average Run Length) and RL quantiles.
        Setting up control charts for given in-control ARL. The control charts
        under consideration are one- and two-sided EWMA, CUSUM, and
        Shiryaev-Roberts schemes for monitoring the mean or variance of normally
        distributed independent data. ARL calculation of the same set of schemes under drift (in the mean) are added.
        Eventually, all ARL measures for the multivariate EWMA (MEWMA) are provided.

%package lib
Summary: lib components for the R-spc package.
Group: Libraries

%description lib
lib components for the R-spc package.


%prep
%setup -q -n spc
cd %{_builddir}/spc

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666638220

%install
export SOURCE_DATE_EPOCH=1666638220
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/spc/DESCRIPTION
/usr/lib64/R/library/spc/INDEX
/usr/lib64/R/library/spc/Meta/Rd.rds
/usr/lib64/R/library/spc/Meta/features.rds
/usr/lib64/R/library/spc/Meta/hsearch.rds
/usr/lib64/R/library/spc/Meta/links.rds
/usr/lib64/R/library/spc/Meta/nsInfo.rds
/usr/lib64/R/library/spc/Meta/package.rds
/usr/lib64/R/library/spc/NAMESPACE
/usr/lib64/R/library/spc/R/spc
/usr/lib64/R/library/spc/R/spc.rdb
/usr/lib64/R/library/spc/R/spc.rdx
/usr/lib64/R/library/spc/help/AnIndex
/usr/lib64/R/library/spc/help/aliases.rds
/usr/lib64/R/library/spc/help/paths.rds
/usr/lib64/R/library/spc/help/spc.rdb
/usr/lib64/R/library/spc/help/spc.rdx
/usr/lib64/R/library/spc/html/00Index.html
/usr/lib64/R/library/spc/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/spc/libs/spc.so
/usr/lib64/R/library/spc/libs/spc.so.avx2
/usr/lib64/R/library/spc/libs/spc.so.avx512
