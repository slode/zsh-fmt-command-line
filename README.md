# zsh-fmt-command-line

## Installation

Source `fmt-command-line.zsh` from `.zshrc`. Enabled in vi-mode (as that's what I'm using). By default, it's bound to `<leader>f`.


## Usage

Should not have any effect on the semantics of the command. Will typically transform a line such as 
  
```
./configure --disable-dns --disable-http --disable-rpc --disable-openssl --enable-thread-support --disable-evport --prefix=/sw --datadir=/sw/share/doc --sysconfdir=/sw/etc/openmpi --sharedstatedir=/sw/var/openmpi/shared --localstatedir=/sw/var/openmpi/local --libdir=/sw/lib/openmpi --includedir=/sw/include --infodir=/sw/share/info --mandir=/sw/share/man --enable-shared --enable-static FCFLAGS=-O3 --with-devel-headers FC=gfortran-fsf-5 --with-hwloc=/sw CC=/usr/bin/clang CXX=/usr/bin/clang++ --cache-file=/dev/null --srcdir=. --disable-option-checking

```

into

```
./configure --disable-dns --disable-http --disable-rpc --disable-openssl \
    --enable-thread-support --disable-evport --prefix=/sw \
    --datadir=/sw/share/doc --sysconfdir=/sw/etc/openmpi \
    --sharedstatedir=/sw/var/openmpi/shared \
    --localstatedir=/sw/var/openmpi/local --libdir=/sw/lib/openmpi \
    --includedir=/sw/include --infodir=/sw/share/info --mandir=/sw/share/man \
    --enable-shared --enable-static FCFLAGS=-O3 --with-devel-headers \
    FC=gfortran-fsf-5 --with-hwloc=/sw CC=/usr/bin/clang CXX=/usr/bin/clang++ \
    --cache-file=/dev/null --srcdir=. --disable-option-checking
```
