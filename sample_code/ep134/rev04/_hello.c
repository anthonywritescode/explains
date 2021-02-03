#include <Python.h>

static PyObject* _hello_world(PyObject* self) {
    return PyUnicode_FromString("hello world");  // python c api
}

static PyObject* _hello(PyObject* self, PyObject* args) {
    PyObject* name;
    if (!PyArg_ParseTuple(args, "U", &name)) {
        return NULL;
    }

    PyObject* upper = PyObject_CallMethod(name, "upper", NULL);
    if (!upper) {
        return NULL;
    }

    PyObject* ret = PyUnicode_FromFormat("hello %U", upper);
    return ret;
}

static struct PyMethodDef methods[] = {
    {"hello_world", (PyCFunction)_hello_world, METH_NOARGS},
    {"hello", (PyCFunction)_hello, METH_VARARGS},
    {NULL, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "_hello",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit__hello(void) {
    return PyModule_Create(&module);
}
