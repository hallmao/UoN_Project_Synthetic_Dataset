from icalendar import Event, Calendar
from datetime import datetime, timedelta
from faker import Faker
import random
import argparse
from templates.templates import TEMPLATES, LOCATIONS_AND_STAFF

# Initialize faker
fake = Faker()

def generate_appointment():
    # Generate random patient name
    patient_name = fake.name()
    
    # Select a random template
    template_id = random.choice(list(TEMPLATES.keys()))
    template = TEMPLATES[template_id]
    reason = random.choice(template["reasons"])

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

    # Check which blocks have a "staff" who is able to handle those "tasks" the same as "reason". 
    # Select only blocks that have at least one "staff" who can do the same "tasks" as "reason"
    suitable_blocks = []
    for block, details in LOCATIONS_AND_STAFF.items():
        print(f"Checking block: {block}")
        for staff in details["staff"]:
            print(f"Checking staff: {staff}")
            tasks = staff["tasks"]
            if reason in tasks:
                print(f"Found suitable staff: {staff} in block: {block}")
                suitable_blocks.append(block)
                break
    if not suitable_blocks:
        raise ValueError(f"No suitable block found for reason: {reason}")
    print(f"Suitable blocks: {suitable_blocks}")
    block = random.choice(suitable_blocks)
    print(f"Selected block: {block}")
    building = LOCATIONS_AND_STAFF[block]["building"]
    floor = LOCATIONS_AND_STAFF[block]["floor"]
    room = random.choice(LOCATIONS_AND_STAFF[block]["rooms"])
    location = f'Block {block} - Building {building} - Floor {floor} - Room {room}'

    # Select a staff member who specializes in the reason for the appointment
    staff_members = []
    for staff in LOCATIONS_AND_STAFF[block]["staff"]:
        tasks = staff["tasks"]
        print(f"Comparing {reason} with {tasks}")
        if reason in tasks:
            staff_members.append(staff)
    if not staff_members:
        raise ValueError(f"No staff member found for reason: {reason}")
    staff_member = random.choice(staff_members)
    doctor = f'{staff_member["name"]} ({staff_member["role"]}, {staff_member["specialization"]})'

    # Create an iCalendar event
    event = Event()
    event.add('summary', template["summary"].format(patient_name=patient_name, reason=reason))
    event.add('dtstart', start_time)
    event.add('dtend', end_time)
    event.add('description', template["description"].format(patient_name=patient_name, reason=reason))
    event.add('location', location)
    event.add('attendee', doctor)
    event.add('organizer', doctor)  # Add the staff member as the organizer of the event
    
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
