"""
Coregistration Error Analysis for Geometrical Coregistration
--------------------------------------------------------------------

Description:
    - This script performs interferometric processing of Sentinel-1 SAR images (.zip) using the ESA SNAP Graph Processing Tool (GPT).
    - The workflows include SAR data read, split, precise orbit, geocoding, optional ESD, deburst, interferogram, and write.
    - The processing times of both workflows are recorded to estimate the additional computational time associated with ESD.

Inputs (paths must be configured):
    1. Sentinel-1 SAR images (.zip).
    2. SNAP XML processing graph without ESD (snap_esd0.xml).
    3. SNAP XML processing graph with ESD (snap_esd1.xml).

Outputs (paths must be configured):
    1. Interferometric products without ESD (diff_orb1_esd0/itfg_YYYYMMDD.dim).
    2. Coregistered stack products without ESD (stack_orb1_esd0/stack_YYYYMMDD.dim).
    3. Interferometric products with ESD (diff_orb1_esd1/itfg_YYYYMMDD.dim).
    4. Coregistered stack products with ESD (stack_orb1_esd1/stack_YYYYMMDD.dim).

Notes:
    - The first SAR image in the sorted list is selected as the master.
    - All remaining SAR images are processed as slave images.
    - The processing steps are defined in the SNAP XML graphs, and their parameters must be configured according to the input data.
    - The SNAP GPT executable path and computational resource settings must be adjusted according to the local processing environment.
    - The additional processing time associated with ESD is estimated from the difference between the execution times of the two workflows.
"""


# Import required libraries
import os
import glob
import subprocess
import time

# Directory containing Sentinel-1 SAR images (.zip)
data_path = r'/01InSAR/data'

# SNAP XML processing graphs (including precise orbit correction)
xml_file_esd0 = r'/01InSAR/snap_esd0.xml'
xml_file_esd1 = r'/01InSAR/snap_esd1.xml'

# Output directories for processing without and with ESD
output_path1_esd0 = r'/01InSAR/diff_orb1_esd0'
output_path2_esd0 = r'/01InSAR/stack_orb1_esd0'
output_path1_esd1 = r'/01InSAR/diff_orb1_esd1'
output_path2_esd1 = r'/01InSAR/stack_orb1_esd1'

# Sort Sentinel-1 SAR images by filename
datas = sorted(glob.glob(os.path.join(data_path, '*.zip')))

# Select the first image as the master and the remaining images as slaves
master = datas[0]
slave = datas[1:]

# Extract the acquisition date of the master image
input1 = master
basename_input1 = os.path.basename(input1)
date1 = basename_input1.split('_')[5][:8]

# Record the processing time without ESD
start_time_esd0 = time.time()

for input2 in slave:

    # Extract the acquisition date of the slave image
    basename_input2 = os.path.basename(input2)
    date2 = basename_input2.split('_')[5][:8]

    # Define output filenames in BEAM-DIMAP format (.dim)
    # Filenames follow the GECORIS naming convention
    out_file1 = 'itfg_' + date2 + '.dim'
    out_file2 = 'stack_' + date2 + '.dim'

    # Construct absolute paths for output products
    output1 = os.path.join(output_path1_esd0, out_file1)
    output2 = os.path.join(output_path2_esd0, out_file2)

    # Define the SNAP GPT command and processing parameters
    command = ['/opt/esa-snap/bin/gpt', '-c', '180G', '-q', '56',
               xml_file_esd0, '-Pinput1=' + input1, '-Pinput2=' + input2,
               '-Poutput1=' + output1, '-Poutput2=' + output2]

    # Execute the SNAP processing graph
    subprocess.check_output(command)
    print(date2 + "_esd0 Done!")

end_time_esd0 = time.time()
run_time_esd0 = end_time_esd0 - start_time_esd0

# Record the processing time with ESD
start_time_esd1 = time.time()

for input2 in slave:

    # Extract the acquisition date of the slave image
    basename_input2 = os.path.basename(input2)
    date2 = basename_input2.split('_')[5][:8]

    # Define output filenames in BEAM-DIMAP format (.dim)
    # Filenames follow the GECORIS naming convention
    out_file1 = 'itfg_' + date2 + '.dim'
    out_file2 = 'stack_' + date2 + '.dim'

    # Construct absolute paths for output products
    output1 = os.path.join(output_path1_esd1, out_file1)
    output2 = os.path.join(output_path2_esd1, out_file2)

    # Define the SNAP GPT command and processing parameters
    command = ['/opt/esa-snap/bin/gpt', '-c', '180G', '-q', '56',
               xml_file_esd1, '-Pinput1=' + input1, '-Pinput2=' + input2,
               '-Poutput1=' + output1, '-Poutput2=' + output2]

    # Execute the SNAP processing graph
    subprocess.check_output(command)
    print(date2 + "_esd1 Done!")

end_time_esd1 = time.time()
run_time_esd1 = end_time_esd1 - start_time_esd1

# Estimate the additional processing time associated with ESD
esd_time_all = run_time_esd1 - run_time_esd0
esd_time = esd_time_all / len(slave)

# Calculate the relative ESD processing time
a = esd_time_all / run_time_esd1

# Display processing time statistics
print(f"Total processing time without ESD: {run_time_esd0} seconds")
print(f"Total processing time with ESD: {run_time_esd1} seconds")
print(f"Estimated ESD processing time per image pair: {esd_time} seconds")
print(f"Relative ESD processing time: {a}")

print("All done!")
