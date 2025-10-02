
patient = ("mary adhiambo", 45, 120, 80)  


print("Age:", patient[1])
print("Heart Rate:", patient[3])


print("""
Tuples are immutable, meaning data cannot be accidentally modified.
This makes them ideal for storing fixed patient vitals to preserve data integrity.
""")


patient_list = list(patient)
patient_list[3] = 85
patient = tuple(patient_list)
print("Updated patient tuple:", patient)


patients = (
    ("Alice", 30, 115, 78),
    ("Brian", 50, 130, 90),
    ("Cynthia", 25, 110, 70),
    ("Daniel", 40, 125, 88),
    ("Eva", 35, 118, 82)
)

names = [p[0] for p in patients]
print("Patient names:", names)
