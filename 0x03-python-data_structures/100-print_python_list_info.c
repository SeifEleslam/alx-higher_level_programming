#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <string.h>

void print_python_list(PyObject *p)
{
    int n;
    PyObject *itm;

    printf("[*] Size of the Python List = %lu\n", ((PyVarObject *)(p))->ob_size);
    printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
    for (n = 0; n < ((PyVarObject *)(p))->ob_size; n++)
    {
        itm = PyList_GET_ITEM(p, n);
        printf("Element %d: %s\n", n, itm->ob_type->tp_name);
        if (strcmp(PyList_GET_ITEM(p, n)->ob_type->tp_name, "bytes") == 0)
            print_python_bytes(itm);
    }
}