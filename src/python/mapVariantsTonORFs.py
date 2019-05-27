#!/usr/bin/env python
"""
mapVariantsTonORFs.py
Narendra Meena
May 23, 2019



LICENSE

This is free and unencumbered software released into the public domain.
Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
"""

import sys
import argparse


from bed import dataframe 



def map():
    parser = argparse.ArgumentParser(description='Map Variants to AA Seq:', epilog="Mapping is Complete!")
    group.add_argument('-f', '--fasta', required=True)
    group.add_argument('-b', '--bed', required=True)
    parser.add_argument('-v', '--vcf', required=True)
    parser.add_argument('-m', '--mode', default='single', choices=['single', 'multi'], required=True, help='single: to map single variant to AA Seq, multi to map multiple variants to AA seq (default: %(default)s)')
    args = parser.parse_args()


if __name__ == '__main__':
    map()

