#!/bin/bash
python3 -m numpy.f2py --quiet --f90flags="-fopenmp -O3 -ffast-math" \
-lgomp \
-c \
src/kinds/kinds.f90 \
src/sls/sls.f90 \
src/knot_spline/knot_spline.f90 \
-m knot_spline


