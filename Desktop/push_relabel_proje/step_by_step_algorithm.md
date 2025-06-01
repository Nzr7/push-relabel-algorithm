
# Push-Relabel Algoritmasının Adım Adım Görsel Açıklaması

Bu belgede, Push-Relabel algoritmasının temel adımları görsel destekle açıklanmaktadır. Amaç, algoritmanın nasıl çalıştığını kullanıcıya anlaşılır şekilde sunmaktır.

---

1-) Başlangıç: Ön Yükleme (Preflow Initialization)
- Source düğümünün yüksekliği toplam düğüm sayısı kadar yapılır (h[source] = |V|).
- Source düğümünden çıkış yapan tüm kenarlara mümkün olan maksimum akış gönderilir.
- Komşu düğümler `excess` akışla dolar.

Görsel 1: Başlangıçta Source düğümünden çıkan akışlar
![step_push_init](https://github.com/user-attachments/assets/f2ce1499-600f-4d62-a33f-25aef5c0880f)

---

2-) Push Adımı
- Bir düğümün `excess` akışı varsa ve komşusunda kapasite boşluğu varsa, akış o düğüme itilir.
- Bu işlem düğümler arasında lokal olarak gerçekleşir.
![step_sink_arrival](https://github.com/user-attachments/assets/140cc33b-6bea-4f5e-9f13-b2b91a348ef6)

Görsel 2: Fazlalık akışın komşuya itilmesi

![step_sink_arrival](https://github.com/user-attachments/assets/140cc33b-6bea-4f5e-9f13-b2b91a348ef6)

---

3-) Relabel Adımı
- Eğer hiçbir komşuya push yapılamıyorsa, düğümün yüksekliği artırılır.
- Böylece daha fazla akışa yol açacak potansiyel yaratılır.

Görsel 3: Düğüm yüksekliği arttırılıyor (relabel işlemi)

![step_relabel_action](https://github.com/user-attachments/assets/14cc

---

4-)Sink 'e Ulaşım
- Sink düğümüne gelen toplam akış, maksimum akışı gösterir.
- Tüm düğümler için push ve relabel işlemleri tamamlanana kadar döngü devam eder.

Görsel 4: Maksimum akış değerine ulaşılması

![step_push_action](https://github.com/user-attachments/assets/61315c14-5f31-4bc7-982d-15ffa9d96d89)

---

Bağlantılar
- Proje Kaynağı: [GitHub Repo](https://github.com/Nzr7/push-relabel-algoritmasi.git)
