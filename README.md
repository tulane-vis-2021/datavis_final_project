# datavis_final_project

### THIS CODE SHOULD BE RUN IN AN IPYTHON INTERACTIVE SHELL OR THE SPYDER IDE. ### 
 
 This repository contains a python script that loads in four files:

 data_vis_mapping.csv
 power_traces_averaged.csv
 power_traces.csv
 s_03763302.jpg

 The three .csv files contain information from SHARAD track s_03763302. The .jpg is a radargram of this track, for visual reference.

 The python script: datavis_project.py

 - imports relevant libraries
 - loads in data
 - data cleaning, dielectric conversions, variable definitions
 
 There are two visualizations that this script generates:

 1. RADARGRAM + SINGLE COLUMN PROFILE

 - The image on the left shows a red vertical line indicating the starting trace (trace = column) location for pixel averaging. Each point in this trace is averaged with 9 more pixels to the right of it, to reduce noise seen in a single trace. The red line is just for reference--the averaging was done in a separate IDL script, not shown.

 - The plot on the right allows click interaction. This visualization shows the material-corrected depth and dB signal power of the averaged traces in the selected radargram. The default profile shows the depth of the column assuming the material is entirely CO2 ice. Clicking once on the visualization displays the conversion to pure water ice. Right-clicking the visualization displays the conversion to seawater ice. Double-clicking the visualization returns to CO2 ice profile.


2. RADARGRAM + THREE COLUMN PROFILES

- Shown again on the left is the radargram with the reference trace location.

- Visualizations to the right of the radargram show individual plots for the column depth with power for a given material. Crosshairs on each of these plots snap to the profile and follow the direction (up or down the profile) of the mouse cursor. The plot that your mouse cursor hovers over is the referenced by the other plots, and all three are updated to the according cursor location in this plot. Power (x) and depth (y) locations are printed at the bottom of each plot, for reference.