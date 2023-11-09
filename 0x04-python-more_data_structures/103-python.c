#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <string.h>

void print_python_bytes(PyObject *p)
{
    int i, n_bytes;
    char s[1024], *bytes;

    printf("[.] bytes object info\n");
    if (strcmp(p->ob_type->tp_name, "bytes") != 0)
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    n_bytes = strlen(((PyBytesObject *)(p))->ob_sval);
    n_bytes = n_bytes > 8 ? 10 : n_bytes + 1;
    bytes = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
    strcpy(s, bytes);
    printf("  size: %lu\n", (assert(PyBytes_Check(p)), ((PyVarObject *)(p))->ob_size));
    printf("  trying string: %s\n", s);
    printf("  first %i bytes:", n_bytes);
    for (i = 0; i < n_bytes; i++)
        printf(" %02x", bytes + i ? *(bytes + i) & 0xFF : 0x00);
    printf("\n");
}

void print_python_list(PyObject *p)
{
    int n;
    PyObject *itm;

    printf("[*] Python list info\n");
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