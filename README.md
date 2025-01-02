# Component Grid Array Placement for Altium

A Python utility that **generates pick-and-place coordinates** (in CSV format) for placing components on a **grid array**. This tool uses the [Shapely](https://github.com/shapely/shapely) library to determine valid placement areas, outputting a list of coordinates suitable for **Altium Designer** PCB designs. The generated CSV file can be used to specify component coordinates within Altium Designer.

## Overview

1. **Board Shape**: Defined by a primary `polygon` that encloses the valid area on the PCB.  
2. **Excluded Areas**: Defined by four polygons (`ignoreBL`, `ignoreBR`, `ignoreTR`, `ignoreTL`), which represent no-go zones where components should *not* be placed (e.g., mechanical cutouts, keep-out zones, or reserved areas).

The script:
- Iterates systematically over a user-defined grid of points.
- Checks each point to ensure it lies within the main board `polygon` and not within any of the `ignore*` polygons.
- Prints and writes valid placements as a CSV for **Altium**.

## Requirements

1. **Python 3.7+**
2. **Shapely**:
   '''
   pip install shapely
   '''

## Usage

1. **Clone or Download** this repository.  
2. **Install Dependencies** (e.g., Shapely) via:
   '''
   pip install shapely
   '''
3. **Configure Board Geometry**:
   - **Polygon (`polygon`)**: Defines the main PCB boundary.  
   - **Ignore Polygons** (`ignoreBL`, `ignoreBR`, `ignoreTR`, `ignoreTL`): Define smaller rectangular areas to be excluded from placement.
4. **Run the Script**:
   - In a terminal:
     '''
     python GridArrayPlacement.py
     '''
   - A CSV file (e.g., `C:\TestOutput.csv`) is generated with component placements.

5. **Import into Altium**:
   - Open your PCB in Altium Designer.
   - Use Altium’s import functionality to place your newly generated component array coordinates.

## Code Snippet

Below is a **partial** code snippet highlighting the polygon definitions and their purpose:

'''
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

# Main PCB boundary
polygon = Polygon([
    (0.0, 0.0),
    (113.0, 0.0),
    (168.0, 91.0),
    (0.0, 132.0)
])

# Ignore (exclusion) polygons
ignoreBL = Polygon([
    (0.0, 0.0),
    (1.0, 0.0),
    (1.0, 38.0),
    (0.0, 38.0)
])

ignoreBR = Polygon([
    (111.0, 0.0),
    (113.0, 0.0),
    (113.0, 3.0),
    (111.0, 3.0)
])

ignoreTR = Polygon([
    (164.0, 87.0),
    (168.0, 87.0),
    (168.0, 91.0),
    (164.0, 91.0)
])

ignoreTL = Polygon([
    (0.0, 128.0),
    (4.0, 128.0),
    (4.0, 132.0),
    (0.0, 132.0)
])
'''

- The main `polygon` variable outlines the PCB shape.  
- The `ignore*` polygons mark regions to exclude (e.g., mechanical cutouts, connectors).

## Contributing

1. **Fork** this repository.  
2. **Create** a feature branch (e.g., `feature/my-new-feature`).  
3. **Commit** your changes and open a **pull request**.

## License

This project is provided as-is with no specific license. If you use or modify the code, please retain appropriate credit.
