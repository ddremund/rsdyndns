#!/usr/bin/python -tt

# Copyright 2013 Derek Remund (derek.remund@rackspace.com)

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pyrax
import stun
#import socket
#import pprint
import argparse
import sys
import os


def main():

	parser = argparse.ArgumentParser(description = "Updates a Rackspace Cloud "
		"DNS A record with your system's current IP address.")

	parser.add_argument('-z', '--zone', required = True, 
		help = "The zone containing the DNS record.")
	parser.add_argument('-n', '--name', required = True, 
		help = "The name of the A record to update.")
	parser.add_argument('-c', '--creds_file', default = None, 
		help = "An INI format file containing your cloud credentials.")
	parser.add_argument('-u', '--user', default = None, 
		help = "Your Rackspace Cloud user name.")
	parser.add_argument('-k', '--api_key', default = None, 
		help = "Your Rackspace Cloud API key.")

	args = parser.parse_args()

	pyrax.set_setting("identity_type", "rackspace")

	if args.creds_file:
		pyrax.set_credential_file(os.path.abspath(
									os.path.expanduser(args.creds_file)))
	elif args.user and args.api_key:
		pyrax.set_credentials(args.user, args.api_key)
	else:
		print "Must provide either creds file or credentials as arguments."
		sys.exit(1)


	#printer = pprint.PrettyPrinter()
	#printer.pprint(socket.getaddrinfo(socket.gethostname(), None))

	#addresses = [item[4][0] for item 
	#			in socket.getaddrinfo(socket.gethostname(), None)]

	_, ext_ip, _ = stun.get_ip_info()


if __name__ == '__main__':
	main()