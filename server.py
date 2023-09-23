from flask import Flask, render_template, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "gsb215nzt64e68tr4e6g4gf1b35n46tez4"

# lists
months = ["january", "february", "march", "april", "may", "june", "july", "august",
          "september", "october", "november", "december"]
elements = [
    "H", "He",
    "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "K", "Ar",
    "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Ni", "Co", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
    "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe",
    "Cs", "Ba",
    "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu",
    "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn",
    "Fr", "Ra",
    "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr",
    "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
]


# functions
# basic password
def base(password):
    message = ""
    if password:
        if len(password) >= 8:
            if any(char.islower() for char in password):
                if any(char.isupper() for char in password):
                    if any(char.isdigit() for char in password):
                        if any(not char.isalnum() for char in password):
                            message = digit_sum(password)
                        else:
                            message = "password must have a special character"
                    else:
                        message = "password must have a number"
                else:
                    message = "password must have uppercase letter"
            else:
                message = "password must have lowercase letter"
        else:
            message = "password must have minimal 8 characters"
    return message


# the sum must be <number>
def digit_sum(password):
    num = 0
    for char in password:
        if char.isdigit():
            num += int(char)
    if num == 25:
        message = month(password)
    else:
        message = "sum of the all numbers must be 25"
    return message


# month
def month(password):
    password_l = password.lower()
    if any(m in password_l for m in months):
        message = leap_year(password)
    else:
        message = "password must have month"
    return message


# leap year
def leap_year(password):
    combinations = []
    message = ""
    for i in range(len(password) - 3):
        substring = password[i:i + 4]
        if substring.isdigit():
            combinations.append(substring)
    for year in combinations:
        year = int(year)
        if (year % 400 == 0) and (year % 100 == 0):
            message = calculate(password)
            break
        elif (year % 4 == 0) and (year % 100 != 0):
            message = calculate(password)
            break
        else:
            message = "password must have leap year"
    return message


# calculate
def calculate(password):
    if "35" in password:
        message = periodic_elements(password)
    else:
        message = "password must have result of (6×4)−3+(8/2)+(10−5)×2"
    return message


# periodic table
def periodic_elements(password):
    count = 0
    for element in elements:
        if element in password:
            count += 1
    if count >= 2:
        message = animal_img(password)
    else:
        message = "password must have 2 or more elements from periodic table"
    return message


# find the animal
def animal_img(password):
    if "Axolotl" in password:
        message = "OK"
    else:
        message = "password must include name of the animal on the picture"
    return message


@app.route('/')
def index():
    password = ""
    return render_template("index.html", password=password)


@app.route('/new_password', methods=["GET", "POST"])
def new_password():
    password = request.args.get("password")
    message = base(password)

    return render_template("message.html", message=message)


# run app
if __name__ == '__main__':
    app.debug = 1
    app.run()
