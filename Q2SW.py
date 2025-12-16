from js import document   # THIS is the key line

def generate(e):
#names (personal info)
    first_name = document.getElementById("First_Name").value
    last_name = document.getElementById("Last_Name").value

#grades
    science = float(document.getElementById("science").value)
    math = float(document.getElementById("math").value)
    english = float(document.getElementById("english").value)
    ss = float(document.getElementById("ss").value)
    ict = float(document.getElementById("ict").value)
    music = float(document.getElementById("music").value)

#show the grades
    document.getElementById("message").innerText = f"""
Grades:
Science : {science}
Math    : {math}
English : {english}
SS      : {ss}
ICT     : {ict}
Music   : {music}
"""

#gwa calculator  
    weighted_sum = (
        science * 5 +
        math * 5 +
        english * 5 +
        ss * 3 +
        ict * 2 +
        music * 1
    )

    gwa = weighted_sum / 21

#displays the personal info and computed gwa
    document.getElementById("output1").innerText = (
        f"Name: {first_name} {last_name}\n"
        f"GWA: {gwa:.2f}"
    )
