import ifcopenshell 
import bpy
import blenderbim.bim
import ifcopenshell.util
import ifcopenshell.util.element
       
from blenderbim.bim.ifc import IfcStore
ifc = ifcopenshell.open(IfcStore.path)

######
# We use the script to find information about walls, roof, floor, windows and doors.
######

####
# Walls
####
# Finding the walls and the amount    
walls = ifc.by_type('IfcWall')
print('Number of walls:', len(walls)) 

# Finding the the properties for the walls, to find the walls, and properties, that matter for us
for wall in walls:
     wall.Name
     for definition in wall.IsDefinedBy:

         if definition.is_a('IfcRelDefinesByProperties'):
             property_set = definition.RelatingPropertyDefinition

             if property_set.Name == "Pset_WallCommon":
                for property in property_set.HasProperties:

                     #print(property)
                     
#Trying to define the external walls, because it is the only walls that matter for us
                     if property.Name == "IsExternal":
                        wall_ext=wall
                        print(property.NominalValue.wrappedValue)



# Finding the material for the walls
# work in the progress
#for wall in walls:
         #for relAssociatesMaterialLayerSetUsage in wall.HasAssociations:
             #print(relAssociatesMaterialLayerSetUsage.RelatingMaterial.ForLayerSet)
                
               # for relAssociatesMaterialLayerSet in wall.HasAssociations:
                   # for relAssociatesMaterialLayer in wall.HasAssociations:
                       #print(relAssociatesMaterialLayer.RelatingMaterial.ForMaterial)


# For the walls we need to find the size

####
# Roof
####

roofs = ifc.by_type('IfcRoof')
print('Number of roofs:', len(roofs))

for roof in roofs:
     roof.Name
     for definition in roof.IsDefinedBy:

         if definition.is_a('IfcRelDefinesByProperties'):
             property_set = definition.RelatingPropertyDefinition

             if property_set.Name == "Pset_RoofCommon":
                for property in property_set.HasProperties:

                     #print(property)
                     
##Finding the area of the roof
                     if property.Name == "TotalArea":
                        print('area =',property.NominalValue.wrappedValue)
                     
                     
for roof in roofs:
         for relAssociatesMaterialLayerSetUsage in roof.HasAssociations:
             print(relAssociatesMaterialLayerSetUsage.RelatingMaterial.ForLayerSet)

# Do the same about the material from the walls

#############
# We stoped here Because we know we have to do the same scripting for the rest, floors, 
# windows and doors, but we didn't want to do it now, if the things we have done isn't 
# the right way to do. So work in progress. Also we maybe need to look at the spaces to 
# find the size of the building, but the size of the roof, can maybe be used for this.
# For doors and windows, we also need to find out on which walls they are placed.
#############


####
# Floors
####

floors = ifc.by_type('IfcSlab')
print('Number of floors:', len(floors))

####
# Windows
####

windows = ifc.by_type('IfcWindow')
print('Number of windows:', len(windows))

####
# Doors 
####

doors = ifc.by_type('IfcDoor')
print('Number of doors:', len(doors))

####
# Spaces
####


