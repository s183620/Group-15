
# Final project - Indoor climate 

## Presentation of the tool

The overall purpose of the project, was to create a tool for the MEP engineers, which could support the calculation of indoor climate. 

The tool is divided in several parts:
- Get info from building parts (material, dimensions, etc.)
- The materials have thermal conductivity values (lambda) which must be used to calculate the u-values for the different components.
- The u-values are compared with u-values from the building regulations which have requirements for the various building parts.

We are focusing on the external walls as part of the building. The idea is that the tool can be developed to calculate and compare u-values for all building parts (roof, floor, foundation, inner walls, etc.)

Due to the specific requirements regarding indoor climate in the building regulation, these calculations can have essential meaning for both the overall design and the construction use cases. It should also be considered in relation to other use cases, since it can have a smaller impact upon those. The tool is a shortcut to an assessment of the building with regard to the climate screen.
The tool can be used along the way when you have sketches, measurements and materials ready for the various building parts. The purpose is to catch the errors along the way so that it can be adjusted.

Our BPMN diagram has changed a bit through the project, but this is the final one. The process also shows determination of the requirements and a possibly optimization. This is not fully included in the actual tool we've made, but is suppose to be a part of a further development. 

![diagram-2](https://user-images.githubusercontent.com/112402480/203063864-79c07321-011d-4aa8-8829-4d201af49ddc.svg)

## Step by step guide

Step 1: Place the model in the "model" folder

Step 2: Check the lambda-values in the json file in the "input" folder, change them if they don't match

Step 3: Open the "indoor climate" blender file, they script is already included here

Step 4: Import the IFC-file from the "model" folder

Step 5: Now you run the script

Step 6: The calculation of the u-values are now in the excel file "output" in the "output" folder

Step 7: Look at the conclusions for the different components, and consider changes if nescessary in the lambda-values

## Business value and further development

The tool gives a quick overview about whether or not the building complies with simple requirements from the building regulation. The tool will be a timesaver, and the employer will quickly be able to determined if the design should be optimized or not.

One of the disadvantages with the tool so far, is that you have to place the transition insulation in the script manually, which is a bit of a vulnerability. But the tool could be optimized in a company with several better programmers, and us as the projectleaders instead. 

Since the tools secures a more productive process, the tool also reduce human ressources on a building project. The tool does not consider overconsumption of materials, but could be implemented in a later version. The tool could also be a part of another program or just able to be used concurrently with it. 

Another further development could be to load in values from BR or DS directly into it, and make it possible to check requirements for all sorts of things for the building components. 

It could also later on be developed for other contries with their building regulation, instead of the danish one. 

## Idea for HTML

We didn't make an actual HTML for this project, but we have an idea for it. A possible solution could be a webpage, where the buildingcomponents from the script are being displayed in 3D. The components should have a colorcode for whether or not they complies with the building regulation. For instance if the walls are green, it means that the u-value complies and no changes are necessary for this. If the wall is red, the u-value is too low and changes needs to be made. There could also be a colorcode for the buildingcomponent that has an u-value close to the limit, and thus something you need to be aware of. 
