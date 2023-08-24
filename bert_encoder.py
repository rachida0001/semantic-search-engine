from transformers import BertTokenizer, BertModel
import torch

class BERTTextEncoder:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
        self.model = BertModel.from_pretrained("bert-base-uncased")
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def encode_plots(self, plots):
        encoded_plots = self.tokenizer.batch_encode_plus(
            plots,
            max_length=512,
            padding="max_length",
            truncation=True,
            return_tensors="pt",
        )

        encoded_plots.to(self.device)

        with torch.no_grad():
            outputs = self.model(**encoded_plots)

        return outputs.pooler_output
