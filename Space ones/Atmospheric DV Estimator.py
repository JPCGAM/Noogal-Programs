from numpy import log as ln
from numpy import pi as pi
from numpy import sqrt
RadiusBodyKm= float(input("Enter the radius of the object in km: "))
RadiusBodyCm = RadiusBodyKm*1000*100
ScaleHeight = float(input("Enter the scale height of the object: "))
AtmosphericPressureBar = float(input("Enter the ASL atmospheric pressure in Bar: "))
AtmosphericPressurePa= 100000*AtmosphericPressureBar
if AtmosphericPressurePa != 0:
    AtmosphereHeightKm= -ScaleHeight*ln((7.099*10**-3)/AtmosphericPressurePa)
elif AtmosphericPressurePa == 0:
    AtmosphereHeightKm=0
AtmosphereHeightCm=AtmosphereHeightKm*1000*100
TotalRadius = AtmosphereHeightCm+RadiusBodyCm
VolumeTotal = (4/3)*pi*TotalRadius**3
VolumeBody = (4/3)*pi*RadiusBodyCm**3
VolumeAtmosphere = VolumeTotal-VolumeBody
if AtmosphereHeightKm != 0:
    AtmosphereMassKG= float(input("Enter the mass of the atmosphere in KG: "))
    AtmosphereMassG = AtmosphereMassKG*1000
    AtmosphereDensity = AtmosphereMassG/VolumeAtmosphere
elif AtmosphereHeightKm == 0:
    AtmosphereDensity = 0
MassInCm2= AtmosphereDensity*AtmosphereHeightCm
GramsPerMpS_O = 0.043390891*AtmosphericPressureBar+0.442134384
GramsPerMpS_T = 0.442134384*AtmosphericPressureBar+0.043390891
DeltaVAtm_O=MassInCm2/GramsPerMpS_O
DeltaVAtm_T=MassInCm2/GramsPerMpS_T

RadiusBodyM = RadiusBodyKm*1000
BodyMass = float(input("Enter the mass of the object in KG: "))
SpeedAtSurface = sqrt(((6.67*10**-11)*BodyMass)/RadiusBodyM)
AtmosphereHeightM=AtmosphereHeightKm*1000
RadiusOutSideAtm = AtmosphereHeightM+RadiusBodyM
SpeedOutsideAtm = sqrt(((6.67*10**-11)*BodyMass)/RadiusOutSideAtm)
DeltaVNoAtm = 2*SpeedAtSurface-SpeedOutsideAtm


TotalDeltaV_O = DeltaVAtm_O+DeltaVNoAtm
TotalDeltaV_T = DeltaVAtm_T+DeltaVNoAtm
print(f"Delta V values calculated with atmosphere are: {TotalDeltaV_O} and {TotalDeltaV_T}. The value for without atmosphere is: {DeltaVNoAtm}")
print(f"Other noteworthy data:")
print(f"Atmospheric height: {AtmosphereHeightCm/(100*1000)} km")