#!/usr/bin/python
#Author Sunil Sankar
#Date 15-Oct-2017
#Purpose send the mail using Gmail
#Ref: https://support.google.com/accounts/answer/6010255
from __future__ import print_function
from optparse import OptionParser
import os
import smtplib
GMAILID=''
GMAILPASSWD=''

def main():
    p = OptionParser(usage="usage: %prog [options]",version="%prog 0.1")
    p.add_option('--address', '-a', action='store', type='string')
    p.add_option('--body', '-b', action='store', type='string')
    p.add_option('--subject', '-s', action='store', type='string')
    p.add_option('--verbose', '-v', action='store_true', default=False, dest='flag')
    options, arguments = p.parse_args()
    if options.flag == True:
       test = 1
    else:
       test = 0
    body = options.body
    address = options.address
    Addresses = address.split(',')
    subject = options.subject
    body = '\n'.join(body.split('\\nnn'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.set_debuglevel(test) #0 for quiet or 1 for verbosity
        server.ehlo()
        server.starttls()
        server.ehlo()  # say hello again
        server.login(GMAILID,GMAILPASSWD)
        server.sendmail(GMAILID, Addresses, "Subject: " + subject + '\nTo:' + address + '\n\n' + body)
        print('message sent')
        server.close()
    except smtplib.SMTPAuthenticationError:
	print('unable to send email')


if __name__ == '__main__':
    main()
