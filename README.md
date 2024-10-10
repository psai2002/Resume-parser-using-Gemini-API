**Description:**
1. Give a resume(.pdf) as input in the code.
2. The given resume is converted into text data.
3. The textual resume data is passed then to Gemini API.
4. Extracts name, email, phone, college, skills from the data passed to Gemini API.
5. Finally, displays the extracted output in pandas dataframe.

* The code is written in python.
* Install python in your system.
* Copy your gemini_api_key and export your key:
  - In ubuntu:
  {
    export "GEMINI_API_KEY=your_api_key"
  }

**Import modules:**
- pandas
- requests
- google-generativeai
- pypdf
- json
- os

Gemini API: https://ai.google.dev/
