# Mash Calculator for All-Grain Brewing
# Constants
wort_shrinkage = 0.04  # 4% volume loss during cooling
grain_absorption_constant = 1.082  # liters per kg
percent_boil_off = 0.10  # 10% per hour

def mash_calculator(grain_bill, boil_time, trub_loss, equipment_loss, mash_thickness, grain_temp, target_mash_temp):
    # Core calculations
    mash_water = grain_bill * mash_thickness
    grain_absorption = grain_bill * grain_absorption_constant
    boil_off = (boil_time/60) * percent_boil_off * mash_water
    
    # Mantenemos el cálculo original para sparge_water que estaba funcionando bien
    sparge_water = boil_off + grain_absorption + trub_loss + equipment_loss
    
    # Agua total es la suma de mash y sparge
    total_water = mash_water + sparge_water
    
    # Temperature calculation con la fórmula corregida
    strike_temp = (0.41 / (mash_water/grain_bill)) * (target_mash_temp - grain_temp) + target_mash_temp
    
    # Volume calculation with shrinkage adjustment
    pre_boil_volume = (mash_water - grain_absorption + sparge_water + trub_loss + equipment_loss) / (1 - wort_shrinkage)
    
    return (
        round(total_water, 2),
        round(mash_water, 2),
        round(sparge_water, 2),
        round(strike_temp, 2),
        round(pre_boil_volume, 2)
    )

# User input section
print("Mash Calculator - Enter values:")
params = (
    float(input("Grain bill (kg): ")),
    float(input("Boil time (minutes): e.g. 60: ")),
    float(input("Trub loss (liters): e.g. 2: ")),
    float(input("Equipment loss (liters) e.g. 1.5: ")),
    float(input("Mash thickness (l/kg): e.g. 2.77: ")),
    float(input("Grain temperature (°C): ")),
    float(input("Target mash temp (°C): e.g. 67: "))
)

# Calculate and display results
total_water, mash_water, sparge_water, strike_temp, pre_boil = mash_calculator(*params)
print(f"\nResults:")
print(f"Total water needed: {total_water} L")
print(f"Mash water required: {mash_water} L")
print(f"Sparge water required: {sparge_water} L")
print(f"Strike temperature: {strike_temp} °C")
print(f"Pre-boil wort volume: {pre_boil} L")
