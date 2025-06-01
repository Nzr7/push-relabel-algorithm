
# Push-Relabel Algoritmasının Adım Adım Görsel Açıklaması

Bu belgede, Push-Relabel algoritmasının temel adımları görsel destekle açıklanmaktadır. Amaç, algoritmanın nasıl çalıştığını kullanıcıya anlaşılır şekilde sunmaktır.

---

## 🎯 Başlangıç: Ön Yükleme (Preflow Initialization)
- Source düğümünün yüksekliği toplam düğüm sayısı kadar yapılır (h[source] = |V|).
- Source düğümünden çıkış yapan tüm kenarlara mümkün olan maksimum akış gönderilir.
- Komşu düğümler `excess` akışla dolar.

📌 **Görsel 1:** Başlangıçta Source düğümünden çıkan akışlar

![Başlangıç](images/init.png)

---

## 🔄 Push Adımı
- Bir düğümün `excess` akışı varsa ve komşusunda kapasite boşluğu varsa, akış o düğüme itilir.
- Bu işlem düğümler arasında lokal olarak gerçekleşir.

📌 **Görsel 2:** Fazlalık akışın komşuya itilmesi

![Push](images/push_step.png)

---

## 📈 Relabel Adımı
- Eğer hiçbir komşuya push yapılamıyorsa, düğümün yüksekliği artırılır.
- Böylece daha fazla akışa yol açacak potansiyel yaratılır.

📌 **Görsel 3:** Düğüm yüksekliği arttırılıyor (relabel işlemi)

![Relabel](images/relabel_step.png)

---

## 🏁 Sink'e Ulaşım
- Sink düğümüne gelen toplam akış, maksimum akışı gösterir.
- Tüm düğümler için push ve relabel işlemleri tamamlanana kadar döngü devam eder.

📌 **Görsel 4:** Maksimum akış değerine ulaşılması

![Sink](images/sink_arrival.png)

---

## 🔗 Bağlantılar
- Proje Kaynağı: [GitHub Repo](https://github.com/Nzr7/push-relabel-algoritmasi.git)
- Rapor: `push_relabel_raporu.pdf` içerisinde özet bilgiler yer almaktadır.
- Opsiyonel: Görsel adımların animasyonlu hali YouTube'a eklenebilir.

---

**Not:** `images/` klasörüne görselleri eklemeyi unutmayın. Örnek `.png` dosyaları matplotlib ile oluşturulabilir veya çizimle hazırlanabilir.
