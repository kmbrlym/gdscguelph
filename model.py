import google.generativeai as genai
from pdfparser import *

API_KEY = '' #Add API key here
genai.configure(api_key=API_KEY)

def generate(): 
  multimodal_model = genai.GenerativeModel("gemini-1.0-pro")
  # response = multimodal_model.generate_content("Please grade the paper by assigning points to each sentence. For each sentence, please provide feedback by saying (+1) followed by the sentence if it deserves a point, or (+0) if it doesn't. %s", %text)   
  prompt = (f"Using this marking scheme {parse_marking_scheme()}, grade this paper {parse_answer()}. Make sure to indicate precisely where the student gained or lost a point and provide feedback.")
  response = multimodal_model.generate_content(prompt)
  print(response.text)
  return response.text
#"Please grade the paper by assigning points to each sentence. For each sentence, please provide feedback by saying 'Positive' followed by a positive remark, such as 'Well explained' or 'Clear and concise', and then specify the number of points awarded using the '+' symbol. If the sentence does not meet the criteria, please provide feedback by saying 'Negative' followed by a constructive comment, and then specify the number of points lost using the '-' symbol."
