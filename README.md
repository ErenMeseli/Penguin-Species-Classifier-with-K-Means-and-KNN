# 🐧 Penguin Species Classifier with K-Means and KNN

Bu proje, Palmer Penguins veri seti kullanılarak penguen türlerinin sınıflandırılmasını amaçlamaktadır. Hem denetimli (KNN) hem de denetimsiz (K-Means) öğrenme yöntemleriyle penguen türlerini sınıflandırmayı ve bu iki yaklaşımı karşılaştırmayı sağlar.

---

## 📊 Kullanılan Yöntemler

🔹 K-Means (K-Ortalamalar) Kümeleme
K-Means, denetimsiz bir makine öğrenmesi algoritmasıdır. Veri noktalarını benzerliklerine göre **önceden belirlenmiş K adet kümeye** ayırır. Bu projede penguenlerin `gaga uzunluğu` ve `gaga yüksekliği` kullanılarak tür tahmini yapılır.

🔹 KNN (K-Nearest Neighbors)
KNN, denetimli bir öğrenme algoritmasıdır. Yeni bir örnek, eğitim setindeki **en yakın K komşusuna** göre sınıflandırılır. Bu projede kullanıcıdan alınan ölçümlere göre penguen türü tahmin edilir.

---

## ⚙️ Kurulum

Projeyi çalıştırmak için aşağıdaki adımları izleyin:

1. Bu projeyi klonlayın:

```
git clone https://github.com/ErenMeseli/Penguin-Species-Classifier-with-K-Means-and-KNN.git
cd Penguin-Species-Classifier-with-K-Means-and-KNN
pip install -r requirements.txt

```

## ▶️ Kullanım
🔬 Notebook Üzerinden:
palmerpenguins_kmeansclustering-knn.ipynb dosyasını Jupyter Notebook veya Google Colab’da açın.

Hücreleri sırasıyla çalıştırın.

Gaga uzunluğu, gaga yüksekliği ve K değeri gibi verileri girerek sınıflandırmayı deneyin.

## 🖥️ Konsol Üzerinden:
main.py dosyasını çalıştırın:

python main.py
İstenen kullanıcı girişlerini yaptıktan sonra, model tahmini ve sonuçlar görüntülenecektir.

## 📈 Sonuçlar
K-Means ve KNN algoritmalarının başarı oranları karşılaştırılır.

Confusion Matrix yardımıyla tahmin doğruluğu görselleştirilir.

İki algoritmanın tahminleri arasındaki benzerlik analiz edilir.

## 📦 Kullanılan Kütüphaneler

- **pandas**: Veri işleme
- **numpy**: Sayısal hesaplamalar
- **scikit-learn**: Makine öğrenimi algoritmaları
- **matplotlib**: Grafik ve görselleştirme

## 📚 Veri Seti
Palmer Penguins veri seti, palmerpenguins R paketi kaynaklıdır ve aşağıdaki üç penguen türüne ait biyolojik ölçümleri içerir:

 - **Adelie**
 - **Chinstrap**
 - **Gentoo**

Özellikler arasında gaga uzunluğu, gaga yüksekliği, vücut kütlesi ve yüzgeç uzunluğu gibi bilgiler bulunmaktadır.

## ✍️ Yazar
**Eren Meseli**  

🔗 [GitHub Profilim](https://github.com/ErenMeseli)

## 📝 Lisans
Bu proje **MIT Lisansı** ile lisanslanmıştır. Detaylar için `LICENSE` dosyasına göz atabilirsiniz.

