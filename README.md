# Clang-Tidy Exclude-Header-Filter Patch

A patch adding `-exclude-header-filter` option to clang-tidy: [Allow passing a regex for headers to exclude from clang-tidy](https://reviews.llvm.org/D34654).

The author is [Todd Lipcon](https://reviews.llvm.org/p/toddlipcon/).

This patch is quite useful to me, but not accepted by the clang-tidy dev team, and is a bit out-of-date, so I created this repo to maintain it.

## Usage

### Apply the patch

```bash
# cd into the directory which contains clang-tidy
cd llvm-8.0.0.src/tools/clang/tools/extra
# apply the patch
patch -p0 < /path/to/patch.diff
# then build llvm
```

### Specify the filter

- Command line option: `-exclude-header-filter`
- `.clang-tidy` option: `ExcludeHeaderRegex`

## Note

There are some other ideas and patches for suppressing clang-tidy warnings by header file name, e.g.

[clang-tidy Negative Lookahead Support](http://lists.llvm.org/pipermail/cfe-dev/2015-November/046202.html)

[Add '-suppress-checks-filter' option to suppress diagnostics from certain files](https://reviews.llvm.org/D26418)

But none is accepted.
