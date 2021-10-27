# Semantic_Similarity_Doc_n_Doc
Semantic similarity code that can match a string within a document or a document with document giving added, modified and deleted sentences


The code is used to do 2 different things
1 - Find a string in the document
2 - Match a document with other document


# Finding a string in the document
The Matching is based on semantic similarity and not just word matching. Bert model is used to find the match between text and document.  The output will be a document report which will laid down all the matching of the given sentence within document based on the threshold provided.
similarity_report.docx is the reference file repository for the report

```python
## The function to find string in a document based on semantic similarity

input_string = "The string text"   # the string t0 match
file_path = "file_to_find_in.docx" 	# path of where the file is  pdf/docx
threshold = 0.85	# 0-1
output_format = "word"    # excel / word


# the function to match string
string_match(input_string,file_path,threshold,output_format)   
```
# Match a document with other document
The document matching is also based on semantic similarity and it works sentence by sentence. It generates a report that gives the Added, modified and deleted sentences according to the given document. The first document is consider as the main document and the according to this document match is consider in reference document.
similarity_report_doc.docx is the reference file repository for the report

```python
file_path_reference = "file_to_match.docx" 	# path of refernce  file is pdf/docx
file_path_target = "file_to_match_with.docx" 	# path of target file is  pdf/docx
output_format_type = "word"    # excel / word


#the function to match doc
doc_match(file_path_reference,file_path_target,output_format_type)
```
