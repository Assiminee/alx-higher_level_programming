#!/usr/bin/python3
import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
s = b"Hello"

print("lib.print_python_bytes(s);");
lib.print_python_bytes(s);
b = b'\xff\xf8\x00\x00\x00\x00\x00\x00';
print("\n\nlib.print_python_bytes(b);");
lib.print_python_bytes(b);
b = b'What does the \'b\' character do in front of a string literal?';
print("\n\nlib.print_python_bytes(b);");
lib.print_python_bytes(b);
l = [b'Hello', b'World']
print("\n\nlib.print_python_list(l)");
lib.print_python_list(l)
del l[1]
print("\n\nlib.print_python_list(l)");
lib.print_python_list(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], b"Holberton", "Betty"]
print("\n\nlib.print_python_list(l)");
lib.print_python_list(l)
l = []
print("\n\nlib.print_python_list([])");
lib.print_python_list(l)
l.append(0)
print("\n\nlib.print_python_list([0])");
lib.print_python_list(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
print("\n\nlib.print_python_list([0 1 2 3 4])");
lib.print_python_list(l)
l.pop()
print("\n\nlib.print_python_list([0 1 2 3])");
lib.print_python_list(l)
l = ["Holberton"]
print("\n\nlib.print_python_list([\"Holberton\"])");
lib.print_python_list(l)
print("\n\nlib.print_python_bytes(l);");
lib.print_python_bytes(l);
