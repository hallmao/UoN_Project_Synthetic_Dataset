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
        "reasons": ["Routine Checkup", "Follow-up from Surgery", "Blood Pressure Monitoring", "Physical Therapy", "Vaccination", "Dental Checkup", "Eye Examination", "Cardiology Consultation", "Neurology Consultation", "Orthopedic Consultation"]
    }
}
