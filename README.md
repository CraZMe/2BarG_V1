# 2BarG
 
 The Dynamic Fracture Laboratory, Faculty of Mechanical Engineering, Technion Israel Institue of Technology, 2022.
 
 Developed by Tzvi Gershanik, Itay Levin and Prof. Daniel Rittel.
 
2BarG is a program that analyses Split Hopkinson (Kolsky) Pressure Bar experiments. It is Python-based and features several libraries that make processing fast, simple, and efficient with minimal operator’s intervention. The program performs automatic identification of the incident, reflected and transmitted signals from the recorded experimental raw signals. The software reduces the data into stresses, strains, and velocities following the mandatory wave dispersion correction. A user-friendly and intuitive graphic interface allows for straightforward data reduction for various experimental specimens (standard or customized) and testing configurations (tension, compression, and shear). 
 
# General Info & Required Libraries
2BarG was developed in Python, using the Kivymd GUI. The following libraries **must** be installed for full operation of the software:

* Kivy
* Kivymd
* Numpy
* Pandas
* SciPy
* Plotly
* Matplotlib
* csv
* easygui

We packaged 2BarG using PyInstaller, and a zipped file with an excecutable of the current version can be found at https://rittel.group/downloads/.
