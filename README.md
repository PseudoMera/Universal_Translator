# Universal_Translator
Universal translator is a console application that allows you to convert any length unit under the metric system to another in the same system. Universal translator will requiere you to feed it a file with the units you want to convert.

Universal translator uses the same base unit as the metric system, which is the meter.

## File_Format
If you want to know how the file should be structured you should go to the file examples folder.  
There you will find an example of the the file you should give the program (test.txt) and the result file after the convertion (result.txt)

v = value   
fu = from unit  
tu = to unit  
km = kilimeters.  
m = meters.  
cm = centimeter.  
mm = millimeter.  
um = micrometer.  
nm = nanometer.  

## Install
To start using the universal translator, you have two options:  

1-Download this repository and have python 3.6 installed. If you choose this option go to the how to use it section.  

2-Download the following folder, and go to the how to use it section:  
https://drive.google.com/open?id=1wShMRjQE4aUyWympdPk5a3UbyMC3XVgI


## How to use it  
Before we start make sure you have everything setup as per the requirements section.   

If you decided to choose the first option, this is your guide to using the universal translator:   

1. Type python3 universal_translator.py into your console (you have to be on the same directory as the universal_translator.py file).   

2. The program will ask you for your file route. If you already are on the same folder as your file you just have to type your file name + it's extension (.txt). If you are not on the same directory as your file you will have to type the full path. Example: /home/username/Documents/test.txt.  

3. You will then be asked to introduce the name of the result file(this file will contain the results of the convertion), You should not put the extension, the program will set it to .txt by default.  

4. A result file will be generated with the solution. This file will be on the same directory you ran universal_translator.py.    

If you chose the second option, this is your guide:

1. Download the dist folder in the given link (Install section).    

2. Open your local dist folder and go to dist/universal_translator/. Here you will find an executable with the name universal_translator.   

3. Run it and follow the same steps (2 and below) as the first option.


## Class diagram of the program (UML)    
![alt text](Diagrams/classDiagram.png "Class Diagram")  



## CRC card of the program    
![alt text](Diagrams/crcTranslator.png "crc diagram")  


## Requirements  
You need:  
python >= 3.6+   
