package main

// #include <Python.h>
// int PyArgParseTuple_ll(PyObject* args, long* a, long* b);
// int PyArgParseTuple_s(PyObject* args, const char** ptr, Py_ssize_t* size);
import "C"
import "unsafe"

//export hello
func hello(self *C.PyObject, args *C.PyObject) *C.PyObject {
    var s *C.char
    var size C.Py_ssize_t
    if C.PyArgParseTuple_s(args, &s, &size) == 0 {
        return nil
    }

    ret := "hello hello " + C.GoString(s)
    cstr := C.CString(ret)
    ret_u := C.PyUnicode_FromString(cstr)
    C.free(unsafe.Pointer(cstr))
    return ret_u
}

//export sum
func sum(self *C.PyObject, args *C.PyObject) *C.PyObject {
    var a C.long
    var b C.long
    if C.PyArgParseTuple_ll(args, &a, &b) == 0 {
        return nil
    }

    ret := a + b
    return C.PyLong_FromLong(ret)
}

func main() {}
