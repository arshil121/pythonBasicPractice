# # dictionaries example:
# progamming_dic = {
#     "bug": "some lorem epsm text",
#     "Function": "Many other text",
# }

# print(progamming_dic["Function"])
# progamming_dic["Loop"] = "The action of doing things over and over again"
# print(progamming_dic)
# # progamming_dic = {}
# # print(progamming_dic)
# # loop through dictionaries
# for key in progamming_dic:
#     print(key)
#     print(progamming_dic[key])

##################################################################################
# student_scores = {
#     "Harry": 84,
#     "Ron": 79,
#     "Hermione": 92,
#     "Draco": 74,
#     "Neville": 82,
# }

# print("Grades are as follows: ")
# for grade in student_scores:
#     if student_scores[grade] > 91:
#         print(f"{grade}: Outstanding")
#     elif student_scores[grade] > 81:
#         print(f"{grade}: Exceeds Expectations")
#     elif student_scores[grade] >= 75:
#         print(f"{grade}: Good")
#     else:
#         print(f"{grade}: Fail")

travel_log = [
    {"country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]},
    {"country": "Germany", "visits": 5, "cities": ["Berlin", "Hamburg", "Stuttgart"]},
]


def add_new_country(country, visits, cities):
    travel_log.append({"country": country, "visits": visits, "cities": cities})


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
