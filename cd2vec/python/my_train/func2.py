def append_list_as_row(file_name, list_of_elem):
	# Open file in append mode
	with open(file_name, 'a+', newline='',encoding='utf-8') as write_obj:
	   csv_writer = writer(write_obj)
	   csv_writer.writerow(list_of_elem)
