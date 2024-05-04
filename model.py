import google.generativeai as genai
from pdfparser import *

API_KEY = 'AIzaSyBj3uMBj_Y3yoCyH0WVUA_ml6cDwoihads' #Add API key here
genai.configure(api_key=API_KEY)

def test(): 
  multimodal_model = genai.GenerativeModel("gemini-1.0-pro")
  response = multimodal_model.generate_content("Give me the pros and cons of hiring this candidate: %s" %text)   
  print(response.text)

test()