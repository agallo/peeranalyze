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

parser = ArgumentParser(description="Script to pull prefixes advertised by (or through)"
                                    " a given ASN")

parser.add_argument('ASN', metavar='ASN', type=int)

parser.add_argument('router', metavar='target_router')


args = parser.parse_args()

ASN = args.ASN
router = args.router


dev = Device(router)
dev.open()

pprint( dev.facts )

dev.close()
