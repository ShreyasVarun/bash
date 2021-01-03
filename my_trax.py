'jai guru dev'
import trax
import numpy as np
import os

# Create a Transformer model.
# Pre-trained model config in gs://trax-ml/models/translation/ende_wmt32k.gin
def create_transformer():
    model = trax.models.Transformer(
        input_vocab_size=33300,
        d_model=512, d_ff=2048,
        n_heads=8, n_encoder_layers=6, n_decoder_layers=6,
        max_len=2048, mode='predict')
    # Initialize using pre-trained weights.
    model.init_from_file('gs://trax-ml/models/translation/ende_wmt32k.pkl.gz',
                     weights_only=True)
    return model

def tokenize_sent(sentence):
    # Tokenize a sentence.
    #sentence = 'It is nice to learn new things today!'
    tokenized = list(trax.data.tokenize(iter([sentence]),  # Operates on streams.
                                        vocab_dir='gs://trax-ml/vocabs/',
                                        vocab_file='ende_32k.subword'))[0]
    return tokenized

def decode_and_detokenize(tokenized,model):
    # Decode from the Transformer.
    tokenized = tokenized[None, :]  # Add batch dimension.
    tokenized_translation = trax.supervised.decoding.autoregressive_sample(
        model, tokenized, temperature=0.0)  # Higher temperature: more diverse results.

    # De-tokenize,
    tokenized_translation = tokenized_translation[0][:-1]  # Remove batch and EOS.
    translation = trax.data.detokenize(tokenized_translation,
                                    vocab_dir='gs://trax-ml/vocabs/',
                                    vocab_file='ende_32k.subword')
    return translation

def main():
    model = create_transformer()
    tokenized = tokenize_sent(input('enter a sentence: '))#It is nice to learn new things today!')
    translation = decode_and_detokenize(tokenized,model)
    print(translation)

if __name__ == '__main__':
    main()