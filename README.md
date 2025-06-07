#🐧 Penguin Species Classifier with K-Means and KNN
Bu proje, Palmer Penguins veri seti kullanılarak penguen türlerinin sınıflandırılmasını amaçlamaktadır. Hem denetimli (KNN) hem de denetimsiz (K-Means) makine öğrenme algoritmaları kullanılarak sınıflandırma yapılmakta ve sonuçlar karşılaştırılmaktadır.

📊 Kullanılan Yöntemler
🔹 K-Means (K-Ortalamalar) Kümeleme
K-Means, denetimsiz bir makine öğrenimi algoritmasıdır. Veri noktalarını benzerliklerine göre önceden belirlenen k adet kümeye ayırır. Etiketli verilere ihtiyaç duymadan çalışır. Bu projede penguenlerin gaga uzunluğu ve gaga yüksekliği gibi özellikleri kullanılarak kümeler oluşturulmakta ve bu kümeler türlerle karşılaştırılmaktadır.

🔹 KNN (K-Nearest Neighbors)
KNN, denetimli bir sınıflandırma algoritmasıdır. Eğitim verileri ile çalışır. Yeni bir veri noktası, eğitim verisindeki en yakın k komşusuna göre sınıflandırılır. Bu projede kullanıcının girdiği biyolojik ölçülere göre hangi türe ait olduğunu tahmin eder.

📁 Proje Yapısı
bash
Kopyala
Düzenle
penguin-classifier/
│
├── data/
│   └── penguins.csv                  # Veri seti
│
├── main.py                           # Konsol üzerinden çalıştırılabilir Python dosyası
├── palmerpenguins_kmeansclustering-knn.ipynb   # Jupyter Notebook dosyası
├── requirements.txt                  # Gerekli Python kütüphaneleri listesi
└── README.md                         # Proje açıklamaları
⚙️ Kurulum
Projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyin:

Bu projeyi klonlayın:

sql
Kopyala
Düzenle
git clone https://github.com/ErenMeseli/Penguin-Species-Classifier-with-K-Means-and-KNN.git
cd Penguin-Species-Classifier-with-K-Means-and-KNN
Gerekli kütüphaneleri yükleyin:

nginx
Kopyala
Düzenle
pip install -r requirements.txt
▶️ Kullanım
Notebook Üzerinden:
palmerpenguins_kmeansclustering-knn.ipynb dosyasını Jupyter Notebook ya da Google Colab ile açın.

Tüm hücreleri sırayla çalıştırın.

Gaga uzunluğu, gaga yüksekliği ve K değeri girerek sınıflandırmayı test edin.

Konsol Üzerinden:
css
Kopyala
Düzenle
python main.py
Komut satırından çalıştırıldığında sizden bazı değerler istenir:

Gaga uzunluğu (float)

Gaga yüksekliği (float)

K değeri (pozitif tam sayı)

Bu girdilere göre hem K-Means hem KNN algoritmaları ile tahmin yapılır ve sonuçlar karşılaştırılır.

📈 Sonuçlar
KNN algoritması yüksek doğruluk oranları ile tahmin yapar.

K-Means ise sınıflandırmasız şekilde kümeler oluşturur.

Confusion Matrix kullanılarak tahmin başarımı görselleştirilir.

İki yöntem arasındaki performans farkı analiz edilir.

📦 Kullanılan Kütüphaneler
pandas

numpy

scikit-learn

matplotlib

📚 Veri Seti
Bu proje, Palmer Penguins veri setini kullanmaktadır. Set; üç farklı penguen türü (Adelie, Chinstrap, Gentoo) hakkında biyolojik ölçümler içerir. Özellikler arasında gaga uzunluğu, gaga yüksekliği, vücut kütlesi, yüzgeç uzunluğu gibi veriler yer alır. Bu veri seti, palmerpenguins R paketi üzerinden sağlanmıştır.

✍️ Yazar
Eren Meseli
📧 GitHub: https://github.com/ErenMeseli

📝 Lisans
Bu proje MIT lisansı ile lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına göz atabilirsiniz.