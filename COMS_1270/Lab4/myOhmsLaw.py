# Caden Burbridge 02/16/2026
# Lab week 4 - This file has various functions involving Ohms law

def calculateCurrent(res, volt):
    return res/volt

def calculateResistance(cur, volt):
    return volt/cur

def calculateVoltage(cur, res):
    return res * cur