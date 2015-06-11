#!/usr/bin/python

__author__ = 'agallo'


from jnpr.junos import Device
from argparse import ArgumentParser

parser = ArgumentParser(description="Script to pull prefixes advertised by (or through)"
                                    " a given ASN")

parser.add_argument('ASN', metavar='ASN', type=int)

parser.add_argument('router', metavar='target_router')

parser.add_argument('-u', '--user', dest='user', type=str,
                    help='username for router authentication (specify if different than current shell user)')

parser.add_argument('-k', '--key', dest='key', type=str,
                    help='full path to ssh private key (specify if different than current shell user')


args = parser.parse_args()

ASN = args.ASN
router = args.router
auser = args.user
keyfile = args.key


def getpaths(ASN, router, auser, keyfile):
    dev = Device(router)
    dev.open()
    pprint( dev.facts )
    dev.close()



def main():
    ASpaths = getpaths(ASN, router, auser, keyfile)


main()