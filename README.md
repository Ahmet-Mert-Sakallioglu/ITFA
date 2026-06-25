# ITFA
Wildfire Resource Management and Response Optimization using Deep Reinforcement Learning
# Orman Yangını Pekiştirmeli Öğrenme Sistemi (ITFA)


---

## Proje Özeti

Bu proje, orman yangınlarının yayılımını simüle eden ve yangınla mücadele kaynaklarının en verimli şekilde yönlendirilmesini amaçlayan yapay zekâ tabanlı bir karar destek sistemi geliştirmektedir.

Sistem, hücre tabanlı (grid) bir ortam üzerinde yangın yayılımını modellemekte ve şu faktörleri dikkate almaktadır:

- Rüzgar etkisi  
- Yakıt yoğunluğu (bitki örtüsü)  
- Arazi eğimi  
- Hava durumu koşulları  
- Spot yangın (yeni ani tutuşmalar)

Bu ortam üzerinde bir pekiştirmeli öğrenme (DRL) ajanı, yangına müdahale için en uygun aksiyonları öğrenmeye çalışır.

---

## Sistem Mimarisi

Proje modüler bir yapı ile geliştirilmiştir:

- `config.py` → sistem parametreleri  
- `fire_simulation.py` → yangın yayılım motoru (hücresel model)  
- `weather_system.py` → dinamik hava durumu modeli  
- `vehicles.py` → yangın söndürme araçları  
- `suppression_system.py` → müdahale sistemi  
- `environment.py` → DRL ortamı (Gym tarzı yapı)  
- `train.py` → PPO eğitim süreci  

---

## Yapay Zekâ Yaklaşımı

Sistem, Stable-Baselines3 kütüphanesi ile PPO (Proximal Policy Optimization) algoritmasını kullanır.

### Gözlem (Observation) Alanı:
- Yangın grid yapısı (flatten edilmiş)
- Hava durumu verileri (rüzgar, nem, sıcaklık)

### Aksiyon (Action) Alanı:
- Müdahale edilecek hücre koordinatı

### Ödül (Reward) Sistemi:
- Yanan hücre sayısının azalması → pozitif ödül  
- Yangının yayılması → negatif ödül  
- Yanmış alan artışı → ceza  

---

## Yangın Yayılım Modeli

Yangın simülasyonu hücresel otomata yaklaşımı ile modellenmiştir ve şu faktörleri içerir:

- Yakıt miktarı  
- Rüzgar etkisi  
- Yükseklik farkı  
- Rastgele spot fire oluşumu  

Bu model, gerçek dünya yangın davranışlarını basitleştirilmiş şekilde temsil eder.

---

## Kurulum

Gerekli kütüphaneleri yüklemek için:

```bash
pip install numpy stable-baselines3 gymnasium
Eğitim

Modeli eğitmek için:

python train.py

Proje Amacı

Bu projenin amacı, yapay zekânın orman yangınlarıyla mücadelede karar destek sistemi olarak kullanılabileceğini göstermek ve kaynakların daha verimli şekilde yönlendirilmesini sağlamaktır.

Proje eğitim ve araştırma amaçlı geliştirilmiştir.
Simülasyon rastgelelik içeren (stokastik) bir yapıya sahiptir.
Sistem modülerdir ve geliştirilmeye açıktır.
