# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:23:55 2020

@author: k_sha
"""

#sometimes working with a long input string to the command line can be tedious
#its best to run using the OS package. 

#this script automates the creation of a docker container from an image 


import os

wd = "C:/GitLocal/random_stuff" #replace with your directory...

os.chdir(wd)

text = 'docker run -d -v "/${PWD}:/workspace" -p 8080:8080 --name "ml-workspace" --env AUTHENTICATE_VIA_JUPYTER="mytoken" --shm-size 2g --restart always dagshub/ml-workspace:latest'

#run the command above
os.system(text)
