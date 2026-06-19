def generate_prompt(project, skills):

    prompt = f"""
Generate ATS friendly bullet points.

Project:
{project}

Skills:
{skills}

Requirements:
- Use action verbs
- Keep points professional
- Highlight technical skills
- Focus on measurable impact
"""

    return prompt