
# Final project - Indoor climate 

## Purpose and presentation of the tool

The overall purpose of the project, was to create a tool for the MEP engineers, which could support the calculation of indoor climate. 

The tool is in several parts:
- Get info from building parts (material, dimensions, etc.)
- The materials have thermal conductivity values (lambda) which must be used to calculate the u-values for the different components.
- The u-values are compared with u-values from the building regulations which have requirements for the various building parts.

We focus on the outer walls as part of the building. The idea is that the tool can be developed to calculate and compare u-values for all building parts (roof, floor, foundation, inner walls, etc.)

Due to the specific requirements regarding indoor climate in the building regulation, these calculations can have essential meaning for both the overall design and the construction use cases. It should also be considered in relation to other use cases, since it can have a smaller impact upon those. The tool is a shortcut to an assessment of the building with regard to the climate screen.
The tool can be used along the way when you have sketches, measurements, materials ready for the various building parts. The purpose is to catch the errors along the way so that it can be adjusted.

- Evt BPMN

## Step by step guide for the tool

The tool will be made of four steps scripted in python:

Step 1 - Gather information: Analyze the different external components.

Step 2 - Calculations: Heat loss and heat transport.

Step 3 - Building regulation: Is it complied or not?

Step 4 - Optimization: Are any changes or optimization nescessary?

- Evt billeder fra scripts?

## Business value

The tool gives an quick overview about whether or not the building complies with simple requirements from the building regulation. The tool will be a timesaver, and the employer will quickly be able to determined if the design should be optimized or not.

One of the disadvantages with the tool so far, is that you have to place the transition insulation in the script manually, which is a bit of a vulnerability. But the tool could be optimized in a company with several better programmers, and us as the projectleaders instead. 

Since the tools secures a more productive process, the tool also reduce human ressources on a building project. The tool does not consider overconsumption of materials, but could be implemented in a later version. The tool could also be a part of another program or just able to be used concurrently with it. 

Another further development could be to load in values from BR or DS directly into it, and make it possible to check requirements for all sorts of things for the building components. 

It could also later on be developed for other contries, where the BR instead of the danish one. 

## HTML
- Evt beskrivelse af hvordan man ville lave HTML?
- Skitse?

Present your solution to your peers and get feedback from them. your presentation should consist of a 2 minute video, that describes your use case and how your solution addresses the use case.
