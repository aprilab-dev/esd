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

| Experimental Scale       | Main Objective                                                                                                | Paper Section | Corresponding Code |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- | ------------- | ------------------ |
| **Full SAR Scene Scale** | Evaluate residual azimuth shifts after geometrical coregistration using precise orbit products                | Section IV-A  | 01InSAR            |
| **Burst & Block Scales** | Assess the spatial consistency and reliability of ESD-derived azimuth shifts across burst overlaps and blocks | Section IV-B  | 02Burst            |
| **Time-Series Scale**    | Compare MT-InSAR deformation results with and without ESD using StaMPS                                        | Section IV-C  | 03MT-InSAR         |

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

```text
.
├── 01InSAR/
│   ├── README.txt
│   ├── snap_insar.py
│   ├── snap_esd0.xml
│   └── snap_esd1.xml
│
├── 02Burst/
│   ├── README.txt
│   ├── snap_burst.py
│   └── snap_burst.xml
│
└── 03MT-InSAR/
    ├── README.txt
    ├── snap_stamps.py
    └── snap_stamps.xml
```

Each directory contains a `README.txt` file with processing details and configuration instructions.
