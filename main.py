
# Google Calendar Event Scheduling Using Greedy Strategy

events = [
    {"name": "Project Meeting", "start": "09:00", "end": "10:00"},
    {"name": "Lecture", "start": "09:30", "end": "10:30"},
    {"name": "Team Discussion", "start": "10:00", "end": "11:00"},
    {"name": "Lunch Break", "start": "11:00", "end": "12:00"},
    {"name": "Coding Session", "start": "10:30", "end": "12:00"},
    {"name": "Lab Session", "start": "12:00", "end": "13:30"},
    {"name": "Presentation", "start": "13:00", "end": "14:00"},
    {"name": "Study Group", "start": "14:00", "end": "15:00"}
]


def to_minutes(time):
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes


def display_events():
    print("\nAvailable Events:")
    print("-" * 45)

    for event in sorted(events, key=lambda e: e["start"]):
        print(
            f'{event["name"]:<20} '
            f'{event["start"]} - {event["end"]}'
        )


def schedule_events():
    # Greedy strategy: select events that finish earliest
    sorted_events = sorted(
        events,
        key=lambda event: to_minutes(event["end"])
    )

    selected = []
    last_end_time = 0

    for event in sorted_events:
        start_time = to_minutes(event["start"])
        end_time = to_minutes(event["end"])

        if start_time >= last_end_time:
            selected.append(event)
            last_end_time = end_time

    print("\nOptimized Event Schedule")
    print("-" * 45)

    for event in selected:
        print(
            f'{event["name"]:<20} '
            f'{event["start"]} - {event["end"]}'
        )

    print("-" * 45)
    print("Total events scheduled:", len(selected))
    print("Strategy: Greedy Activity Selection")


while True:
    print("\n===== Google Calendar Event Scheduler =====")
    print("1. Display Available Events")
    print("2. Generate Optimized Schedule")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_events()

    elif choice == "2":
        schedule_events()

    elif choice == "3":
        print("Exiting Google Calendar Event Scheduler.")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
