# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 23:44:01 2022

@author: Natalia
"""
'''
a. El calculo del 1er cuartil de datos, el percentil 50 por columna; 
explique qué significa en cada caso mediante Python sin uso de librerías
'''
Age=[25,35,29,30,35,23,23,35,32,42,23,19,25,20,48,15,50,25,30,10,40,50,21,18,21,16,19,22,49,28,20,23,22,21,21,12,60,55,45,35,22,23,25,30,23,32,42,23,15,15,25,22,35,19,60,23,32,42,23,15,15,15,12,29,31,29,17,19,20,32,26,29,19,54,44,23,22,55,35,21,16,33,12,28,21,18,21,16,19,23,22,60,13,23,28,50,29,19,19,60,55,25,48,25,23,34,50,25,42,32,50,38,39,30,63,25,30,55,32,30,48,49,25,40,32,35,54,55,29,48,40,32,35,54,40,22,40,55,50,18,32,17,17,25,17,14,15,15,12,37,18,21,17,25,23,12,28,40,55,25,35,21,18,21,16,19,40,32,22,49,28,12,20,23,22,21,35,54,40,21,12,60,55,50,60,55,45,35,22,13,23,17,28,50,25,30,31,23,29,17,32,42,23,19,15,33,48,15,25,22,50,35,19,60,28,50,29,30,31,23,29,17,32,42,23,19,15,29,48,15,50,25,55,20,40,28,32,17,17,25,17,19,15,32,12,37,18,21,17,25,10,12,28,40,55,25,35,21,18,21,16,19,40,32,22,49,28,12,20,23,22,21,35,54,40,21,12,60,55,50,60,55,45,35,22,13,23,17,26,50,19,30,31,23,29,17,32,42,23,19,15,40,48,15,25,22,12,35,19,60,55,35,51,62,25,21,22,55,54,35,43,12,65,60,25,22,66,56,35,43,35,44,23,22,55,35,21,45,70,65,55,45,22,16,12,37,18,21,17,25,33,12,28,40,55,25,35,21,18,21,16,19,40,32,23,22,21,35,54,40,21,12,60,55,50,60,55,45,35,22,13,23,17,28,50,19,30,31,23,29,17,32,42,23,19,15,20,48,15,25,22,12,35,19,60,55,25,22,12,35,19,60,55,50,27,60,55,60,12,17,60,22,36,22,25,35,40,27,36,22,25,35,40,27,27,65,35,29,30,35,23,23,35,32,43,23,19,15,30,48,15,48,25,29,32,35,23,23,34,32,42,23,19,15,20,48,15,50,25,30,31,42,18,32,17,19,15,19,48,15,25,22,50,35,19,60,38,50,39,30,31,23,29,17,32,42,23,19,15,16,48,15,63,25,30,17,55,18,32,17,17,25,17,19,15,60,18,50,19,30,31,23,29,17,32,42,42,19,15,23,48,15,49,25,30,16,16,19,40,32,22,49,28,12,20,23,22,21,35,54,40,21,12,60,55,50,60,55,45,35,22,13,23,17,28,59,29,23,31,23,29,17,32,42,23,19,15,20,48,15,24,16,19,40,32,22,49,28,12,20,23,22,21,35,54,40,21,22,40,55,50,60,40,55,50,41,55,45,35,22,13,23,17,27,50,34,32,31,23,29,17,32,42,23,19,15,20,48,15,24,22,50,35,19,30,28,50,35,29,19,46,28,50,39,25,31,23,29,17,32,42,23,19,15,34,48,15,27,25,36,30,15,40,15,21,15,21,15,15,15,10,15,15,12,15,35,29,30,23,35,42,50,25,40,32,14,37,17,40,40,20,15,24,19,31,23,23,19,15,34,15,15,21,15,12,21,23,32,19,20,48,30,18,17,17,25,17,13,31,29,19,28,50,29,31,29,17,19,20,19,20,48,30,18,17,17,25,17,13,31,29,19,28,50,29,31,29,17,19,20,32,26,29,19,54,44,23,22,55,35,21,16,33,12,28,21,18,21,16,19,23,22,60,13,23,28,50,29,19,19,60,55,25,12,35,19,60,50,27,55,12,60,25,22,30,35,23,43,19,30,32,23,42,19,31,19,25,31,23,29,48,18,18,29,23,15,30,40,60,50,28,31,23,29,22,49,28,12,20,23,22,21,60,50,17,29,19,19,30,28,50,39,29,17,32,42,36,30,15,10,12,12,23,32,19,20,48,30,18,17,17,25,17,13,31,29,19,28,50,29,31,29,17,19,20,32,27,27,32,23,15,15,29,35,32,23,15,20,48,15,30,18,17,15,19,48,15,22,35,19,60,50,17,32,42,23,19,15,16,15,17,17,17,25,17,19,15,60,50,19,31,23,17,32,42,42,19,15,16,16,19,22,49,28,12,20,23,22,21,21,12,60,55,45,35,22,13,23,17,59,23,17,32,42,25,40,32,14,37,17,40,40,32,12,35,54,40,60,55,50,17,28,50,17,33,48,50,30,29,48,50,25,55,40,28,32,17,17,25,17,19,37,17,25,40,32,12,35,54,40,12,60,55,50,13,17,17,40,48,22,55,35,43,32]
SystolicBP=[130,140,90,140,120,140,130,85,120,130,90,120,110,120,120,120,140,140,120,70,140,140,90,90,120,100,120,100,120,90,100,100,120,120,75,95,120,100,120,100,120,120,90,120,120,120,120,90,76,120,120,100,100,120,90,120,120,120,90,76,120,80,95,90,120,130,85,120,110,120,85,130,120,130,120,130,85,120,120,90,90,115,95,120,90,90,120,100,120,100,120,120,90,120,115,120,130,120,120,90,120,120,140,140,140,85,140,140,140,140,140,135,90,140,140,140,120,140,140,140,120,140,140,160,140,140,140,140,120,120,160,140,140,140,120,90,120,140,130,120,140,90,90,120,120,90,80,100,95,120,100,100,110,120,85,95,120,120,129,100,120,90,90,120,100,120,160,140,100,120,90,90,100,100,120,120,140,140,120,75,95,120,140,130,120,100,120,100,120,90,120,90,83,120,90,120,120,120,130,85,120,120,90,120,76,120,120,120,120,100,140,100,120,90,85,140,90,140,120,120,130,85,120,120,90,120,76,120,120,120,140,140,140,110,140,120,140,90,90,120,120,90,80,120,95,120,100,100,110,120,85,95,120,120,110,100,120,90,90,120,100,120,160,140,100,120,90,90,100,100,120,120,140,140,120,75,90,120,140,130,120,100,120,100,120,90,120,90,85,120,90,120,120,120,130,85,120,120,90,120,75,120,120,120,120,100,120,100,120,90,120,90,85,120,90,120,120,120,130,85,120,120,90,120,120,90,85,120,90,120,120,120,130,85,120,120,90,120,85,120,120,90,120,90,95,120,100,100,110,120,115,95,120,120,110,100,120,90,90,120,100,120,160,140,100,120,120,140,140,120,75,90,120,140,130,120,100,120,100,120,90,120,90,115,120,90,120,120,120,130,85,120,120,90,120,76,120,120,120,120,100,120,100,120,90,120,120,100,120,100,120,90,120,130,120,140,100,140,120,140,120,100,140,90,120,100,140,120,140,90,120,100,140,120,120,130,140,90,120,120,140,130,85,120,130,99,120,76,120,120,120,140,140,100,120,120,140,130,85,120,130,90,120,76,120,120,120,140,140,120,110,140,120,140,90,120,76,120,120,120,120,100,140,100,120,90,135,120,90,140,120,120,130,85,120,120,90,120,76,120,120,120,140,140,120,70,140,120,140,90,90,120,120,90,80,90,85,120,90,140,120,120,130,85,120,120,90,120,78,120,120,120,140,140,120,70,100,120,160,140,100,120,90,90,100,100,120,120,140,140,120,75,90,120,140,130,120,100,120,100,120,90,120,90,115,120,120,120,120,120,130,85,120,120,90,120,78,120,120,120,120,100,120,160,140,100,120,90,90,100,100,120,120,140,140,120,75,90,120,140,130,120,120,140,130,120,100,120,100,120,90,120,90,135,120,110,120,120,120,130,85,120,120,90,120,76,120,120,120,120,100,140,100,120,90,85,130,140,90,120,140,95,120,110,140,120,120,130,90,120,120,90,120,76,120,120,120,140,140,120,120,70,120,90,90,90,90,90,90,90,100,100,100,100,100,140,90,140,140,85,130,140,140,140,140,90,120,110,120,160,120,120,120,120,120,120,90,120,76,120,120,90,90,100,100,100,130,120,120,120,120,120,120,90,90,120,120,90,120,130,120,85,140,90,120,130,85,120,110,120,120,120,120,120,90,90,120,120,90,120,130,120,85,140,90,120,130,85,120,110,120,85,130,120,130,120,130,85,120,120,90,90,115,95,120,90,90,120,100,120,100,120,120,90,120,115,120,130,120,120,90,120,120,120,100,120,90,130,120,100,120,120,120,90,120,120,130,130,120,120,120,130,130,120,110,120,120,120,120,130,120,120,85,130,120,120,120,120,120,130,115,120,120,130,100,120,90,90,100,100,120,120,120,130,90,130,120,120,90,85,120,110,130,90,120,120,120,120,70,100,100,100,130,120,120,120,120,120,120,90,90,120,120,90,120,130,120,85,140,90,120,130,85,120,110,120,120,120,120,99,76,120,100,120,120,90,76,120,120,120,120,120,90,76,120,120,120,100,100,120,90,120,85,120,120,90,120,76,120,120,70,90,90,120,120,90,80,90,120,90,120,120,85,120,120,90,120,78,70,100,120,100,120,90,90,100,100,120,120,75,90,120,100,120,100,120,90,120,90,120,120,85,120,120,140,140,140,90,120,110,120,160,140,90,140,140,120,120,140,130,90,83,120,85,120,120,140,140,120,120,140,140,140,140,120,140,90,90,120,120,90,120,110,120,160,140,90,140,140,120,90,120,140,130,90,90,85,120,120,120,120,85,120,120]
DiastolicBP=[80,90,70,85,60,80,70,60,90,80,60,80,89,75,80,80,90,100,80,50,100,80,65,60,80,70,75,65,90,60,90,85,90,80,50,60,80,65,95,70,85,90,70,80,90,90,80,60,49,80,80,65,70,85,65,90,90,80,60,49,80,60,60,70,60,70,60,80,60,65,60,70,80,70,90,70,60,90,80,60,65,65,60,90,65,60,80,70,75,85,90,85,65,90,60,80,70,80,85,65,90,80,90,100,90,60,90,100,100,100,95,60,70,100,90,100,80,100,100,100,80,90,100,100,90,100,100,95,70,80,100,90,100,100,95,60,85,95,100,80,100,60,63,90,80,65,60,65,60,90,70,85,75,90,65,60,90,90,85,90,80,65,60,80,70,75,100,90,65,90,60,60,90,85,90,80,100,100,95,50,60,85,95,100,80,65,95,70,85,65,90,65,60,80,70,80,60,90,70,60,90,80,60,80,49,75,80,80,80,65,95,70,85,65,60,80,70,100,60,90,70,60,90,80,60,80,49,75,80,80,90,100,80,60,100,80,100,60,63,90,80,65,60,65,60,90,70,85,75,90,65,60,90,90,85,90,80,65,60,80,70,75,100,90,65,90,60,60,90,85,90,80,100,100,95,50,60,85,95,100,80,65,95,70,85,65,90,65,60,80,70,80,60,80,70,60,90,80,60,80,49,75,80,80,80,65,95,70,85,65,90,65,60,80,70,80,60,90,70,60,90,80,60,80,90,65,60,80,70,80,60,90,70,60,90,80,60,80,60,90,80,60,80,65,60,90,70,85,75,90,65,60,90,90,85,90,80,65,60,80,70,75,100,90,85,90,80,100,100,95,50,60,85,95,100,80,65,95,70,85,65,90,65,60,80,70,80,60,70,70,69,90,80,60,80,49,75,80,80,80,65,95,70,85,65,90,80,65,95,70,90,65,90,80,90,90,70,80,90,100,80,65,100,60,100,60,100,70,100,60,100,60,100,70,70,80,80,70,80,60,90,70,60,90,80,60,80,49,75,80,80,90,100,70,80,60,90,70,60,90,80,60,80,49,75,80,80,90,100,80,90,100,80,100,60,80,49,75,80,80,80,65,95,70,85,65,60,80,70,100,60,90,70,60,90,80,60,80,49,75,80,80,90,100,80,50,100,80,100,60,63,90,80,65,60,65,60,80,70,100,60,90,70,60,90,80,60,80,49,75,80,80,90,100,80,50,70,75,100,90,65,90,60,60,90,85,90,80,100,100,95,50,60,85,95,100,80,65,95,70,85,65,90,65,60,80,70,80,60,80,70,60,90,80,60,80,49,75,80,80,80,70,76,100,90,65,90,60,60,90,85,90,80,100,100,95,50,60,85,95,100,80,85,95,100,80,65,95,70,85,65,90,65,60,80,70,80,60,90,70,60,90,80,60,80,49,76,80,80,80,65,95,70,85,65,60,80,90,70,60,100,60,80,70,100,60,85,70,60,90,90,60,80,68,75,80,80,90,100,90,80,50,95,60,50,49,50,49,49,49,50,49,49,50,60,90,70,85,80,60,80,90,100,100,100,65,90,75,90,100,76,80,80,60,60,85,60,80,68,75,80,60,50,49,50,50,70,90,80,75,80,80,80,60,63,90,80,65,60,70,80,60,80,70,60,70,60,80,60,80,75,80,80,80,60,63,90,80,65,60,70,80,60,80,70,60,70,60,80,60,65,60,70,80,70,90,70,60,90,80,60,65,65,60,90,65,60,80,70,75,85,90,85,65,90,60,80,70,80,85,65,90,80,95,70,90,65,80,90,70,90,80,100,60,80,60,70,80,80,75,80,70,80,80,90,80,80,60,90,70,80,80,60,70,75,80,80,95,85,100,60,60,80,70,65,90,60,60,90,85,90,80,80,100,65,70,80,85,65,60,80,70,70,60,90,90,90,80,50,50,50,50,70,90,80,75,80,80,80,60,63,90,80,65,60,70,80,60,80,70,60,70,60,80,60,65,70,70,90,60,49,80,70,60,90,60,49,75,80,80,80,80,60,49,75,80,80,65,70,85,65,80,60,90,80,60,80,49,75,80,50,60,63,90,80,65,60,65,80,70,60,90,60,90,80,60,80,49,50,70,75,65,90,60,60,90,85,90,80,50,60,80,65,95,70,85,65,90,65,80,80,60,90,80,100,100,100,65,90,75,90,100,90,60,100,100,95,85,95,100,65,60,80,60,75,80,95,100,75,80,90,100,80,100,80,100,60,63,90,80,65,90,75,90,100,90,60,100,100,95,60,85,95,100,65,65,60,75,80,60,90,60,90,65]
BS=[15,13,8,7,6.1,7.01,7.01,11,6.9,18,7.01,7,7.01,7.01,11,7.01,15,7.01,6.9,6.9,18,6.7,7.5,7.5,7.5,7.2,7.2,7.2,7.2,7.2,7.1,7.1,7.1,7.1,6.1,6.1,6.1,6.1,6.1,6.1,6.1,6.1,6.1,6.1,6.1,7.5,7.5,7.5,7.5,7,7,7,7,7,7,6.7,6.4,6.4,6.4,6.4,7.2,7,7.2,6.7,6.1,6.7,9,7,7,6,6,7.7,7,12,16,6.9,6.9,12,6.9,6.9,6.9,7,6.9,6.9,6.9,6.9,6.9,6.9,6.9,6.9,7.8,15,7.8,7.8,7.8,7.8,7.8,7,7.8,6.8,6.8,6.8,15,6.8,6.8,11,15,6.8,18,7.9,17,7.9,9,15,15,7.9,7.9,18,7.9,15,11,15,7.5,19,18,7.5,15,19,9,11,19,18,7.5,15,11,7.5,15,19,16,6.9,6.9,6.9,6.9,6.7,6.7,7,6.7,6.7,6.7,11,6.7,6.7,12,7.5,7.5,7.5,7.5,12,7.5,7.5,7.5,7.5,7.5,7.5,7.2,7.2,19,18,7.2,7.2,7.2,7.9,7.1,7.1,7.1,7.1,8,15,11,6.1,6.1,15,19,16,6.1,6.1,6.1,6.1,6.1,7.9,6.1,6.1,8,15,6.1,6.1,6.1,6.1,6.1,9,7.5,7.5,7.5,7,7.5,10,11,7,7,7,17,7,7,7,9,6.7,6.7,15,6.1,6.7,6.7,9,6.4,6.4,6.4,7,6.4,7.2,11,7.2,15,7.2,7.2,7,18,9,8,11,8,12,7,11,7,6,7.2,11,6.8,6.9,13,15,6.9,6.9,6.9,6.9,6.9,6.9,6.9,6.9,6.9,6.9,6.9,6.9,19,18,6.9,6.9,6.9,8,7,7,7,7,9,15,11,7.7,11,15,19,16,7.7,7.7,7.7,7.7,7.7,9,7.7,7.7,6,7.7,7.7,7.7,6.1,7.7,7.7,6.3,7.7,7.7,7.7,7,7.7,7.7,11,7.7,7.7,6.9,6.9,6.9,6.9,6.9,6.9,6.9,6.9,6.9,6.9,6.9,15,18,12,19,18,6.9,6.9,6.9,6.9,6.9,6.9,13,6.9,15,6.9,16,6.9,6.9,12,6.9,6.9,6.9,6.9,6.9,6.9,18,6.9,6.9,6.9,11,6.9,6.9,6.9,6.9,7,6.9,6.9,6.9,6.9,6.9,6.9,6.9,6.9,6.9,6.9,6.9,19,18,6.9,7.8,7.8,7.8,15,11,7.8,7.8,15,19,16,7.8,7.8,7.8,7.8,7.8,7.8,7.8,7.8,7.8,7.8,7.8,7.8,6.1,7.8,7.8,7.8,7.8,7.8,7.8,7,7.8,7.8,11,7.8,7.8,7.8,7.8,7.8,7.8,6.8,6.8,6.8,6.8,6.8,6.8,6.8,6.8,6.8,16,6.8,12,6.8,16,6.8,6.8,6.8,6.8,6.8,6.8,6.8,15,13,6.8,6.8,6.8,6.8,15,13,6.8,6.8,15,13,10,6.8,6.1,6.8,6.8,11,6.8,18,6.8,7,6.8,6.8,11,6.8,15,6.8,6.8,6.8,6.1,6.8,6.8,11,6.8,18,6.8,7,6.8,6.8,11,6.8,15,6.8,6.8,6.8,18,6.8,7.9,7.9,7,7.9,7.9,11,7.9,7.9,7.9,17,7.9,7.9,7.9,7.9,7.9,9,15,6.1,7.9,7.9,7.9,7.9,7.9,7.9,7,7.9,7.9,11,7.9,15,7.9,7.9,7.9,18,7.9,7.9,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,15,6.1,7.5,7.5,7.5,7.5,7.5,7.5,7,7.5,8,11,7.5,15,7.5,7.5,7.5,7.5,7.5,19,18,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,15,11,7.5,7.5,15,19,16,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,9,7.5,6.1,7.5,7.5,7.5,7.5,7.5,7.5,7,7.5,7.5,11,7.5,7.5,7.5,7.5,19,18,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,15,11,7.5,7.5,15,19,16,7.5,15,19,16,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,15,7,7.5,6.1,7.5,7.5,7.5,7.5,7.5,7.5,7,7.5,7.5,11,7.5,7.5,12,17,11,9,8,9,15,13,11,7,12,10,7,7.9,15,6.1,8,8,9,7,9,6.7,7,7,8,11,6.6,15,12,7,9,6,7,6,6.9,6,6.5,6,6.7,6,6,6.8,6,6.4,6,13,8,7,7.01,11,18,15,7.01,18,6.9,7,11,12,12,19,7.5,7.5,7.5,7,6.1,8,6.7,7,7,8,6.6,6,6.9,7.6,6,6.8,7.01,6.9,7,7.01,11,6.9,6.9,6.9,6.9,6.7,6.7,7.9,6.1,6.1,7,9,6.7,6.7,6.1,6.7,9,7,7,7,7.01,11,6.9,6.9,6.9,6.9,6.7,6.7,7.9,6.1,6.1,7,9,6.7,6.7,6.1,6.7,9,7,7,6,6,7.7,7,12,16,6.9,6.9,12,6.9,6.9,6.9,7,6.9,6.9,6.9,6.9,6.9,6.9,6.9,6.9,7.8,15,7.8,7.8,7.8,7.8,7.8,7,7.8,6.8,6.8,6.8,6.8,6.8,6.8,6.8,16,6.8,6.8,6.8,6.8,6.8,6.8,6.8,6.1,6.8,18,7,6.8,6.8,6.8,18,7,6.8,7,7.9,6.1,7.9,7.9,11,7.9,7.5,7.5,8,7.5,7.5,11,15,16,7.5,6.1,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,16,7.5,7.5,7,9,8,9,7,7.9,8,9,7,9,7,9,6,6,6.4,6,7.01,6.9,7,7.01,11,6.9,6.9,6.9,6.9,6.7,6.7,7.9,6.1,6.1,7,9,6.7,6.7,6.1,6.7,9,7,7,6,6.8,6.8,6.8,6.8,6.8,6.8,6.8,6.1,6.8,6.8,6.8,6.8,11,6.8,6.8,6.8,7.9,7.9,7.9,11,7.9,7.9,7.9,7.9,7.9,7.9,7.9,7.9,7.9,7.9,7,7.9,7.9,7.9,7.9,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,6.1,7.5,7.5,7.5,7.5,7.5,7,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.01,18,6.9,7,11,12,12,19,18,7.9,8,15,11,15,19,16,6.1,8,15,9,10,11,17,15,7.2,11,15,7.2,7.2,18,9,8,11,8,12,7,11,11,13,15,19,18,8,9,15,11,11,15,19,16,9,7.7,6.3,7.7,11,15,18,19,18,6]
BodyTemp=[98,98,100,98,98,98,98,102,98,98,98,98,98,100,98,98,98,98,101,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,102,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,102,98,100,101,101,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,101,98,101,98,98,98,98,98,98,98,98,98,98,102,98,98,98,98,98,101,98,98,98,98,101,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,102,98,98,98,102,98,101,101,101,102,101,98,98,98,98,98,98,101,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,102,98,98,98,98,98,98,98,98,102,98,98,98,98,98,98,98,98,101,98,103,101,98,98,98,98,98,98,102,98,98,98,98,98,98,98,98,98,98,98,98,98,98,101,98,98,98,98,98,98,102,98,98,98,98,98,100,98,98,98,98,101,100,98,102,98,101,101,101,102,101,98,101,98,98,98,98,101,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,102,98,98,98,98,98,98,98,98,102,98,98,98,98,98,98,98,98,101,98,103,101,98,98,98,98,98,98,102,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,103,102,103,102,101,103,98,98,98,98,98,101,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,102,98,98,98,98,98,98,98,98,101,98,103,101,98,98,98,98,98,98,102,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,102,102,98,101,98,98,103,98,98,102,98,98,98,101,98,102,98,98,98,101,98,98,98,98,98,98,98,98,98,102,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,102,98,98,98,98,98,98,98,98,98,98,101,100,98,102,98,101,98,98,98,98,98,98,98,98,98,98,98,101,98,98,98,98,98,98,102,98,98,98,98,98,98,98,98,98,98,101,98,98,102,98,101,101,101,102,101,98,98,101,98,98,98,98,98,98,102,98,98,98,98,98,98,98,98,98,98,101,100,98,98,98,98,98,98,98,102,98,98,98,98,98,98,98,98,102,98,98,98,98,98,98,98,98,101,98,103,101,98,98,98,98,98,98,102,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,102,98,98,98,98,98,98,98,98,102,98,98,98,98,98,98,98,98,98,98,98,98,101,98,103,101,98,98,98,98,98,98,101,98,98,98,98,98,98,98,98,98,98,98,98,98,98,101,98,98,100,98.4,99,101,98,98,98.6,98,98,98,102,100,98,98,98,98,98,98,99,98,99,98,101,98,98,98,98,98,98,98,99,99,99,99,99,98,98,98,100,98,98,102,98,98,98,98,98,101,98,101,98,98,98,98,98,98.4,98,98,98,98,98,98,99,98,98,98,98,98,98,98,98,100,98,101,102,101,101,101,102,101,98,98,98,101,98,98,98,98,102,98,100,98,100,98,101,102,101,101,101,102,101,98,98,98,101,98,98,98,98,102,98,100,101,101,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,101,98,101,98,98,98,98,98,98,98,98,98,98,98,102,102,101,98,98,98,98,98,98,98,98,98,98,98,98,98,98,100,98,98,98,98,98,98,102,101,98,98,98,101,98,98,98,101,98,98,98,98,98,98,102,98,98,98,98,98,98,103,98,98,98,98,101,98,98,98,102,100,98,98,101,98,99,98,98,98,98,98,100,98,101,102,101,101,101,102,101,98,98,98,101,98,98,98,98,102,98,100,101,98,98,98,98,98,98,98,98,98,98,98,98,98,98,101,102,101,98,98,98,98,98,98,98,98,98,102,98,98,98,98,98,98,98,98,101,101,101,102,101,98,98,98,98,98,98,102,98,98,98,98,98,100,98,98,98,98,98,102,98,98,98,98,98,102,98,98,98,98,98,101,98,103,98,98,102,98,98,98,98,98,101,98,101,98,98,98,102,98,98,98,98,98,98,103,101,98,102,98,98,98,98,100,98,98,98,101,98,102,98,101,101,101,102,101,98,101,98,98,98,102,98,98,98,102,98,98,98,101,103,102,98,98,98,98,98,98,101]
HeartRate=[86,70,80,70,76,70,78,86,70,70,76,70,77,70,88,70,90,80,76,70,90,70,76,70,76,80,66,70,77,82,88,66,82,77,70,60,75,66,66,66,88,60,80,70,70,70,70,76,77,70,66,80,60,60,77,70,70,70,76,77,70,80,77,80,76,78,86,70,70,76,86,78,70,67,80,70,76,70,78,86,76,70,65,70,76,70,76,80,66,66,82,60,80,60,86,70,78,70,60,77,66,66,90,80,70,86,90,80,90,78,60,86,80,70,90,80,76,90,78,70,88,90,80,77,88,66,66,77,80,88,77,88,66,66,80,60,60,77,75,76,78,76,70,80,76,70,80,76,77,88,76,70,76,80,70,65,70,80,88,76,80,76,70,76,80,66,77,88,70,77,82,66,88,66,82,77,66,66,80,70,60,60,77,75,75,66,66,66,88,80,60,67,86,70,80,70,76,70,78,86,70,70,76,70,77,70,88,70,66,80,60,60,60,77,86,70,80,70,76,70,78,86,70,70,76,70,77,70,88,70,77,80,76,70,77,76,70,78,70,80,76,70,80,76,77,88,76,70,76,80,70,65,70,80,88,76,80,76,70,76,80,66,77,88,70,77,82,66,88,66,82,77,66,66,80,60,60,60,77,76,75,66,66,66,88,80,60,67,86,70,80,70,76,70,78,86,70,70,76,70,77,70,88,70,66,80,60,60,60,77,76,75,66,66,66,88,80,60,67,86,70,80,70,76,70,78,86,70,70,76,70,80,70,76,70,78,86,70,70,76,80,70,76,76,77,88,76,70,76,80,70,65,70,80,88,76,80,76,70,76,80,66,77,88,66,82,77,66,66,80,60,60,60,77,75,75,66,66,66,88,80,60,67,86,70,80,70,76,70,78,86,70,70,76,70,77,70,88,70,66,80,60,60,60,77,66,66,88,60,60,60,77,78,76,68,77,80,66,80,80,77,88,76,77,60,80,66,77,76,77,60,80,66,77,77,86,70,80,70,76,70,78,86,70,70,76,70,77,70,88,70,90,80,80,70,76,70,78,86,70,70,76,70,77,70,88,70,90,80,76,70,90,76,78,76,70,77,70,88,70,66,80,60,60,60,77,86,70,80,70,76,70,78,86,70,70,76,70,77,7,88,70,90,80,76,70,90,76,78,76,70,80,76,70,80,77,86,70,80,70,76,70,78,86,70,70,76,70,77,70,88,70,90,80,76,70,80,66,77,88,70,77,82,66,88,66,82,77,66,66,80,60,60,60,77,75,75,66,66,66,88,80,60,67,86,70,80,70,76,70,78,86,70,70,76,70,77,70,88,70,66,80,66,77,88,70,77,82,66,88,66,82,77,66,66,80,60,60,60,77,75,75,60,77,75,75,66,66,66,88,80,60,67,86,70,80,70,76,70,78,86,70,70,76,70,77,70,88,70,66,80,60,60,60,77,86,86,70,80,70,90,86,70,80,70,76,70,78,86,70,70,76,70,77,70,88,70,90,80,82,76,70,70,80,60,77,60,77,77,77,70,77,77,70,80,70,80,70,70,86,70,90,80,90,78,70,88,76,80,77,70,70,66,70,76,70,76,70,77,70,70,80,60,77,70,60,78,70,70,70,88,76,76,76,70,80,76,80,76,78,70,86,70,80,76,78,86,70,70,70,70,88,76,76,76,70,80,76,80,76,78,70,86,70,80,76,78,86,70,70,76,86,78,70,67,80,70,76,70,78,86,76,70,65,70,76,70,76,80,66,66,82,60,80,60,86,70,78,70,60,77,66,66,60,60,60,77,76,68,80,80,77,60,77,70,76,78,70,70,70,70,78,70,70,70,70,66,76,70,78,88,76,86,78,70,70,76,80,60,75,86,76,70,78,70,77,82,66,88,66,82,77,75,75,67,78,70,60,77,86,70,80,78,86,70,70,82,76,70,70,70,70,78,70,70,70,88,76,76,76,70,80,76,80,76,78,70,86,70,80,76,78,86,70,70,76,77,77,70,76,77,70,80,76,70,76,77,70,88,70,76,76,76,77,70,88,70,80,60,60,77,70,86,70,70,76,70,77,7,70,70,76,70,80,76,70,80,77,70,80,76,70,86,70,70,76,70,77,70,80,66,70,77,82,66,88,66,82,77,60,60,75,66,66,66,88,80,60,67,70,70,86,70,70,80,90,78,70,88,76,80,77,88,66,66,66,80,60,77,75,67,86,70,86,70,88,60,70,70,88,77,80,76,77,76,70,78,70,80,76,70,88,76,80,77,88,66,66,66,80,60,60,77,76,80,67,86,70,88,80,60,86,70,76]

def burbuja(A):
    for i in range(1,len(A)):
        for j in range(0,len(A)-i):
            if(A[j+1] < A[j]):
                aux=A[j]
                A[j]=A[j+1]
                A[j+1]=aux
    return A
print("1er cuartil:")
cuartil = round((len(Age)-1)/4)
print(burbuja(Age)[cuartil])
print(burbuja(SystolicBP)[cuartil])
print(burbuja(DiastolicBP)[cuartil])
print(burbuja(BS)[cuartil])
print(burbuja(BodyTemp)[cuartil])
print(burbuja(HeartRate)[cuartil])

print("Percentil 50:")
percentil = round((50/100)*(len(Age)-1))
print(burbuja(Age)[percentil])
print(burbuja(SystolicBP)[percentil])
print(burbuja(DiastolicBP)[percentil])
print(burbuja(BS)[percentil])
print(burbuja(BodyTemp)[percentil])
print(burbuja(HeartRate)[percentil])

'''
b. Realice lo mismo del inciso (a) con el uso de numpy y pandas
'''
import numpy as np
import pandas as pd
datos = pd.read_csv("Maternal Health Risk Data Set.csv")
#print(datos)

print("1er cuartil:")
print(np.quantile(datos["Age"], .25))
print(np.quantile(datos["SystolicBP"], .25))
print(np.quantile(datos["DiastolicBP"], .25))
print(np.quantile(datos["BS"], .25))
print(np.quantile(datos["BodyTemp"], .25))
print(np.quantile(datos["HeartRate"], .25))


print("Percentil 50:")
print(np.percentile(datos["Age"],50))
print(np.percentile(datos["SystolicBP"],50))
print(np.percentile(datos["DiastolicBP"],50))
print(np.percentile(datos["BS"],50))
print(np.percentile(datos["BodyTemp"],50))
print(np.percentile(datos["HeartRate"],50))

print(datos.columns)
print(pd.unique(datos['Class']))

import matplotlib.pyplot as plt
colors = {"high risk":"Crimson","mid risk":"RoyalBlue","low risk":"DarkSeaGreen"}
class_color = datos.Class.map(colors)
figure, ax = plt.subplots(6, 6)

ax[0, 0].text(0.40,0.55,'Age', fontsize=20, color='black')
ax[1, 0].scatter(datos.Age,datos.SystolicBP,color=class_color)
ax[2, 0].scatter(datos.Age,datos.DiastolicBP,color=class_color)
ax[3, 0].scatter(datos.Age,datos.BS,color=class_color)
ax[4, 0].scatter(datos.Age,datos.BodyTemp,color=class_color)
ax[5, 0].scatter(datos.Age,datos.HeartRate,color=class_color)

ax[1, 1].text(0.20,0.55,'SystolicBP', fontsize=20, color='black')
ax[0, 1].scatter(datos.SystolicBP,datos.Age,color=class_color)
ax[2, 1].scatter(datos.SystolicBP,datos.DiastolicBP,color=class_color)
ax[3, 1].scatter(datos.SystolicBP,datos.BS,color=class_color)
ax[4, 1].scatter(datos.SystolicBP,datos.BodyTemp,color=class_color)
ax[5, 1].scatter(datos.SystolicBP,datos.HeartRate,color=class_color)

ax[2, 2].text(0.15,0.55,'DiastolicBP', fontsize=20, color='black')
ax[0, 2].scatter(datos.DiastolicBP,datos.Age,color=class_color)
ax[1, 2].scatter(datos.DiastolicBP,datos.SystolicBP,color=class_color)
ax[3, 2].scatter(datos.DiastolicBP,datos.BS,color=class_color)
ax[4, 2].scatter(datos.DiastolicBP,datos.BodyTemp,color=class_color)
ax[5, 2].scatter(datos.DiastolicBP,datos.HeartRate,color=class_color)

ax[3, 3].text(0.40,0.55,'BS', fontsize=20, color='black')
ax[0, 3].scatter(datos.BS,datos.Age,color=class_color)
ax[1, 3].scatter(datos.BS,datos.SystolicBP,color=class_color)
ax[2, 3].scatter(datos.BS,datos.DiastolicBP,color=class_color)
ax[4, 3].scatter(datos.BS,datos.BodyTemp,color=class_color)
ax[5, 3].scatter(datos.BS,datos.HeartRate,color=class_color)

ax[4, 4].text(0.20,0.55,'BodyTemp', fontsize=20, color='black')
ax[0, 4].scatter(datos.BodyTemp,datos.Age,color=class_color)
ax[1, 4].scatter(datos.BodyTemp,datos.SystolicBP,color=class_color)
ax[2, 4].scatter(datos.BodyTemp,datos.DiastolicBP,color=class_color)
ax[3, 4].scatter(datos.BodyTemp,datos.BS,color=class_color)
ax[5, 4].scatter(datos.BodyTemp,datos.HeartRate,color=class_color)

ax[5, 5].text(0.20,0.55,'HeartRate', fontsize=20, color='black')
ax[0, 5].scatter(datos.HeartRate,datos.Age,color=class_color)
ax[1, 5].scatter(datos.HeartRate,datos.SystolicBP,color=class_color)
ax[2, 5].scatter(datos.HeartRate,datos.DiastolicBP,color=class_color)
ax[3, 5].scatter(datos.HeartRate,datos.BS,color=class_color)
ax[4, 5].scatter(datos.HeartRate,datos.BodyTemp,color=class_color)


figure.set_size_inches(20,15)
plt.show()
























