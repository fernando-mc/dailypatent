#this uses python3

import random

patent_areas = "Utility", "Design"

def rand_pat_area():
	area = patent_areas[(randrange(2))]
	print(area)
	return area

def url_generators(an_area):
	if an_area == patent_areas[0]:
		final_url = "https://www.google.com/patents/US"+ str(random.randrange(9247000))
		return final_url
		print(final_url)
	elif an_area == patent_areas[1]:
		final_url = "https://www.google.com/patents/USD"+ str(random.randrange(748365))
		return final_url
		print(final_url)
	else:
		print("Somehow you broke me!")




