#!/usr/bin/env python
filepath = 'test.txt'
with open(filepath, 'r') as f:
    original_lines = f.readlines()

new_lines = ('\n' + 'b"' + line.strip() + ' \\n"' for line in original_lines)

with open(filepath, 'w') as f:
    f.writelines(new_lines)
