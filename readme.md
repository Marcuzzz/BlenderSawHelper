# MySawHelper
=======================

This Blender addon provides a simple way to generate a set of planks using random colors, dimensions, and materials based on input parameters.

## Installation
User Preferences -> Addons -> Plugins (Python) -> mysawhelper
Note: You may have to click the arrow icon next to 'Disabled' to enable the addon before you can see it listed here. Also check that 'Allow Scripting' checkbox if everything appears disabled.

## Configuration
The following options are available under the plugin settings dialog:

### Length: float value determines the length of all generated objects (default is 2.44).
Minimum and Maximum limits can also be set.
### Width: float value determines the width of all generated objects (default is 1.22).
Minimum and Maximum limits can also be set.
### Height: float value determines the height of all generated objects (default is .018).
A minimum limit only applies since zero height wouldn't make much sense.
### Cut: float value determines the thickness of stock material being cut into blocks (default is .006).
No specific limit but note too small of a value could cause precision loss during calculations.
### Object Name: string determines what to name the resulting block meshes once created.
Default value sets the name prefix like "Block" while leaving a number at the end indicating order of creation starting with 1.

## Features
### Randomized Colors: 
Generates objects with randomly selected RGB color values between 0 and 1
### Optional Preset Colors: 
Configure predefined list of colors and/or toggle their usage in color generation logic
### Customizable Dimensions & Randomization: 
Determine how generative parameters behave -- lenthWidthRatio (floating point ratio between length and width; default is 7.5), -- heightPercent (percentage amount to subtract fr

![ Alt text](screenrecording.gif)