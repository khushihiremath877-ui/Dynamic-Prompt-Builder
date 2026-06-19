from pydantic import BaseModel

class PromptData(BaseModel):
    project: str
    skills: str