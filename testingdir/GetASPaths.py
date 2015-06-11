#!/usr/bin/python

__author__ = 'agallo'

try:
    from AuthWrapper import *
except ImportError:
    print "Unable to find AuthWrapper; falling back to shell username and private key"


from jnpr.junos import Device
from argparse import ArgumentParser
from pprint import pprint

# setup some command line arguments

print "I made it mast the try/import/except/print block"

parser2 = ArgumentParser(description="Script to pull prefixes advertised by (or through)"
                                    " a given ASN")

parser2.add_argument('ASN', metavar='ASN', type=int)

parser2.add_argument('router', metavar='target_router')


args = parser2.parse_args()

ASN = args.ASN
router = args.router


dev = Device(router)
dev.open()

pprint( dev.facts )

dev.close()
