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

# Convert all images to Base64
img_avatar = get_base64_image("images/foto_muka.jpg")
img_p1 = get_base64_image("images/thumbnail project 1.jpg")
img_p2 = get_base64_image("images/thumbnail project 2.jpg")
img_p3 = get_base64_image("images/thumbnail project 3.jpg")
img_tower = get_base64_image("images/Thumnail tower.jpg")
img_lapor = get_base64_image("images/Thumnail laporan (1).jpg")

# Certificate images
c_infosec = get_base64_image("images/Certificate-of-Completion-Introduction-to-Information-Security_page-0001.jpg")
c_aws = get_base64_image("images/Certificate_Of_Completion-AWSSecurity1639-6617d0b8686fc11c6e4bde60.png")
c_analytics = get_base64_image("images/Certificate_Of_Completion-AnalyticsFundamentals-6617d5b2686fc11c6e4bdf52.png")
c_python = get_base64_image("images/Certificate_Of_Completion-LearnaboutPythonandBlockchainTheCompleteGuide-6617d4cf686fc11c6e4bdf0f.png")
c_stmik = get_base64_image("images/2241405.2024.2.SI20409.7.1e98d3d47e5bbeee1c842cf022e09ace_page-0001.jpg")
c_humas = get_base64_image("images/WhatsApp Image 2026-10-01 at 14.36.52.jpeg")
c_drafter = get_base64_image("images/WhatsApp Image 2026-10-01 at 14.36.53.jpeg")
c_award = get_base64_image("images/WhatsApp Image 2026-10-01 at 14.39.43.jpeg")
c_digital = get_base64_image("images/X5373661570267a27cdedcd88a7de2480_copy_page-0001.jpg")

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
            font-size: 9.2pt;
            line-height: 1.45;
        }}
        .page {{
            width: 210mm;
            height: 297mm;
            page-break-after: always;
            position: relative;
            background: #ffffff;
            overflow: hidden;
            padding: 14mm 16mm;
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
            padding-bottom: 3mm;
            margin-bottom: 4mm;
        }}
        .page-header-title {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-weight: 700;
            font-size: 10.5pt;
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
            padding: 2px 7px;
            border-radius: 4px;
            font-size: 7pt;
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
            padding: 16px 20px;
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 18px;
            margin-bottom: 5mm;
            box-shadow: 0 4px 15px rgba(15, 23, 42, 0.15);
        }}
        .cover-avatar {{
            width: 95px;
            height: 95px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid #818cf8;
            box-shadow: 0 0 15px rgba(129, 140, 248, 0.5);
            flex-shrink: 0;
        }}
        .cover-info h1 {{
            font-size: 15pt;
            font-weight: 800;
            color: #ffffff;
            letter-spacing: -0.3px;
        }}
        .cover-role {{
            font-size: 9.5pt;
            color: #a5b4fc;
            font-weight: 600;
            margin-top: 2px;
            margin-bottom: 6px;
        }}
        .cover-contacts {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            font-size: 7.2pt;
            color: #cbd5e1;
        }}
        .cover-contacts span {{
            background: rgba(255, 255, 255, 0.08);
            padding: 2px 6px;
            border-radius: 4px;
        }}

        .section-title {{
            font-size: 10.5pt;
            font-weight: 700;
            color: #0f172a;
            border-left: 4px solid #4f46e5;
            padding-left: 8px;
            margin-bottom: 3mm;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .card-box {{
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 10px 12px;
            margin-bottom: 3.5mm;
        }}

        /* PROJECT CARDS */
        .project-card {{
            display: flex;
            gap: 14px;
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 10px;
            margin-bottom: 3.5mm;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        }}
        .project-thumb {{
            width: 155px;
            height: 98px;
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
            font-size: 9.5pt;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 2px;
        }}
        .project-desc {{
            font-size: 7.8pt;
            color: #475569;
            line-height: 1.35;
            margin-bottom: 4px;
        }}
        .project-features {{
            font-size: 7.3pt;
            color: #334155;
            margin-bottom: 4px;
            padding-left: 14px;
        }}
        .project-features li {{
            margin-bottom: 1px;
        }}
        .project-link {{
            font-size: 7.2pt;
            color: #4338ca;
            font-weight: 600;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }}

        /* CAD TABLE */
        .cad-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 7.8pt;
            margin-top: 2mm;
        }}
        .cad-table th {{
            background: #0f172a;
            color: #ffffff;
            padding: 6px 9px;
            text-align: left;
            font-weight: 600;
            font-size: 7.2pt;
        }}
        .cad-table td {{
            padding: 5.5px 9px;
            border-bottom: 1px solid #e2e8f0;
            color: #334155;
            vertical-align: top;
        }}
        .cad-table tr:nth-child(even) td {{
            background: #f8fafc;
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
            padding: 6.5px 8.5px;
            font-size: 7.2pt;
        }}
        .humas-item-title {{
            font-weight: 700;
            color: #0f172a;
            font-size: 7.8pt;
            margin-bottom: 2px;
            line-height: 1.25;
        }}
        .humas-item a {{
            color: #4338ca;
            text-decoration: none;
            font-size: 6.8pt;
            word-break: break-all;
        }}

        /* CERTIFICATES GALLERY */
        .cert-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-top: 2mm;
        }}
        .cert-card {{
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            overflow: hidden;
            background: #f8fafc;
            display: flex;
            flex-direction: column;
        }}
        .cert-img {{
            width: 100%;
            height: 94px;
            object-fit: cover;
            border-bottom: 1px solid #e2e8f0;
            background: #f1f5f9;
        }}
        .cert-info {{
            padding: 5px 7px;
        }}
        .cert-title {{
            font-size: 7.3pt;
            font-weight: 700;
            color: #0f172a;
            line-height: 1.2;
            margin-bottom: 2px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}
        .cert-issuer {{
            font-size: 6.5pt;
            color: #6366f1;
            font-weight: 600;
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
                <div class="cover-role">Web Developer &bull; WebGIS Specialist &bull; Drafter Telekomunikasi</div>
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
            <span>Ringkasan Eksekutif & Profil Profesional</span>
            <span class="badge">S1 Sistem Informasi</span>
        </div>
        <div class="card-box" style="margin-bottom: 4mm;">
            <p style="font-size: 8.3pt; color: #334155; text-align: justify; line-height: 1.48;">
                Lulusan <strong>S1 Sistem Informasi STMIK AMIK Bandung</strong> dengan keahlian utama dalam <strong>Web Development, Sistem Informasi Geografis (WebGIS), Technical Drafting AutoCAD Telekomunikasi</strong>, dan <strong>Media Publikasi Kreatif</strong>. Berpengalaman magang &plusmn;10 bulan di Diskominfo Kota Bandung dan PT Nexwave, mencakup perancangan aplikasi interaktif berbasis spasial, penyusunan puluhan dokumen blueprint teknik telekomunikasi (SID, Monopole, Rooftop Mount), serta publikasi puluhan rilis pers dan konten video kreatif pada portal pemerintahan resmi.
            </p>
        </div>

        <div class="section-title">
            <span>Keahlian Utama & Tech Stack</span>
            <span class="badge badge-cyan">15+ Tools & Frameworks</span>
        </div>
        <div class="card-box" style="margin-bottom: 4mm;">
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; font-size: 7.8pt;">
                <div>
                    <strong style="color: #4338ca; display: block; margin-bottom: 3px;">Web & GIS Engineering</strong>
                    <div style="display: flex; flex-wrap: wrap; gap: 3px;">
                        <span class="badge">WebGIS</span>
                        <span class="badge">Leaflet.js</span>
                        <span class="badge">JavaScript (ES6+)</span>
                        <span class="badge">React.js</span>
                        <span class="badge">Laravel</span>
                        <span class="badge">HTML5 / CSS3</span>
                        <span class="badge">Tailwind CSS</span>
                        <span class="badge">Bootstrap</span>
                    </div>
                </div>
                <div>
                    <strong style="color: #0e7490; display: block; margin-bottom: 3px;">Drafting & Engineering</strong>
                    <div style="display: flex; flex-wrap: wrap; gap: 3px;">
                        <span class="badge badge-cyan">AutoCAD 2D</span>
                        <span class="badge badge-cyan">Site Survey (SID)</span>
                        <span class="badge badge-cyan">Monopole Design</span>
                        <span class="badge badge-cyan">As-Built Drawing</span>
                        <span class="badge badge-cyan">Rooftop Integration</span>
                        <span class="badge badge-cyan">Headloss Calc</span>
                    </div>
                </div>
                <div>
                    <strong style="color: #15803d; display: block; margin-bottom: 3px;">Creative Media & Tools</strong>
                    <div style="display: flex; flex-wrap: wrap; gap: 3px;">
                        <span class="badge badge-green">Press Release</span>
                        <span class="badge badge-green">Video Editing</span>
                        <span class="badge badge-green">Instagram Reels</span>
                        <span class="badge badge-green">Git / GitHub</span>
                        <span class="badge badge-green">VS Code</span>
                        <span class="badge badge-green">Figma</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="section-title">
            <span>Riwayat Pengalaman Relevan</span>
        </div>
        <div class="card-box" style="padding: 9px 12px;">
            <div style="margin-bottom: 7px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <strong style="font-size: 8.8pt; color: #0f172a;">Drafter Telekomunikasi — PT Nexwave</strong>
                    <span style="font-size: 7.2pt; color: #64748b; font-weight: 600;">Magang Industri</span>
                </div>
                <p style="font-size: 7.3pt; color: #475569; margin-top: 2px;">
                    Menyusun dan menyelesaikan 10+ berkas gambar blueprint teknik (SID, Pole Project Q2, As-Built Drawing, Rooftop Antenna Layout) operator telekomunikasi dengan standar akurasi teknis tinggi.
                </p>
            </div>
            <div style="border-top: 1px dashed #cbd5e1; padding-top: 7px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <strong style="font-size: 8.8pt; color: #0f172a;">Humas & Creative Media — Diskominfo Kota Bandung</strong>
                    <span style="font-size: 7.2pt; color: #64748b; font-weight: 600;">Magang Kedinasan</span>
                </div>
                <p style="font-size: 7.3pt; color: #475569; margin-top: 2px;">
                    Memproduksi dan menerbitkan 11 artikel rilis pers resmi di portal bandung.go.id serta memproduksi 13 konten video reels edukasi publik dan peliputan program Pemkot Bandung.
                </p>
            </div>
        </div>

        <div class="page-footer">
            <span>Portofolio Resmi Muhamad Nizar Nurfalah</span>
            <span>Halaman 1 / 5</span>
        </div>
    </div>

    <!-- ==================== PAGE 2: WEB & WEBGIS PROJECTS (PART 1) ==================== -->
    <div class="page">
        <div class="page-header">
            <div class="page-header-title">Showcase Proyek Web & WebGIS (Bagian 1)</div>
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
                        <li>Visualisasi peta interaktif multi-layering zonasi rawan bencana berbasis Leaflet.js.</li>
                        <li>Analisis parameter spasial kemiringan lereng, curah hujan, dan geologi tanah.</li>
                        <li>Integrasi legenda informatif dan detail wilayah responsif di berbagai perangkat.</li>
                    </ul>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f1f5f9; padding-top: 4px;">
                    <div style="display: flex; gap: 3px;">
                        <span class="badge">Leaflet</span>
                        <span class="badge">JavaScript</span>
                        <span class="badge">GeoJSON</span>
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
                        Sistem Informasi Geografis pemetaan jarak, radius coverage gelombang mikro (microwave) antar menara BTS, dan kalkulator analisis kelengkungan Fresnel Zone.
                    </div>
                    <ul class="project-features">
                        <li>Kalkulator Fresnel Zone otomatis untuk validasi Line of Sight (LoS) transmisi microwave.</li>
                        <li>Visualisasi radius coverage multi-antena dan marker BTS interaktif dengan data koordinat.</li>
                        <li>Fitur uji titik koordinat dalam radius dan pencarian BTS terdekat berbasis geolokasi.</li>
                    </ul>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f1f5f9; padding-top: 4px;">
                    <div style="display: flex; gap: 3px;">
                        <span class="badge badge-cyan">Leaflet</span>
                        <span class="badge badge-cyan">Fresnel Calc</span>
                        <span class="badge badge-cyan">Bootstrap 5</span>
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
                        Platform WebGIS pelaporan dan pemetaan kerusakan infrastruktur publik (jalan rusak, lampu PJU, drainase) dengan pelacakan status penanganan dan dashboard admin.
                    </div>
                    <ul class="project-features">
                        <li>Formulir pengaduan interaktif dengan fitur pin lokasi titik koordinat langsung pada peta.</li>
                        <li>Filter multi-kategori jenis kerusakan dan filter status (Baru, Diproses, Selesai).</li>
                        <li>Dashboard manajemen laporan terpadu untuk monitoring dan evaluasi instansi.</li>
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
            <span>Halaman 2 / 5</span>
        </div>
    </div>

    <!-- ==================== PAGE 3: WEB PROJECTS & TECHNICAL DRAFTING CAD ==================== -->
    <div class="page">
        <div class="page-header">
            <div class="page-header-title">Web Projects & Blueprint CAD Telekomunikasi</div>
            <div class="page-header-tag">Engineering & Fullstack Solutions</div>
        </div>

        <!-- Project 4 & 5 Compact Row -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 4mm;">
            <div class="card-box" style="padding: 8px;">
                <img src="{img_p2}" alt="Perhitungan Pipa" style="width: 100%; height: 85px; object-fit: cover; border-radius: 4px; margin-bottom: 5px; border: 1px solid #cbd5e1;">
                <div style="font-weight: 700; font-size: 8.3pt; color: #0f172a;">Kalkulator Perhitungan Pipa Teknis</div>
                <p style="font-size: 7.1pt; color: #475569; margin: 2px 0;">Simulasi teknik untuk menghitung dimensi pipa, kecepatan aliran, dan kerugian tekanan (headloss) fluida secara presisi.</p>
                <a href="https://nizarnurfalah.github.io/PerhitunganPipa/" class="project-link">🔗 Demo: nizarnurfalah.github.io/PerhitunganPipa</a>
            </div>
            <div class="card-box" style="padding: 8px;">
                <img src="{img_p3}" alt="Jadwal Theater" style="width: 100%; height: 85px; object-fit: cover; border-radius: 4px; margin-bottom: 5px; border: 1px solid #cbd5e1;">
                <div style="font-weight: 700; font-size: 8.3pt; color: #0f172a;">Website Informasi Jadwal Teater Unisba</div>
                <p style="font-size: 7.1pt; color: #475569; margin: 2px 0;">Platform katalog pertunjukan seni, informasi jadwal pementasan teater, dan registrasi pementasan budaya interaktif.</p>
                <a href="https://nizarnurfalah.github.io/jadwaltheaterunisba/" class="project-link">🔗 Demo: nizarnurfalah.github.io/jadwaltheaterunisba</a>
            </div>
        </div>

        <div class="section-title">
            <span>Dokumentasi Gambar Teknik CAD Telekomunikasi — PT Nexwave</span>
            <span class="badge badge-cyan">10 Dokumen Blueprint</span>
        </div>
        <p style="font-size: 7.5pt; color: #475569; margin-bottom: 2mm;">
            Kompilasi gambar kerja rancang bangun struktur telekomunikasi (format DWG & PDF) mencakup Site Survey Report (SID), Pole Infrastructure, As-Built Drawing, dan Rooftop Antenna Mount.
        </p>

        <table class="cad-table">
            <thead>
                <tr>
                    <th style="width: 17%;">Site ID</th>
                    <th style="width: 25%;">Judul Blueprint</th>
                    <th style="width: 22%;">Kategori Dokumen</th>
                    <th>Spesifikasi Teknis & Lingkup Kerja</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>13CJR0456</strong></td>
                    <td>Cianjur Leberan Expansion SID</td>
                    <td><span class="badge badge-cyan">Site Expansion SID</span></td>
                    <td>Rancang ekspansi penempatan antena sektoral dan layout shelter operator.</td>
                </tr>
                <tr>
                    <td><strong>13CJR0474</strong></td>
                    <td>Cianjur Non-Macro New SID</td>
                    <td><span class="badge badge-cyan">Non-Macro SID</span></td>
                    <td>Technical drafting tata letak tiang, pondasi beton, dan tray rute kabel feeder.</td>
                </tr>
                <tr>
                    <td><strong>13CJR0506</strong></td>
                    <td>Cianjur Q2 Pole Project New</td>
                    <td><span class="badge badge-cyan">Pole Project Q2</span></td>
                    <td>Desain rancang bangun monopole baru dengan kalkulasi load bearing & wind load.</td>
                </tr>
                <tr>
                    <td><strong>13GRT0422</strong></td>
                    <td>Garut PPQ2 Infrastructure</td>
                    <td><span class="badge badge-cyan">Monopole Design</span></td>
                    <td>Konstruksi menara monopole area Garut dengan kabinet ground & power rack.</td>
                </tr>
                <tr>
                    <td><strong>13PLR0597</strong></td>
                    <td>Plered Q2 Pole Project 0597</td>
                    <td><span class="badge badge-cyan">Pole Infrastructure</span></td>
                    <td>Cross-section detail tiang telekomunikasi dan bracket antena sektoral Plered.</td>
                </tr>
                <tr>
                    <td><strong>13PLR0600</strong></td>
                    <td>Plered Q2 Pole Project 0600</td>
                    <td><span class="badge badge-cyan">Site Construction</span></td>
                    <td>Blueprint teknis pondasi beton bertulang dan elevasi ketinggian antena 0600.</td>
                </tr>
                <tr>
                    <td><strong>ZBDG_4722</strong></td>
                    <td>Bandung Site 4722 Urban</td>
                    <td><span class="badge badge-cyan">Urban Site Layout</span></td>
                    <td>Layout penempatan perangkat telekomunikasi di area padat perkotaan Bandung.</td>
                </tr>
                <tr>
                    <td><strong>ZBDG_6234</strong></td>
                    <td>Bandung Site 6234 Rooftop</td>
                    <td><span class="badge badge-cyan">Rooftop Integration</span></td>
                    <td>Perkuatan struktur rooftop, dudukan pole antenna, dan rute feeder indoor.</td>
                </tr>
                <tr>
                    <td><strong>ZBDG_6379</strong></td>
                    <td>Bandung 6379 As-Built</td>
                    <td><span class="badge badge-cyan">As-Built Drawing</span></td>
                    <td>Verifikasi dimensi aktual lapangan dan tata letak eksisting perangkat site.</td>
                </tr>
                <tr>
                    <td><strong>ZBDG_6380</strong></td>
                    <td>Bandung 6380 Azimuth Plan</td>
                    <td><span class="badge badge-cyan">Azimuth & Height</span></td>
                    <td>Konfigurasi arah azimuth antena, electrical/mechanical tilt, dan sistem grounding.</td>
                </tr>
            </tbody>
        </table>

        <div class="page-footer">
            <span>Portofolio Resmi Muhamad Nizar Nurfalah</span>
            <span>Halaman 3 / 5</span>
        </div>
    </div>

    <!-- ==================== PAGE 4: HUMAS MEDIA & PUBLIKASI ==================== -->
    <div class="page">
        <div class="page-header">
            <div class="page-header-title">Dokumentasi Media Humas — Diskominfo Kota Bandung</div>
            <div class="page-header-tag">24 Artikel Berita & Video Publikasi</div>
        </div>

        <div class="section-title">
            <span>Publikasi Artikel Rilis Pers Resmi (Portal bandung.go.id)</span>
            <span class="badge">11 Artikel Berita</span>
        </div>

        <div class="humas-grid" style="margin-bottom: 4mm;">
            <div class="humas-item">
                <div class="humas-item-title">1. Penanganan Sampah TPS Gunung Batu Timur</div>
                <div style="color: #64748b; margin-bottom: 2px;">Liputan reaksi cepat aparat Kelurahan Sukagalih menjaga kebersihan wilayah.</div>
                <a href="https://www.bandung.go.id/news/read/12616/tumpukan-sampah-tps-gunung-batu-timur-menghilang-aparat-kelurahan-suk">bandung.go.id/news/read/12616/...</a>
            </div>
            <div class="humas-item">
                <div class="humas-item-title">2. RSUD Bandung Kiwari: Simulasi Gempa Bumi</div>
                <div style="color: #64748b; margin-bottom: 2px;">Kesiapsiagaan mitigasi bencana tenaga medis dan keamanan fasilitas RS.</div>
                <a href="https://www.bandung.go.id/news/read/12369/rsud-bandung-kiwari-tingkatkan-kesiapsiagaan-bencana-lewat-simulasi-pe">bandung.go.id/news/read/12369/...</a>
            </div>
            <div class="humas-item">
                <div class="humas-item-title">3. KDM Fest: Pemilihan Duta Dekranasda Jabar</div>
                <div style="color: #64748b; margin-bottom: 2px;">Promosi inovasi kerajinan kriya dan representasi duta kreatif Kota Bandung.</div>
                <a href="https://www.bandung.go.id/news/read/12379/kembang-nusa-x-kdm-fest-dua-wakil-kota-bandung-bersaing-jadi-duta-dek">bandung.go.id/news/read/12379/...</a>
            </div>
            <div class="humas-item">
                <div class="humas-item-title">4. Great Bandung 2025: Program Terintegrasi</div>
                <div style="color: #64748b; margin-bottom: 2px;">Sinergi tata kelola sampah, stabilisasi pangan, dan kesehatan masyarakat.</div>
                <a href="https://www.bandung.go.id/news/read/12447/great-bandung-2025-antara-sampah-sembako-layanan-kesehatan-dan-lin">bandung.go.id/news/read/12447/...</a>
            </div>
            <div class="humas-item">
                <div class="humas-item-title">5. Galeri Patrakomala Jadi Inspirasi DPRD Kalteng</div>
                <div style="color: #64748b; margin-bottom: 2px;">Studi banding kurasi dan ekspansi pemasaran produk UMKM lokal unggulan.</div>
                <a href="https://www.bandung.go.id/news/read/12472/galeri-patrakomala-jadi-inspirasi-komisi-ii-dprd-kalteng-kembangkan-pr">bandung.go.id/news/read/12472/...</a>
            </div>
            <div class="humas-item">
                <div class="humas-item-title">6. Sumirat Carnival Citylight: Pesta UMKM</div>
                <div style="color: #64748b; margin-bottom: 2px;">Puncak festival ekonomi kreatif menggerakkan transaksi ekonomi rakyat.</div>
                <a href="https://www.bandung.go.id/news/read/12487/sumirat-carnival-citylight-pelaku-umkm-rasakan-manfaat-besar-di-punca">bandung.go.id/news/read/12487/...</a>
            </div>
            <div class="humas-item">
                <div class="humas-item-title">7. Bazar Gemar Ikan DKPP Kota Bandung</div>
                <div style="color: #64748b; margin-bottom: 2px;">Kampanye gizi protein ikan dan pemberdayaan budidaya perikanan kota.</div>
                <a href="https://www.bandung.go.id/news/read/12499/azar-gemar-ikan-dkpp-kota-bandung-sukses-ajang-promobandung-city-depa">bandung.go.id/news/read/12499/...</a>
            </div>
            <div class="humas-item">
                <div class="humas-item-title">8. Floranimal Bandung: Edukasi & Wisata UMKM</div>
                <div style="color: #64748b; margin-bottom: 2px;">Pameran flora-fauna mengedukasi pecinta lingkungan dan wirausaha.</div>
                <a href="https://www.bandung.go.id/news/read/12581/floranimal-bandung-wadah-edukasi-dan-pemberdayaan-umkm-lokal">bandung.go.id/news/read/12581/...</a>
            </div>
        </div>

        <div class="section-title">
            <span>Produksi Video Reels Publikasi & Dokumentasi Kreatif</span>
            <span class="badge badge-cyan">13 Konten Instagram Reels</span>
        </div>

        <div class="humas-grid">
            <div class="humas-item">
                <div class="humas-item-title">🎬 Pemantauan Kebersihan & TPS Kota</div>
                <div style="color: #64748b;">Dokumentasi lapangan kesiapan tim kebersihan wilayah.</div>
                <a href="https://www.instagram.com/reel/DRD3WZmEx2J/">instagram.com/reel/DRD3WZmEx2J</a>
            </div>
            <div class="humas-item">
                <div class="humas-item-title">🎬 Edukasi Layanan Diskominfo Bandung</div>
                <div style="color: #64748b;">Informasi portal terpadu dan keterbukaan publik.</div>
                <a href="https://www.instagram.com/reel/DQ5-thk6RP/">instagram.com/reel/DQ5-thk6RP</a>
            </div>
            <div class="humas-item">
                <div class="humas-item-title">🎬 Simulasi Gempa RSUD Bandung Kiwari</div>
                <div style="color: #64748b;">Video aksi tanggap darurat keselamatan pasien.</div>
                <a href="https://www.instagram.com/reel/DQDmgzxE2aM/">instagram.com/reel/DQDmgzxE2aM</a>
            </div>
            <div class="humas-item">
                <div class="humas-item-title">🎬 Peluncuran Jajap Persib Heritage Tour</div>
                <div style="color: #64748b;">Wisata sejarah sepak bola kebanggaan bobotoh.</div>
                <a href="https://www.instagram.com/reel/DPX0_SLkznm/">instagram.com/reel/DPX0_SLkznm</a>
            </div>
        </div>

        <div class="page-footer">
            <span>Portofolio Resmi Muhamad Nizar Nurfalah</span>
            <span>Halaman 4 / 5</span>
        </div>
    </div>

    <!-- ==================== PAGE 5: SERTIFIKAT & PENUTUP ==================== -->
    <div class="page">
        <div class="page-header">
            <div class="page-header-title">Galeri Sertifikasi Kompetensi & Keahlian</div>
            <div class="page-header-tag">12 Validated Credentials</div>
        </div>

        <div class="cert-grid">
            <div class="cert-card">
                <img src="{c_infosec}" alt="InfoSec" class="cert-img">
                <div class="cert-info">
                    <div class="cert-title">Intro to Information Security</div>
                    <div class="cert-issuer">Great Learning Academy</div>
                </div>
            </div>
            <div class="cert-card">
                <img src="{c_aws}" alt="AWS Security" class="cert-img">
                <div class="cert-info">
                    <div class="cert-title">AWS Cloud Security Fundamentals</div>
                    <div class="cert-issuer">AWS Training</div>
                </div>
            </div>
            <div class="cert-card">
                <img src="{c_analytics}" alt="Google Analytics" class="cert-img">
                <div class="cert-info">
                    <div class="cert-title">Analytics Fundamentals</div>
                    <div class="cert-issuer">Google Analytics Academy</div>
                </div>
            </div>
            <div class="cert-card">
                <img src="{c_python}" alt="Python Blockchain" class="cert-img">
                <div class="cert-info">
                    <div class="cert-title">Python & Blockchain Mastery</div>
                    <div class="cert-issuer">Online Professional</div>
                </div>
            </div>
            <div class="cert-card">
                <img src="{c_stmik}" alt="STMIK AMIK" class="cert-img">
                <div class="cert-info">
                    <div class="cert-title">Kompetensi Sistem Informasi</div>
                    <div class="cert-issuer">STMIK AMIK Bandung</div>
                </div>
            </div>
            <div class="cert-card">
                <img src="{c_humas}" alt="Magang Humas" class="cert-img">
                <div class="cert-info">
                    <div class="cert-title">Sertifikat Magang Humas</div>
                    <div class="cert-issuer">Diskominfo Kota Bandung</div>
                </div>
            </div>
            <div class="cert-card">
                <img src="{c_drafter}" alt="Magang Drafter" class="cert-img">
                <div class="cert-info">
                    <div class="cert-title">Sertifikat Drafter CAD</div>
                    <div class="cert-issuer">PT Nexwave</div>
                </div>
            </div>
            <div class="cert-card">
                <img src="{c_award}" alt="Piagam Penghargaan" class="cert-img">
                <div class="cert-info">
                    <div class="cert-title">Piagam Kontribusi Khusus</div>
                    <div class="cert-issuer">Program Magang Industri</div>
                </div>
            </div>
            <div class="cert-card">
                <img src="{c_digital}" alt="Pelatihan Digital" class="cert-img">
                <div class="cert-info">
                    <div class="cert-title">Keahlian Digital & IT</div>
                    <div class="cert-issuer">Lembaga Sertifikasi</div>
                </div>
            </div>
        </div>

        <div style="margin-top: 4.5mm; background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); border-radius: 8px; padding: 11px 15px; color: #ffffff; display: flex; justify-content: space-between; align-items: center;">
            <div>
                <strong style="font-size: 9.2pt; color: #ffffff; display: block;">Siap Berkontribusi & Berkolaborasi</strong>
                <span style="font-size: 7.3pt; color: #cbd5e1;">Terbuka untuk posisi Web Developer, GIS Specialist, Drafter CAD, dan IT Staff.</span>
            </div>
            <div style="text-align: right; font-size: 7.3pt;">
                <div style="font-weight: 700; color: #818cf8;">Muhamad Nizar Nurfalah, S.Kom.</div>
                <div style="color: #94a3b8;">nizarbeet88@gmail.com</div>
            </div>
        </div>

        <div class="page-footer">
            <span>Portofolio Resmi Muhamad Nizar Nurfalah</span>
            <span>Halaman 5 / 5</span>
        </div>
    </div>

</body>
</html>
"""

with open("generate_portfolio_doc.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Base64 embedded HTML generated successfully!")
