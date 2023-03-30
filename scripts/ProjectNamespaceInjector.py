# CREATED BY: Stewart Anderson
# CREATED DATE: 07 NOVEMBER 2022
# USAGE:
#
# 1. Copy this file to the root of your CumulusCI Project Folder
# 2. Right-click and run the file in Terminal. Note that you can set update_files(True) to just remove the namespace prefix from all files.
# 3. Done
#

import glob
import os
import re

NAMESPACE_REPLACEMENT = f"%%%NAMESPACED_ORG%%%"
SEARCH_FOLDER = "force-app/main/default"

# List of metadata types that do not support namespaces
UNSUPPORTED_TYPES = {
    'lwc': ['LightningComponentBundle'],
    'staticresources': ['StaticResource'],
    'contentassets': ['ContentAsset'],
}

def update_files(RemoveOnly = False):

  # Search for all metadata files in your Salesforce DX project
  xml_files = glob.glob('force-app/main/default/**/*.xml', recursive=True)
  cls_files = glob.glob('force-app/main/default/**/*.cls', recursive=True)
  page_files = glob.glob('force-app/main/default/**/*.page', recursive=True)
  metadata_files = xml_files + cls_files + page_files
  print(f"Found {len(metadata_files)} File(s)")

  # Filter out metadata files that belong to unsupported types
  supported_files = [f for f in metadata_files if all([t not in f for t in UNSUPPORTED_TYPES.get(os.path.basename(os.path.dirname(f)), [])])]
  print(f"Found {len(supported_files)} Supported File(s)")

  # Do something with the supported files, for example:
  for f in supported_files:

    # Search for all custom references within file
    print(f"\n**Processing File**: {f}")
    with open(f, "r") as temp_file:
      temp_file.seek(0)
      temp_file_string = temp_file.read()

    # Update File String with new References
    temp_file_string = temp_file_string.replace(NAMESPACE_REPLACEMENT, "")

    if not RemoveOnly:
      temp_file_string = re.sub("[\w]+__c", f"{NAMESPACE_REPLACEMENT}\g<0>", temp_file_string)
      temp_file_string = re.sub("[\w]+__r", f"{NAMESPACE_REPLACEMENT}\g<0>", temp_file_string)
      temp_file_string = re.sub("[\w]+__s", f"{NAMESPACE_REPLACEMENT}\g<0>", temp_file_string)

    with open(f, "w") as tmpFile:
          tmpFile.write(temp_file_string)

# Run Task
update_files(False)
