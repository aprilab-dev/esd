# Coregistration Error Analysis at Burst and Block Scales for ESD

This experiment investigates the spatial consistency and reliability of ESD-derived azimuth shift estimates at the burst-overlap and block scales. By comparing estimates from different burst overlaps and individual blocks, the analysis examines whether ESD can consistently achieve the nominal 0.001-pixel accuracy required for S-1 TOPS coregistration under practical conditions.

## Files

### 1. Main Script

- **`snap_burst.py`**: Main Python script for executing the SNAP processing workflow.

### 2. SNAP XML Processing Graph

The XML file defines the processing workflow created using SNAP Graph Builder.

- **`snap_burst.xml`** (with ESD):

  Read → TOPSAR-Split → Apply-Orbit-File → Back-Geocoding → ESD

**Note:** The XML processing parameters, including `subswath`, `firstBurstIndex`, and `lastBurstIndex`, must be adjusted according to the input Sentinel-1 data. Input paths and SNAP GPT execution settings in `snap_burst.py`, must also be configured before running the script.