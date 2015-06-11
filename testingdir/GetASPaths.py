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
    devcommand = 0

    if auser is not None:
        username = auser
        devcommand += 1

    if keyfile is not None:
        path2keyfile = keyfile
        devcommand += 2

    if devcommand == 0:
        dev = Device(router)
    elif devcommand == 1:
        dev = Device(router, user=username)
    elif devcommand == 2:
        dev = Device(router, ssh_private_key_file=path2keyfile)
    else:
        dev = Device(router, user=username, ssh_private_key_file=path2keyfile)

    dev.open()
    pprint( dev.facts )
    dev.close()



def main():
    ASpaths = getpaths(ASN, router, auser, keyfile)


main()