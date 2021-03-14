import csv
import json
import random
from collections import defaultdict


path_root = "https://ipfs.io/ipfs/"

def main ():
  # prepare all attributes into dictionary of lists
  f = 'attributes.csv'
  reader = csv.DictReader(open(f))
  attribs = next(reader)
  for key in attribs.keys():
    attribs[key] = [attribs[key]]
  for record in reader:
    for key in attribs.keys():
      if record[key] != '':
        attribs[key].append(record[key])
  
  # prepare all box names and descriptions into a dictionary
  with open('boxNames.csv') as f:
    box_names = [ {k: v for k, v in row.items()} for row in csv.DictReader(f) ]

  """ with open('boxNames.csv') as f:
    box_names = f.readlines()
  box_names = [ box_name.strip('\n').split(',') for box_name in box_names ] """

  # prepare all contentIDs into a dictionary
  with open('pizzaBoxes') as f:
    box_content_ids = f.readlines()
  box_content_ids = [ s.strip('\n') for s in box_content_ids ]
  
  # create a metadata .json file for each box art style
  meta_data = json.load(open('pizza_box.json'))
  for count, box in enumerate(box_content_ids):
    with open('./box-metadata/box-'+ str(count) + '.json', 'w') as output:
      meta_data['name'] = box_names[count]['name']
      meta_data['description'] = box_names[count]['description']
      meta_data['image'] = path_root+box
      meta_data['attributes'] = []
      for attrib in attribs:
        #print (meta_data['attributes'])
        meta_data['attributes'].append({
          "trait_type": attrib,
          "value": random.choice(attribs[attrib])
          })
      json.dump(meta_data, output)


if __name__ == '__main__':
  main()