"""Compile each standalone C++ solution and run representative examples."""
from pathlib import Path
import subprocess
import tempfile

examples = {
    "single_number": ("singleNumber", [
        ([2, 2, 1], 1), ([4, 1, 2, 1, 2], 4), ([-3], -3)
    ]),
    "contains_duplicate": ("containsDuplicate", [
        ([1, 2, 3, 1], True), ([1, 2, 3], False), ([], False), ([-2, -2], True)
    ]),
}

with tempfile.TemporaryDirectory() as folder:
    for name, (method, cases) in examples.items():
        solution = Path(__file__).with_name(name + ".cpp").resolve()
        lines = [f'#include "{solution}"', 'int main() {', 'Solution solver;']
        for i, (values, expected) in enumerate(cases):
            initializer = ", ".join(map(str, values))
            lines.append(f"std::vector<int> v{i} = {{{initializer}}};")
            lines.append(f"if (solver.{method}(v{i}) != {int(expected)}) return 1;")
        lines.append("}")
        driver = Path(folder, "driver.cpp")
        exe = Path(folder, "check")
        driver.write_text("\n".join(lines))
        subprocess.run(["g++", "-std=c++17", "-Wall", "-Wextra", "-Werror",
                        str(driver), "-o", str(exe)], check=True)
        subprocess.run([str(exe)], check=True)
        for values, expected in cases:
            print(f"PASS  {method}({values}) -> {expected}")
