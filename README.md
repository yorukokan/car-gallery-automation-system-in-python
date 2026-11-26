<div align="center">

<!-- Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F172A,50:2563EB,100:F59E0B&height=210&section=header&text=Car%20Gallery%20Automation&fontSize=42&fontColor=F8FAFC&fontAlignY=38&desc=Python%20CLI%20Inventory%20%E2%80%A2%20CRUD%20%E2%80%A2%20File%20Persistence%20%E2%80%A2%20Analytics&descSize=16&descAlignY=62&animation=fadeIn" width="100%" alt="Car Gallery Automation Banner" />

<!-- Typing Animation -->
<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&duration=2600&pause=900&color=60A5FA&center=true&vCenter=true&width=780&lines=Car+Gallery+Automation+System+in+Python;Zero-Dependency+CLI+CRUD+%E2%80%A2+Search+%E2%80%A2+Price+Filter;S%C4%B1f%C4%B1r+Ba%C4%9F%C4%B1ml%C4%B1l%C4%B1kl%C4%B1+Python+Galeri+Otomasyonu;Dosya+Tabanl%C4%B1+Kay%C4%B1t+%E2%80%A2+Arama+%E2%80%A2+Fiyat+%C4%B0statistikleri" alt="Typing SVG" />

<br/>

<!-- Quick Action Pills -->
<a href="https://www.python.org/">
  <img src="https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=0B0F19" alt="Python 3.12+" />
</a>
<a href="https://github.com/yorukokan">
  <img src="https://img.shields.io/badge/GitHub-yorukokan-181717?style=for-the-badge&logo=github&logoColor=white&labelColor=0B0F19" alt="GitHub" />
</a>
<a href="https://linkedin.com/in/okanyoruk">
  <img src="https://img.shields.io/badge/LinkedIn-Okan%20Y%C3%B6r%C3%BCk-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0B0F19" alt="LinkedIn" />
</a>
<a href="mailto:okanyoruk.tr@gmail.com">
  <img src="https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0B0F19" alt="Email" />
</a>

</div>

---

## 🎯 Overview · Proje Özeti

<table>
<tr>
<td width="50%" valign="top">
<h3>🇬🇧 English</h3>
<p>
<b>Car Gallery Automation System</b> is a lightweight, zero-dependency Python CLI application designed for managing a vehicle dealership inventory directly from the terminal.
</p>
<p>
It provides full <b>CRUD operations</b> (add, list, update, delete), <b>multi-criteria search</b>, <b>price-range filtering</b>, and <b>fleet price analytics</b>. All vehicle records (<code>id</code>, <code>marka</code>, <code>model</code>, <code>renk</code>, <code>yil</code>, <code>fiyat</code>) are automatically loaded on startup and persisted to a structured text file (<code>22100011067.txt</code>) after every modification.
</p>
</td>
<td width="50%" valign="top">
<h3>🇹🇷 Türkçe</h3>
<p>
<b>Araç Galerisi Otomasyon Sistemi</b>, terminal üzerinden araç galerisi envanterini yönetmek için geliştirilmiş, harici bağımlılık gerektirmeyen hafif bir Python CLI uygulamasıdır.
</p>
<p>
Uygulama; eksiksiz <b>CRUD işlemleri</b> (ekleme, listeleme, güncelleme, silme), <b>çok kriterli arama</b>, <b>fiyat aralığı filtreleme</b> ve <b>galeri fiyat istatistikleri</b> sunar. Tüm araç kayıtları (<code>id</code>, <code>marka</code>, <code>model</code>, <code>renk</code>, <code>yil</code>, <code>fiyat</code>) açılışta otomatik yüklenir ve her değişiklik sonrası yapılandırılmış metin dosyasına (<code>22100011067.txt</code>) kaydedilir.
</p>
</td>
</tr>
</table>

---

## ✨ Key Features · Öne Çıkan Özellikler

<table>
<tr>
<td width="50%" valign="top">
<h4>🚗 Full Vehicle CRUD · Tam Araç CRUD</h4>
<p>
<b>EN:</b> Add multiple vehicles in a continuous loop, list all inventory records in a clean block layout, or remove a vehicle by ID with automatic sequential ID re-indexing (<code>1..N</code>).<br/>
<b>TR:</b> Kesintisiz döngü ile yeni araç ekleyin, tüm kayıtları düzenli bloklar halinde listeleyin veya ID ile araç silerken kalan kayıtların ID değerlerinin otomatik yeniden sıralanmasını (<code>1..N</code>) sağlayın.
</p>
<code>car-gallery-automation-system.py · aracKayitEkle · aracKayitListele · aracKayitSil</code>
</td>
<td width="50%" valign="top">
<h4>✏️ Field-Level Updates · Alan Bazlı Güncelleme</h4>
<p>
<b>EN:</b> Select a vehicle by ID and update individual attributes (Brand, Model, Color, Year, Price) via an interactive submenu. Leaving an input blank safely keeps the current value.<br/>
<b>TR:</b> ID ile seçilen aracın Marka, Model, Renk, Yıl veya Fiyat alanlarını alt menü üzerinden tek tek güncelleyin. Boş bırakılan alanlar mevcut değerini otomatik olarak korur.
</p>
<code>car-gallery-automation-system.py · aracKayitGuncelle</code>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<h4>🔍 Multi-Criteria Search · Çok Kriterli Arama</h4>
<p>
<b>EN:</b> Filter inventory records with case-insensitive matching across four dedicated criteria: Brand (<code>marka</code>), Model (<code>model</code>), Color (<code>renk</code>), and Year (<code>yil</code>).<br/>
<b>TR:</b> Marka (<code>marka</code>), Model (<code>model</code>), Renk (<code>renk</code>) ve Yıl (<code>yil</code>) kriterlerine göre büyük/küçük harf duyarsız arama yaparak eşleşen araçları anında listeleyin.
</p>
<code>car-gallery-automation-system.py · aracArama</code>
</td>
<td width="50%" valign="top">
<h4>💰 Price Range Filter · Fiyat Aralığı Filtreleme</h4>
<p>
<b>EN:</b> Query vehicles whose price falls within a user-defined <code>[min, max]</code> range, with numeric input validation via <code>ValueError</code> handling.<br/>
<b>TR:</b> Kullanıcının belirlediği minimum ve maksimum fiyat aralığına (<code>[min, max]</code>) uyan araçları, <code>ValueError</code> doğrulamasıyla güvenli biçimde filtreleyin.
</p>
<code>car-gallery-automation-system.py · aracFiyatAraligi</code>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<h4>📊 Fleet Analytics · Araç İstatistikleri</h4>
<p>
<b>EN:</b> Automatically calculates total vehicle count, average fleet price, and identifies both the most expensive and least expensive vehicles in the gallery.<br/>
<b>TR:</b> Toplam araç sayısını, ortalama araç fiyatını ve galerideki en pahalı ile en ucuz araçları anlık olarak hesaplayıp raporlar.
</p>
<code>car-gallery-automation-system.py · aracKayitIstatistik</code>
</td>
<td width="50%" valign="top">
<h4>💾 Flat-File Persistence · Dosya Tabanlı Kalıcılık</h4>
<p>
<b>EN:</b> Parses <code>--------------------------</code>-delimited records from <code>22100011067.txt</code> on startup and syncs in-memory state back to disk after every create, update, or delete.<br/>
<b>TR:</b> Açılışta <code>22100011067.txt</code> dosyasındaki <code>--------------------------</code> ayraçlı kayıtları belleğe yükler ve her ekleme, güncelleme veya silme işleminde diske geri yazar.
</p>
<code>car-gallery-automation-system.py · aracDosyadanOkuma · aracKayitDosyalama · 22100011067.txt</code>
</td>
</tr>
</table>

---

## 🏗️ Architecture · Mimari

```text
                       ┌────────────────────────────┐
                       │      22100011067.txt       │
                       │  (Flat-File Record Store)  │
                       └─────────────┬──────────────┘
                                     │
                 Startup load        │        Persist on write
             aracDosyadanOkuma()     │     aracKayitDosyalama()
                                     ▼
                  ┌────────────────────────────────────┐
                  │  In-Memory State (arac_liste, id)  │
                  └──────────────────┬─────────────────┘
                                     │
                                     ▼
                  ┌────────────────────────────────────┐
                  │       menu()  <──>  ana_menu()     │
                  │     (Interactive CLI Event Loop)   │
                  └──────────────────┬─────────────────┘
                                     │
       ┌──────────────┬──────────────┼──────────────┬──────────────┐
       ▼              ▼              ▼              ▼              ▼
  [1] Add        [2] List       [3] Delete     [4] Update    [5-7] Query & Stats
aracKayitEkle  aracKayitListele aracKayitSil  aracKayitGuncelle  aracArama()
                                                                 aracKayitIstatistik()
                                                                 aracFiyatAraligi()
```

---

## 🛠️ Tech Stack · Teknoloji Yığını

<div align="center">

<img src="https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=0D1117" alt="Python 3.12+" />
<img src="https://img.shields.io/badge/Standard%20Library-Zero%20Dependencies-2563EB?style=for-the-badge&logo=python&logoColor=white&labelColor=0D1117" alt="Python Standard Library" />
<img src="https://img.shields.io/badge/Interface-CLI%20%2F%20Terminal-0F172A?style=for-the-badge&logo=gnubash&logoColor=white&labelColor=0D1117" alt="CLI Terminal" />
<img src="https://img.shields.io/badge/Storage-Flat%20File%20(.txt)-F59E0B?style=for-the-badge&logo=files&logoColor=white&labelColor=0D1117" alt="Flat File Storage" />

</div>

---

## 📂 Project Structure · Proje Yapısı

```text
car-gallery-automation-system-in-python/
├── car-gallery-automation-system.py   # Main CLI application (all menu, CRUD, search & analytics functions)
├── 22100011067.txt                    # Persistent flat-file vehicle database (includes 3 sample records)
├── car-gallery-automation-info.pdf    # Project specification & documentation PDF
├── .gitattributes                     # Git line-ending configuration
├── .gitignore                         # Git ignore rules
└── README.md                          # Project documentation
```

---

## 🚀 Getting Started · Kurulum ve Çalıştırma

### Prerequisites · Gereksinimler
- **Python 3.12+** (required for PEP 701 nested quotes inside f-strings used in `car-gallery-automation-system.py`)
- No third-party packages required (`pip install` is not needed)

### Clone & Run · Klonla ve Çalıştır

```bash
# 1. Clone the repository / Repoyu klonlayın
git clone https://github.com/yorukokan/car-gallery-automation-system-in-python.git
cd car-gallery-automation-system-in-python

# 2. Run the CLI automation / CLI otomasyonunu çalıştırın
python3 car-gallery-automation-system.py
```

### CLI Menu Reference · Menü Referansı

| Option | Operation (TR) | Operation (EN) | Handler Function |
| :---: | :--- | :--- | :--- |
| `1` | Araç Kayıt Ekleme | Add Vehicle Record | `aracKayitEkle()` |
| `2` | Araç Kaydı Listeleme | List All Vehicles | `aracKayitListele()` |
| `3` | Araç Kaydı Silme | Delete Vehicle by ID | `aracKayitSil()` |
| `4` | Araç Kaydı Güncelleme | Update Vehicle Fields | `aracKayitGuncelle()` |
| `5` | Araç Kaydı Arama | Search by Brand / Model / Color / Year | `aracArama()` |
| `6` | Araç İstatistikleri | View Fleet Price Statistics | `aracKayitIstatistik()` |
| `7` | Belirli Fiyat Aralığında Araba Bulma | Filter Vehicles by Price Range | `aracFiyatAraligi()` |
| `0` | Çıkış | Exit Application | — |

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F172A,50:2563EB,100:F59E0B&height=100&section=footer" width="100%" alt="Footer Banner" />

<sub>⚡ <b>Okan Yörük</b> · Car Gallery Automation System in Python · <a href="https://github.com/yorukokan">github.com/yorukokan</a></sub>

</div>
