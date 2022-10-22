# A3 - Use case

## 3A: Analyse use case

1. Goal: 

"The goal is to support calculations of indoor climate in terms of heatloss over the external contruction, to insure the building complies the building regulation." 

2. Model Use (Bim Uses): 

The tools can be used by a broad group of engineers, but is design for the MEP engineers specialized in indoor climate. Due to the specific requirements regarding indoor climate in the building regulation, these calculations can have essential meaning for both the overall design and the construction use cases. It should also be considered in relation to other use cases, since it can have a smaller impact upon those. 

## 3B: Propose of tool / workflow

3. Process: 

![diagram](https://user-images.githubusercontent.com/112874093/197334057-464f3b44-ef7c-4b0f-9583-37179d856fc4.svg "BPMN diagram")


4. Description:

So the workflow is divided into three iterated parts. The first part secures that only the relevant elements are used in calculations. The only information exchange is the architectural IFC model. The second part is the calculation of heat loss and heat transport. Here we have information exchange in terms of material info, BR18 and weather data. In this part the requirements is termined based on the information from the building regulation. The last part evaluates if the calculations complies the requirements or if any optimization is needed. 

## 3C: Information exchange

5. Information Exchange: Fill out the excel template with the information for your planned tool / workflow. For this you will need access to the excel, and the Dikon document to help you specify the LOD (LOR,LOG,LOI) for each element you need for you tool / workflow. This can get confusing - don’t worry we can help 😊

6. IFC: Describe the IFC entities and properties for each of the elements you identified in your information exchange. Describe the data that you need to:

Find in the IFC
Find in an external sources i.e. BR18
Based on assumptions (useful when we don't have the 'real' data that we need for our tool)

## 3D: What is the potential improvement offered by this tool?

7. Describe the business value:

The tool gives an quick overview about whether or not the building complies with simple requirements from the building regulation. The tool will be a timesaver, and the employer will quickly be able to determined if the design should be optimized or not. 

8. Describe the societal value:

Since the tools secures a more productive process, the tool also reduce human ressources on a building project. The tool does not consider 
overconsumption of materials, but could be implemented in a later version. 

## 3E: Delivery



9. Description of how your tool / workflow would solve the use case:

The script will be used to gather information needed for indoor climate calculations. This will be amount, material and size of the external building parts. After gathering the information, the script will calculate heat loss and heat transport, and evaluate whether or not the BR18 is complied. 

10. Description of how you would make the tool / workflow - what steps would you go through?

The tool will be made of four steps scripted in python:

Step 1 - Gather information: Analyze the different external components.

Step 2 - Calculations: Heat loss and heat transport.

Step 3 - Building regulation: Is it complied or not?

Step 4 - Optimization: Are any changes or optimization nescessary?

