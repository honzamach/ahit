#!/bin/bash
#-------------------------------------------------------------------------------
#
# aHIT (Ansible Host Inspection Tool)
#
# Copyright (C) 2015 Jan Mach <honza.mach.ml@gmail.com>
# Use of this source is governed by the MIT license, see LICENSE file.
#-------------------------------------------------------------------------------

echo "Reading config...." >&2
. ./ahit.conf

echo "Fetching host facts...." >&2
/usr/bin/ansible -i "$AHIT_INVENTORY_FILE" "$AHIT_HOST_GROUP" -m setup --tree "$AHIT_FACT_DIR"

echo "Formating results...." >&2
/usr/bin/python3 ./ahit.py
