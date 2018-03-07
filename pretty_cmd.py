#!/usr/bin/env python
"""
Formats a long command on stdin sensibly, and prints it to output.
"""

def print_cmd(command, line_length=80, indent="    "):
    import sys, textwrap
    lines = textwrap.wrap(
        command,
        width=line_length,
        subsequent_indent=" \\\\\n" + indent,
        break_long_words=False,
        break_on_hyphens=False)

    for line in lines:
        sys.stdout.write(line)
    sys.stdout.write("\n")

if __name__ == "__main__":
    import sys
    stripped_lines = []
    for line in sys.stdin.readlines():
        l = line.strip()
        l = l.rstrip('\\')
        stripped_lines.append(l)
    print_cmd(" ".join(stripped_lines))
