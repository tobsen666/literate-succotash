import importlib
import cffi
import pytest


def load_and_compile(filename, includes=None):
    try:
        # Read C code from the external file
        with open(filename + '.c') as c_file:
            c_code = c_file.read()

        # Read includes from the external header file
        if includes is not None:
            with open(includes) as includes_file:
                includes_content = includes_file.read()
        else:
            includes_content = None

        # Pass source code to CFFI
        ffibuilder = cffi.FFI()

        if includes_content:
            ffibuilder.cdef(includes_content)

        ffibuilder.set_source(filename + '_', c_code)
        ffibuilder.compile()

        # Import and return resulting module
        module = importlib.import_module(filename + '_')
        return module.lib

    except Exception as e:
        raise RuntimeError(f"Error loading and compiling {filename}: {str(e)}")


def test_addition():
    module = load_and_compile('add', includes='add.h')
    result = module.add(1, 2)

    # Custom logging
    print(f"Test Result: {result}")

    assert result == 1 + 2


if __name__ == '__main__':
    pytest.main(['-v', '--html=report.html'])

