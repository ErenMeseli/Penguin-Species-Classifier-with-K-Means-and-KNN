# 🐧 Penguin Species Classifier with K-Means and KNN

Bu proje, **Palmer Penguins** veri setini kullanarak iki farklı makine öğrenimi yaklaşımını karşılaştırır: denetimli öğrenme (KNN) ve denetimsiz öğrenme (K-Means). Amaç, biyolojik verilere dayalı olarak penguen türlerini doğru şekilde sınıflandırmak ve bu iki yöntemin performanslarını analiz etmektir.

---

![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Platform](https://img.shields.io/badge/platform-Colab%20%7C%20Jupyter%20%7C%20Python-informational)

---

## 📌 Giriş

Makine öğrenmesi, biyolojik veri analizi gibi çok disiplinli alanlarda güçlü bir araçtır. Bu proje kapsamında, **penguenlerin biyometrik ölçümleri** kullanılarak tür sınıflandırması yapılmış, hem **denetimli** hem de **denetimsiz** algoritmalar uygulanarak sonuçlar görselleştirilmiştir.

---

## 🎯 Proje Amaçları

- Penguen türlerini K-Means ve KNN ile sınıflandırmak  
- Denetimli ve denetimsiz yöntemlerin başarı oranlarını karşılaştırmak  
- Confusion Matrix ile model uyumunu analiz etmek  

---

## 📁 Proje Yapısı

```
Penguin-Species-Classifier-with-K-Means-and-KNN/
│
├── data/                          # Veri dosyalarının bulunduğu klasör 
│   └── penguins.csv
│
├── images/                        # Grafik çıktılarının bulunduğu klasör 
│   ├── kmeans_output.png 
│   ├── knn_result.png  
│   └── confusionmatrix_output.png
│
├── main_colab.ipynb              # Google Colab uyumlu notebook
├── main.py                       # Konsol üzerinden çalıştırılabilen Python betiği
├── requirements.txt              # Gerekli kütüphaneler
├── README.md                     # Proje dökümantasyonu
```

---

## 🧠 Kullanılan Yöntemler

### 🔹 K-Means (Denetimsiz Öğrenme)
- Veri noktalarını benzerliğe göre kümeleyen algoritmadır.
- Gaga uzunluğu ve yüksekliğine göre kümeler oluşturur.
- Etiketli veri gerektirmez.

### 🔹 KNN (Denetimli Öğrenme)
- Eğitim verisindeki en yakın komşulara bakarak sınıflandırma yapar.
- Kullanıcıdan alınan ölçümlere göre tür tahmini yapılır.
- Etiketli veri gerektirir.

---

## 📚 Veri Seti

**Palmer Penguins** veri seti, üç farklı penguen türüne ait aşağıdaki özellikleri içerir:

- Gaga uzunluğu (mm)  
- Gaga yüksekliği (mm)  
- Vücut kütlesi (g)  
- Yüzgeç uzunluğu (mm)  
- Tür etiketi (Adelie, Chinstrap, Gentoo)

Kaynak: [palmerpenguins R paketi](https://allisonhorst.github.io/palmerpenguins/)

---

## 📦 Kullanılan Kütüphaneler

- `pandas`: Veri analizi  
- `numpy`: Sayısal işlemler  
- `scikit-learn`: Makine öğrenimi modelleri  
- `matplotlib`: Görselleştirme  

---

## 📊 Sonuçlar ve Grafikler

### K-Means Sonuç Görselleştirmesi:
![kmeans-cluster](images/kmeans_output.png)

- Yeni Veri: Gaga uzunluğu = 50mm, Gaga yüksekliği = 19mm  
- **K-Means Doğruluğu**: `92.73%`

---

### KNN Tahmin Sonucu:
![knn-result](images/knn_result.png)

- Yeni Veri: Gaga uzunluğu = 50mm, Gaga yüksekliği = 19mm  
- **KNN Doğruluğu**: `96.22%`

---

### Confusion Matrix:
![confusionmatrix](images/confusionmatrix_output.png)

- K-Means ve KNN tahminleri arasında **%93.02** oranında uyum gözlenmiştir.

---

## 📈 Karşılaştırma Tablosu

| Algoritma | Türü         | Doğruluk | Avantajı                     | Dezavantajı                    |
|-----------|--------------|----------|------------------------------|-------------------------------|
| K-Means   | Denetimsiz   | %92.73   | Etiketsiz verilerle çalışabilir | Tahminlerde belirsizlik olabilir |
| KNN       | Denetimli    | %96.22   | Yüksek doğruluk               | Yüksek veri hacminde yavaş olabilir |

---

## 👨‍🔬 Örnek Kullanım

```plaintext
Gaga uzunluğu (mm): 50  
Gaga yüksekliği (mm): 19  
K (KNN için): 3  
```

- K-Means Tahmini: **Chinstrap**  
- KNN Tahmini: **Chinstrap**

---

## ⚙️ Kurulum

### ✅ Google Colab (Önerilen)

1. `main_colab.ipynb` dosyasını [Colab](https://colab.research.google.com/) üzerinden açın.  
2. `penguins.csv` dosyasını veri klasörüne yükleyin.  
3. Notebook hücrelerini sırasıyla çalıştırın.  

---

### 💻 Jupyter Notebook

```bash
git clone https://github.com/ErenMeseli/Penguin-Species-Classifier-with-K-Means-and-KNN.git
cd Penguin-Species-Classifier-with-K-Means-and-KNN
pip install -r requirements.txt
jupyter notebook
```

Notebook dosyasını açın, hücreleri sırayla çalıştırın ve kullanıcı girişlerinizi yaparak sınıflandırmayı gözlemleyin.

---

### 🐍 Python CLI (Terminal)

```bash
git clone https://github.com/ErenMeseli/Penguin-Species-Classifier-with-K-Means-and-KNN.git
cd Penguin-Species-Classifier-with-K-Means-and-KNN
pip install -r requirements.txt
python main.py
```

Terminalden girilen değerlerle model tahmini yapılır ve sonuçlar yazdırılır.

---

## 🧾 Sonuç

Bu proje, Palmer Penguins veri seti üzerinde **K-Means** ve **KNN** algoritmalarını karşılaştırmalı olarak uygulamış, her iki yöntemin sınıflandırma başarısını analiz etmiştir:

- **KNN**, etiketli verilerle daha yüksek başarı sağlamış, %96.22 doğruluk oranına ulaşmıştır.  
- **K-Means**, etiket olmadan da güçlü sonuçlar vererek %92.73 doğrulukla etkili bir denetimsiz yöntem olduğunu göstermiştir.  
- **Confusion Matrix** ile modellerin %93.02 oranında aynı tahminlerde bulunduğu gösterilmiştir.

Bu bulgular, verinin yapısına ve hedefe göre uygun algoritma seçiminin önemini vurgular.

---

## 🔗 Ek Kaynaklar

- [Palmer Penguins Dataset](https://allisonhorst.github.io/palmerpenguins/)
- [Scikit-learn Belgeleri](https://scikit-learn.org/stable/documentation.html)

---

## 📄 Lisans

Bu proje MIT lisansı altında sunulmaktadır.

---