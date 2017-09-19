#!/usr/bin/env python
import CloudFlare
import config

cf = CloudFlare.CloudFlare(email=config.CF_API_EMAIL, token=config.CF_API_KEY)

for zone in cf.zones.get():
    print '{}: {}'.format(zone['name'], zone['id'])
