from sementic_analysis import doc_match, string_match



## The function to find string in a document based on semantic similarity

input_string = "For semiconductors used as an OCPD an active overload/over-temperature protection is required."   # the string t0 match
file_path = "11.docx" 	# path of where the file is
threshold = 0.85	# 0-1
output_format = "word"    # excel / word


# the function to match string
string_match(input_string,file_path,threshold,output_format)   



### matching 2 doc to find added, modified and deleted sentences

file_path_reference = "11.docx" 	# path of refernce  file is
file_path_target = "12.docx" 	# path of target file is
output_format_type = "word"    # excel / word


#the function to match doc
doc_match(file_path_reference,file_path_target,output_format_type)

