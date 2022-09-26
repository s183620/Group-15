# A1 Open Bim
## Group 15

### Use case, script and IFC
The focus area is indoor climate analysis. This is primarily for MEP engineers, but also relevant for the client and the architects.
The main priority is to optimize the building performance in terms of heat loss, radiation, thermal convection and conductivity in the outer construction. 

The script will be used for gathering information regarding the focus area, from the IFC model. The goal is to find information about walls, windows, doors, floor and roof. Including dimensions, materials and placement of openings in the facade. 

The script will address the problem in a way, where it will be used to find the amount, material and size about the external building parts. It will also be used to find the total size of the building and to find the placement of the different elements.

### Disciplinary expertise and analysis 

To achieve the goal, it will be necessary to have knowledge regarding indoor climate in general, the building regulation and the intended use of the building. One would also need knowledge regarding the different buildingmaterials and it's functions which might impact the indoor environment. For instance the windowglass and it's transmission.

In this project we will try to break down the analysis into four steps. 

Step 1:
Analyze the different components of the building, how they are constructed and it's properties.

Step 2:
Analyze the purpose of the building. What does it need?
Determine the requirements. 

Step 3:
Calculation of the three types of heat transfer and the heat loss.

Step 4:
Checking results towards requirements. Are any changes or optimization nescessary?

### Building elements and IFC concepts

For checking the indoor climate, it will be necessary to analyze the walls and it's openings, spaces, floors and roof. Also the site and orientation of the building could have an influence on the climate and therefore possibly interesting. 

For gathering information about the elements, the following IFC concepts have been used:

- IFC_space
- IFC_wall
- IFC_door
- IFC_window
- IFC_roof
- IFC_floor
- To get around the different elements, we have used the IFC_properties, which is connected to each of them.

### Connection with other use cases

The architectural use case needs to be done, because the overview of spaces and elements needs to be done. This is possibly also in this case that the materials will be chosen, which also impact the calculations in this case. 

The structural use case also needs to be almost done, to get an overview of elements that could clash with ventilation etc. 

The fire use case, LCA use case and the overall architectural ifc model will all be waiting for this use case to be done, since they all could be influenced by the nescessary changes in the indoor climate model. 

Other use cases such as the cost case are waiting for the overall model to be done, which includes this use case. 

