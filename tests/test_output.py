import io
import runpy
import sys


def run_student_code():
    buf = io.StringIO()
    old_stdout = sys.stdout
    try:
        sys.stdout = buf
        runpy.run_path("main.py", run_name="__main__")
    finally:
        sys.stdout = old_stdout
    return buf.getvalue().strip().splitlines()


def test_output_lines():
    output = run_student_code()
    assert len(output) >= 2, "Должно быть минимум 2 строки вывода (два print)."
    assert output[0] == "Hello, world!"
    assert output[1] == "42"
