# A2 Future Bim

### Use case - indoor climate

The use case focus is indoor climate, and especially the heatloss over the external building parts. For this, we need the materials and the openings in the outer building parts. Therefore we have tried to get some of these informations out with the new script.

The changes we have made, is described in the Changes.md file.

### What information can you get from the IFC for your use case from the previous assignment?

In the previous assignment, we got to know about different IFC components, such as IFCWindows, IFCWalls etc. 
We also benefit from the knowlegde about how different IFC properties are linked to each IFC component. And how it is used to link more than one component to another. 

### What guidance might the 'end user' need?

The end user will need to know something about the general construction and design of the building.

Since the changes so far are pretty simple, the end user won't need so much guidance at the moment. But the end user need to able to extract the information by itself. 

### What analysis can you perform to support this guidance based on the info you have available?

Ensure that the site is still userfriendly, no matter how many function that are being incorporated. 
This means you have to make the analysis as a part of the script, so the end user only sees the results in the site. 

### Changes made directly to the index.html file

In the index.html file we added a new part to the body called "building". In here we added the number of windows, so it's possible for the js.file to "find" the variable and display it. 

