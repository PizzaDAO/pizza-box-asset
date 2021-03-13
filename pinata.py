from config import *
import json
import requests

pin_list = "https://api.pinata.cloud/data/pinList?status=pinned"

r = requests.get(
  pin_list, headers={
    'pinata_api_key': API_KEY,
    'pinata_secret_api_key': API_SECRET
    })

#content_hashes = [ content['ipfs_pin_hash'] for content in r.json()['rows'] ]