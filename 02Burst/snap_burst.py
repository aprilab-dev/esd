"""
Coregistration Error Analysis at Burst and Block Scales for ESD
-----------------------------------------------------------------------

Description:
    - This script performs interferometric processing of Sentinel-1 SAR images (.zip) using the ESA SNAP Graph Processing Tool (GPT).
    - The processing workflow includes SAR data read, split, precise orbit, geocoding, and ESD.

Inputs (paths must be configured):
    1. Sentinel-1 SAR images (.zip).
    2. SNAP XML processing graph (snap_burst.xml).

Notes:
    - The first SAR image in the sorted list is selected as the master.
    - All remaining SAR images are processed as slave images.
    - The processing steps are defined in the SNAP XML graph, and their parameters must be configured according to the input data.
    - The SNAP GPT executable path and computational resource settings must be adjusted according to the local processing environment.
"""


# Import required libraries
import os
import glob
import subprocess

# Directory containing Sentinel-1 SAR images (.zip)
data_path = r'/02Burst/data'

# SNAP XML processing graph (including precise orbit correction)
xml_file_esd1 = r'/02Burst/snap_burst.xml'

# Sort Sentinel-1 SAR images by filename
datas = sorted(glob.glob(os.path.join(data_path, '*.zip')))

# Select the first image as the master and the remaining images as slaves
master = datas[0]
slave = datas[1:]

# Extract the acquisition date of the master image
input1 = master
basename_input1 = os.path.basename(input1)
date1 = basename_input1.split('_')[5][:8]

for input2 in slave:

    # Extract the acquisition date of the slave image
    basename_input2 = os.path.basename(input2)
    date2 = basename_input2.split('_')[5][:8]

    # Define the SNAP GPT command and processing parameters
    command = ['/opt/esa-snap/bin/gpt', '-c', '180G', '-q', '56',
               xml_file_esd1, '-Pinput1=' + input1, '-Pinput2=' + input2]

    # Execute the SNAP processing graph
    subprocess.check_output(command)
    print(date2 + "_burst Done!")

print("All done!")