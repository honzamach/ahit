# ahit (Ansible Host Inspection Tool)

This is a simple utility for viewing Ansible host fact files.

## Installation

Installation is currently very easy, just clone this repository:

```
git clone https://github.com/honzamach/ahit.git
```

## Configuration

First copy the example configuration file:

```
cp ahit.conf.dist ahit.conf
```

Next modify the configuration file to suit your needs:

| Configuration | Meaning |
| --- | --- |
| inventory | What inventory file should be used |
| group | What Ansible host group should be used |
| fact_dir | Where to put the gathered host facts |

Make sure, that the *fact_dir* directory exists, this program will intentionally
not create any non existing directories.

## Usage

There is a integrated help, to view it just run:

```
./ahit.py -h
./ahit.py --help
```

When running without any arguments, program automatically performs the fact
gathering, when necessary and then displays the result:

```
./ahit.py
```

You can force the fact gathering with:

```
./ahit.py --refresh
```

By default, program tries to present the best output possible and uses special
utf8 characters for widget borders and ANSI escape sequences for coloring and
additional formating. If this is not desired, you may turn this formating off
with following command line option:

```
./ahit.py --ascii
```

## Copyright

Copyright (C) 2015 Jan Mach <honza.mach.ml@gmail.com>
Use of this package is governed by the MIT license, see LICENSE file.
