from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pandas as pd
import numpy as np
from scipy.special import softmax
import os

class SentimentAnalyzer:
    def __init__(self, model_name="nlptown/bert-base-multilingual-uncased-sentiment"):
        print("Cargando modelo...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        print("Modelo cargado")

    def map_to_sentiment(self, score_idx):
        if score_idx <= 1:
            return 'negative'
        elif score_idx == 2:
            return 'neutral'
        else:
            return 'positive'

    def predict_sentiment(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True)
        with torch.no_grad():
            logits = self.model(**inputs).logits
        probs = softmax(logits.numpy()[0])
        pred_idx = np.argmax(probs)
        return self.map_to_sentiment(pred_idx)

    def label_tokenized_columns(self, input_path, output_folder="../../data/analice"):
        print(f"\n📁 Procesando archivo: {input_path}")
        df = pd.read_csv(input_path)
        print(f"Tiene {df.shape[0]} filas y {df.shape[1]} columnas")    

        tokenized_cols = [col for col in df.columns if col.endswith("_tokenized")]

        if not tokenized_cols:
            print("⚠️ No se encontraron columnas '_tokenized'. Nada que hacer.")
            return

        for col in tokenized_cols:
            print(f"🧪 Analizando columna: {col}")
            df[col] = df[col].astype(str)  
            labeled_col = col.replace("_tokenized", "_labeled")
            df[labeled_col] = df[col].apply(lambda x: self.predict_sentiment(x) if pd.notnull(x) else None)

        file_name = os.path.basename(input_path)
        output_path = os.path.join(output_folder, file_name.replace(".csv", "_labeled.csv"))

        os.makedirs(output_folder, exist_ok=True)
        df.to_csv(output_path, index=False)
        print(f"Archivo guardado con sentimientos en: {output_path}")
    
    def analize_all(self):
        self.label_tokenized_columns("../data/processed/comments_processed.csv")
        self.label_tokenized_columns("../data/processed/posts_processed.csv")
        self.label_tokenized_columns("../data/processed/subreddit_info_processed.csv")
        self.label_tokenized_columns("../data/processed/top_posts_processed.csv")
        self.label_tokenized_columns("../data/processed/ultimos_posts_processed.csv")

