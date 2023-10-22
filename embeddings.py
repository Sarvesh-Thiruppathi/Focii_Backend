from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F

class Embeddings():
    # Define class-level variables for the model and tokenizer
    model = None
    tokenizer = None

    def __init__(self, modeldir: str):
        # Load the model and tokenizer if they haven't been loaded yet
        if Embeddings.model is None or Embeddings.tokenizer is None:
            print("Loading tokenizer and model for the first time")
            Embeddings.tokenizer = AutoTokenizer.from_pretrained(modeldir)
            Embeddings.model = AutoModel.from_pretrained(modeldir)

    # Mean Pooling - Take attention mask into account for correct averaging
    def meanPooling(self, model_output: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
        token_embeddings = model_output[0] # First element of model_output contains all token embeddings
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

    # Method 1: Get the embeddings of a list of sentences/words
    def getEmbeddings1(self, sentences: list) -> torch.Tensor:
        # Tokenize sentences
        encoded_input = Embeddings.tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')
        # Compute token embeddings
        with torch.no_grad():
            model_output = Embeddings.model(**encoded_input)
        # Perform pooling
        embeddings = self.meanPooling(model_output, encoded_input['attention_mask'])
        # Normalize embeddings
        embeddings = F.normalize(embeddings, p=2, dim=1)

        return embeddings

    # Method 2: Get the embeddings of a list of sentences/words and then average the embeddings
    def getEmbeddings2(self, sentences: list, et: float) -> torch.Tensor:
        # Tokenize sentences
        encoded_input = Embeddings.tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')
        # Compute token embeddings
        with torch.no_grad():
            model_output = Embeddings.model(**encoded_input)
        # Perform pooling
        embeddings = self.meanPooling(model_output, encoded_input['attention_mask'])
        # Normalize embeddings
        embeddings = F.normalize(embeddings, p=2, dim=1)
        # Method 2: Average the embeddings
        embeddings = torch.mean(embeddings, dim=0)
        embeddings = torch.add(embeddings, torch.tensor(et))

        return embeddings
