# A3 - Use case

## 3A: Analyse use case

1. Goal: 

"The goal is to support calculations of indoor climate in terms of heatloss over the external contruction, to insure the building complies the building regulation." 

2. Model Use (Bim Uses): 

The tools can be used by a broad group of engineers, but is design for the MEP engineers specialized in indoor climate. Due to the specific requirements regarding indoor climate in the building regulation, these calculations can have essential meaning for both the overall design and the construction use cases. It should also be considered in relation to other use cases, since it can have a smaller impact upon those. 

## 3B: Propose of tool / workflow

3. Process: 

![diagram](https://user-images.githubusercontent.com/112874093/197334988-d7d3402f-6952-4147-92b1-557112d083cd.svg "BPMN diagram")


4. Description:

So the workflow is divided into three iterated parts. The first part secures that only the relevant elements are used in calculations. The only information exchange is the architectural IFC model. The second part is the calculation of heat loss and heat transport. Here we have information exchange in terms of material info, BR18 and weather data. In this part the requirements is termined based on the information from the building regulation. The last part evaluates if the calculations complies the requirements or if any optimization is needed. 

## 3C: Information exchange

5. Information exchange

For the information exchange, see the excel file in the folder.

6. IFC entities and BR18

The IFC entities we need for our tool is the following: IFC_walls, IFC_roof, IFC_floor, IFC_windows, IFC_doors, IFC_foundation, IFC_spaces. We also gona need some IFC_properties like; thickness, height, width, material.
In our tool BR18 is used to determine the requirements for the heat-transport and loss.

For the building materials, it will be nescessary to assume an G-value and an U-value to calculations. 


## 3D: What is the potential improvement offered by this tool?

7. Describe the business value:

The tool gives an quick overview about whether or not the building complies with simple requirements from the building regulation. The tool will be a timesaver, and the employer will quickly be able to determined if the design should be optimized or not. 

8. Describe the societal value:

Since the tools secures a more productive process, the tool also reduce human ressources on a building project. The tool does not consider 
overconsumption of materials, but could be implemented in a later version. 

## 3E: Delivery



9. Description of how your tool / workflow would solve the use case:

The script will be used to gather information needed for indoor climate calculations. This will be amount, material and size of the external building parts. After gathering the information, the tool will have to calculate heat loss and heat transport, and evaluate whether or not the BR18 is complied. 

10. Description of how you would make the tool / workflow - what steps would you go through?

The tool will be made of four steps scripted in python:

Step 1 - Gather information: Analyze the different external components.

Step 2 - Calculations: Heat loss and heat transport.

Step 3 - Building regulation: Is it complied or not?

Step 4 - Optimization: Are any changes or optimization nescessary?

