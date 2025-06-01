from grafik_olustur import rastgele_graf_olustur, source_sink_belirle
from push_relabel import PushRelabel
from gorsel import grafi_gorsellestir  # 💡 GÖRSELLEŞTİRME BURADA EKLENDİ

if __name__ == "__main__":
    # 🔷 1. Grafiği oluştur
    G = rastgele_graf_olustur(n=1250, p=0.01)
    source, sink = source_sink_belirle(G)

    print(f"Source: {source}, Sink: {sink}")
    
    # 🔷 2. Maksimum akışı hesapla
    pr = PushRelabel(G, source, sink)
    max_flow = pr.run()
    
    print(f"💧 Maksimum Akış: {max_flow}")

    # 🔷 3. GRAFİĞİ GÖSTER
    grafi_gorsellestir(G, source, sink, node_limit=150, title="Push-Relabel Ağ Görselleştirmesi")
