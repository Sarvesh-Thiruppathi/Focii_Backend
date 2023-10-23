from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F

class Embeddings():
    '''
    ## Get the embeddings given a pretrained word embedding model
    ### Embeddings.getEmbeddings()
    #### Inputs
    -----------
    sentences (list): list of sentences/phrases/words to be embedded
    et (float): error term to be applied
    weight (float): weight to be applied
    
    #### Outputs
    -----------
    embeddings (tensor): single tensor of embeddings representing the entire
    inputted list
    '''
    # Define class-level variables for the model and tokenizer
    model = None
    tokenizer = None

    def __init__(self, modeldir: str):
        # Load the model from HuggingFace
        if Embeddings.model is None or Embeddings.tokenizer is None:
            print("Loading tokenizer and model for the first time")
            try:
                Embeddings.tokenizer = AutoTokenizer.from_pretrained(modeldir)
                Embeddings.model = AutoModel.from_pretrained(modeldir)
            except Exception as e:
                print(e)

    # Mean Pooling - Take attention mask into account for correct averaging
    def meanPooling(self, model_output: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
        token_embeddings = model_output[0] # First element of model_output contains all token embeddings
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)
    
    # Get the embeddings of a list of sentences/words and then average the embeddings
    def getEmbeddings(self, sentences: list, et: float, weight: float) -> torch.Tensor:
        '''
        Get the embeddings of a list of sentences/words
        '''
        # Tokenize sentences
        encoded_input = Embeddings.tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')
        # Compute token embeddings
        with torch.no_grad():
            model_output = Embeddings.model(**encoded_input)
        # Perform pooling
        embeddings = self.meanPooling(model_output, encoded_input['attention_mask'])
        # Normalize embeddings
        embeddings = F.normalize(embeddings, p=2, dim=1)
        # Average the embeddings
        embeddings = torch.mean(embeddings, dim=0)
        # Multiply by weight and add error term
        embeddings = torch.add(torch.mul(embeddings,weight), torch.tensor(et))

        return embeddings
