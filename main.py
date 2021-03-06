import requests
import re
from os import system, name
from pyfiglet import Figlet
import inquirer
from inquirer.themes import GreenPassion
from time import sleep

from domainWiseDetails import technicalDomainDetails, designingDomainDetails, managementDomainDetails, contentDomainDetails

def clear():
	if name=='nt':
		_ = system('cls')
	else:
		_ = system('clear')

def fun(f):
	while True:
		clear()
		print(f.renderText('DSC BVP Pune'))
		print(f.renderText('Teams at DSC'))
		print("We have the following domains at DSC BVP Pune.")
		print("1. Technical (Web apps, Mobile apps, ML, Cloud, Ethical Hacking, AR / VR, Miscellaneous)")
		print("2. Designing (Designers, UI / UX designers, Video Editors)")
		print("3. Content (Content writers)")
		print("4. Management (Management and Publicity)")
		print("Know more about each domain by entering\n1 for Technical\n2 for Designing\n3 for Content\n4 for Management")
		print("5. to exit")
		e = int(input("Enter your choice "))
		if e == 1:
			clear()
			technicalDomainDetails(f)
		elif e == 2:
			clear()
			designingDomainDetails(f)
		elif e == 3:
			clear()
			contentDomainDetails(f)
		elif e == 4:
			clear()
			managementDomainDetails(f)
		elif e == 5:
			break
		input("Press enter to continue")

clear()
f = Figlet()
print(f.renderText('DSC BVP Pune'))
print("\n\n\n")
print(f.renderText("Instructions"))

print("All fields are mandatory.")
print("Make sure you have an active internet connection")
print("Press the up, down, left, right arrow keys to navigate up or down when multiple options are present. Press enter to continue.")
print("Press the up, down, left, right arrow keys to navigate up or down when multiple radio box options are present. Press space to select and enter to submit.")
print("While entering your skills, make sure to follow the format specified.")

input("\n\n\n\nPress enter to continue ")

clear()
print(f.renderText('DSC BVP Pune'))
print("\n\n\n")
print(f.renderText("Personal Details"))

personalQuestions = [
	inquirer.Text('name', message="What's your name",
		validate=lambda _, x: re.match(r"^[a-zA-Z]{4,}(?: [a-zA-Z]+){0,2}$", x),
	),
	inquirer.Text('email', message="What's your email",
		validate=lambda _, x: re.match(r"([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)", x),
	),
	inquirer.Text('phone', message="What's your phone number",
		validate=lambda _, x: re.match(r"^[0][1-9]\d{9}$|^[1-9]\d{9}$", x),
	),
	inquirer.List('stream',
		message="Which stream do you belong to?",
		choices=['CS/BS', 'Computer', 'IT', 'ENTC', 'Electronics', 'Electrical', 'Mechanical', 'Civil', 'Chemical', 'Production'],
	),
	inquirer.List('year',
		message="Which year are you in?",
		choices=["First Year", "Second Year", "Third Year", "Fourth Year"],
	)
]

personalAnswers = inquirer.prompt(personalQuestions, theme=GreenPassion())

print("\n\nPlease join our community at https://bit.ly/dscbvppune\n\n")
fun(f)
clear()
print(f.renderText('DSC BVP Pune'))
print(f.renderText("Teams"))

domainRelatedQuestions = [
	inquirer.Checkbox('domains',
		message="Select the domains you would like to be a part of (Press space to select, enter to submit)",
		choices=['Technical Team', 'Designing Team', 'Content Team', 'Management and Publicity Team'],
	),
]

domainChoiceAnswers = inquirer.prompt(domainRelatedQuestions, theme=GreenPassion())

clear()
print(f.renderText('DSC BVP Pune'))
print("\n\n\n")
print(f.renderText("Your skills"))
print("Please enter your skills either technical or non technical => ")
print("""Input should be in the form of 'Flutter', 'Django', 'Google Cloud', 'Content Writer' """)

skills = [x.replace("'", "").lstrip(" ") for x in input("Your skills => ").split(',')]

clear()
print(f.renderText('DSC BVP Pune'))
print("\n\n\n")
print(f.renderText("Your application"))

print("\n\n")
print("Name =>", personalAnswers["name"])
print("Email =>", personalAnswers["email"])
print("Phone number =>", personalAnswers["phone"])
print("Stream =>", personalAnswers["stream"])
print("year =>", personalAnswers["year"])

print("\n\nDomains you would like to be a part of => ")
for i, domain in enumerate(domainChoiceAnswers["domains"]):
	print(i + 1, "=>", domain)

print("\n\nYour skills are => ")
for i, skill in enumerate(skills):
	print(i + 1, "=>", skill)

sleep(3)

selectedDomains = ", ".join(domainChoiceAnswers["domains"])
skillsEntered = ", ".join(skills)

finalData = {
	"name": personalAnswers["name"],
	"email": personalAnswers["email"],
	"mobileNumber": personalAnswers["phone"],
	"year": personalAnswers["year"],
	"branch": personalAnswers["stream"],
	"domain": selectedDomains,
	"skills": skillsEntered
}


# DO NOT MODIFY

print("Submitting data")

postApiEndPoint = "https://01ff411d6dbe9fe7f110f796d8e116f9.m.pipedream.net"
clear()
try:
	r = requests.post(postApiEndPoint, data=finalData)
except Exception as e:
	clear()
	print(f.renderText('DSC BVP Pune'))
	print("\n\n\n")
	print(f.renderText("Uh oh"))
	print("\n\n")
	print("We faced an error while submitting your application. Please share this screenshot with the team at dscbvppune@gmail.com.")
else:
	clear()
	print(f.renderText('DSC BVP Pune'))
	print("\n\n\n")
	print(f.renderText("Success"))
	print("\n\n")
	print("We have received your application. We would contact you with further steps. Please be on the lookout for our email. :)")

