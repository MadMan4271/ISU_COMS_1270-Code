# Caden Burbridge 02/16/2026
# Lab week 4 - This file has various functions involving finances

def annualPercentageRate(intc, fee, loan, days):
    return (((intc + fee) / loan) / days) *100

def compoundAmount(prin, rate, comp):
    return prin * (1 + (rate/100) / comp) ** comp