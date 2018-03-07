#!/usr/bin/env python
"""
Formats long command lines on stdin by breaking the lines and adding a
backslash. Indents subsequent lines. Then prints the output followed by a
newline.

Author: Stian Lode stian.lode@gmail.com

"""
import sys, textwrap

def print_cmd(command, line_length=80, indent=r" "*4):
    lines = textwrap.wrap(
        command,
        width=line_length,
        subsequent_indent=r" \\\n" + indent,
        break_long_words=False,
        break_on_hyphens=False)

    for line in lines:
        sys.stdout.write(line)
    sys.stdout.write("\n")

if __name__ == "__main__":
    stripped = [line.strip(r'\ ') for line in sys.stdin.readlines()]
    print_cmd(" ".join(stripped))
