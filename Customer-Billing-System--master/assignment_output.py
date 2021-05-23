from collections import Counter  ##  Counter is a container that will hold the count of each of the elements present in the container

user_names =[
                                  ## list items
            "sachin tweet_id_1", 
			"sehwag tweet_id_2", 
			"sachin tweet_id_3", 
			"sachin tweet_id_4"]


def mainfunction():
	
	uniq_names = [pref_names.split()[0] for pref_names in user_names] 

	times = Counter(uniq_names) 
	repeat = times.values() 

	for element in set(repeat): 
		dupl = ([(key, value) for
				key, value in sorted(times.items()) if
				value == element]) 
		
		if len(dupl) > 1: 
			for (key, value) in dupl: 
				print (key,'',value) 
		max_value = max(times.values()) 
		temp_max_result = [(key, value) for
						key, value in sorted(times.items()) if
						value == max_value] 
		
		if temp_max_result != dupl: 
			for (key,value) in temp_max_result: 
				print (key,'',value) 
				
mainfunction()