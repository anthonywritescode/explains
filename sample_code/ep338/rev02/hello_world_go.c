#include <Python.h>

PyObject* hello(PyObject*, PyObject*);
PyObject* sum(PyObject*, PyObject*);

int PyArgParseTuple_ll(PyObject* args, long* a, long* b) {
    return PyArg_ParseTuple(args, "ll", a, b);
}

int PyArgParseTuple_s(PyObject* args, const char** ptr, Py_ssize_t* size) {
    return PyArg_ParseTuple(args, "s", ptr, size);
}

static struct PyMethodDef methods[] = {
    {"hello", (PyCFunction)hello, METH_VARARGS},
    {"sum", (PyCFunction)sum, METH_VARARGS},
    {NULL, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "hello_world_go",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit_hello_world_go(void) {
    return PyModule_Create(&module);
};
