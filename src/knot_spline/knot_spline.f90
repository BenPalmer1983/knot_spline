!#############################################################
!#  HOW TO USE:
!#
!#
!#                                                        
!#
!#############################################################

MODULE knot_spline

USE kinds
USE sls, ONLY: sls_solve

IMPLICIT NONE

CONTAINS

! knot_spline
INCLUDE "knot_spline.cubic.f90"
INCLUDE "knot_spline.cubic_fixed_end.f90"


END MODULE knot_spline
