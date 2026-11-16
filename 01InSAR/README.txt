# Coregistration Error Analysis for Geometrical Coregistration

This experiment evaluates whether geometrical coregistration using ESA precise orbit products can achieve sufficient accuracy without ESD. The ESD-derived azimuth shifts are analyzed across different study areas, satellite flight directions, and orbit-data periods to assess the residual azimuth-shift dispersion after geometrical coregistration.

## Files

### 1. Main Script

- **`snap_insar.py`**: Main Python script for executing the SNAP processing workflows and estimating the additional processing time associated with ESD.

### 2. SNAP XML Processing Graphs

The XML files define the processing workflows created using SNAP Graph Builder.

- **`snap_esd0.xml`** (without ESD):

  Read → TOPSAR-Split → Apply-Orbit-File → Back-Geocoding → TOPSAR-Deburst → Interferogram → Write

- **`snap_esd1.xml`** (with ESD):

  Read → TOPSAR-Split → Apply-Orbit-File → Back-Geocoding → ESD → TOPSAR-Deburst → Interferogram → Write

**Note:** The XML processing parameters, including `subswath`, `firstBurstIndex`, and `lastBurstIndex`, must be adjusted according to the input Sentinel-1 data. Input/output paths and SNAP GPT execution settings in `snap_insar.py` must also be configured before running the script.