import ifcopenshell 
import bpy
import blenderbim.bim
import ifcopenshell.util
import ifcopenshell.util.element   
from blenderbim.bim.ifc import IfcStore
ifc = ifcopenshell.open(IfcStore.path)
import json
import math
import decimal
from decimal import Decimal 
import xlsxwriter


with open("/Users/christianahlefeldt-laurvigen/Library/CloudStorage/OneDrive-DanmarksTekniskeUniversitet/Skole/K - semester 1/41934 Advanced BIM/indoor_climate/input/input.json") as file:
    data= json.load(file)
#print(data)
 
walls = ifc.by_type('IfcWall')
#print('Number of walls:', len(walls))

####
# Define some of the standard values and dictionary #

transistion_insulation_ext= 0.04
transistion_insulation_int = 0.13

count = 0
u_value = 0
thickness_total = 0

dict ={} 

####
# Finding the the properties for the walls, to find the walls, and properties, that matter for us

for wall in walls:
     wall.Name
     for definition in wall.IsDefinedBy:

         if definition.is_a('IfcRelDefinesByProperties'):
             property_set = definition.RelatingPropertyDefinition

             if property_set.Name == "Pset_WallCommon":
                for property in property_set.HasProperties:

                     #print(property)
                            
                     if property.Name == "IsExternal":
                        if property.NominalValue.wrappedValue == True:
                            wall_ext = wall.Name
                            count += 1
                            u_value = 0
                            thickness_total = 0
                            #print(wall.Name)
                            for relAssociatesMaterialLayerSetUsage in wall.HasAssociations:
                                #print(relAssociatesMaterialLayerSetUsage.RelatingMaterial.ForLayerSet.MaterialLayers)
                                for materialLayer in relAssociatesMaterialLayerSetUsage.RelatingMaterial.ForLayerSet.MaterialLayers:
                                    print(materialLayer.Material.Name)
                                    #print(materialLayer.LayerThickness)
                                    
                                    materialtype = [materialLayer.Material.Name]
                                    thickness = [materialLayer.LayerThickness]
                                    
                                    if materialLayer.Material.Name in data:

                                        material_name = materialLayer.Material.Name

                                        y = data[material_name]
                                
                                        u = materialLayer.LayerThickness/y
                                        u_value += u
                                        thickness_total += materialLayer.LayerThickness
                                        u_valv = u_value+transistion_insulation_int+transistion_insulation_ext
                                        u_valv_2=1/u_valv
                                        
                                    if u_valv_2 < 0.3:
                                        result = 'not approved'
                                    else:
                                        result = 'approved'
       
                
                            dict.setdefault('Name', [])
                            dict.setdefault('U Value', [])
                            dict.setdefault('Thickness', [])
                            dict.setdefault('Conclusion', [])
                            dict['Name'].append(wall_ext)
                            dict['U Value'].append(round(1/u_valv,3))
                            dict['Thickness'].append(thickness_total)
                            dict['Conclusion'].append(result)
                            

####
# Test if dict is right #
#print(dict)

####
# Export to excel #

workbook = xlsxwriter.Workbook('/Users/christianahlefeldt-laurvigen/Library/CloudStorage/OneDrive-DanmarksTekniskeUniversitet/Skole/K - semester 1/41934 Advanced BIM/indoor_climate/output/output.xlsx')

worksheet = workbook.add_worksheet("Sheet 1")

row = 1
col = 0
worksheet.write(0,0, 'Name')
worksheet.write(0,1, 'U value in [W / m^2 * K]')
worksheet.write(0,2, 'Thickness in [m]')
worksheet.write(0,3, 'Conclusion')

for x in range(1,len(dict['Name'])):
    worksheet.write(row, col, dict["Name"][x])
    worksheet.write(row, col + 1, dict["U Value"][x])
    worksheet.write(row, col + 2, dict["Thickness"][x])
    worksheet.write(row, col + 3, dict["Conclusion"][x])
    row += 1
 
workbook.close()
