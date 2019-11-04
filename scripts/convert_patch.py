#!/usr/bin/env python

"""convert_patch.py: Convert a patch from git-style to svn-style."""

import re
import sys

# git:
#   diff --git a/clang-tidy/tool/ClangTidyMain.cpp b/clang-tidy/tool/ClangTidyMain.cpp
# svn:
#   Index: clang-tidy/tool/ClangTidyMain.cpp
FILE_PATH_PATTERN = re.compile(r'diff --git a/(.*) b/(.*)')

# git:
#   index 12a6024..45ac37c 100644
# svn:
#   ===================================================================
SEPARATOR_PATTERN = re.compile(r'index [a-f0-9]+\.\.[a-f0-9]+ [0-9]+')


def main():
    if len(sys.argv) != 2:
        print('usage: %s patch-file' % sys.argv[0])
        sys.exit(-1)
    patch_file = sys.argv[1]
    with open(patch_file, 'r') as f:
        for line in f:
            line = line.rstrip('\r\n')  # remove trailing '\r' or '\n'
            if line.startswith('--- a/'):
                print('--- ' + line.strip()[6:])
            elif line.startswith('+++ b/'):
                print('+++ ' + line.strip()[6:])
            else:
                m = re.match(FILE_PATH_PATTERN, line)
                if m:
                    assert m.group(1) == m.group(2)
                    print("Index: " + m.group(1))
                    continue
                m = re.match(SEPARATOR_PATTERN, line)
                if m:
                    print("===================================================================")
                    continue
                print(line)


if __name__ == "__main__":
    main()
