#this uses python3

import random

patent_areas = "Utility", "Design", "Plant", "Reissue", "Defensive Publication", "Statutory Invention Registration", "Re-examination", "Additional Improvement"

def say_hi():
	print("hello!")

def rand_range(i_range):
	patent_type_random_number = random.randrange(0,i_range)
	return patent_type_random_number

def rand_pat_area():
	area = patent_areas[(rand_range(7))]
	print(area)
	return area

def generators(an_area):
	if an_area == patent_areas[0]:
		result = random.choice("1234567890")
		final_result = result * 7
		return final_result
		print final_result
