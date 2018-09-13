import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats
data=np.loadtxt('../lab0_spectral_data.txt')
xdata=np.arange(0,8191,1)
def gaus(x,A,B,C):
    return A*np.exp(-(x-B)**2/(2*C**2))
our_guess=(3700, 210,3)
pAm,res=curve_fit(gaus,xdata[200:215],data[200:215,0],p0=our_guess)
print(pAm[1])
our_guess=(50000,2354,3)
pCs,res=curve_fit(gaus,xdata[2343:2365],data[2343:2365,2],p0=our_guess)
print(pCs[1])
our_guess=(14000,4177,3)
pCo1,res=curve_fit(gaus,xdata[4165:4190],data[4165:4190,3],p0=our_guess)
print "the first peak of Co-60 is ", pCo1[1]
our_guess=(10000,4745,3)
pCo2,res=curve_fit(gaus,xdata[4730:4760],data[4730:4760,3],p0=our_guess)
print "the second peak of Co-60 is ", pCo2[1]
our_guess=(160000,429,1.5)
pEu1,res=curve_fit(gaus,xdata[423:437],data[423:437,4],p0=our_guess)
print "the first peak of Eu-153 is ", pEu1[1]
our_guess=(25000,868,1.5)
pEu2,res=curve_fit(gaus,xdata[860:875],data[860:875,4],p0=our_guess)
print "the second peak of Eu-153 is ", pEu2[1]
our_guess=(50000,1222.5,2)
pEu3,res=curve_fit(gaus,xdata[1215:1231],data[1215:1231,4],p0=our_guess)
print "the 3rd peak of Eu-153 is ", pEu3[1]
our_guess=(4000,1461,2)
pEu4,res=curve_fit(gaus,xdata[1454:1467],data[1454:1467,4],p0=our_guess)
print "the 4th peak of Eu-153 is ", pEu4[1]
our_guess=(8000,2772,2)
pEu5,res=curve_fit(gaus,xdata[2762:2783],data[2762:2783,4],p0=our_guess)
print "the 5th peak of Eu-153 is ", pEu5[1]
our_guess=(6000,3432,3)
pEu6,res=curve_fit(gaus,xdata[3421:3444],data[3421:3444,4],p0=our_guess)
print "the 6th peak of Eu-153 is ", pEu6[1]

our_guess=(6000,5015,3)
pEu7,res=curve_fit(gaus,xdata[5000:5030],data[5000:5030,4],p0=our_guess)
print "the 7th peak of Eu-153 is ", pEu7[1]

our_guess=(5000,3961,2.5)
pEu8,res=curve_fit(gaus,xdata[3947:3972],data[3947:3972,4],p0=our_guess)
print "the 8th peak of Eu-153 is ", pEu8[1]

our_guess=(60000,284,2)
pBa1,res=curve_fit(gaus,xdata[275:292],data[275:292,1],p0=our_guess)
print "the 1st peak of Ba-133 is ", pBa1[1]

our_guess=(6000,981,2)
pBa2,res=curve_fit(gaus,xdata[973:989],data[973:989,1],p0=our_guess)
print "the 2nd peak of Ba-133 is ", pBa2[1]

our_guess=(15000,1075,3)
pBa3,res=curve_fit(gaus,xdata[1067:1083],data[1067:1083,1],p0=our_guess)
print "the 3rd peak of Ba-133 is ", pBa3[1]

our_guess=(40000,1265,3)
pBa4,res=curve_fit(gaus,xdata[1256:1273],data[1256:1273,1],p0=our_guess)
print "the 4th peak of Ba-133 is ", pBa4[1]

our_guess=(4000,1364,2)
pBa5,res=curve_fit(gaus,xdata[1356:1371],data[1356:1371,1],p0=our_guess)
print "the 5th peak of Ba-133 is ", pBa5[1]
chn=(pAm[1],pCs[1],pCo1[1],pCo2[1],pEu1[1],pEu2[1],pEu3[1],pEu4[1],pEu5[1],pEu6[1],pEu7[1],pEu8[1],pBa1[1],pBa2[1],pBa3[1],pBa4[1],pBa5[1])
pE=(661.657,1173.228,1332.492,344.2785,411.1165,778.9045,964.072,1408.013,1112.076,276.3989,302.8508,356.0129,383.8485)
slope, intercept, r_value, p_value, std_err = stats.linregress(chn,pE)
xi=np.arange(200,5050)
yi=slope*xi+intercept
print 'Energy=', slope,'*chanel number+',intercept
print 'r value', r_value
print chn, pE
print "Creating figure..."
plt.figure()
plt.plot(xi,yi,'r-',chn,pE,'o')
plt.title("Energy Calibration")
plt.xlabel('Chanel Number')
plt.ylabel('Energy,keV')
plt.savefig('../images/Calibration.png')
plt.show()
print "Done!"
