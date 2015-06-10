#!/usr/bin/python

__author__ = 'agallo'


from argparse import ArgumentParser
import getpass



parser.add_argument('-u', '--user', dest='user', type=str,
                    help='username for router authentication (specify if different than current shell user)')

parser.add_argument('-k', '--key', dest='key', type=str,
                    help='full path to ssh private key (specify if different than current shell user')

parser.add_argument('-p', '--use-password', dest='p',
                    help="Use password authentication (will ask for password; don't supply on the command line)",
                    action="store_true")

args = parser.parse_args()

username = args.user
keyfile = args.key
usepass = args.p

def authtype():
    if username:
        idtype="userpass"
    if keyfile:
        authtype="key"
    if usepass:
        authype="password"
        password = getpass.getpass(prompt="Enter password: ")
    print "username: " + username
    print "keyfile: " + keyfile
    print "password: " + password
