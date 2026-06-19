# Dynamic Prompt Builder

## Overview

Dynamic Prompt Builder is a web application developed using FastAPI, HTML, CSS, and JavaScript. The application allows users to enter project details and skills, then automatically generates a structured AI-ready prompt.

The project demonstrates frontend-backend communication, API development, JSON handling, and dynamic prompt generation using user-provided information.

---

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* FastAPI
* Pydantic

### Communication

* REST API
* JSON

---

## Features

* Clean and responsive user interface
* Dynamic prompt generation
* FastAPI backend integration
* JSON request and response handling
* Real-time prompt display
* User input validation

---

## Workflow

1. User enters:

   * Project Name
   * Skills Used

2. Frontend collects the input data.

3. JavaScript sends a POST request to the FastAPI backend.

4. FastAPI processes the request and generates a structured prompt.

5. The generated prompt is returned as a JSON response.

6. The prompt is displayed instantly on the webpage.

---

## API Endpoint

### Build Prompt

```http
POST /build-prompt
```

### Sample Request

```json
{
  "project": "AI Resume Builder",
  "skills": "Python, FastAPI, HTML, CSS"
}
```

### Sample Response

```json
{
  "prompt": "Generate ATS friendly bullet points.\n\nProject:\nAI Resume Builder\n\nSkills:\nPython, FastAPI, HTML, CSS\n\nRequirements:\n- Use action verbs\n- Keep points professional\n- Highlight technical skills\n- Focus on measurable impact"
}
```

---

## Sample Generated Prompt

```text
Generate ATS friendly bullet points.

Project:
AI Resume Builder

Skills:
Python, FastAPI, HTML, CSS

Requirements:
- Use action verbs
- Keep points professional
- Highlight technical skills
- Focus on measurable impact
```

---

## Project Structure

```text
Dynamic-Prompt-Builder/
│
├── main.py
├── index.html
├── requirements.txt
└── README.md
```

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

## Learning Outcomes

* FastAPI basics
* REST API development
* JSON request and response handling
* Frontend-backend integration
* Dynamic prompt generation
* Client-server communication

---

## Future Enhancements

* Multiple prompt templates
* AI-powered prompt optimization
* Prompt export functionality
* User authentication
* Prompt history storage

---

## Author

Khushi Hiremath
Reviewer Request

