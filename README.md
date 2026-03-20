# 🧠 Classificador Jurídico com IA Projeto de Machine Learning para classificar textos jurídicos em categorias como: 
- 📄 Contrato
- - 📝 Petição -
  -  ⚖️ Lei - ❓ Outros
  -   ## 🚀 Tecnologias
  -    - Python
       -  - Pandas
          -  - Scikit-learn
             -  - NLP (CountVectorizer)
                - - Naive Bayes
    - ## 📊 Como funciona 1. Os textos são transformados em números usando CountVectorizer
    -  2. Um modelo Multinomial Naive Bayes é treinado
       3. 3. O modelo aprende padrões de linguagem jurídica
          4.  4. Novos textos são classificados automaticamente
              5. ## ▶️ Como executar
bash
pip install -r requirements.txt
python src/train.py
python src/predict.py
