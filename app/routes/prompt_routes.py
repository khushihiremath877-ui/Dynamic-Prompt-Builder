from fastapi import APIRouter
from app.schemas.prompt_schema import PromptData
from app.services.prompt_service import generate_prompt

router = APIRouter()

@router.post("/build-prompt")
def build_prompt(data: PromptData):

    prompt = generate_prompt(
        data.project,
        data.skills
    )

    return {"prompt": prompt}