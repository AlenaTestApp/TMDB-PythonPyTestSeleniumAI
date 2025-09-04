🎬 TMDB Automation Project

Overview
This project automates test scenarios for TMDB using Python and PyTest, following a Page Object Model (POM) structure. 
The framework supports advanced scenarios, including AI-powered image comparison.

🖼️ AI Image Comparison

🌐 Selenium – navigate the web and collect actor images.

🖌️ Pillow (PIL) – load images from local files or URLs.

👁️ MTCNN – detect and align faces in images.

🤖 InceptionResnetV1 (Facenet-PyTorch) – convert faces into numerical embeddings.

📊 PyTorch (cosine similarity) – compare embeddings to determine image matches.

