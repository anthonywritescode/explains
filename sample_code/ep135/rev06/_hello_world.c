#include <Python.h>

static PyObject* _hello_world(PyObject* self) {
    PyObject* ret = PyUnicode_FromString("hello world");
    printf("%d\n", PyUnicode_GetLength(ret));
    return ret;
}

static struct PyMethodDef methods[] = {
    {"hello_world", (PyCFunction)_hello_world, METH_NOARGS},
    {NULL, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "_hello_world",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit__hello_world(void) {
    return PyModule_Create(&module);
}
