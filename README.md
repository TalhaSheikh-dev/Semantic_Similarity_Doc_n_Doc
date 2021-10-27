# Semantic_Similarity_Doc_n_Doc
Semantic similarity code that can match a string within a document or a document with document giving added, modified and deleted sentences

```python
## The function to find string in a document based on semantic similarity

input_string = "For semiconductors used as an OCPD an active overload/over-temperature protection is required."   # the string t0 match
file_path = "11.docx" 	# path of where the file is
threshold = 0.85	# 0-1
output_format = "word"    # excel / word


# the function to match string
string_match(input_string,file_path,threshold,output_format)   
```
