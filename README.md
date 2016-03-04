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
| AHIT_INVENTORY_FILE | What inventory file should be used |
| AHIT_HOST_GROUP | What Ansible host group should be used |
| AHIT_FACT_DIR | Where to put the gathered host facts |

## Usage

To perform fact gathering first, run:

```
./ahit.sh
```

To only view the results from previous runs, just run:

```
./ahit.py
```
