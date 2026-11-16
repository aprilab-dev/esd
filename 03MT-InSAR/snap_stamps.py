"""
InSAR Time Series Results with and without ESD
-------------------------------------------------------

Description:
    - This script performs interferometric processing of Sentinel-1 SAR images (.zip) using the ESA SNAP Graph Processing Tool (GPT).
    - The workflows include SAR data read, split, precise orbit, geocoding, optional ESD, deburst, interferogram, and StaMPS export.

Inputs (paths must be configured):
    1. Sentinel-1 SAR images (.zip).
    2. SNAP XML processing graph (snap.xml).

Outputs (paths must be configured):
    1. Interferometric products without ESD (diff_orb1_esd0/YYYYMMDD_YYYYMMDD.dim).
    2. Interferometric products with ESD (diff_orb1_esd1/YYYYMMDD_YYYYMMDD.dim).
    3. StaMPS-compatible products without ESD (stampsexport_orb1_esd0/).
    4. StaMPS-compatible products with ESD (stampsexport_orb1_esd1/).

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
import time

# Directory containing Sentinel-1 SAR images (.zip)
data_path = r'/03MT-InSAR/data'

# SNAP XML processing graph (including precise orbit correction)
xml_file = r'/03MT-InSAR/snap_stamps.xml'

# Output directories for processing without and with ESD
output_path1 = r'/03MT-InSAR/diff_orb1_esd0'
output_path2 = r'/03MT-InSAR/diff_orb1_esd1'
output_path3 = r'/03MT-InSAR/stampsexport_orb1_esd0'
output_path4 = r'/03MT-InSAR/stampsexport_orb1_esd1'

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

    # Define output filenames in BEAM-DIMAP format (.dim)
    out_file = date1 + '_' + date2 + '.dim'
    out_folder = date1 + '_' + date2

    # Construct absolute paths for output products
    output1 = os.path.join(output_path1, out_file)
    output2 = os.path.join(output_path2, out_file)
    output3 = os.path.join(output_path3, out_folder)
    output4 = os.path.join(output_path4, out_folder)

    # Define the SNAP GPT command and processing parameters
    command = ['/opt/esa-snap/bin/gpt', '-c', '180G', '-q', '56',
               xml_file, '-Pinput1=' + input1, '-Pinput2=' + input2,
               '-Poutput1=' + output1, '-Poutput2=' + output2,
               '-Poutput3=' + output3, '-Poutput4=' + output4]

    # Execute the SNAP processing graph
    subprocess.check_output(command)
    print(out_file + " Done!")

    # Pause for 30 seconds to reduce potential memory resource issues
    time.sleep(30)

print("All done!")