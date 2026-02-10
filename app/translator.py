import config
from app.models import model_manager

def translate_text(text: str, target_lang: str):
    model, tokenizer = model_manager.load()

    tgt_code = config.LANG_MAP[target_lang]
    forced_bos_token_id = tokenizer.convert_tokens_to_ids(tgt_code)

    inputs = tokenizer(text, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        forced_bos_token_id=forced_bos_token_id,
        max_length=128,
        num_beams=5
    )

    translation = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
    return translation
