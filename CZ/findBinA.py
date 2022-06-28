#!/usr/bin/python3
# -*- coding: UTF-8 -*- 

class CZHandler:
    def __init__(self):
        pass
    
    #从B.txt里面遍历，找到在A.txt中的位置，放在后面，没有就打印NA
    #A.txt
    #1,2,3,4,5,6
    #33,22,44,55,66,69
    #31,21
    #86
    #87, 88,89
    #111,222,333
    
    #B.txt
    #88
    #89
    #90
    #5
    #6
    #33
    #22
    #44
    #55
    #31
    
    #C.txt
    #1,2,3,4,5,6 5,6
    #33,22,44,55,66,69 33,22,44,55
    #31,21 31
    #86 NA
    #87,88,89 88,89
    #111,222,333 NA
    def handleGrepAB(self):
        filenameA="A.txt"
        filenameB="B.txt"
        outputfile = "C.txt"
        fileA = open(filenameA, "r")
        filelinesA = fileA.readlines()

        fileB = open(filenameB, 'r')
        filelinesB = fileB.readlines()

        dictA = dict()
        for eachline in filelinesA :
            # remove the last '\n'
            eachlinenonewline = eachline.strip()
            dictA[eachlinenonewline] = ''

        print(dictA)

        for eachlineB in filelinesB:
            # remove the last '\n'
            eachB=eachlineB.strip()
            for eachlineA in filelinesA:
                eachA=eachlineA.strip()
                eachAArray = eachA.split(',')
                for eachelement in eachAArray:
                    if eachelement==eachB:
                        #found it
                        if dictA[eachA]=='':
                            #donot add ',' at the beginning
                            dictA[eachA]=eachelement
                        else:
                            dictA[eachA]=dictA[eachA]+','+eachelement     
        
        print(dictA)
        fileA.close()
        fileB.close()

        #write to output file
        outfile=open(outputfile, "w+")
        for k,v in dictA.items():
            if v=='':
                outfile.write(k+" NA")
            else:
                outfile.write(k+" "+v)
            outfile.write("\n")
        outfile.close()

if __name__ == "__main__":
    print("V1.0")

    czHandler = CZHandler()
    czHandler.handleGrepAB()
