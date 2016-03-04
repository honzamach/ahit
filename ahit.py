#!/usr/bin/python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
#
# aHIT (Ansible Host Inspection Tool)
#
# Copyright (C) 2015 Jan Mach <honza.mach.ml@gmail.com>
# Use of this source is governed by the MIT license, see LICENSE file.
#-------------------------------------------------------------------------------

import os
import json
import pprint

FACTDIR = './host_facts'

def load_host_facts(fact_dir):
    """
    Load host facts from files within given directory.
    """
    facts = {}
    factfiles = os.listdir(fact_dir)
    for f in factfiles:
        fn = os.path.join(fact_dir, f)
        if os.path.isfile(fn):
            fh = open(fn, 'r')
            data = json.load(fh)
            fh.close()
            facts[f] = data
    return facts

def fact_replace(fact):
    """
    Replace some particular fact values with different ones.
    """
    fact = fact.replace('VMware Virtual Platform', 'VMware Virtual')
    return fact

def extract_facts(facts, config):
    """
    Extract specific facts.
    """
    result = {}
    for host in facts:
        result[host] = {}
        for cfg in config:
            fact_value = facts[host]
            for key in cfg['keys']:
                if key in fact_value:
                    fact_value = fact_value[key]
                else:
                    fact_value = '???'
                    break
            if 'shorten' in cfg and cfg['shorten']:
                fact_value = fact_shorten(fact_value)
            if 'trim' in cfg:
                fact_value = fact_value[:cfg['trim']]
            result[host][cfg['name']] = fact_value
    return result

def result_table_build(facts, config):
    """
    Build result table from given facts and according to given configuration.
    """
    table = []
    for host in sorted(facts):
        row = []
        for cfg in config:
            row.append("{}".format(facts[host][cfg['name']]))
        table.append(row)
    return table

def result_table_measure(table, config):
    """
    Measure the dimension of each table column.
    """
    dimensions = {}
    for row in table:
        i = 0
        for cell in row:
            dimensions[i] = max(len(cell), dimensions.get(i, 0), len(config[i]['name']))
            i += 1
    return dimensions

def table_format_sep(dimensions):
    """
    Format table row separator line.
    """
    cells = []
    for column in dimensions:
        cells.append('-' + ('-' * dimensions[column]) + '-')
    return '+' + '+'.join(cells) + '+'
    
def table_format_cell(value, width, config):
    """
    Format sigle table cell.
    """
    strptrn = " {:" + '{:d}'.format(width) + "s} "
    return strptrn.format(value)
    
def table_format_row(config, dimensions, row = None):
    """
    Format single table row
    """
    cells = []
    i = 0
    for column in config:
        if row:
            cells.append(table_format_cell(row[i], dimensions[i], column))
        else:
            cells.append(table_format_cell(column['name'], dimensions[i], column))
        i += 1
    return '|' + '|'.join(cells) + '|'
    
def result_table_display(table, config):
    """
    Display result in tabular format.
    """
    dimensions = result_table_measure(table, config)
    size = len(table)
    i = 0

    sstr = table_format_sep(dimensions)
    hstr = table_format_row(config, dimensions)
    print(sstr)
    print(hstr)
    print(sstr)
    
    for row in table:
        i += 1
        rstr = table_format_row(config, dimensions, row)
        print(rstr)
    print(sstr)

#-------------------------------------------------------------------------------

# Result format configuration
config = [
        { 'name': 'Host',     'keys': ['ansible_facts', 'ansible_hostname'] },
        { 'name': 'Distro',   'keys': ['ansible_facts', 'ansible_lsb', 'id'] },
        { 'name': 'Release',  'keys': ['ansible_facts', 'ansible_lsb', 'release'] },
        { 'name': 'Codename', 'keys': ['ansible_facts', 'ansible_lsb', 'codename'] },
        { 'name': 'Arch',     'keys': ['ansible_facts', 'ansible_userspace_architecture'] },
        { 'name': 'Kernel',   'keys': ['ansible_facts', 'ansible_kernel'] },
        { 'name': 'Server',   'keys': ['ansible_facts', 'ansible_product_name'], 'shorten': True },
        { 'name': 'Serial',   'keys': ['ansible_facts', 'ansible_product_serial'], 'trim': 9 },
        { 'name': 'Python',   'keys': ['ansible_facts', 'ansible_python_version'] },
        { 'name': 'IPv4',     'keys': ['ansible_facts', 'ansible_default_ipv4', 'address'] },
        { 'name': 'IPv6',     'keys': ['ansible_facts', 'ansible_default_ipv6', 'address'] }
    ]

# Fact preparation
facts_raw = load_fact_files(FACTDIR)
facts = extract_facts(facts_raw, config)

# Result output
result = result_table_build(facts, config)
result_table_display(result, config)
