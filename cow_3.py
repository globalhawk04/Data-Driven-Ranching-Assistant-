import json

f = open('daily_wf_GHCND:USW00013966.json')

# returns JSON object as
# a dictionary
data = json.load(f)


for key in data:
	#print(key)
	#print(key['datatype'])
	if 'TMAX' in key['datatype']:
		print((key['value']/10) * (9/5) +32)
	if 'TMIN' in key['datatype']:
		print((key['value']/10) * (9/5) +32)



	#for datatype in key['datatype']:
		#print(datatype)
    #store = 0
    #matches = []
    #for key_words in search_terms:
        #if key_words.lower() in key['text']: