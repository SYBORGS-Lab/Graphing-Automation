# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 14:59:03 2020

@author: jacob
"""

import tkinter as tk
from tkinter import *
import numpy as np


global new_ar
new_ar = np.empty((8,12))

global arin

Y = tk.Tk()

Y.title('Well Setup') 

A1 = BooleanVar()
A2 = BooleanVar()
A3 = BooleanVar()
A4 = BooleanVar()
A5 = BooleanVar()
A6 = BooleanVar()
A7 = BooleanVar()
A8 = BooleanVar()
A9 = BooleanVar()
A10 = BooleanVar()
A11 = BooleanVar()
A12 = BooleanVar()

B1 = BooleanVar()
B2 =BooleanVar()
B3 = BooleanVar()
B4 = BooleanVar()
B5 = BooleanVar()
B6 = BooleanVar()
B7 = BooleanVar()
B8 = BooleanVar()
B9 = BooleanVar()
B10 = BooleanVar()
B11 = BooleanVar()
B12 = BooleanVar()

C1 = BooleanVar()
C2 = BooleanVar()
C3 = BooleanVar()
C4 = BooleanVar()
C5 = BooleanVar()
C6 = BooleanVar()
C7 = BooleanVar()
C8 = BooleanVar()
C9 = BooleanVar()
C10 = BooleanVar()
C11 = BooleanVar()
C12 = BooleanVar()

D1 = BooleanVar()
D2 = BooleanVar()
D3 = BooleanVar()
D4 = BooleanVar()
D5 = BooleanVar()
D6 = BooleanVar()
D7 = BooleanVar()
D8 = BooleanVar()
D9 = BooleanVar()
D10 = BooleanVar()
D11 = BooleanVar()
D12 = BooleanVar()

E1 = BooleanVar()
E2 = BooleanVar()
E3 = BooleanVar()
E4 = BooleanVar()
E5 = BooleanVar()
E6 = BooleanVar()
E7 = BooleanVar()
E8 = BooleanVar()
E9 = BooleanVar()
E10 = BooleanVar()
E11 = BooleanVar()
E12 = BooleanVar()

F1 = BooleanVar()
F2 = BooleanVar()
F3 = BooleanVar()
F4 = BooleanVar()
F5 = BooleanVar()
F6 = BooleanVar()
F7 = BooleanVar()
F8 = BooleanVar()
F9 = BooleanVar()
F10 = BooleanVar()
F11 = BooleanVar()
F12 = BooleanVar()

F1 = BooleanVar()
F2 = BooleanVar()
F3 = BooleanVar()
F4 = BooleanVar()
F5 = BooleanVar()
F6 = BooleanVar()
F7 = BooleanVar()
F8 = BooleanVar()
F9 = BooleanVar()
F10 = BooleanVar()
F11 = BooleanVar()
F12 = BooleanVar()

G1 = BooleanVar()
G2 = BooleanVar()
G3 = BooleanVar()
G4 = BooleanVar()
G5 = BooleanVar()
G6 = BooleanVar()
G7 = BooleanVar()
G8 = BooleanVar()
G9 = BooleanVar()
G10 = BooleanVar()
G11 = BooleanVar()
G12 = BooleanVar()

H1 = BooleanVar()
H2 = BooleanVar()
H3 = BooleanVar()
H4 = BooleanVar()
H5 = BooleanVar()
H6 = BooleanVar()
H7 = BooleanVar()
H8 = BooleanVar()
H9 = BooleanVar()
H10 = BooleanVar()
H11 = BooleanVar()
H12 = BooleanVar()



def ALL():
    A1.set(1)
    A2.set(1)
    A3.set(1)
    A4.set(1)
    A5.set(1)
    A6.set(1)
    A7.set(1)
    A8.set(1)
    A9.set(1)
    A10.set(1)
    A11.set(1)
    A12.set(1)
    
    B1.set(1)
    B2.set(1)
    B3.set(1)
    B4.set(1)
    B5.set(1)
    B6.set(1)
    B7.set(1)
    B8.set(1)
    B9.set(1)
    B10.set(1)
    B11.set(1)
    B12.set(1)

    C1.set(1)
    C2.set(1)
    C3.set(1)
    C4.set(1)
    C5.set(1)
    C6.set(1)
    C7.set(1)
    C8.set(1)
    C9.set(1)
    C10.set(1)
    C11.set(1)
    C12.set(1)

    D1.set(1)
    D2.set(1)
    D3.set(1)
    D4.set(1)
    D5.set(1)
    D6.set(1)
    D7.set(1)
    D8.set(1)
    D9.set(1)
    D10.set(1)
    D11.set(1)
    D12.set(1)
    
    E1.set(1)
    E2.set(1)
    E3.set(1)
    E4.set(1)
    E5.set(1)
    E6.set(1)
    E7.set(1)
    E8.set(1)
    E9.set(1)
    E10.set(1)
    E11.set(1)
    E12.set(1)
    
    F1.set(1)
    F2.set(1)
    F3.set(1)
    F4.set(1)
    F5.set(1)
    F6.set(1)
    F7.set(1)
    F8.set(1)
    F9.set(1)
    F10.set(1)
    F11.set(1)
    F12.set(1)
    
    G1.set(1)
    G2.set(1)
    G3.set(1)
    G4.set(1)
    G5.set(1)
    G6.set(1)
    G7.set(1)
    G8.set(1)
    G9.set(1)
    G10.set(1)
    G11.set(1)
    G12.set(1)
    
    H1.set(1)
    H2.set(1)
    H3.set(1)
    H4.set(1)
    H5.set(1)
    H6.set(1)
    H7.set(1)
    H8.set(1)
    H9.set(1)
    H10.set(1)
    H11.set(1)
    H12.set(1)


Button(Y, text='ALL', command=ALL).grid(row=0, column = 0)



Checkbutton(Y, text='A1', variable=A1).grid(row=1, column = 1) 
Checkbutton(Y, text='A2', variable=A2).grid(row=2, column = 1) 
Checkbutton(Y, text='A3', variable=A3).grid(row=3, column = 1) 
Checkbutton(Y, text='A4', variable=A4).grid(row=4, column = 1) 
Checkbutton(Y, text='A5', variable=A5).grid(row=5, column = 1) 
Checkbutton(Y, text='A6', variable=A6).grid(row=6, column = 1) 
Checkbutton(Y, text='A7', variable=A7).grid(row=7, column = 1) 
Checkbutton(Y, text='A8', variable=A8).grid(row=8, column = 1) 
Checkbutton(Y, text='A9', variable=A9).grid(row=9, column = 1) 
Checkbutton(Y, text='A10', variable=A10).grid(row=10, column = 1) 
Checkbutton(Y, text='A11', variable=A11).grid(row=11, column = 1) 
Checkbutton(Y, text='A12', variable=A12).grid(row=12, column = 1)

Checkbutton(Y, text='B1', variable=B1).grid(row=1, column = 2) 
Checkbutton(Y, text='B2', variable=B2).grid(row=2, column = 2) 
Checkbutton(Y, text='B3', variable=B3).grid(row=3, column = 2) 
Checkbutton(Y, text='B4', variable=B4).grid(row=4, column = 2) 
Checkbutton(Y, text='B5', variable=B5).grid(row=5, column = 2) 
Checkbutton(Y, text='B6', variable=B6).grid(row=6, column = 2) 
Checkbutton(Y, text='B7', variable=B7).grid(row=7, column = 2) 
Checkbutton(Y, text='B8', variable=B8).grid(row=8, column = 2) 
Checkbutton(Y, text='B9', variable=B9).grid(row=9, column = 2) 
Checkbutton(Y, text='B10', variable=B10).grid(row=10, column = 2) 
Checkbutton(Y, text='B11', variable=B11).grid(row=11, column = 2) 
Checkbutton(Y, text='B12', variable=B12).grid(row=12, column = 2)

Checkbutton(Y, text='C1', variable=C1).grid(row=1, column = 3) 
Checkbutton(Y, text='C2', variable=C2).grid(row=2, column = 3) 
Checkbutton(Y, text='C3', variable=C3).grid(row=3, column = 3) 
Checkbutton(Y, text='C4', variable=C4).grid(row=4, column = 3) 
Checkbutton(Y, text='C5', variable=C5).grid(row=5, column = 3) 
Checkbutton(Y, text='C6', variable=C6).grid(row=6, column = 3) 
Checkbutton(Y, text='C7', variable=C7).grid(row=7, column = 3) 
Checkbutton(Y, text='C8', variable=C8).grid(row=8, column = 3) 
Checkbutton(Y, text='C9', variable=C9).grid(row=9, column = 3) 
Checkbutton(Y, text='C10', variable=C10).grid(row=10, column = 3) 
Checkbutton(Y, text='C11', variable=C11).grid(row=11, column = 3) 
Checkbutton(Y, text='C12', variable=C12).grid(row=12, column = 3)

Checkbutton(Y, text='D1', variable=D1).grid(row=1, column = 4) 
Checkbutton(Y, text='D2', variable=D2).grid(row=2, column = 4) 
Checkbutton(Y, text='D3', variable=D3).grid(row=3, column = 4) 
Checkbutton(Y, text='D4', variable=D4).grid(row=4, column = 4) 
Checkbutton(Y, text='D5', variable=D5).grid(row=5, column = 4) 
Checkbutton(Y, text='D6', variable=D6).grid(row=6, column = 4) 
Checkbutton(Y, text='D7', variable=D7).grid(row=7, column = 4) 
Checkbutton(Y, text='D8', variable=D8).grid(row=8, column = 4) 
Checkbutton(Y, text='D9', variable=D9).grid(row=9, column = 4) 
Checkbutton(Y, text='D10', variable=D10).grid(row=10, column = 4) 
Checkbutton(Y, text='D11', variable=D11).grid(row=11, column = 4) 
Checkbutton(Y, text='D12', variable=D12).grid(row=12, column = 4)

Checkbutton(Y, text='E1', variable=E1).grid(row=1, column = 5) 
Checkbutton(Y, text='E2', variable=E2).grid(row=2, column = 5) 
Checkbutton(Y, text='E3', variable=E3).grid(row=3, column = 5) 
Checkbutton(Y, text='E4', variable=E4).grid(row=4, column = 5) 
Checkbutton(Y, text='E5', variable=E5).grid(row=5, column = 5) 
Checkbutton(Y, text='E6', variable=E6).grid(row=6, column = 5) 
Checkbutton(Y, text='E7', variable=E7).grid(row=7, column = 5) 
Checkbutton(Y, text='E8', variable=E8).grid(row=8, column = 5) 
Checkbutton(Y, text='E9', variable=E9).grid(row=9, column = 5) 
Checkbutton(Y, text='E10', variable=E10).grid(row=10, column = 5) 
Checkbutton(Y, text='E11', variable=E11).grid(row=11, column = 5)
Checkbutton(Y, text='E12', variable=E12).grid(row=12, column = 5)

Checkbutton(Y, text='F1', variable=F1).grid(row=1, column = 6)
Checkbutton(Y, text='F2', variable=F2).grid(row=2, column = 6)
Checkbutton(Y, text='F3', variable=F3).grid(row=3, column = 6)
Checkbutton(Y, text='F4', variable=F4).grid(row=4, column = 6) 
Checkbutton(Y, text='F5', variable=F5).grid(row=5, column = 6)
Checkbutton(Y, text='F6', variable=F6).grid(row=6, column = 6)
Checkbutton(Y, text='F7', variable=F7).grid(row=7, column = 6) 
Checkbutton(Y, text='F8', variable=F8).grid(row=8, column = 6)
Checkbutton(Y, text='F9', variable=F9).grid(row=9, column = 6) 
Checkbutton(Y, text='F10', variable=F10).grid(row=10, column = 6) 
Checkbutton(Y, text='F11', variable=F11).grid(row=11, column = 6)
Checkbutton(Y, text='F12', variable=F12).grid(row=12, column = 6)

Checkbutton(Y, text='G1', variable=G1).grid(row=1, column = 7)
Checkbutton(Y, text='G2', variable=G2).grid(row=2, column = 7)
Checkbutton(Y, text='G3', variable=G3).grid(row=3, column = 7)
Checkbutton(Y, text='G4', variable=G4).grid(row=4, column = 7)
Checkbutton(Y, text='G5', variable=G5).grid(row=5, column = 7)
Checkbutton(Y, text='G6', variable=G6).grid(row=6, column = 7)
Checkbutton(Y, text='G7', variable=G7).grid(row=7, column = 7)
Checkbutton(Y, text='G8', variable=G8).grid(row=8, column = 7) 
Checkbutton(Y, text='G9', variable=G9).grid(row=9, column = 7)
Checkbutton(Y, text='G10', variable=G10).grid(row=10, column = 7)
Checkbutton(Y, text='G11', variable=G11).grid(row=11, column = 7)
Checkbutton(Y, text='G12', variable=G12).grid(row=12, column = 7)

Checkbutton(Y, text='H1', variable=H1).grid(row=1, column = 8)
Checkbutton(Y, text='H2', variable=H2).grid(row=2, column = 8) 
Checkbutton(Y, text='H3', variable=H3).grid(row=3, column = 8)
Checkbutton(Y, text='H4', variable=H4).grid(row=4, column = 8)
Checkbutton(Y, text='H5', variable=H5).grid(row=5, column = 8)
Checkbutton(Y, text='H6', variable=H6).grid(row=6, column = 8) 
Checkbutton(Y, text='H7', variable=H7).grid(row=7, column = 8) 
Checkbutton(Y, text='H8', variable=H8).grid(row=8, column = 8)
Checkbutton(Y, text='H9', variable=H9).grid(row=9, column = 8)
Checkbutton(Y, text='H10', variable=H10).grid(row=10, column = 8)
Checkbutton(Y, text='H11', variable=H11).grid(row=11, column = 8)
Checkbutton(Y, text='H12', variable=H12).grid(row=12, column = 8)


def A_com():
    A1.set(1)
    A2.set(1)
    A3.set(1)
    A4.set(1)
    A5.set(1)
    A6.set(1)
    A7.set(1)
    A8.set(1)
    A9.set(1)
    A10.set(1)
    A11.set(1)
    A12.set(1)
    
def B_com():
    B1.set(1)
    B2.set(1)
    B3.set(1)
    B4.set(1)
    B5.set(1)
    B6.set(1)
    B7.set(1)
    B8.set(1)
    B9.set(1)
    B10.set(1)
    B11.set(1)
    B12.set(1)
    
def C_com():
    C1.set(1)
    C2.set(1)
    C3.set(1)
    C4.set(1)
    C5.set(1)
    C6.set(1)
    C7.set(1)
    C8.set(1)
    C9.set(1)
    C10.set(1)
    C11.set(1)
    C12.set(1)
    
def D_com():
    D1.set(1)
    D2.set(1)
    D3.set(1)
    D4.set(1)
    D5.set(1)
    D6.set(1)
    D7.set(1)
    D8.set(1)
    D9.set(1)
    D10.set(1)
    D11.set(1)
    D12.set(1)
    
def E_com():
    E1.set(1)
    E2.set(1)
    E3.set(1)
    E4.set(1)
    E5.set(1)
    E6.set(1)
    E7.set(1)
    E8.set(1)
    E9.set(1)
    E10.set(1)
    E11.set(1)
    E12.set(1)
    
def F_com():
    F1.set(1)
    F2.set(1)
    F3.set(1)
    F4.set(1)
    F5.set(1)
    F6.set(1)
    F7.set(1)
    F8.set(1)
    F9.set(1)
    F10.set(1)
    F11.set(1)
    F12.set(1)
    
def G_com():
    G1.set(1)
    G2.set(1)
    G3.set(1)
    G4.set(1)
    G5.set(1)
    G6.set(1)
    G7.set(1)
    G8.set(1)
    G9.set(1)
    G10.set(1)
    G11.set(1)
    G12.set(1)
    
def H_com():
    H1.set(1)
    H2.set(1)
    H3.set(1)
    H4.set(1)
    H5.set(1)
    H6.set(1)
    H7.set(1)
    H8.set(1)
    H9.set(1)
    H10.set(1)
    H11.set(1)
    H12.set(1)
 

Button(Y, text='A', command = A_com).grid(row=0, column = 1)
Button(Y, text='B', command = B_com).grid(row=0, column = 2)
Button(Y, text='C', command = C_com).grid(row=0, column = 3)
Button(Y, text='D', command = D_com).grid(row=0, column = 4)
Button(Y, text='E', command = E_com).grid(row=0, column = 5)
Button(Y, text='F', command = F_com).grid(row=0, column = 6)
Button(Y, text='G', command = G_com).grid(row=0, column = 7)
Button(Y, text='H', command = H_com).grid(row=0, column = 8)


def one_com():
    A1.set(1)
    B1.set(1)
    C1.set(1)
    D1.set(1)
    E1.set(1)
    F1.set(1)
    G1.set(1)
    H1.set(1)

def two_com():
    A2.set(1)
    B2.set(1)
    C2.set(1)
    D2.set(1)
    E2.set(1)
    F2.set(1)
    G2.set(1)
    H2.set(1)

def three_com():
    A3.set(1)
    B3.set(1)
    C3.set(1)
    D3.set(1)
    E3.set(1)
    F3.set(1)
    G3.set(1)
    H3.set(1)

def four_com():
    A4.set(1)
    B4.set(1)
    C4.set(1)
    D4.set(1)
    E4.set(1)
    F4.set(1)
    G4.set(1)
    H4.set(1)

def five_com():
    A5.set(1)
    B5.set(1)
    C5.set(1)
    D5.set(1)
    E5.set(1)
    F5.set(1)
    G5.set(1)
    H5.set(1)
    
def six_com():
    A6.set(1)
    B6.set(1)
    C6.set(1)
    D6.set(1)
    E6.set(1)
    F6.set(1)
    G6.set(1)
    H6.set(1)

def seven_com():
    A7.set(1)
    B7.set(1)
    C7.set(1)
    D7.set(1)
    E7.set(1)
    F7.set(1)
    G7.set(1)
    H7.set(1)

def eight_com():
    A8.set(1)
    B8.set(1)
    C8.set(1)
    D8.set(1)
    E8.set(1)
    F8.set(1)
    G8.set(1)
    H8.set(1)

def nine_com():
    A9.set(1)
    B9.set(1)
    C9.set(1)
    D9.set(1)
    E9.set(1)
    F9.set(1)
    G9.set(1)
    H9.set(1)

def ten_com():
    A10.set(1)
    B10.set(1)
    C10.set(1)
    D10.set(1)
    E10.set(1)
    F10.set(1)
    G10.set(1)
    H10.set(1)

def eleven_com():
    A11.set(1)
    B11.set(1)
    C11.set(1)
    D11.set(1)
    E11.set(1)
    F11.set(1)
    G11.set(1)
    H11.set(1)

def twelve_com():
    A12.set(1)
    B12.set(1)
    C12.set(1)
    D12.set(1)
    E12.set(1)
    F12.set(1)
    G12.set(1)
    H12.set(1)

Button(Y, text='1', command = one_com).grid(row=1, column = 0)
Button(Y, text='2', command = two_com).grid(row=2, column = 0)
Button(Y, text='3', command = three_com).grid(row=3, column = 0) 
Button(Y, text='4', command = four_com).grid(row=4, column = 0)
Button(Y, text='5', command = five_com).grid(row=5, column = 0)
Button(Y, text='6', command = six_com).grid(row=6, column = 0)
Button(Y, text='7', command = seven_com).grid(row=7, column = 0)
Button(Y, text='8', command = eight_com).grid(row=8, column = 0)
Button(Y, text='9', command = nine_com).grid(row=9, column = 0)
Button(Y, text='10', command = ten_com).grid(row=10, column = 0) 
Button(Y, text='11', command = eleven_com).grid(row=11, column = 0)
Button(Y, text='12', command = twelve_com).grid(row=12, column = 0)


def CLEAR():
    A1.set(0)
    A2.set(0)
    A3.set(0)
    A4.set(0)
    A5.set(0)
    A6.set(0)
    A7.set(0)
    A8.set(0)
    A9.set(0)
    A10.set(0)
    A11.set(0)
    A12.set(0)
    
    B1.set(0)
    B2.set(0)
    B3.set(0)
    B4.set(0)
    B5.set(0)
    B6.set(0)
    B7.set(0)
    B8.set(0)
    B9.set(0)
    B10.set(0)
    B11.set(0)
    B12.set(0)

    C1.set(0)
    C2.set(0)
    C3.set(0)
    C4.set(0)
    C5.set(0)
    C6.set(0)
    C7.set(0)
    C8.set(0)
    C9.set(0)
    C10.set(0)
    C11.set(0)
    C12.set(0)

    D1.set(0)
    D2.set(0)
    D3.set(0)
    D4.set(0)
    D5.set(0)
    D6.set(0)
    D7.set(0)
    D8.set(0)
    D9.set(0)
    D10.set(0)
    D11.set(0)
    D12.set(0)
    
    E1.set(0)
    E2.set(0)
    E3.set(0)
    E4.set(0)
    E5.set(0)
    E6.set(0)
    E7.set(0)
    E8.set(0)
    E9.set(0)
    E10.set(0)
    E11.set(0)
    E12.set(0)
    
    F1.set(0)
    F2.set(0)
    F3.set(0)
    F4.set(0)
    F5.set(0)
    F6.set(0)
    F7.set(0)
    F8.set(0)
    F9.set(0)
    F10.set(0)
    F11.set(0)
    F12.set(0)
    
    G1.set(0)
    G2.set(0)
    G3.set(0)
    G4.set(0)
    G5.set(0)
    G6.set(0)
    G7.set(0)
    G8.set(0)
    G9.set(0)
    G10.set(0)
    G11.set(0)
    G12.set(0)
    
    H1.set(0)
    H2.set(0)
    H3.set(0)
    H4.set(0)
    H5.set(0)
    H6.set(0)
    H7.set(0)
    H8.set(0)
    H9.set(0)
    H10.set(0)
    H11.set(0)
    H12.set(0)

def Next():
  
    new_ar[0,0] = A1.get()
    new_ar[0,1] = A2.get()
    new_ar[0,2] = A3.get()
    new_ar[0,3] = A4.get()
    new_ar[0,4] = A5.get()
    new_ar[0,5] = A6.get()
    new_ar[0,6] = A7.get()
    new_ar[0,7] = A8.get()
    new_ar[0,8] = A9.get()
    new_ar[0,9] = A10.get()
    new_ar[0,10] = A11.get()
    new_ar[0,11] = A12.get()

    new_ar[1,0] = B1.get()
    new_ar[1,1] = B2.get()
    new_ar[1,2] = B3.get()
    new_ar[1,3] = B4.get()
    new_ar[1,4] = B5.get()
    new_ar[1,5] = B6.get()
    new_ar[1,6] = B7.get()
    new_ar[1,7] = B8.get()
    new_ar[1,8] = B9.get()
    new_ar[1,9] = B10.get()
    new_ar[1,10] = B11.get()
    new_ar[1,11] = B12.get()
    
    new_ar[2,0] = C1.get()
    new_ar[2,1] = C2.get()
    new_ar[2,2] = C3.get()
    new_ar[2,3] = C4.get()
    new_ar[2,4] = C5.get()
    new_ar[2,5] = C6.get()
    new_ar[2,6] = C7.get()
    new_ar[2,7] = C8.get()
    new_ar[2,8] = C9.get()
    new_ar[2,9] = C10.get()
    new_ar[2,10] = C11.get()
    new_ar[2,11] = C12.get()

    new_ar[3,0] = D1.get()
    new_ar[3,1] = D2.get()
    new_ar[3,2] = D3.get()
    new_ar[3,3] = D4.get()
    new_ar[3,4] = D5.get()
    new_ar[3,5] = D6.get()
    new_ar[3,6] = D7.get()
    new_ar[3,7] = D8.get()
    new_ar[3,8] = D9.get()
    new_ar[3,9] = D10.get()
    new_ar[3,10] = D11.get()
    new_ar[3,11] = D12.get()
    
    new_ar[4,0] = E1.get()
    new_ar[4,1] = E2.get()
    new_ar[4,2] = E3.get()
    new_ar[4,3] = E4.get()
    new_ar[4,4] = E5 .get()
    new_ar[4,5] = E6.get()
    new_ar[4,6] = E7.get()
    new_ar[4,7] = E8.get()
    new_ar[4,8] = E9.get()
    new_ar[4,9] = E10.get()
    new_ar[4,10] = E11.get()
    new_ar[4,11] = E12.get()

    new_ar[5,0] = F1.get()
    new_ar[5,1] = F2.get()
    new_ar[5,2] = F3.get()
    new_ar[5,3] = F4.get()
    new_ar[5,4] = F5.get()
    new_ar[5,5] = F6.get()
    new_ar[5,6] = F7.get()
    new_ar[5,7] = F8.get()
    new_ar[5,8] = F9.get()
    new_ar[5,9] = F10.get()
    new_ar[5,10] = F11.get()
    new_ar[5,11] = F12.get()

    new_ar[6,0] = G1.get()
    new_ar[6,1] = G2.get()
    new_ar[6,2] = G3.get()
    new_ar[6,3] = G4.get()
    new_ar[6,4] = G5.get()
    new_ar[6,5] = G6.get()
    new_ar[6,6] = G7.get()
    new_ar[6,7] = G8.get()
    new_ar[6,8] = G9.get()
    new_ar[6,9] = G10.get()
    new_ar[6,10] = G11.get()
    new_ar[6,11] = G12.get()

    new_ar[7,0] = H1.get()
    new_ar[7,1] = H2.get()
    new_ar[7,2] = H3.get()
    new_ar[7,3] = H4.get()
    new_ar[7,4] = H5.get()
    new_ar[7,5] = H6.get()
    new_ar[7,6] = H7.get()
    new_ar[7,7] = H8.get()
    new_ar[7,8] = H9.get()
    new_ar[7,9] = H10.get()
    new_ar[7,10] = H11.get()
    new_ar[7,11] = H12.get()
    

    A1.set(0)
    A2.set(0)
    A3.set(0)
    A4.set(0)
    A5.set(0)
    A6.set(0)
    A7.set(0)
    A8.set(0)
    A9.set(0)
    A10.set(0)
    A11.set(0)
    A12.set(0)
    
    B1.set(0)
    B2.set(0)
    B3.set(0)
    B4.set(0)
    B5.set(0)
    B6.set(0)
    B7.set(0)
    B8.set(0)
    B9.set(0)
    B10.set(0)
    B11.set(0)
    B12.set(0)

    C1.set(0)
    C2.set(0)
    C3.set(0)
    C4.set(0)
    C5.set(0)
    C6.set(0)
    C7.set(0)
    C8.set(0)
    C9.set(0)
    C10.set(0)
    C11.set(0)
    C12.set(0)

    D1.set(0)
    D2.set(0)
    D3.set(0)
    D4.set(0)
    D5.set(0)
    D6.set(0)
    D7.set(0)
    D8.set(0)
    D9.set(0)
    D10.set(0)
    D11.set(0)
    D12.set(0)
    
    E1.set(0)
    E2.set(0)
    E3.set(0)
    E4.set(0)
    E5.set(0)
    E6.set(0)
    E7.set(0)
    E8.set(0)
    E9.set(0)
    E10.set(0)
    E11.set(0)
    E12.set(0)
    
    F1.set(0)
    F2.set(0)
    F3.set(0)
    F4.set(0)
    F5.set(0)
    F6.set(0)
    F7.set(0)
    F8.set(0)
    F9.set(0)
    F10.set(0)
    F11.set(0)
    F12.set(0)
    
    G1.set(0)
    G2.set(0)
    G3.set(0)
    G4.set(0)
    G5.set(0)
    G6.set(0)
    G7.set(0)
    G8.set(0)
    G9.set(0)
    G10.set(0)
    G11.set(0)
    G12.set(0)
    
    H1.set(0)
    H2.set(0)
    H3.set(0)
    H4.set(0)
    H5.set(0)
    H6.set(0)
    H7.set(0)
    H8.set(0)
    H9.set(0)
    H10.set(0)
    H11.set(0)
    H12.set(0)


Button(Y, text='Next', command = Next).grid(row=13, column = 3)
Button(Y, text='Clear', command = CLEAR).grid(row=13, column = 4)
Button(Y, text = 'Quit', command = Y.destroy).grid(row=13, column = 5)


Y.mainloop() 