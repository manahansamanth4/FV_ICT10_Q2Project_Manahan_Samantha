from pyscript import display, Element

# Set page title
document.getElementById("School Club Information", target="webtitle")

#club data 
club_info = {
    "MB": {
        "Name": "Marching Band",
        "Description": "A club that lets students showcase their talents in playing instruments.",
        "Time": "Tuesday and Wednesday, 3:00–4:30 PM",
        "Location": "Band Room",
        "Advisor": "Mr. Emilio Alumno",
        "Number of Members": "30",
        "Category": "Non Academic"
    },
    "GC": {
        "Name": "Glee Club",
        "Description": "A club that lets students showcase their talents in singing.",
        "Time": "Monday, 3:00–5:00 PM",
        "Location": "High School Music Room",
        "Advisor": "Mr. Denver Martin",
        "Number of Members": "20",
        "Category": "Non Academic"
    },
    "DC": {
        "Name": "Dance Club",
        "Description": "A club that lets students showcase their talents in dancing.",
        "Time": "Tuesday, 3:00–5:00 PM",
        "Location": "Teatro Preciosa",
        "Advisor": "Mr. Alfred Cases",
        "Number of Members": "27",
        "Category": "Non Academic"
    },
    "SC": {
        "Name": "Science Club",
        "Description": "A club that lets students learn and investigate about the world.",
        "Time": "Tuesday, 3:00–4:00 PM",
        "Location": "Room 404",
        "Advisor": "Ms. Jameelyn Maramag",
        "Number of Members": "20",
        "Category": "Academic"
    },
    "MC": {
        "Name": "Math Club",
        "Description": "A club that lets students practice their skills in numbers.",
        "Time": "Monday, 2:30–3:00 PM",
        "Location": "Room 404",
        "Advisor": "Mr. Nichol Gabuya",
        "Number of Members": "20",
        "Category": "Academic"
    },
    "CAC": {
        "Name": "Communication Arts Club",
        "Description": "A club for students who do creative writing.",
        "Time": "Wednesday and Friday, 3:00–4:00 PM",
        "Location": "Room 406",
        "Advisor": "Ms. Yannis Fernandez",
        "Number of Members": "23",
        "Category": "Academic"
    },
    "SSC": {
        "Name": "Social Studies Club",
        "Description": "A club that lets students showcase their thinking skills.",
        "Time": "Tuesday, 3:00–4:00 PM",
        "Location": "Room 409",
        "Advisor": "Mr. Lim",
        "Number of Members": "20",
        "Category": "Academic"
    },
    "COCC": {
        "Name": "COCC",
        "Description": "A club for cadets.",
        "Time": "Wednesday, 2:30–4:00 PM",
        "Location": "Quadrangle / Teatro Preciosa",
        "Advisor": "SSgt. Jemima David PA (Res)",
        "Number of Members": "20",
        "Category": "Non Academic"
    },
    "VV": {
        "Name": "Volleyball Varsity",
        "Description": "A club for students who learn how to play volleyball.",
        "Time": "Wednesday, 3:00–5:00 PM",
        "Location": "Quadrangle",
        "Advisor": "Mr. Adrian Ruiz",
        "Number of Members": "20",
        "Category": "Non Academic"
    },
    "BV": {
        "Name": "Basketball Varsity",
        "Description": "A club for students who learn how to play basketball.",
        "Time": "Monday, 3:00–4:00 PM",
        "Location": "Quadrangle",
        "Advisor": "Mr. Adrian Ruiz",
        "Number of Members": "20",
        "Category": "Non Academic"
    }
}

def show_club_info(e): #event handling
    selected_club = Element("clubs").value
    output = Element("club-info")

    info = club_info.get(selected_club)

    if info:
        text = (
            f"Name: {info['Name']}\n"
            f"Description: {info['Description']}\n"
            f"Time: {info['Time']}\n"
            f"Location: {info['Location']}\n"
            f"Advisor: {info['Advisor']}\n"
            f"Number of Members: {info['Number of Members']}\n"
            f"Category: {info['Category']}"
        )
    else:
        text = "No information available."

    output.write(text)
