from icalendar import Event, Calendar
from datetime import datetime, timedelta
from faker import Faker
import random
import argparse

# Initialize faker
fake = Faker()

def generate_appointment():
    # Generate random patient name
    patient_name = fake.name()
    
    # List of mock reasons for appointments
    reasons = [
        "Routine Checkup", 
        "Flu Shot", 
        "Follow-up from Surgery", 
        "Blood Pressure Monitoring", 
        "Physical Therapy", 
        "Vaccination", 
        "Dental Checkup", 
        "Eye Examination",
        "Cardiology Consultation",
        "Dermatology Consultation",
        "Gastroenterology Consultation",
        "Endocrinology Consultation",
        "Neurology Consultation",
        "Orthopedic Consultation",
        "Psychiatry Consultation",
        "Pulmonology Consultation",
        "Radiology Consultation",
        "Urology Consultation",
        "Allergy Testing",
        "Audiology Testing",
        "Blood Work",
        "CT Scan",
        "MRI",
        "Ultrasound",
        "X-Ray",
        "Biopsy",
        "Colonoscopy",
        "Endoscopy",
        "Mammogram"
    ]
    reason = random.choice(reasons)

    # Generate random appointment date and time within working hours
    today = datetime.today()
    random_day = random.randint(0, 29)  # Random day within a month
    appointment_date = today + timedelta(days=random_day)
    
    # Ensure the appointment is on a weekday
    while appointment_date.weekday() > 4:  # 0-4 denotes Monday to Friday
        random_day = random.randint(0, 29)
        appointment_date = today + timedelta(days=random_day)
        
    start_time = datetime(appointment_date.year, appointment_date.month, appointment_date.day, random.randint(8, 18), random.choice([0, 30]))
    end_time = start_time + timedelta(minutes=30)

    # Mock locations
    block = random.choice(['A', 'B', 'C', 'D'])
    building = random.randint(1, 5)
    floor = random.randint(1, 6)
    room = random.randint(1, 10)
    location = f'Block {block} - Building {building} - Floor {floor} - Room {room}'

    # Create an iCalendar event
    event = Event()
    event.add('summary', f'Appointment for {patient_name} - {reason}')
    event.add('dtstart', start_time)
    event.add('dtend', end_time)
    event.add('description', f'Medical appointment for {patient_name} regarding {reason}')
    event.add('location', location)
    
    return event

def generate_calendar(num_appointments):
    # Create a calendar
    cal = Calendar()
    cal.add('prodid', '-//Mock Medical Appointments//')
    cal.add('version', '2.0')

    # Add random events to the calendar
    for _ in range(num_appointments):
        event = generate_appointment()
        cal.add_component(event)

    return cal

def save_calendar_to_file(cal, filename):
    # Save the calendar to an .ics file
    with open(filename, 'wb') as f:
        f.write(cal.to_ical())

def main():
    parser = argparse.ArgumentParser(description='Generate a dataset of mock medical appointments. Run the command as follows: python generate_dataset.py -n <number_of_appointments> -f <filename>. For example, python generate_dataset.py -n 1000 -f appointments.ics')
    parser.add_argument('-n', '--num_appointments', type=int, default=1000, help='Number of appointments to generate. For example, -n 1000')
    parser.add_argument('-f', '--filename', type=str, default='appointments.ics', help='Filename to save the appointments to. For example, -f appointments.ics')
    args = parser.parse_args()

    cal = generate_calendar(args.num_appointments)
    save_calendar_to_file(cal, args.filename)

    print(f"Generated {args.filename} with {args.num_appointments} mock medical appointments.")

if __name__ == "__main__":
    main()
