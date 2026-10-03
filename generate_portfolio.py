import os
import base64
import subprocess

def get_base64_image(rel_path):
    full_path = os.path.join("public", rel_path)
    if not os.path.exists(full_path):
        print("Not found:", full_path)
        return ""
    mime = "image/jpeg"
    if full_path.lower().endswith(".png"):
        mime = "image/png"
    elif full_path.lower().endswith(".svg"):
        mime = "image/svg+xml"
    with open(full_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    return f"data:{mime};base64,{encoded}"

# Convert project images to Base64
img_avatar = get_base64_image("images/foto_muka.jpg")
img_p1 = get_base64_image("images/thumbnail project 1.jpg")
img_p2 = get_base64_image("images/thumbnail project 2.jpg")
img_p3 = get_base64_image("images/thumbnail project 3.jpg")
img_tower = get_base64_image("images/Thumnail tower.jpg")
img_lapor = get_base64_image("images/Thumnail laporan (1).jpg")

html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Portofolio Profesional - Muhamad Nizar Nurfalah</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        @page {{
            size: A4 portrait;
            margin: 0;
        }}
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }}
        body {{
            font-family: 'Inter', sans-serif;
            background: #ffffff;
            color: #1e293b;
            font-size: 9.5pt;
            line-height: 1.45;
        }}
        .page {{
            width: 210mm;
            height: 297mm;
            page-break-after: always;
            position: relative;
            background: #ffffff;
            overflow: hidden;
            padding: 16mm 18mm;
            display: flex;
            flex-direction: column;
        }}
        .page:last-child {{
            page-break-after: avoid;
        }}
        
        .page-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 3.5mm;
            margin-bottom: 5mm;
        }}
        .page-header-title {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-weight: 700;
            font-size: 11pt;
            color: #4338ca;
            text-transform: uppercase;
            letter-spacing: 0.8px;
        }}
        .page-header-tag {{
            font-size: 8pt;
            color: #64748b;
            font-weight: 600;
        }}
        .page-footer {{
            margin-top: auto;
            border-top: 1px solid #e2e8f0;
            padding-top: 3mm;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 7.5pt;
            color: #64748b;
        }}

        h1, h2, h3, h4 {{
            font-family: 'Plus Jakarta Sans', sans-serif;
        }}
        .badge {{
            display: inline-block;
            padding: 2.5px 8px;
            border-radius: 4px;
            font-size: 7.5pt;
            font-weight: 600;
            background: #eef2ff;
            color: #4338ca;
            border: 1px solid #c7d2fe;
        }}
        .badge-cyan {{
            background: #ecfeff;
            color: #0e7490;
            border: 1px solid #a5f3fc;
        }}
        .badge-green {{
            background: #f0fdf4;
            color: #15803d;
            border: 1px solid #bbf7d0;
        }}

        /* PAGE 1: COVER & PROFILE */
        .cover-header {{
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #312e81 100%);
            border-radius: 12px;
            padding: 18px 22px;
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 20px;
            margin-bottom: 6mm;
            box-shadow: 0 4px 15px rgba(15, 23, 42, 0.15);
        }}
        .cover-avatar {{
            width: 100px;
            height: 100px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid #818cf8;
            box-shadow: 0 0 15px rgba(129, 140, 248, 0.5);
            flex-shrink: 0;
        }}
        .cover-info h1 {{
            font-size: 16pt;
            font-weight: 800;
            color: #ffffff;
            letter-spacing: -0.3px;
        }}
        .cover-role {{
            font-size: 10pt;
            color: #a5b4fc;
            font-weight: 600;
            margin-top: 2px;
            margin-bottom: 8px;
        }}
        .cover-contacts {{
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            font-size: 7.5pt;
            color: #cbd5e1;
        }}
        .cover-contacts span {{
            background: rgba(255, 255, 255, 0.08);
            padding: 2px 7px;
            border-radius: 4px;
        }}

        .section-title {{
            font-size: 11pt;
            font-weight: 700;
            color: #0f172a;
            border-left: 4px solid #4f46e5;
            padding-left: 8px;
            margin-bottom: 3.5mm;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .card-box {{
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 12px 14px;
            margin-bottom: 4.5mm;
        }}

        /* PROJECT CARDS */
        .project-card {{
            display: flex;
            gap: 14px;
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 11px;
            margin-bottom: 4mm;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        }}
        .project-thumb {{
            width: 160px;
            height: 102px;
            object-fit: cover;
            border-radius: 6px;
            border: 1px solid #cbd5e1;
            flex-shrink: 0;
            background: #f1f5f9;
        }}
        .project-body {{
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        .project-title {{
            font-size: 9.8pt;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 2px;
        }}
        .project-desc {{
            font-size: 8pt;
            color: #475569;
            line-height: 1.35;
            margin-bottom: 4px;
        }}
        .project-features {{
            font-size: 7.5pt;
            color: #334155;
            margin-bottom: 4px;
            padding-left: 14px;
        }}
        .project-features li {{
            margin-bottom: 1px;
        }}
        .project-link {{
            font-size: 7.5pt;
            color: #4338ca;
            font-weight: 600;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }}

        /* HUMAS ARTICLES & VIDEOS */
        .humas-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
        }}
        .humas-item {{
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            padding: 7px 9px;
            font-size: 7.5pt;
        }}
        .humas-item-title {{
            font-weight: 700;
            color: #0f172a;
            font-size: 8pt;
            margin-bottom: 2px;
            line-height: 1.25;
        }}
        .humas-item a {{
            color: #4338ca;
            text-decoration: none;
            font-size: 7pt;
            word-break: break-all;
        }}
    </style>
</head>
<body>

    <!-- ==================== PAGE 1: COVER & EXECUTIVE SUMMARY ==================== -->
    <div class="page">
        <div class="cover-header">
            <img src="{img_avatar}" alt="Muhamad Nizar Nurfalah" class="cover-avatar">
            <div class="cover-info">
                <h1>MUHAMAD NIZAR NURFALAH, S.Kom.</h1>
                <div class="cover-role">Web Developer &bull; WebGIS Specialist &bull; Drafter</div>
                <div class="cover-contacts">
                    <span>📍 Bandung, Jawa Barat</span>
                    <span>✉️ nizarbeet88@gmail.com</span>
                    <span>🔗 linkedin.com/in/muhamad-nizar-nurfalah-6b1011440</span>
                    <span>💻 github.com/nizarnurfalah</span>
                    <span>🌐 nizarnurfalah.github.io/PortofolioNizarNurfalah</span>
                </div>
            </div>
        </div>

        <div class="section-title">
            <span>Ringkasan Profil Profesional</span>
            <span class="badge">S1 Sistem Informasi</span>
        </div>
        <div class="card-box" style="margin-bottom: 5mm;">
            <p style="font-size: 8.8pt; color: #334155; text-align: justify; line-height: 1.55;">
                Lulusan <strong>S1 Sistem Informasi STMIK AMIK Bandung</strong> dengan fokus keahlian pada <strong>Web Development, Sistem Informasi Geografis (WebGIS), AutoCAD Drafting</strong>, dan <strong>Media Publikasi Kreatif</strong>. Berpengalaman magang &plusmn;10 bulan di Diskominfo Kota Bandung dan PT Nexwave, mencakup pembuatan aplikasi web interaktif berbasis peta spasial, penyusunan berkas gambar teknik telekomunikasi, serta publikasi berita dan konten video kreatif.
            </p>
        </div>

        <div class="section-title">
            <span>Keahlian & Tech Stack</span>
            <span class="badge badge-cyan">Keahlian Terapan</span>
        </div>
        <div class="card-box" style="margin-bottom: 5mm;">
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; font-size: 8.2pt;">
                <div>
                    <strong style="color: #4338ca; display: block; margin-bottom: 5px;">Web & GIS Development</strong>
                    <div style="display: flex; flex-wrap: wrap; gap: 4px;">
                        <span class="badge">WebGIS</span>
                        <span class="badge">Leaflet.js</span>
                        <span class="badge">JavaScript</span>
                        <span class="badge">React.js</span>
                        <span class="badge">Laravel</span>
                        <span class="badge">HTML5 / CSS3</span>
                    </div>
                </div>
                <div>
                    <strong style="color: #0e7490; display: block; margin-bottom: 5px;">Drafting & Tools</strong>
                    <div style="display: flex; flex-wrap: wrap; gap: 4px;">
                        <span class="badge badge-cyan">AutoCAD</span>
                        <span class="badge badge-cyan">Gambar Teknik</span>
                        <span class="badge badge-cyan">SID Site Survey</span>
                        <span class="badge badge-cyan">PDF & DWG</span>
                    </div>
                </div>
                <div>
                    <strong style="color: #15803d; display: block; margin-bottom: 5px;">Creative Media & Tools</strong>
                    <div style="display: flex; flex-wrap: wrap; gap: 4px;">
                        <span class="badge badge-green">Artikel Rilis</span>
                        <span class="badge badge-green">Video Editing</span>
                        <span class="badge badge-green">Git / GitHub</span>
                        <span class="badge badge-green">VS Code</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="section-title">
            <span>Pengalaman Magang Relevan</span>
        </div>
        <div class="card-box" style="padding: 11px 14px;">
            <div style="margin-bottom: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <strong style="font-size: 9.2pt; color: #0f172a;">Drafter Telekomunikasi — PT Nexwave</strong>
                    <span style="font-size: 7.5pt; color: #64748b; font-weight: 600;">Magang Industri</span>
                </div>
                <p style="font-size: 7.8pt; color: #475569; margin-top: 3px;">
                    Menyusun dokumen gambar teknik blueprint AutoCAD (SID survey, tiang monopole, as-built drawing) dengan standar format industri telekomunikasi.
                </p>
            </div>
            <div style="border-top: 1px dashed #cbd5e1; padding-top: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <strong style="font-size: 9.2pt; color: #0f172a;">Humas & Creative Media — Diskominfo Kota Bandung</strong>
                    <span style="font-size: 7.5pt; color: #64748b; font-weight: 600;">Magang Kedinasan</span>
                </div>
                <p style="font-size: 7.8pt; color: #475569; margin-top: 3px;">
                    Menulis dan menerbitkan 11 artikel berita rilis pers di portal bandung.go.id serta memproduksi 13 video reels publikasi kegiatan kedinasan.
                </p>
            </div>
        </div>

        <div class="page-footer">
            <span>Portofolio Resmi Muhamad Nizar Nurfalah</span>
            <span>Halaman 1 / 3</span>
        </div>
    </div>

    <!-- ==================== PAGE 2: SHOWCASE PROYEK WEBGIS ==================== -->
    <div class="page">
        <div class="page-header">
            <div class="page-header-title">Showcase Proyek WebGIS Unggulan</div>
            <div class="page-header-tag">Interactive Geospatial Solutions</div>
        </div>

        <!-- Project 1 -->
        <div class="project-card">
            <img src="{img_p1}" alt="WebGIS Longsor Kuningan" class="project-thumb">
            <div class="project-body">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                        <div class="project-title">WebGIS Pemetaan Rawan Longsor Kabupaten Kuningan</div>
                        <span class="badge">WebGIS &bull; Spasial</span>
                    </div>
                    <div class="project-desc">
                        Sistem Informasi Geografis interaktif berbasis web untuk pemetaan zonasi kerawanan dan visualisasi spasial mitigasi bencana tanah longsor di Kabupaten Kuningan.
                    </div>
                    <ul class="project-features">
                        <li>Peta interaktif multi-layering zonasi rawan bencana berbasis Leaflet.js.</li>
                        <li>Visualisasi batas wilayah, kemiringan lereng, dan parameter kerawanan tanah.</li>
                        <li>Desain responsif yang mudah diakses oleh publik.</li>
                    </ul>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f1f5f9; padding-top: 4px;">
                    <div style="display: flex; gap: 3px;">
                        <span class="badge">Leaflet</span>
                        <span class="badge">JavaScript</span>
                        <span class="badge">HTML / CSS</span>
                    </div>
                    <a href="https://nizarnurfalah.github.io/webgis_longsor_kuningan/" class="project-link">🔗 Live Demo: nizarnurfalah.github.io/webgis_longsor_kuningan</a>
                </div>
            </div>
        </div>

        <!-- Project 2 -->
        <div class="project-card">
            <img src="{img_tower}" alt="WebGIS Microwave Tower" class="project-thumb">
            <div class="project-body">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                        <div class="project-title">WebGIS Pemetaan Radius & Transmisi Microwave Tower BTS</div>
                        <span class="badge badge-cyan">GIS & Telecom</span>
                    </div>
                    <div class="project-desc">
                        Sistem Informasi Geografis pemetaan jarak dan radius pancaran gelombang mikro (microwave) antar menara BTS dilengkapi kalkulator Fresnel Zone.
                    </div>
                    <ul class="project-features">
                        <li>Kalkulator Fresnel Zone otomatis untuk validasi transmisi gelombang mikro.</li>
                        <li>Visualisasi radius coverage antena dan marker tower interaktif.</li>
                        <li>Fitur uji titik koordinat dalam radius dan pencarian BTS terdekat.</li>
                    </ul>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f1f5f9; padding-top: 4px;">
                    <div style="display: flex; gap: 3px;">
                        <span class="badge badge-cyan">Leaflet</span>
                        <span class="badge badge-cyan">Kalkulator Fresnel</span>
                        <span class="badge badge-cyan">Bootstrap</span>
                    </div>
                    <a href="https://nizarnurfalah.github.io/pancaranradius_microwave/" class="project-link">🔗 Live Demo: nizarnurfalah.github.io/pancaranradius_microwave</a>
                </div>
            </div>
        </div>

        <!-- Project 3 -->
        <div class="project-card">
            <img src="{img_lapor}" alt="WebGIS Laporan Fasilitas" class="project-thumb">
            <div class="project-body">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                        <div class="project-title">WebGIS Pemetaan & Pengaduan Fasilitas Publik</div>
                        <span class="badge badge-green">Public Service App</span>
                    </div>
                    <div class="project-desc">
                        Platform WebGIS pelaporan dan pemetaan titik kerusakan fasilitas publik (jalan berlubang, lampu jalan, drainase) dengan pelacakan status penanganan.
                    </div>
                    <ul class="project-features">
                        <li>Formulir pengaduan dengan fitur pin lokasi titik koordinat langsung di peta.</li>
                        <li>Filter multi-kategori kerusakan dan filter status (Baru, Diproses, Selesai).</li>
                        <li>Dashboard admin untuk monitoring laporan masuk.</li>
                    </ul>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f1f5f9; padding-top: 4px;">
                    <div style="display: flex; gap: 3px;">
                        <span class="badge badge-green">Leaflet</span>
                        <span class="badge badge-green">JavaScript</span>
                        <span class="badge badge-green">Admin Panel</span>
                    </div>
                    <a href="https://nizarnurfalah.github.io/pemetaan-laporan-fasilitas/" class="project-link">🔗 Live Demo: nizarnurfalah.github.io/pemetaan-laporan-fasilitas</a>
                </div>
            </div>
        </div>

        <div class="page-footer">
            <span>Portofolio Resmi Muhamad Nizar Nurfalah</span>
            <span>Halaman 2 / 3</span>
        </div>
    </div>

    <!-- ==================== PAGE 3: PROYEK WEB TAMBAHAN & PUBLIKASI HUMAS ==================== -->
    <div class="page">
        <div class="page-header">
            <div class="page-header-title">Proyek Aplikasi & Dokumentasi Humas</div>
            <div class="page-header-tag">Web & Media Publication</div>
        </div>

        <!-- Compact Projects -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 5mm;">
            <div class="card-box" style="padding: 10px;">
                <img src="{img_p2}" alt="Perhitungan Pipa" style="width: 100%; height: 90px; object-fit: cover; border-radius: 4px; margin-bottom: 6px; border: 1px solid #cbd5e1;">
                <div style="font-weight: 700; font-size: 8.8pt; color: #0f172a;">Aplikasi Kalkulator Perhitungan Pipa Teknis</div>
                <p style="font-size: 7.5pt; color: #475569; margin: 3px 0;">Kalkulator simulasi teknik untuk menghitung dimensi pipa, kecepatan aliran, dan kerugian tekanan (headloss) fluida secara presisi.</p>
                <a href="https://nizarnurfalah.github.io/PerhitunganPipa/" class="project-link">🔗 Demo: nizarnurfalah.github.io/PerhitunganPipa</a>
            </div>
            <div class="card-box" style="padding: 10px;">
                <img src="{img_p3}" alt="Jadwal Theater" style="width: 100%; height: 90px; object-fit: cover; border-radius: 4px; margin-bottom: 6px; border: 1px solid #cbd5e1;">
                <div style="font-weight: 700; font-size: 8.8pt; color: #0f172a;">Website Informasi Jadwal Teater Unisba</div>
                <p style="font-size: 7.5pt; color: #475569; margin: 3px 0;">Platform web katalog pementasan teater Unisba, informasi jadwal acara, dan registrasi pementasan seni budaya interaktif.</p>
                <a href="https://nizarnurfalah.github.io/jadwaltheaterunisba/" class="project-link">🔗 Demo: nizarnurfalah.github.io/jadwaltheaterunisba</a>
            </div>
        </div>

        <div class="section-title">
            <span>Contoh Publikasi Artikel Rilis Pers — Diskominfo Kota Bandung</span>
            <span class="badge">Portal Resmi bandung.go.id</span>
        </div>

        <div class="humas-grid" style="margin-bottom: 5mm;">
            <div class="humas-item">
                <div class="humas-item-title">1. Penanganan Sampah TPS Gunung Batu Timur</div>
                <div style="color: #64748b; margin-bottom: 2px;">Liputan reaksi cepat penanganan TPS oleh aparat Kelurahan Sukagalih.</div>
                <a href="https://www.bandung.go.id/news/read/12616/tumpukan-sampah-tps-gunung-batu-timur-menghilang-aparat-kelurahan-suk">bandung.go.id/news/read/12616/...</a>
            </div>
            <div class="humas-item">
                <div class="humas-item-title">2. RSUD Bandung Kiwari: Simulasi Gempa</div>
                <div style="color: #64748b; margin-bottom: 2px;">Kesiapsiagaan mitigasi bencana gempa bumi tenaga medis dan staf RS.</div>
                <a href="https://www.bandung.go.id/news/read/12369/rsud-bandung-kiwari-tingkatkan-kesiapsiagaan-bencana-lewat-simulasi-pe">bandung.go.id/news/read/12369/...</a>
            </div>
            <div class="humas-item">
                <div class="humas-item-title">3. KDM Fest: Pemilihan Duta Dekranasda</div>
                <div style="color: #64748b; margin-bottom: 2px;">Promosi inovasi kerajinan kriya dan representasi duta Kota Bandung.</div>
                <a href="https://www.bandung.go.id/news/read/12379/kembang-nusa-x-kdm-fest-dua-wakil-kota-bandung-bersaing-jadi-duta-dek">bandung.go.id/news/read/12379/...</a>
            </div>
            <div class="humas-item">
                <div class="humas-item-title">4. Bazar Gemar Ikan DKPP Kota Bandung</div>
                <div style="color: #64748b; margin-bottom: 2px;">Kampanye gizi protein ikan dan promosi pembudidaya ikan lokal.</div>
                <a href="https://www.bandung.go.id/news/read/12499/azar-gemar-ikan-dkpp-kota-bandung-sukses-ajang-promobandung-city-depa">bandung.go.id/news/read/12499/...</a>
            </div>
        </div>

        <div style="margin-top: auto; background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); border-radius: 8px; padding: 14px 18px; color: #ffffff; display: flex; justify-content: space-between; align-items: center;">
            <div>
                <strong style="font-size: 10pt; color: #ffffff; display: block; margin-bottom: 2px;">Siap Berkontribusi & Berkolaborasi</strong>
                <span style="font-size: 7.8pt; color: #cbd5e1;">Terbuka untuk posisi Web Developer, WebGIS Specialist, Drafter, dan IT Staff.</span>
            </div>
            <div style="text-align: right; font-size: 7.8pt;">
                <div style="font-weight: 700; color: #818cf8;">Muhamad Nizar Nurfalah, S.Kom.</div>
                <div style="color: #94a3b8;">nizarbeet88@gmail.com</div>
            </div>
        </div>

        <div class="page-footer">
            <span>Portofolio Resmi Muhamad Nizar Nurfalah</span>
            <span>Halaman 3 / 3</span>
        </div>
    </div>

</body>
</html>
"""

with open("generate_portfolio_doc.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Clean 3-page HTML generated successfully!")
