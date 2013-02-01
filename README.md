# catarc

A tool to output archives and compressed files to stdout.

## Use cases

* Grep through multiple archives (of different types) without unpacking them.
* Unpack multiple 7z archives to stdout, ignoring errors (7z will choke on corrupted archives).
* Concatenate multiple archived logfiles into one file.
* ...

## Installation

`pip install catarc`

## Dependencies

You'll need the following binaries, depending on what kinds of archives you wish to extract:

* tar (.tar, .tar.gz, .tar.bz2, .tar.xz)
* 7zip (.7z)
* gzip (.gz, .tar.gz)
* bzip2 (.bz2, .tar.bz2)
* xz (.xz, .tar.xz)
* unzip (.zip)
* unrar (.rar)

Note that .tar.* types have two dependencies!

## Usage

	catarc *.7z | grep "something"`

	catarc one.zip two.rar three.tar.gz | grep "something"

	catarc access.*.gz > access.log.total
	
## Arguments

Optionally, you can use the `-s` switch to specify a certain filesize requirement for a file to be processed. This specification is in the following format:

	>1m,<2g,=3t
	
You can use any of these combinations, but obviously only one specification per operator. Valid suffixes are `k`, `m`, `g`, `t`.

## Functionality and behaviour

catarc will attempt to unpack the following types:

* .7z
* .tar
* .tar.gz
* .tar.bz2
* .tar.xz
* .gz
* .bz2
* .xz
* .zip
* .rar

When a file is encountered that is none of the above types, catarc will write a warning to stderr and skip the file. If you are missing a dependency, catarc will tell you so.

## Bugs

No known bugs. If you find any, please do report them.
