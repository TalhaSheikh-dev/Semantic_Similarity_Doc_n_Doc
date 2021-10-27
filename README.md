# Semantic_Similarity_Doc_n_Doc
Semantic similarity code that can match a string within a document or a document with document giving added, modified and deleted sentences

```python
## The function to find string in a document based on semantic similarity

input_string = "The string text"   # the string t0 match
file_path = "file_to_find_in.docx" 	# path of where the file is  pdf/docx
threshold = 0.85	# 0-1
output_format = "word"    # excel / word


# the function to match string
string_match(input_string,file_path,threshold,output_format)   
```

```python
file_path_reference = "file_to_match.docx" 	# path of refernce  file is pdf/docx
file_path_target = "file_to_match_with.docx" 	# path of target file is  pdf/docx
output_format_type = "word"    # excel / word


#the function to match doc
doc_match(file_path_reference,file_path_target,output_format_type)
```
