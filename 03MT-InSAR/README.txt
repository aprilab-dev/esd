# InSAR Time Series Results with and without ESD

This experiment evaluates the practical impact of including or omitting ESD in multi-temporal InSAR (MT-InSAR) processing. Using identical processing parameters except for the ESD step, interferometric products are generated with and without ESD and subsequently processed using StaMPS. The resulting deformation estimates and persistent scatterer (PS) distributions are compared to determine whether ESD provides meaningful improvements in time-series deformation monitoring.

## Files

### 1. Main Script

- **`snap_insar.py`**: Main Python script for executing the SNAP processing workflows and exporting interferometric products and StaMPS-compatible data.

### 2. SNAP XML Processing Graph

- **`snap.xml`**: A single XML file created using SNAP Graph Builder that integrates both processing workflows (with and without ESD).

  - Read → TOPSAR-Split → Apply-Orbit-File → Back-Geocoding → TOPSAR-Deburst → Interferogram → StaMPS-Export
  - Read → TOPSAR-Split → Apply-Orbit-File → Back-Geocoding → ESD → TOPSAR-Deburst → Interferogram → StaMPS-Export

## Outputs

- **`diff_orb1_esd0/`**: Interferometric products without ESD.
- **`diff_orb1_esd1/`**: Interferometric products with ESD.
- **`stampsexport_orb1_esd0/`**: StaMPS-compatible products without ESD.
- **`stampsexport_orb1_esd1/`**: StaMPS-compatible products with ESD.

**Note:** Both processing workflows are integrated into the same `snap.xml` file. The XML processing parameters, including `subswath`, `firstBurstIndex`, and `lastBurstIndex`, must be adjusted according to the input Sentinel-1 data. Input/output paths and SNAP GPT execution settings in `snap_insar.py` must also be configured before running the script.