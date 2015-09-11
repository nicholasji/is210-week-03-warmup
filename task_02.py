#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Equation to find out the weeks in a year."""

WEEKS = ((19 % 10 + 100) + 2**8) / 7

print WEEKS
