# esd
Experimental code for revisiting the necessity of Enhanced Spectral Diversity (ESD) in Sentinel-1 TOPS InSAR coregistration.

----------------------------------------------------------------------------------------------------------------------------------


This repository accompanies the paper:

> **"Revisiting the Necessity of Enhanced Spectral Diversity for Sentinel-1 TOPS InSAR Coregistration"**  
> *[Authors], [Journal/Year]*  
> [DOI/Link]

----------------------------------------------------------------------------------------------------------------------------------


## 📌 Overview

With the improving accuracy of ESA's precise orbit data, this work systematically evaluates whether ESD remains an indispensable step for S-1 TOPS coregistration. We conduct experiments across **three scales** to compare coregistration errors **with and without ESD**:

| Scale | Description |
|-------|-------------|
| **Full SAR Scene Scale** | Coregistration error assessment across the full study-area extent |
| **Burst & Block Scales** | Coregistration error assessment on a per-overlap (between adjacent bursts) and per-block basis |
| **Time-Series Scale** | Coregistration error assessment for time-series InSAR applications |

----------------------------------------------------------------------------------------------------------------------------------


## 🧰 Dependencies & Platforms

This code is built upon **open-source** tools and is fully reproducible using standard Sentinel-1 data:

- [ESA SNAP](https://step.esa.int/main/download/) (version 9.0+)
- [STaMPS](https://homepages.see.leeds.ac.uk/~earahoo/stamps/) (for MT-InSAR processing)
- Python 3.8+ with the following packages:
  - `esa_snappy` (SNAP Python interface)
  - `numpy`, `scipy`, `matplotlib`
  - `xml.etree.ElementTree` (for XML parsing)

Anyone with access to Sentinel-1 data (freely available from ESA) can reproduce our experimental results.

----------------------------------------------------------------------------------------------------------------------------------


## 📁 Repository Structure
