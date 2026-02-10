from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.translator import translate_text

router = APIRouter()

class TranslateRequest(BaseModel):
    text: str
    target_lang: str

@router.post("/translate")
def translate(req: TranslateRequest):
    if req.target_lang not in ["hi", "fr"]:
        raise HTTPException(status_code=400, detail="Supported: hi, fr")

    translation = translate_text(req.text, req.target_lang)

    return {
        "input": req.text,
        "target_language": req.target_lang,
        "translation": translation
    }
