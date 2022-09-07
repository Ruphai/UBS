/*  Wrapping DTW similarity function with the Python-C-API. */

#include <Python.h>
#include <numpy/arrayobject.h>
#include <math.h>

/* ==== powered Minkowski Distance   ======================
*/
static double Dlp(const double *a, const double *b, int dim, int degree){
double x, out=0.0;
for (int k=0; k<dim; k++){
  x=fabs(a[k]-b[k]);
  out+=pow(x, degree);
  }
return out;
}

/* ==== Evaluate DTW  ======================
*/
double CDTW(double **A, int lA, double **B, int lB, int dim, int degree) {
	if(lA<0||lB<0){
		fprintf(stderr, "dtw: the lengths of the input timeseries should be greater or equal to 0\n");
		exit(-1);
		}
	int i,j;
	double dist0, dist, dmin;

	// allocations
	double **D = (double **)calloc(lA+1, sizeof(double*));
	for(i=0; i<=lA; i++) {
		D[i]=(double *)calloc(lB+1, sizeof(double));
	}

	// border of the cost matrix initialization

	for(i=1; i<=lA; i++)
  		D[i][0]=INFINITY;
	for(j=1; j<=lB; j++)
  		D[0][j]=INFINITY;
	D[0][0]=0;

	for (i=1; i<=lA; i++){ 
  		for (j=1; j<=lB; j++){
			dist0 = Dlp(A[i-1], B[j-1], dim, degree);
			dmin=D[i-1][j-1]+dist0;
      			dist=dist0+D[i-1][j];
   			if(dmin>dist)
   				dmin=dist;
      			dist=dist0+D[i][j-1]; 
   			if(dmin>dist)
   				dmin=dist;
  			D[i][j] = dmin;
  		}
	}

	dist = D[lA][lB];

	// freeing
	for(i=0; i<=lA; i++) {
		free(D[i]);
   	}

	free(D);
	return dist;
}


/* ==== Allocate a double *vector (vec of pointers) ======================
    Memory is Allocated!  See void free_Carray(double ** )                  */
double **ptrvector(long n)  {
	double **v;
	v=(double **)malloc((size_t) (n*sizeof(double)));
	if (!v)   {
		printf("In **ptrvector. Allocation of memory for double array failed.");
		exit(0);  }
	return v;
}

/* ==== Create 1D Carray from PyArray ======================
    Assumes PyArray is contiguous in memory.             */
double *pyvector_to_Carrayptrs(PyArrayObject *arrayin)  {
	return (double *) arrayin->data;  /* pointer to arrayin data as double */
}

/* ==== Create Carray from PyArray ======================
    Assumes PyArray is contiguous in memory.
    Memory is allocated!                                    */
double **pymatrix_to_Carrayptrs(PyArrayObject *arrayin, int *L, int *D)  {
	double **c, *a;
	int i,n,m;
	
	n=arrayin->dimensions[0];
	m=arrayin->dimensions[1];
	*L=n;
	*D=m;
	c=ptrvector(n);
	a=(double *) arrayin->data;  /* pointer to arrayin data as double */
	for ( i=0; i<n; i++)  {
		c[i]=a+i*m;  }
	/*for ( i=0; i<n; i++)  { 
		for (int j=0; j<m; j++) 
			printf("%f ", c[i][j]);
		printf("\n");
	}*/
	return c;
}

/* ==== Error tracing ======================
*/
PyObject*  failure(int errid, char* mess){
  printf("%s\n",mess);
  return Py_BuildValue("d", -1.0);
}

/* ==== Python/C bydings for TWED distance computation ======================
*/
static PyObject* distance(PyObject* self, PyObject* args)
{
    int degree;
    double answer=0.0;
    double **A;
    double **B;
    PyArrayObject *seq1, *seq2;
    
    if (!PyArg_ParseTuple(args, "OOi",  &seq1,  &seq2, &degree))
        return failure(-1, "TPyArg_ParseTuple error.");

    if (PyArray_DESCR(seq1)->type_num != NPY_DOUBLE)
        return failure(-1, "Type np.float64 expected for p array.");

    if (PyArray_DESCR(seq2)->type_num != NPY_DOUBLE)
        return failure(-1, "Type np.float64 expected for M array.");

    if (PyArray_NDIM(seq1)!=2)
        return failure(-1, "p must be a 2 dimensionnal array.");
    if (PyArray_NDIM(seq2)!=2)
        return failure(-1, "p must be a 2 dimensionnal array.");

    if (degree<0)
	degree = 1;

    int la, lb, dima, dimb;
    A = pymatrix_to_Carrayptrs(seq1, &la, &dima);
    B = pymatrix_to_Carrayptrs(seq2, &lb, &dimb);

    if (dima != dimb){
        printf("dimensions of time series are not equal! \n");
        return Py_BuildValue("f", -1.0);
        }

   answer = CDTW(A, la, B, lb, dima, degree);

   free(A);
   free(B);

   /*  construct the output, from c double to python float */
   return Py_BuildValue("d", answer);
}

/*  define functions in module */
static PyMethodDef distanceMethods[] =
{
     {"distance", distance, METH_VARARGS, "evaluate kdtw with double 2D-arrays args"},
     {NULL, NULL, 0, NULL}
};

#if PY_MAJOR_VERSION >= 3
/* module initialization */
/* Python version 3*/
static struct PyModuleDef cModPyDem =
{
    PyModuleDef_HEAD_INIT,
    "DTW", "Some documentation",
    -1,
    distanceMethods
};

PyMODINIT_FUNC
PyInit_DTW(void)
{
    return PyModule_Create(&cModPyDem);
}

#else

/* module initialization */
/* Python version 2 */
PyMODINIT_FUNC
initDTW(void)
{
    (void) Py_InitModule("DTW", distanceMethods);
}

#endif

