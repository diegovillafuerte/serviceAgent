import datetime
import random

sample_function_set = [
    {
        "name": "cancel_flight",
        "description": "Cancels a flight",
        "parameters": {
            "type": "object",
            "properties": {
                "reservation_number": {"type": "string", "description": "This is the six digit alphanumeric number that identifies the booking. E.g. 3X4Y7Z"},
                "last_name": {"type": "string", "description": "The last name of the person who made the booking. E.g. Smith"},
            },
            "required": ["reservation_number", "last_name"]
        }
    },
    {
        "name": "book_flight",
        "description": "Helps the user book a flight",
        "parameters": {
            "type": "object",
            "properties": {
                "departure_city": {"type": "string", "description": "The city of departure"},
                "destination_city": {"type": "string", "description": "The city of destination"},
                "departure_date": {"type": "string", "description": "The date of departure"},
                "return_date": {"type": "string", "description": "The date of return (optional)"},
            },
            "required": ["departure_city", "destination_city"]
        }
    },
    {
        "name": "request_refund",
        "description": "Requests a refund for a flight",
        "parameters": {
            "type": "object",
            "properties": {
                "reservation_number": {"type": "string", "description": "The reservation number for the refund request"},
                "last_name": {"type": "string", "description": "The last name of the passenger"},
                "reason": {"type": "string", "description": "The reason for the refund request"},
            },
            "required": ["reservation_number", "last_name", "reason"]
        }
    },
    {
        "name": "check_in",
        "description": "Allows a passenger to check-in for a flight",
        "parameters": {
            "type": "object",
            "properties": {
                "reservation_number": {"type": "string", "description": "The reservation number for check-in"},
                "last_name": {"type": "string", "description": "The last name of the passenger"},
            },
            "required": ["reservation_number", "last_name"]
        }
    },
    {
        "name": "file_complaint",
        "description": "Allows a passenger to file a complaint about a flight",
        "parameters": {
            "type": "object",
            "properties": {
                "reservation_number": {"type": "string", "description": "The reservation number related to the complaint"},
                "last_name": {"type": "string", "description": "The last name of the passenger"},
                "complaint_details": {"type": "string", "description": "Details of the complaint"},
            },
            "required": ["reservation_number", "last_name", "complaint_details"]
        }
    },
    {
        "name": "request_human_agent",
        "description": "Requests to speak with a human agent for support",
        "parameters": {
            "type": "object",
            "properties": {
                "request_reason": {"type": "string", "description": "Reason for requesting human agent support"},
            },
            "required": ["request_reason"]
        }
    },
    {
        "name": "flight_status",
        "description": "Requests information regarding a flight status",
        "parameters": {
            "type": "object",
            "properties": {
                "origin": {"type": "string", "description": "The origin airport code"},
                "destination": {"type": "string", "description": "The destination airport code"},
                "date": {"type": "string", "description": "The date of the flight in YYYY-MM-DD format"},
                "time": {"type": "string", "description": "The time of the flight in HH:MM format"},
                "flight_number": {"type": "string", "description": "The flight number"}
            },
            "oneOf": [
                {"required": ["origin", "destination", "date", "time"]},
                {"required": ["flight_number", "date"]}
            ],
            "required": ["request_reason"]
        }
    },
    {
        "name": "make_changes_flight",
        "description": "Make a change to an existing reservation. Doesn't include changing the date of the flight",
        "parameters": {
            "type": "object",
            "properties": {
                "reservation_number": {"type": "string", "description": "The reservation number to be changed"},
                "last_name": {"type": "string", "description": "The last name of the passenger"},
                "type_of_change": {
                    "type": "string",
                    "description": "The kind of change that the user wants to make",
                    "enum": ["select_seat", "add_bag", "change_class"]
                }
            },
            "required": ["reservation_number", "last_name"]
        }
    },
    {
        "name": "flight_date_change_options",
        "description": "If the user wants to change the date of the flight, this function will provide the options based on the current reservation. Remember to only call this function if you have the new date the user wants",
        "parameters": {
            "type": "object",
            "properties": {
                "reservation_number": {"type": "string", "description": "The number of the reservation to be changed"},
                "last_name": {"type": "string", "description": "The last name of the passenger"},
                "new_date": {"type": "string","description": "The new date for the flight. This is the most important property and it is required."}
            },
            "required": ["new_date", "reservation_number", "last_name"]
        }
    },
    {
        "name": "change_flight_date",
        "description": "Once the user decides on a new date and time for their new flight, this function will execute the change",
        "parameters": {
            "type": "object",
            "properties": {
                "reservation_number": {"type": "string", "description": "The number of the reservation to be changed"},
                "original_date_time": {"type": "string", "description": "The original date and time of the flight"},
                "new_date_time": {"type": "string","description": "The new confirmed date and time for the flight"}
            },
            "required": ["reservation_number", "original_date_time", "new_date_time"]
        }
    },
]

# Make changes to flight
def make_changes_flight(reservation_number, last_name, type_of_change):
    return f"Changing {type_of_change} for flight with reservation number {reservation_number} for {last_name}"

def make_changes_flight(reservation_number, last_name, type_of_change):
    return f"Changing {type_of_change} for flight with reservation number {reservation_number} for {last_name}"

def flight_date_change_options(reservation_number, last_name, new_date):
    current_date = datetime.datetime.now() + datetime.timedelta(days=1)
    origin = 'San Francisco (SFO)'
    destination = "Mexico city (MEX)"
    options = [
        {'Flight': 'Flight 14', 'Time of Departure': '6:05 AM', 'Price of change': 0},
        {'Flight': 'Flight 145', 'Time of Departure': '9:25 AM', 'Price of change': 436},
        {'Flight': 'Flight 34', 'Time of Departure': '11:20 AM', 'Price of change': 154},
        {'Flight': 'Flight 45', 'Time of Departure': '2:30 PM', 'Price of change': 0},
        {'Flight': 'Flight 56', 'Time of Departure': '8:00 PM', 'Price of change': 650},
        {'Flight': 'Flight 67', 'Time of Departure': '10:00 PM', 'Price of change': 192}
    ]
    # Select 2 random options
    selected_options = random.sample(options, 2)
    reply = f'Your current flight from {origin} to {destination} is on {current_date.strftime("%m/%d/%Y")} and the new date is {new_date}. Here are the options for the new flight:\n'
    for option in selected_options:
        reply += f'{option["Flight"]} departing at {option["Time of Departure"]} for ${option["Price of change"]}\n'
    return reply

def change_flight_date(reservation_number, original_date_time, new_date_time):
    return f"Flight change confirmation: Changing flight with reservation number {reservation_number} from {original_date_time} to {new_date_time}"


# Cancel flight
def cancel_flight(reservation_number, last_name):
    return f"Cancelling flight with reservation number {reservation_number} for {last_name}"

# Book flight
def book_flight(departure_city, destination_city, departure_date, return_date=None):
    return f"Success!! Booking flight from {departure_city} to {destination_city} departing on {departure_date}"

# Request refund
def request_refund(reservation_number, last_name, reason):
    return f"Requesting refund for flight with reservation number {reservation_number} for {last_name} due to {reason}"

# Check in
def check_in(reservation_number, last_name):
    return f"Checking in for flight with reservation_number {reservation_number} for {last_name}"

# File complaint
def file_complaint(reservation_number, last_name, complaint_details):
    return f"Filing complaint for flight with reservation number {reservation_number} for {last_name} with details {complaint_details}"

# Request human agent
def request_human_agent(request_reason):
    return f"Requesting human agent support due to {request_reason}"

# Flight status
def flight_status(origin, destination, date, time, flight_number=None):
    return f"Requesting flight status for {origin} to {destination} flight on {date} at {time}"


# Function mapping
function_map = {
    'cancel_flight': cancel_flight,
    'book_flight': book_flight,
    'make_changes_flight': make_changes_flight,
    'request_refund': request_refund,
    'check_in': check_in,
    'file_complaint': file_complaint,
    'request_human_agent': request_human_agent,
    'flight_status': flight_status,
    'flight_date_change_options' : flight_date_change_options,
    'change_flight_date' : change_flight_date
}

function_list = [function_map[func['name']] for func in sample_function_set if func['name'] in function_map]
