# 🐧 Penguin Species Classifier with K-Means and KNN

Bu proje, Palmer Penguins veri seti kullanılarak penguen türlerinin sınıflandırılmasını amaçlamaktadır. Hem denetimli (KNN) hem de denetimsiz (K-Means) öğrenme yöntemleriyle penguen türlerini sınıflandırmayı ve karşılaştırmayı sağlar.

---

## 📊 Kullanılan Yöntemler

### 🔹 K-Means (K-Ortalamalar) Kümeleme
K-Means, denetimsiz bir makine öğrenimi algoritmasıdır. Veri noktalarını benzerliklerine göre **önceden belirlenen k adet kümeye** ayırır. Bu projede penguenlerin `gaga uzunluğu` ve `gaga yüksekliği` bilgileri kullanılarak tür tahmini yapılır.

### 🔹 KNN (K-Nearest Neighbors)
KNN, denetimli bir sınıflandırma algoritmasıdır. Yeni bir veri noktası, eğitim verisindeki **en yakın k komşusuna** göre sınıflandırılır. Kullanıcının girdiği değerlerin hangi türe ait olduğunu tahmin ederken bu yöntemi kullanıyoruz.

---

## 📁 Proje Yapısı

penguin-classifier/
│
├── data/
│ └── penguins.csv # Veri seti
│
├── main.py # Ana Python dosyası (konsol üzerinden çalıştırılabilir)
├── palmerpenguins_kmeansclustering-knn.ipynb # Jupyter Notebook (etkileşimli anlatım)
├── requirements.txt # Gerekli Python kütüphaneleri
└── README.md # Proje açıklamaları
---

## ⚙️ Kurulum

Projeyi çalıştırmak için aşağıdaki adımları izleyin:

1. Bu projeyi klonlayın:
```bash
git clone https://github.com/ErenMeseli/Penguin-Species-Classifier-with-K-Means-and-KNN.git
Proje klasörüne geçin:

bash
Kopyala
Düzenle
cd Penguin-Species-Classifier-with-K-Means-and-KNN
Gerekli kütüphaneleri yükleyin:

bash
Kopyala
Düzenle
pip install -r requirements.txt
▶️ Kullanım
Notebook Üzerinden:
palmerpenguins_kmeansclustering-knn.ipynb dosyasını Jupyter Notebook veya Google Colab'da açın.

Hücreleri sırayla çalıştırın.

Sonlara doğru gaga uzunluğu, yüksekliği ve K değeri gibi verileri girerek kendi sınıflandırmanızı deneyin.

Konsol Üzerinden:
main.py dosyasını çalıştırın:

bash
Kopyala
Düzenle
python main.py
Sizden istenen kullanıcı girişlerini yapın.

📈 Sonuçlar
K-Means ve KNN algoritmalarının doğruluk oranları karşılaştırılır.

Confusion Matrix ile tahmin başarımı görselleştirilir.

K-Means ve KNN tahminlerinin birbirine ne kadar uyumlu olduğu analiz edilir.

📦 Kullanılan Kütüphaneler
pandas

numpy

scikit-learn

matplotlib

📚 Veri Seti
Palmer Penguins veri seti, palmerpenguins R paketi aracılığıyla sunulmaktadır. Bu veri seti, üç farklı penguen türü hakkında biyolojik ölçümler içermektedir:

Adelie

Chinstrap

Gentoo

✍️ Yazar
Eren Meseli
📧 GitHub Profilim

📝 Lisans
Bu proje MIT lisansı ile lisanslanmıştır. Ayrıntılar için LICENSE dosyasına göz atabilirsiniz.

yaml
Kopyala
Düzenle