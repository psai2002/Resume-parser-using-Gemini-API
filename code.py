from pypdf import PdfReader
import pandas as pd
import requests
import google.generativeai as genai
import os
import json

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

pdf_file = 'Resume.pdf'
text = ''
with open(pdf_file, 'rb') as file:
	reader = PdfReader(file)
	for page in reader.pages:
		text += page.extract_text() + '\n'
	
model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config={"response_mime_type":"application/json"})
response = model.generate_content(f"from {text} extract name, email, phone, college, skills. give json data")
data = response.text
dictionary = json.loads(data)
df = pd.DataFrame([dictionary])
print(df)

