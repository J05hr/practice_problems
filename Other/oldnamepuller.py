import json
import csv
import glob
import os

## CSV save path
csv_path = "all_names_csv.csv"

## recursive directories for .jsons
jsons_path = glob.glob(
    'U:\Engineering\Geographic Information Systems\Chennai Projects\Conflation pt. 1\Conflation Data\**\*.json',
    recursive=True)

##write csv header
with open(csv_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["File Name", "Name 1", "Name 2", "Name 3", "Directory"])


def name_puller_and_csv(filepath):
    with open(filepath) as json_data:
        json_parse = json.load(json_data)

        ## variety of print options
        # print ("NAME 1")
        # pprint(data['AttributeMapping']['Name1'])
        # print("NAME 2")
        # pprint(data['AttributeMapping']['Name2'])
        # print("NAME 3")
        # pprint(data['AttributeMapping']['Name3'])

        ##append csv to add the jsons dir and all name fields
        with open(csv_path, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([(os.path.basename(fname)), (json_parse['AttributeMapping']['Name1']),
                (json_parse['AttributeMapping']['Name2']),(json_parse['AttributeMapping']['Name3']), fname])

            ## variety of print options if there are 2 name fields
            # print ("- File Path: [ %s ] -") % (fname)
            # print ('  -HAS SECOND NAME-     ')
            # print ("    Name 1 field is:     ")
            # print (json_parse['AttributeMapping']['Name1'])
            # print ("    Name 2 field is:     ")
            # print (json_parse['AttributeMapping']['Name2'])
            # elif data['AttributeMapping']['Name1'] == '':
            # print("- File Path: [ %s ] -") % (fname)
            # print ('        No Name         ')



for fname in jsons_path:
    name_puller_and_csv(fname)