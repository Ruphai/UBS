# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 16:41:48 2019

@author: pfm
"""
import numpy as np
import matplotlib.pyplot as plt
import glob, os, sys
import re, math
import argparse
from collections import Counter
from statistics import mode


def normalizeMaxMin(V):
    M=np.max(V)
    m=np.min(V)
    V=(V-m)/(M-m)
    return V
    
def convertLine(l1):
    lout=[]
    l1=l1.split(' ')
    for e in l1:
        lout.append(float(e))
    return np.array(lout)


def convertLineMOBISIG(l1):
    lout=[]
    l1=re.split(' |,|;|\n|\t|\0',l1)
    #l1=l1.split(' ')
    ii=0
    if len(l1)>1:
        for e in l1:
            if e!="":
                if ii!=2 and ii!=4:
                    lout.append(float(e))
                ii+=1
                if ii==7:
                    break
    return np.array(lout)
    
    
def loadFile(fname, removeMean=True, withSpeed=False, withAcceleration=False):
    f = open(fname, 'r')
    lines=f.readlines()
    L=len(lines)
    data=[]
    for i in range(L):
        d=convertLine(lines[i])
        data.append(d)
    data = np.array(data)
    if withSpeed:
        dim=len(data[0])
        D=np.zeros((len(data),dim+2))
        for i in range(len(data)):
            D[i,0:dim]=data[i,:]
            if i>0:
                D[i,dim]=data[i,0]-data[i-1,0]
                D[i,dim+1]=data[i,1]-data[i-1,1]
        data=D

    dim=len(data[0])
    m=np.zeros(dim)
    if removeMean:
        sigma=np.zeros(dim)
        for k in range(dim):
            m[k]=np.mean(data[:,k])
            sigma[k]=np.std(data[:,k])
            data[:,k]=(data[:,k]-m[k])/sigma[k]
      
    if removeMean:
        M=np.zeros(dim)
        for k in range(dim):
            m[k]=np.min(data[:,k])
            M[k]=np.max(data[:,k])
            data[:,k]=(data[:,k]-m[k])/(M[k]-m[k])
            
    # Suppress Z==0
    D=[]
    for i in range(len(data)):
       if data[i,2]>.01:
           D.append(data[i,:])
    data=np.array(D)
    dim=len(data[0])
    if removeMean:
        sigma=np.zeros(dim)
        for k in range(dim):
            m[k]=np.mean(data[:,k])
            sigma[k]=np.std(data[:,k])
            data[:,k]=(data[:,k]-m[k])/sigma[k]

    return data

    
def loadFileMOBISIG(fname, removeMean=True, path='./DATA/'):
    f = open(fname, 'r')
    lines=f.readlines()
    L=len(lines)
    data=[]
    for i in range(1,L):
        if lines[i]!="\n":
          d=convertLineMOBISIG(lines[i])
          data.append(d)
    data = np.array(data)
    dim=len(data[0])
    m=np.zeros(dim)
    sigma=np.zeros(dim)
    '''if removeMean:

        for k in range(dim):
            m[k]=np.mean(data[:,k])
            sigma[k]=np.std(data[:,k])
            data[:,k]=(data[:,k]-m[k])/sigma[k]'''
      
    if removeMean:
        M=np.zeros(dim)
        for k in range(dim):
            m[k]=np.min(data[:,k])
            M[k]=np.max(data[:,k])
            data[:,k]=(data[:,k]-m[k])/(M[k]-m[k]) 
    # Suppress Z==0
    D=[]
    for i in range(len(data)):
       if data[i,2]>0:#.25:
           '''d=[]
           for k in range(dim):
               if k!=2:
                   d.append(data[i,k])
           D.append(np.array(d))'''
           D.append(data[i,:])
    data=np.array(D)
    dim=len(data[0])
    if removeMean:
        for k in range(dim):
            m[k]=np.mean(data[:,k])
            sigma[k]=np.std(data[:,k])
            data[:,k]=(data[:,k]-m[k])/sigma[k]  

    return data



def getGenuinesTrainTest_MOBISIG(uid, ntrain=5, path='./DATA/'):
    path += uid
    os.chdir(path)
    lfiles=[]
    for file in glob.glob("SIGN_GEN_*.csv"):
        lfiles.append(file)
    lfiles=sorted(lfiles)
    #I=np.arange(len(lfiles))
    np.random.shuffle(lfiles)
    if ntrain>len(lfiles)-1:
        ntrain=len(lfiles)-1
    genuineTrainFiles=lfiles[0:ntrain]
    genuineTestFiles=lfiles[ntrain:]
    return genuineTrainFiles, genuineTestFiles

def getForgeriesTest_MOBISIG(uid, path='./DATA/'):
    path += uid
    os.chdir(path)
    lfiles=[]
    for file in glob.glob("SIGN_FOR_*.csv"):
        lfiles.append(file)
    lfiles=sorted(lfiles)
    return lfiles


def loadTrainQuestionnedMOBISIG(uid, ntrain=5, path='./DATA/'):
    lgtrain, lgtest=getGenuinesTrainTest_MOBISIG(uid, ntrain=ntrain, path=path)
    lftest = getForgeriesTest_MOBISIG(uid, path=path)
    path += uid + '/'
    os.chdir(path)
    dataT=[]
    for file in lgtrain:
        d=loadFileMOBISIG(path+file)
        dataT.append(d)

    data=[]
    yq=[]
    for file in lgtest:
        d=loadFileMOBISIG(path+file)
        data.append(d)
        yq.append('G')

    for file in lftest:
        d=loadFileMOBISIG(path+file)
        data.append(d)
        yq.append('F')
    return np.array(dataT, dtype=object), np.array(data, dtype=object), yq

def processProblem(uid, X_train, X_test, y_test):
    print('Processing problem:', uid, '...')
    ## TO DO
    


    
path=os.getcwd() #+ "/MOBISIG/"
os.chdir(path)
print('path:', path)
luid = glob.glob("USER*")
luid.sort()

# number of training instance for each problem
ntrain=5

# Iteratively load problem for each user (uid)
for uid in luid:
    print("loading problem for user:", uid)
    X_train, X_test, y_test = loadTrainQuestionnedMOBISIG(uid, ntrain=ntrain, path=path)     
    processProblem(uid, X_train, X_test, y_test)