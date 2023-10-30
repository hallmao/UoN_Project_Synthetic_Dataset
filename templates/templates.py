TEMPLATES = {
    1: {
        "summary": "Dear {patient_name}, your appointment for {reason} is coming up. Please remember to bring your medical history.",
        "description": "We are eagerly waiting to see you, {patient_name}, for your upcoming appointment regarding {reason}. Your medical history is crucial for us to provide the best care possible.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    2: {
        "summary": "Reminder for {patient_name}, your {reason} appointment is due. Please remember to fast for 12 hours prior to the appointment.",
        "description": "Dear {patient_name}, your appointment for {reason} is approaching. Fasting for 12 hours prior to the appointment is crucial for accurate results.",
        "reasons": ["Blood Work", "CT Scan", "MRI", "Ultrasound", "Biopsy", "Colonoscopy", "Endoscopy", "Glucose Tolerance Test", "Lipid Profile Test", "Liver Function Test"]
    },
    3: {
        "summary": "Dear {patient_name}, your appointment for {reason} is confirmed. Please arrive 15 minutes early.",
        "description": "We have scheduled your appointment for {reason}, {patient_name}. Arriving 15 minutes early will help us serve you better and maintain our schedule.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    4: {
        "summary": "Hello {patient_name}, your medical checkup for {reason} is due soon. Please bring your insurance card.",
        "description": "We are looking forward to your medical checkup for {reason}, {patient_name}. Having your insurance card at hand will expedite the process and ensure a smooth experience.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    5: {
        "summary": "Dear {patient_name}, during your next appointment for {reason}, please share any symptoms you've been experiencing lately.",
        "description": "We are committed to providing the best care, {patient_name}. During your upcoming appointment for {reason}, it would be helpful if you could share any symptoms you've been experiencing. This will help us understand your health better.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    6: {
        "summary": "Dear {patient_name}, for your upcoming appointment for {reason}, please bring all relevant medical documents.",
        "description": "Your upcoming appointment for {reason} is important to us, {patient_name}. Bringing all relevant medical documents will help us provide better and more personalized care.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    7: {
        "summary": "Dear {patient_name}, your medical consultation for {reason} is scheduled. If you need to reschedule, please inform us in advance.",
        "description": "We have scheduled your medical consultation for {reason}, {patient_name}. If you need to reschedule, please let us know in advance so we can accommodate other patients.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    8: {
        "summary": "Dear {patient_name}, as your medical visit for {reason} approaches, we recommend you to be well-rested for the appointment.",
        "description": "Your health is our priority, {patient_name}. As your medical visit for {reason} approaches, we recommend you to be well-rested. This will help us get the most accurate results during your visit.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    9: {
        "summary": "Dear {patient_name}, ahead of your appointment for {reason}, we advise against any strenuous activity to ensure accurate readings.",
        "description": "We are looking forward to your appointment for {reason}, {patient_name}. To ensure accurate readings during your visit, we advise against any strenuous activity a day before the appointment.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    10: {
        "summary": "Hello {patient_name}, during your next medical checkup for {reason}, please bring a list of medications you are currently taking.",
        "description": "We are committed to your health, {patient_name}. During your next medical checkup for {reason}, please bring a list of medications you are currently taking. This will help us understand your health better and provide the best care possible.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    11: {
        "summary": "Dear {patient_name}, your appointment for {reason} is soon. Please bring your ID for verification.",
        "description": "We are looking forward to your appointment for {reason}, {patient_name}. Please bring your ID for verification. This is to ensure your safety and privacy.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    12: {
        "summary": "Dear {patient_name}, your {reason} appointment is scheduled. Please bring any recent test results if available.",
        "description": "We have scheduled your appointment for {reason}, {patient_name}. If you have any recent test results, please bring them along. This will help us provide the best care possible.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    13: {
        "summary": "Dear {patient_name}, for your {reason} appointment, we recommend wearing comfortable clothing.",
        "description": "We want you to be comfortable during your {reason} appointment, {patient_name}. We recommend wearing comfortable clothing to ensure a smooth and pleasant experience.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    14: {
        "summary": "Dear {patient_name}, for your {reason} appointment, if you wear glasses or contact lenses, please bring them.",
        "description": "We are looking forward to your {reason} appointment, {patient_name}. If you wear glasses or contact lenses, please bring them along. This will help us provide the best care possible.",
        "reasons": ["Eye Examination"]
    },
    15: {
        "summary": "Dear {patient_name}, for your {reason} appointment, please bring a list of any allergies you have.",
        "description": "We are committed to your health, {patient_name}. For your {reason} appointment, please bring a list of any allergies you have. This will help us provide the best care possible.",
        "reasons": ["Allergy Testing"]
    },
    16: {
        "summary": "Dear {patient_name}, for your {reason} appointment, please bring a list of any dietary supplements you are taking.",
        "description": "We are looking forward to your {reason} appointment, {patient_name}. Please bring a list of any dietary supplements you are taking. This will help us understand your health better and provide the best care possible.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    17: {
        "summary": "Dear {patient_name}, for your {reason} appointment, if you use hearing aids, please bring them.",
        "description": "We are committed to your health, {patient_name}. For your {reason} appointment, if you use hearing aids, please bring them. This will help us provide the best care possible.",
        "reasons": ["Audiology Testing"]
    },
    18: {
        "summary": "Dear {patient_name}, for your {reason} appointment, if you need to, please bring a family member.",
        "description": "We understand that medical appointments can be stressful, {patient_name}. For your {reason} appointment, if you need to, please bring a family member. We are here to support you.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    19: {
        "summary": "Dear {patient_name}, for your {reason} appointment, if you use any medical devices, please bring them.",
        "description": "We are committed to your health, {patient_name}. For your {reason} appointment, if you use any medical devices, please bring them. This will help us provide the best care possible.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    20: {
        "summary": "Dear {patient_name}, for your {reason} appointment, please bring your pharmacy contact info.",
        "description": "We are looking forward to your {reason} appointment, {patient_name}. Please bring your pharmacy contact info. This will help us coordinate your care and ensure a smooth experience.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    21: {
        "summary": "Dear {patient_name}, for your {reason} appointment, please bring a list of any symptoms you are currently experiencing.",
        "description": "We are committed to your health, {patient_name}. For your {reason} appointment, please bring a list of any symptoms you are currently experiencing. This will help us understand your health better and provide the best care possible.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    22: {
        "summary": "Dear {patient_name}, for your {reason} appointment, please bring a list of any past surgeries and their dates.",
        "description": "We are looking forward to your {reason} appointment, {patient_name}. Please bring a list of any past surgeries and their dates. This will help us understand your health better and provide the best care possible.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    23: {
        "summary": "Dear {patient_name}, for your {reason} appointment, please bring a list of your family's medical history.",
        "description": "We are committed to your health, {patient_name}. For your {reason} appointment, please bring a list of your family's medical history. This will help us understand your health better and provide the best care possible.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    24: {
        "summary": "Dear {patient_name}, for your {reason} appointment, please bring a list of any vaccinations you have had and their dates.",
        "description": "We are looking forward to your {reason} appointment, {patient_name}. Please bring a list of any vaccinations you have had and their dates. This will help us understand your health better and provide the best care possible.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    25: {
        "summary": "Dear {patient_name}, for your {reason} appointment, please bring a list of any allergies you have.",
        "description": "We are committed to your health, {patient_name}. For your {reason} appointment, please bring a list of any allergies you have. This will help us understand your health better and provide the best care possible.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    26: {
        "summary": "Dear {patient_name}, for your {reason} appointment, please bring a list of any medications you are currently taking and their dosages.",
        "description": "We are looking forward to your {reason} appointment, {patient_name}. Please bring a list of any medications you are currently taking and their dosages. This will help us understand your health better and provide the best care possible.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    27: {
        "summary": "Dear {patient_name}, for your {reason} appointment, please bring a list of any dietary supplements you are taking and their dosages.",
        "description": "We are committed to your health, {patient_name}. For your {reason} appointment, please bring a list of any dietary supplements you are taking and their dosages. This will help us understand your health better and provide the best care possible.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    28: {
        "summary": "Dear {patient_name}, for your {reason} appointment, please bring a list of any past and current medical conditions.",
        "description": "We are looking forward to your {reason} appointment, {patient_name}. Please bring a list of any past and current medical conditions. This will help us understand your health better and provide the best care possible.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    29: {
        "summary": "Dear {patient_name}, for your {reason} appointment, please bring a list of any past and current treatments and their dates.",
        "description": "We are committed to your health, {patient_name}. For your {reason} appointment, please bring a list of any past and current treatments and their dates. This will help us understand your health better and provide the best care possible.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    },
    30: {
        "summary": "Dear {patient_name}, for your {reason} appointment, please bring a list of your emergency contacts.",
        "description": "We are looking forward to your {reason} appointment, {patient_name}. Please bring a list of your emergency contacts. This will help us ensure your safety during your visit.",
        "summary": "{patient_name}, {reason} appointment. Bring a list of your emergency contacts.",
        "description": "{patient_name}, for your {reason} appointment, please bring a list of your emergency contacts.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]

    },
    31: {
        "summary": "Dear {patient_name}, for your {reason} appointment, please bring any previous imaging studies.",
        "description": "We are looking forward to your {reason} appointment, {patient_name}. Please bring any previous imaging studies. This will help us understand your health better and provide the best care possible.",
        "reasons": ["Radiology Consultation", "Orthopedic Consultation", "Neurology Consultation"]
    },
    32: {
        "summary": "Dear {patient_name}, for your {reason} appointment, please bring a list of any questions or concerns you have.",
        "description": "We are committed to your health, {patient_name}. For your {reason} appointment, please bring a list of any questions or concerns you have. This will help us address your needs better.",
        "reasons": ["Routine Checkup", "Post-surgery Follow-up", "Blood Pressure Monitoring", "Physical Therapy Session", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    }

}
    # The LOCATIONS_AND_STAFF dictionary contains information about different blocks in a hospital.
    # Each block is represented by a key (e.g., "A", "B", "C", "D").
    # The value for each block is another dictionary that contains:
    # - the building number,
    # - the floor number,
    # - a list of rooms, and
    # - a list of staff members.
    #
    # Each staff member is represented by a dictionary that contains:
    # - the staff member's name,
    # - their role (e.g., "Doctor", "Nurse"),
    # - their specialization, and
    # - a list of their tasks.



LOCATIONS_AND_STAFF = {
    "A": {
        "building": 1,
        "floor": 2,
        "rooms": ["Neurology Room 1", "General Practice Room 1", "Blood Pressure Monitoring Room 1", "Post-surgery Care Room 1", "Physical Therapy Room 1", "Vaccination Room 1"],
        "staff": [
            {"name": "Dr. John Smith", "role": "Doctor", "specialization": "Neurology", "tasks": ["Neurology Consultation", "Routine Checkup"]},
            {"name": "Dr. James Allen", "role": "Doctor", "specialization": "General Practice", "tasks": ["Routine Checkup", "Post-surgery Follow-up"]},
            {"name": "Nurse Emily Johnson", "role": "Nurse", "specialization": "Blood Pressure Monitoring", "tasks": ["Blood Pressure Monitoring"]},
            {"name": "Nurse Sarah Brown", "role": "Nurse", "specialization": "Post-surgery Care", "tasks": ["Post-surgery Follow-up"]},
            {"name": "Dr. David Davis", "role": "Doctor", "specialization": "Physical Therapy", "tasks": ["Physical Therapy Session"]},
            {"name": "Nurse Robert Clark", "role": "Nurse", "specialization": "Vaccination", "tasks": ["Vaccination"]},
            {"name": "Dr. Michael Extra", "role": "Doctor", "specialization": "General Practice", "tasks": ["Routine Checkup", "Post-surgery Follow-up"]},
            {"name": "Dr. Laura Thompson", "role": "Doctor", "specialization": "Radiology", "tasks": ["CT Scan", "MRI", "Ultrasound"]},
            {"name": "Dr. Olivia Garcia", "role": "Doctor", "specialization": "Endocrinology", "tasks": ["Glucose Tolerance Test", "Lipid Profile Test"]},
            {"name": "Dr. Sophia Martinez", "role": "Doctor", "specialization": "Gastroenterology", "tasks": ["Endoscopy", "Colonoscopy"]},
            {"name": "Dr. Mia Robinson", "role": "Doctor", "specialization": "Pathology", "tasks": ["Biopsy", "Blood Work"]},
            {"name": "Dr. Charlotte Hall", "role": "Doctor", "specialization": "Hepatology", "tasks": ["Liver Function Test"]},
            {"name": "Dr. Andrew Simmons", "role": "Doctor", "specialization": "Allergology", "tasks": ["Allergy Testing"]},
            {"name": "Dr. Benjamin Foster", "role": "Doctor", "specialization": "Audiology", "tasks": ["Audiology Testing"]},
            {"name": "Dr. Samuel Hughes", "role": "Doctor", "specialization": "Radiology", "tasks": ["Radiology Consultation"]}
        ]
    },
    "B": {
        "building": 1,
        "floor": 3,
        "rooms": ["Cardiology Room 1", "Dentistry Room 1", "General Practice Room 2", "Eye Care Room 1", "Post-surgery Care Room 2", "Orthopedics Room 1"],
        "staff": [
            {"name": "Dr. William Thompson", "role": "Doctor", "specialization": "Cardiology", "tasks": ["Cardiology Consultation", "Routine Checkup"]},
            {"name": "Dr. Richard Adams", "role": "Doctor", "specialization": "Dentistry", "tasks": ["Dental Checkup"]},
            {"name": "Nurse Linda Miller", "role": "Nurse", "specialization": "General Practice", "tasks": ["Routine Checkup"]},
            {"name": "Nurse Patricia Baker", "role": "Nurse", "specialization": "Eye Care", "tasks": ["Eye Examination"]},
            {"name": "Dr. Thomas Wilson", "role": "Doctor", "specialization": "Post-surgery Care", "tasks": ["Post-surgery Follow-up"]},
            {"name": "Dr. Charles Carter", "role": "Doctor", "specialization": "Orthopedics", "tasks": ["Orthopedic Consultation"]},
            {"name": "Dr. Michael Extra", "role": "Doctor", "specialization": "General Practice", "tasks": ["Routine Checkup", "Post-surgery Follow-up"]},
            {"name": "Dr. Amelia Turner", "role": "Doctor", "specialization": "Radiology", "tasks": ["CT Scan", "MRI", "Ultrasound"]},
            {"name": "Dr. Harper Perez", "role": "Doctor", "specialization": "Endocrinology", "tasks": ["Glucose Tolerance Test", "Lipid Profile Test"]},
            {"name": "Dr. Evelyn King", "role": "Doctor", "specialization": "Gastroenterology", "tasks": ["Endoscopy", "Colonoscopy"]},
            {"name": "Dr. Abigail Wright", "role": "Doctor", "specialization": "Pathology", "tasks": ["Biopsy", "Blood Work"]},
            {"name": "Dr. Emily Lopez", "role": "Doctor", "specialization": "Hepatology", "tasks": ["Liver Function Test"]},
            {"name": "Dr. Jacob Bailey", "role": "Doctor", "specialization": "Allergology", "tasks": ["Allergy Testing"]},
            {"name": "Dr. Lucas Cooper", "role": "Doctor", "specialization": "Audiology", "tasks": ["Audiology Testing"]},
            {"name": "Dr. Ethan Reed", "role": "Doctor", "specialization": "Radiology", "tasks": ["Radiology Consultation"]}
        ]
    },
    "C": {
        "building": 2,
        "floor": 1,
        "rooms": ["Orthopedics Room 2", "Eye Care Room 2", "Vaccination Room 2", "Cardiology Room 2", "Dentistry Room 2", "Neurology Room 2"],
        "staff": [
            {"name": "Dr. Christopher Taylor", "role": "Doctor", "specialization": "Orthopedics", "tasks": ["Orthopedic Consultation", "Routine Checkup"]},
            {"name": "Dr. Daniel Evans", "role": "Doctor", "specialization": "Eye Care", "tasks": ["Eye Examination"]},
            {"name": "Nurse Jennifer Anderson", "role": "Nurse", "specialization": "Vaccination", "tasks": ["Vaccination"]},
            {"name": "Nurse Jessica Foster", "role": "Nurse", "specialization": "Cardiology", "tasks": ["Cardiology Consultation"]},
            {"name": "Dr. Matthew Thomas", "role": "Doctor", "specialization": "Dentistry", "tasks": ["Dental Checkup"]},
            {"name": "Dr. Anthony Green", "role": "Doctor", "specialization": "Neurology", "tasks": ["Neurology Consultation", "Routine Checkup"]},
            {"name": "Dr. Michael Extra", "role": "Doctor", "specialization": "General Practice", "tasks": ["Routine Checkup", "Post-surgery Follow-up"]},
            {"name": "Dr. Luna Scott", "role": "Doctor", "specialization": "Radiology", "tasks": ["CT Scan", "MRI", "Ultrasound"]},
            {"name": "Dr. Chloe Mitchell", "role": "Doctor", "specialization": "Endocrinology", "tasks": ["Glucose Tolerance Test", "Lipid Profile Test"]},
            {"name": "Dr. Madison Campbell", "role": "Doctor", "specialization": "Gastroenterology", "tasks": ["Endoscopy", "Colonoscopy"]},
            {"name": "Dr. Scarlett Rodriguez", "role": "Doctor", "specialization": "Pathology", "tasks": ["Biopsy", "Blood Work"]},
            {"name": "Dr. Victoria Carter", "role": "Doctor", "specialization": "Hepatology", "tasks": ["Liver Function Test"]},
            {"name": "Dr. Oliver Morris", "role": "Doctor", "specialization": "Allergology", "tasks": ["Allergy Testing"]},
            {"name": "Dr. Elijah Hughes", "role": "Doctor", "specialization": "Audiology", "tasks": ["Audiology Testing"]}
        ]
    },
    "D": {
        "building": 2,
        "floor": 4,
        "rooms": ["Eye Care Room 3", "General Practice Room 3", "Blood Pressure Monitoring Room 2", "Post-surgery Care Room 3", "Physical Therapy Room 2", "Vaccination Room 3"],
        "staff": [
            {"name": "Dr. Joseph Jackson", "role": "Doctor", "specialization": "Eye Care", "tasks": ["Eye Examination"]},
            {"name": "Dr. Mark Hughes", "role": "Doctor", "specialization": "General Practice", "tasks": ["Routine Checkup", "Blood Pressure Monitoring"]},
            {"name": "Nurse Elizabeth White", "role": "Nurse", "specialization": "Blood Pressure Monitoring", "tasks": ["Blood Pressure Monitoring"]},
            {"name": "Nurse Susan Lewis", "role": "Nurse", "specialization": "Post-surgery Care", "tasks": ["Post-surgery Follow-up"]},
            {"name": "Dr. Steven Harris", "role": "Doctor", "specialization": "Physical Therapy", "tasks": ["Physical Therapy Session"]},
            {"name": "Nurse Paul Martin", "role": "Nurse", "specialization": "Vaccination", "tasks": ["Vaccination"]},
            {"name": "Dr. Michael Extra", "role": "Doctor", "specialization": "General Practice", "tasks": ["Routine Checkup", "Post-surgery Follow-up"]},
            {"name": "Dr. Aria Scott", "role": "Doctor", "specialization": "Radiology", "tasks": ["CT Scan", "MRI", "Ultrasound"]},
            {"name": "Dr. Scarlett Evans", "role": "Doctor", "specialization": "Endocrinology", "tasks": ["Glucose Tolerance Test", "Lipid Profile Test"]},
            {"name": "Dr. Zoe Edwards", "role": "Doctor", "specialization": "Gastroenterology", "tasks": ["Endoscopy", "Colonoscopy"]},
            {"name": "Dr. Stella Collins", "role": "Doctor", "specialization": "Pathology", "tasks": ["Biopsy", "Blood Work"]},
            {"name": "Dr. Isla Stewart", "role": "Doctor", "specialization": "Hepatology", "tasks": ["Liver Function Test"]},
            {"name": "Dr. Lucas Bennett", "role": "Doctor", "specialization": "Allergology", "tasks": ["Allergy Testing"]},
            {"name": "Dr. Mason Patterson", "role": "Doctor", "specialization": "Audiology", "tasks": ["Audiology Testing"]}
            
        ]
    }
}



