//==================================================================================================
//
// basic python wrapper for some of SZpack functions
// 
//==================================================================================================
//
// Author: Jens Chluba & Eric Switzer (CITA, University of Toronto)
//
// first implementation:  Aug 2012
// last modification   :  Aug 2012
//
//==================================================================================================


%module SZpack %{

#define SWIG_FILE_WITH_INIT
#include "SZpack.python.h"

%}


//==================================================================================================
// numpy stuff
//==================================================================================================
%include "numpy.i"

%init %{
    import_array();
%}


//==================================================================================================
%apply (double* INPLACE_ARRAY1, int DIM1) {(double *xo, int np)}
%apply (double* INPLACE_ARRAY1, int DIM1) {(double *omega, int nomega)}
%apply (double* INPLACE_ARRAY1, int DIM1) {(double *sigma, int nsigma)}


// This is to allow batch evaluatation for a set of parameters
%apply (double* IN_ARRAY1, int DIM1) {(double *tau, int ntau)}
%apply (double* IN_ARRAY1, int DIM1) {(double *TeSZ, int nTeSZ)}
%apply (double* IN_ARRAY1, int DIM1) {(double *betac_para, int nbetac_para)}
%apply (double* IN_ARRAY1, int DIM1) {(double *omega1, int nomega1)}
%apply (double* IN_ARRAY1, int DIM1) {(double *kappa, int nkappa)}
%apply (double* IN_ARRAY1, int DIM1) {(double *betac2_perp, int nbetac2_perp)}

%apply (double* IN_ARRAY1, int DIM1) {(double *Dtau, int nDtau)}
%apply (double* IN_ARRAY1, int DIM1) {(double *Te, int nTe)}
%apply (double* IN_ARRAY1, int DIM1) {(double *betac, int nbetac)}
%apply (double* IN_ARRAY1, int DIM1) {(double *muc, int nmuc)}
%apply (double* IN_ARRAY1, int DIM1) {(double *betao, int nbetao)}
%apply (double* IN_ARRAY1, int DIM1) {(double *muo, int nmuo)}

%include "SZpack.python.h"

//==================================================================================================
//==================================================================================================
