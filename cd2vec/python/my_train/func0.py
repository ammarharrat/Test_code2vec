def get_non_flaky_list(non_flaky_list):
	count = 0
	List_Url =[]
	List_code_source = []
	for index, row in non_flaky_list.iterrows():
	
		Url = re.sub('https://', 'https://raw.', row['Project_URL'])
		Url = Url + "/master/" + row['Test_filename']
		filename =  row['Test_filename']
		r = requests.get(Url)
		temp = r.content.decode("utf-8")
		new_temp = re.sub(' +', ' ',''.join(temp))
		str_compile = row['Test_funcname']
		start = row['Test_funcname']
		end = 'def'
		str_compile = start 
		extract_func = re.findall(str_compile, new_temp)
		if len(extract_func) !=  0:
		    List_code_source.append('def ' + extract_func[0] + (new_temp.split(start))[1].split(end)[0])
	return List_code_source