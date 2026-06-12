# Virtual Pharmacist Assistant

medications = {
    "Paracetamol": {
        "use": "Pain relief and fever reduction",
        "warning": "Do not exceed recommended dose"
    },
    "Metformin": {
        "use": "Management of Type 2 Diabetes",
        "warning": "Take with food"
    },
    "Aspirin": {
        "use": "Pain relief and blood thinning",
        "warning": "Avoid if allergic to NSAIDs"
    }
}

print("=== Virtual Pharmacist Assistant ===")

drug = input("Enter medication name: ")

if drug in medications:
    print("\nMedication Information")
    print("Drug:", drug)
    print("Use:", medications[drug]["use"])
    print("Warning:", medications[drug]["warning"])
else:
    print("Medication information not available.")
