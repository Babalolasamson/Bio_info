bio_info = {
    "Title":" Mr",
    "name": " Samson Babalola",
    "Address": " 101 Yoruba Road Sabon-gari, Kano State",
    "Marital Status": " Single",
    "Age": " 29years",
    "Skills": [
        "Pyton programing",
        "JavaScript",
        "HTML",
        "CSS",
        "Web Develpoment",
        "Data Analysis",
        "Microsoft Offices"
    ],
    "Profession": " Quality Analyst",
    "Years of Experience": " 3 Years",
    "Educational Backgrouund": " BSc. Food Science"}
Edited_bio_info = bio_info.pop("Skills")
for key, value in bio_info.items(): 
    print(f"{key}:{value}")
print ("My skills are: ")
for skill in Edited_bio_info:
    print("- " + skill)