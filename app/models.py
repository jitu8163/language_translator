from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import config

class ModelManager:
    def __init__(self):
        self.model = None
        self.tokenizer = None

    def load(self):
        if self.model is None:
            self.tokenizer = AutoTokenizer.from_pretrained(config.MODEL_NAME)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(
                config.MODEL_NAME,
                torch_dtype=None,
                device_map="auto"  # important for big models
            )
        return self.model, self.tokenizer

model_manager = ModelManager()
