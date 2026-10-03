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
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
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
            color: #1a1a2e;
            font-size: 9pt;
            line-height: 1.5;
        }}
        .page {{
            width: 210mm;
            height: 297mm;
            page-break-after: always;
            position: relative;
            overflow: hidden;
        }}
        .page:last-child {{
            page-break-after: avoid;
        }}

        /* ======== PAGE 1: COVER ======== */
        .cover {{
            width: 100%;
            height: 100%;
            position: relative;
            display: flex;
            flex-direction: column;
        }}

        /* Dark hero top section */
        .cover-hero {{
            background: linear-gradient(145deg, #0a0a1a 0%, #16162a 40%, #1e1b4b 70%, #2e1065 100%);
            padding: 32mm 22mm 20mm 22mm;
            position: relative;
            flex-shrink: 0;
        }}

        /* Decorative geometric shapes */
        .cover-hero::before {{
            content: '';
            position: absolute;
            top: -30px;
            right: -20px;
            width: 200px;
            height: 200px;
            border: 3px solid rgba(139, 92, 246, 0.15);
            border-radius: 50%;
        }}
        .cover-hero::after {{
            content: '';
            position: absolute;
            bottom: 20px;
            right: 40px;
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.12), rgba(168, 85, 247, 0.08));
            border-radius: 12px;
            transform: rotate(45deg);
        }}

        .cover-accent-line {{
            position: absolute;
            top: 14mm;
            left: 22mm;
            right: 22mm;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .cover-accent-line .dot {{
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #8b5cf6;
        }}
        .cover-accent-line .line {{
            flex: 1;
            height: 1px;
            background: linear-gradient(90deg, rgba(139, 92, 246, 0.5), transparent);
        }}
        .cover-accent-line .label {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 7pt;
            color: rgba(255,255,255,0.35);
            text-transform: uppercase;
            letter-spacing: 3px;
        }}

        .cover-profile {{
            display: flex;
            align-items: center;
            gap: 22px;
            position: relative;
            z-index: 2;
        }}

        .cover-avatar-wrap {{
            position: relative;
            flex-shrink: 0;
        }}
        .cover-avatar {{
            width: 110px;
            height: 110px;
            border-radius: 20px;
            object-fit: cover;
            border: 3px solid rgba(139, 92, 246, 0.6);
            box-shadow: 0 8px 32px rgba(139, 92, 246, 0.3);
        }}
        .cover-avatar-badge {{
            position: absolute;
            bottom: -6px;
            right: -6px;
            background: linear-gradient(135deg, #8b5cf6, #6366f1);
            color: #fff;
            font-size: 6.5pt;
            font-weight: 700;
            padding: 3px 8px;
            border-radius: 6px;
            box-shadow: 0 2px 8px rgba(99, 102, 241, 0.4);
        }}

        .cover-name {{
            font-family: 'Outfit', sans-serif;
            font-size: 22pt;
            font-weight: 800;
            color: #ffffff;
            letter-spacing: -0.5px;
            line-height: 1.1;
            margin-bottom: 4px;
        }}
        .cover-tagline {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 10.5pt;
            color: #a78bfa;
            font-weight: 600;
            letter-spacing: 0.5px;
            margin-bottom: 12px;
        }}
        .cover-contacts {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }}
        .cover-contact-chip {{
            display: inline-flex;
            align-items: center;
            gap: 4px;
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.1);
            padding: 3px 10px;
            border-radius: 20px;
            font-size: 7pt;
            color: #cbd5e1;
        }}
        .cover-contact-chip .icon {{
            font-size: 9pt;
        }}

        /* Bottom white section */
        .cover-body {{
            flex: 1;
            padding: 8mm 22mm 12mm 22mm;
            display: flex;
            flex-direction: column;
            gap: 6mm;
            position: relative;
        }}

        .section-label {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 6.5pt;
            text-transform: uppercase;
            letter-spacing: 3px;
            color: #8b5cf6;
            font-weight: 700;
            margin-bottom: 2mm;
        }}
        .section-heading {{
            font-family: 'Outfit', sans-serif;
            font-size: 13pt;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 3mm;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .section-heading .accent-bar {{
            width: 24px;
            height: 3px;
            background: linear-gradient(90deg, #8b5cf6, #6366f1);
            border-radius: 2px;
        }}

        .profile-summary {{
            font-size: 8.8pt;
            color: #334155;
            line-height: 1.65;
            text-align: justify;
            padding: 12px 16px;
            background: linear-gradient(135deg, #f8faff 0%, #f0f0ff 100%);
            border-left: 3px solid #8b5cf6;
            border-radius: 0 10px 10px 0;
        }}

        /* Skills Capsules */
        .skills-row {{
            display: flex;
            gap: 10px;
        }}
        .skill-group {{
            flex: 1;
            padding: 10px 12px;
            border-radius: 10px;
            position: relative;
            overflow: hidden;
        }}
        .skill-group::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            border-radius: 10px 10px 0 0;
        }}
        .skill-group.purple {{
            background: #faf5ff;
            border: 1px solid #e9d5ff;
        }}
        .skill-group.purple::before {{
            background: linear-gradient(90deg, #8b5cf6, #a78bfa);
        }}
        .skill-group.blue {{
            background: #eff6ff;
            border: 1px solid #bfdbfe;
        }}
        .skill-group.blue::before {{
            background: linear-gradient(90deg, #3b82f6, #60a5fa);
        }}
        .skill-group.emerald {{
            background: #ecfdf5;
            border: 1px solid #a7f3d0;
        }}
        .skill-group.emerald::before {{
            background: linear-gradient(90deg, #10b981, #34d399);
        }}
        .skill-group-title {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 7.5pt;
            font-weight: 700;
            margin-bottom: 6px;
            padding-top: 4px;
        }}
        .skill-group.purple .skill-group-title {{ color: #7c3aed; }}
        .skill-group.blue .skill-group-title {{ color: #2563eb; }}
        .skill-group.emerald .skill-group-title {{ color: #059669; }}
        .skill-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 3px;
        }}
        .skill-tag {{
            display: inline-block;
            padding: 2px 7px;
            border-radius: 4px;
            font-size: 7pt;
            font-weight: 600;
        }}
        .skill-group.purple .skill-tag {{
            background: #ede9fe; color: #6d28d9; border: 1px solid #ddd6fe;
        }}
        .skill-group.blue .skill-tag {{
            background: #dbeafe; color: #1d4ed8; border: 1px solid #bfdbfe;
        }}
        .skill-group.emerald .skill-tag {{
            background: #d1fae5; color: #047857; border: 1px solid #a7f3d0;
        }}

        /* Experience Timeline */
        .timeline {{
            display: flex;
            flex-direction: column;
            gap: 0;
            position: relative;
            padding-left: 18px;
        }}
        .timeline::before {{
            content: '';
            position: absolute;
            left: 5px;
            top: 4px;
            bottom: 4px;
            width: 2px;
            background: linear-gradient(180deg, #8b5cf6, #c4b5fd, #e9d5ff);
            border-radius: 2px;
        }}
        .timeline-item {{
            position: relative;
            padding-left: 12px;
            padding-bottom: 8px;
        }}
        .timeline-item::before {{
            content: '';
            position: absolute;
            left: -16px;
            top: 5px;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: #fff;
            border: 2.5px solid #8b5cf6;
            box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.15);
        }}
        .timeline-role {{
            font-family: 'Outfit', sans-serif;
            font-size: 9.5pt;
            font-weight: 700;
            color: #0f172a;
        }}
        .timeline-company {{
            font-size: 8pt;
            color: #6366f1;
            font-weight: 600;
        }}
        .timeline-desc {{
            font-size: 7.5pt;
            color: #475569;
            margin-top: 2px;
            line-height: 1.4;
        }}

        .cover-footer {{
            margin-top: auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 7pt;
            color: #94a3b8;
            border-top: 1px solid #e2e8f0;
            padding-top: 3mm;
        }}

        /* ======== PAGE 2: PROJECT SHOWCASE ======== */
        .page-inner {{
            padding: 14mm 20mm;
            display: flex;
            flex-direction: column;
            height: 100%;
        }}

        .page-top-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 6mm;
            padding-bottom: 3mm;
            border-bottom: 2px solid #f1f5f9;
        }}
        .page-top-bar-title {{
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 14pt;
            color: #0f172a;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .page-top-bar-title .highlight {{
            color: #8b5cf6;
        }}
        .page-top-bar-subtitle {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 7.5pt;
            color: #8b5cf6;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 2px;
            background: #faf5ff;
            padding: 4px 12px;
            border-radius: 20px;
            border: 1px solid #e9d5ff;
        }}

        /* Featured Project Card */
        .featured-project {{
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
            border-radius: 14px;
            padding: 16px;
            display: flex;
            gap: 16px;
            margin-bottom: 5mm;
            color: #fff;
            position: relative;
            overflow: hidden;
        }}
        .featured-project::after {{
            content: 'FEATURED';
            position: absolute;
            top: 10px;
            right: -28px;
            background: linear-gradient(90deg, #8b5cf6, #6366f1);
            color: #fff;
            font-family: 'Space Grotesk', sans-serif;
            font-size: 6pt;
            font-weight: 700;
            letter-spacing: 2px;
            padding: 3px 36px;
            transform: rotate(45deg);
        }}
        .featured-thumb {{
            width: 180px;
            height: 115px;
            object-fit: cover;
            border-radius: 10px;
            border: 2px solid rgba(139, 92, 246, 0.4);
            flex-shrink: 0;
        }}
        .featured-body {{
            flex: 1;
            display: flex;
            flex-direction: column;
        }}
        .featured-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 11pt;
            font-weight: 700;
            margin-bottom: 4px;
        }}
        .featured-desc {{
            font-size: 7.8pt;
            color: #cbd5e1;
            line-height: 1.4;
            margin-bottom: 6px;
        }}
        .featured-features {{
            font-size: 7pt;
            color: #a5b4fc;
            padding-left: 14px;
            margin-bottom: 6px;
        }}
        .featured-features li {{
            margin-bottom: 1.5px;
        }}
        .featured-footer {{
            margin-top: auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid rgba(255,255,255,0.1);
            padding-top: 6px;
        }}
        .featured-tags {{
            display: flex;
            gap: 4px;
        }}
        .featured-tag {{
            background: rgba(139, 92, 246, 0.2);
            border: 1px solid rgba(139, 92, 246, 0.4);
            padding: 2px 7px;
            border-radius: 4px;
            font-size: 6.5pt;
            color: #c4b5fd;
            font-weight: 600;
        }}
        .featured-link {{
            color: #a78bfa;
            font-size: 7pt;
            font-weight: 600;
            text-decoration: none;
        }}

        /* Standard Project Cards */
        .projects-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-bottom: 5mm;
        }}
        .project-card {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            overflow: hidden;
            position: relative;
            box-shadow: 0 1px 4px rgba(0,0,0,0.04);
        }}
        .project-card-img {{
            width: 100%;
            height: 88px;
            object-fit: cover;
            display: block;
        }}
        .project-card-body {{
            padding: 10px 12px;
        }}
        .project-card-number {{
            position: absolute;
            top: 6px;
            left: 8px;
            background: rgba(0,0,0,0.6);
            color: #fff;
            font-family: 'Outfit', sans-serif;
            font-size: 7pt;
            font-weight: 700;
            width: 22px;
            height: 22px;
            border-radius: 6px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .project-card-category {{
            display: inline-block;
            font-family: 'Space Grotesk', sans-serif;
            font-size: 6pt;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            font-weight: 700;
            color: #8b5cf6;
            margin-bottom: 2px;
        }}
        .project-card-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 9pt;
            font-weight: 700;
            color: #0f172a;
            line-height: 1.2;
            margin-bottom: 3px;
        }}
        .project-card-desc {{
            font-size: 7pt;
            color: #475569;
            line-height: 1.35;
            margin-bottom: 5px;
        }}
        .project-card-features {{
            font-size: 6.5pt;
            color: #334155;
            padding-left: 12px;
            margin-bottom: 5px;
        }}
        .project-card-features li {{
            margin-bottom: 1px;
        }}
        .project-card-footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid #f1f5f9;
            padding-top: 5px;
        }}
        .project-card-tags {{
            display: flex;
            gap: 3px;
        }}
        .mini-tag {{
            padding: 1.5px 5px;
            border-radius: 3px;
            font-size: 6pt;
            font-weight: 600;
            background: #ede9fe;
            color: #6d28d9;
            border: 1px solid #ddd6fe;
        }}
        .mini-tag.blue {{
            background: #dbeafe; color: #1d4ed8; border: 1px solid #bfdbfe;
        }}
        .mini-tag.green {{
            background: #d1fae5; color: #047857; border: 1px solid #a7f3d0;
        }}
        .project-card-link {{
            font-size: 6.5pt;
            color: #8b5cf6;
            font-weight: 600;
            text-decoration: none;
        }}

        /* ======== PAGE 3 ======== */
        .compact-projects-row {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-bottom: 6mm;
        }}
        .compact-card {{
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 1px 4px rgba(0,0,0,0.04);
        }}
        .compact-card-img {{
            width: 100%;
            height: 82px;
            object-fit: cover;
        }}
        .compact-card-body {{
            padding: 9px 12px;
        }}
        .compact-card-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 8.5pt;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 3px;
        }}
        .compact-card-desc {{
            font-size: 7pt;
            color: #475569;
            line-height: 1.35;
            margin-bottom: 4px;
        }}
        .compact-card-link {{
            font-size: 6.5pt;
            color: #8b5cf6;
            font-weight: 600;
            text-decoration: none;
        }}

        /* Humas Section */
        .humas-section {{
            background: #faf5ff;
            border: 1px solid #e9d5ff;
            border-radius: 12px;
            padding: 14px 16px;
            margin-bottom: 5mm;
        }}
        .humas-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
        }}
        .humas-card {{
            background: #fff;
            border: 1px solid #e9d5ff;
            border-radius: 8px;
            padding: 8px 10px;
            position: relative;
        }}
        .humas-number {{
            position: absolute;
            top: 6px;
            right: 8px;
            font-family: 'Outfit', sans-serif;
            font-size: 14pt;
            font-weight: 800;
            color: rgba(139, 92, 246, 0.08);
            line-height: 1;
        }}
        .humas-title {{
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            color: #0f172a;
            font-size: 7.8pt;
            margin-bottom: 2px;
            line-height: 1.25;
        }}
        .humas-desc {{
            font-size: 6.8pt;
            color: #64748b;
            margin-bottom: 3px;
        }}
        .humas-link {{
            color: #8b5cf6;
            text-decoration: none;
            font-size: 6.5pt;
            font-weight: 600;
            word-break: break-all;
        }}

        /* CTA Footer */
        .cta-footer {{
            margin-top: auto;
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #2e1065 100%);
            border-radius: 14px;
            padding: 16px 20px;
            color: #fff;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: relative;
            overflow: hidden;
        }}
        .cta-footer::before {{
            content: '';
            position: absolute;
            top: -20px;
            right: -10px;
            width: 100px;
            height: 100px;
            border: 2px solid rgba(139, 92, 246, 0.15);
            border-radius: 50%;
        }}
        .cta-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 11pt;
            font-weight: 700;
            margin-bottom: 2px;
        }}
        .cta-sub {{
            font-size: 7.5pt;
            color: #a5b4fc;
        }}
        .cta-right {{
            text-align: right;
            font-size: 7.5pt;
            position: relative;
            z-index: 2;
        }}
        .cta-name {{
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            color: #c4b5fd;
            font-size: 9pt;
        }}
        .cta-email {{
            color: #94a3b8;
        }}

        .page-footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 7pt;
            color: #94a3b8;
            padding-top: 3mm;
            border-top: 1px solid #f1f5f9;
            margin-top: auto;
        }}
        .page-footer .page-num {{
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            color: #8b5cf6;
            font-size: 8pt;
        }}
    </style>
</head>
<body>

    <!-- ==================== PAGE 1: CREATIVE COVER ==================== -->
    <div class="page">
        <div class="cover">
            <div class="cover-hero">
                <div class="cover-accent-line">
                    <div class="dot"></div>
                    <div class="line"></div>
                    <div class="label">Portfolio 2024</div>
                </div>
                <div class="cover-profile">
                    <div class="cover-avatar-wrap">
                        <img src="{img_avatar}" alt="Nizar" class="cover-avatar">
                        <div class="cover-avatar-badge">S.Kom</div>
                    </div>
                    <div>
                        <div class="cover-name">MUHAMAD NIZAR<br>NURFALAH</div>
                        <div class="cover-tagline">Web Developer &bull; WebGIS Specialist &bull; Drafter &bull; Creative Media</div>
                        <div class="cover-contacts">
                            <span class="cover-contact-chip"><span class="icon">📍</span> Bandung, Jawa Barat</span>
                            <span class="cover-contact-chip"><span class="icon">✉️</span> nizqrnurfalah@gmail.com</span>
                            <span class="cover-contact-chip"><span class="icon">💻</span> github.com/nizarnurfalah</span>
                            <span class="cover-contact-chip"><span class="icon">🔗</span> linkedin.com/in/muhamad-nizar-nurfalah</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="cover-body">
                <div>
                    <div class="section-label">Tentang Saya</div>
                    <div class="section-heading"><span class="accent-bar"></span> Ringkasan Profil Profesional</div>
                    <div class="profile-summary">
                        Lulusan <strong>S1 Sistem Informasi STMIK AMIK Bandung</strong> dengan fokus keahlian pada <strong>Web Development, Sistem Informasi Geografis (WebGIS), AutoCAD Drafting</strong>, dan <strong>Media Publikasi Kreatif</strong>. Berpengalaman magang &plusmn;10 bulan di Diskominfo Kota Bandung dan PT Nexwave, mencakup pembuatan aplikasi web interaktif berbasis peta spasial, penyusunan berkas gambar teknik telekomunikasi, serta publikasi berita dan konten video kreatif.
                    </div>
                </div>

                <div>
                    <div class="section-label">Keahlian</div>
                    <div class="section-heading"><span class="accent-bar"></span> Tech Stack &amp; Kompetensi</div>
                    <div class="skills-row">
                        <div class="skill-group purple">
                            <div class="skill-group-title">🌐 Web &amp; GIS</div>
                            <div class="skill-tags">
                                <span class="skill-tag">WebGIS</span>
                                <span class="skill-tag">Leaflet.js</span>
                                <span class="skill-tag">JavaScript</span>
                                <span class="skill-tag">React.js</span>
                                <span class="skill-tag">Laravel</span>
                                <span class="skill-tag">HTML/CSS</span>
                            </div>
                        </div>
                        <div class="skill-group blue">
                            <div class="skill-group-title">📐 Drafting</div>
                            <div class="skill-tags">
                                <span class="skill-tag">AutoCAD</span>
                                <span class="skill-tag">Gambar Teknik</span>
                                <span class="skill-tag">SID Survey</span>
                                <span class="skill-tag">DWG/PDF</span>
                            </div>
                        </div>
                        <div class="skill-group emerald">
                            <div class="skill-group-title">🎬 Media &amp; Tools</div>
                            <div class="skill-tags">
                                <span class="skill-tag">Artikel Rilis</span>
                                <span class="skill-tag">Video Editing</span>
                                <span class="skill-tag">Git/GitHub</span>
                                <span class="skill-tag">VS Code</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div>
                    <div class="section-label">Pengalaman</div>
                    <div class="section-heading"><span class="accent-bar"></span> Riwayat Magang Profesional</div>
                    <div class="timeline">
                        <div class="timeline-item">
                            <div class="timeline-role">Drafter Telekomunikasi</div>
                            <div class="timeline-company">PT Nexwave &mdash; Magang Industri</div>
                            <div class="timeline-desc">Menyusun dokumen gambar teknik blueprint AutoCAD (SID survey, tiang monopole, as-built drawing) dengan standar format industri telekomunikasi.</div>
                        </div>
                        <div class="timeline-item">
                            <div class="timeline-role">Humas &amp; Creative Media</div>
                            <div class="timeline-company">Diskominfo Kota Bandung &mdash; Magang Kedinasan</div>
                            <div class="timeline-desc">Menulis dan menerbitkan 11 artikel berita rilis pers di portal bandung.go.id serta memproduksi 13 video reels publikasi kegiatan kedinasan.</div>
                        </div>
                    </div>
                </div>

                <div class="cover-footer">
                    <span>Portofolio Resmi &mdash; Muhamad Nizar Nurfalah, S.Kom.</span>
                    <span style="font-family: 'Outfit'; font-weight: 700; color: #8b5cf6; font-size: 8pt;">01 / 03</span>
                </div>
            </div>
        </div>
    </div>

    <!-- ==================== PAGE 2: PROJECT SHOWCASE ==================== -->
    <div class="page">
        <div class="page-inner">
            <div class="page-top-bar">
                <div class="page-top-bar-title">Showcase <span class="highlight">Proyek</span></div>
                <div class="page-top-bar-subtitle">WebGIS &amp; Geospatial Solutions</div>
            </div>

            <!-- Featured Project -->
            <div class="featured-project">
                <img src="{img_p1}" alt="WebGIS Longsor" class="featured-thumb">
                <div class="featured-body">
                    <div class="featured-title">WebGIS Pemetaan Rawan Longsor Kabupaten Kuningan</div>
                    <div class="featured-desc">
                        Sistem Informasi Geografis interaktif berbasis web untuk pemetaan zonasi kerawanan dan visualisasi spasial mitigasi bencana tanah longsor di Kabupaten Kuningan.
                    </div>
                    <ul class="featured-features">
                        <li>Peta interaktif multi-layering zonasi rawan bencana berbasis Leaflet.js</li>
                        <li>Visualisasi batas wilayah, kemiringan lereng, dan parameter kerawanan tanah</li>
                        <li>Desain responsif yang mudah diakses oleh publik</li>
                    </ul>
                    <div class="featured-footer">
                        <div class="featured-tags">
                            <span class="featured-tag">Leaflet</span>
                            <span class="featured-tag">JavaScript</span>
                            <span class="featured-tag">HTML/CSS</span>
                        </div>
                        <a href="https://nizarnurfalah.github.io/webgis_longsor_kuningan/" class="featured-link">🔗 nizarnurfalah.github.io/webgis_longsor_kuningan</a>
                    </div>
                </div>
            </div>

            <!-- 2 Project Cards Grid -->
            <div class="projects-grid">
                <div class="project-card">
                    <div class="project-card-number">02</div>
                    <img src="{img_tower}" alt="Microwave Tower" class="project-card-img">
                    <div class="project-card-body">
                        <div class="project-card-category">GIS &amp; Telecom</div>
                        <div class="project-card-title">WebGIS Radius &amp; Transmisi Microwave Tower BTS</div>
                        <div class="project-card-desc">
                            Pemetaan jarak dan radius pancaran gelombang mikro antar menara BTS dilengkapi kalkulator Fresnel Zone.
                        </div>
                        <ul class="project-card-features">
                            <li>Kalkulator Fresnel Zone otomatis untuk validasi transmisi</li>
                            <li>Visualisasi radius coverage antena dan marker tower interaktif</li>
                            <li>Fitur uji titik koordinat dan pencarian BTS terdekat</li>
                        </ul>
                        <div class="project-card-footer">
                            <div class="project-card-tags">
                                <span class="mini-tag">Leaflet</span>
                                <span class="mini-tag blue">Fresnel</span>
                                <span class="mini-tag blue">Bootstrap</span>
                            </div>
                            <a href="https://nizarnurfalah.github.io/pancaranradius_microwave/" class="project-card-link">🔗 Live Demo</a>
                        </div>
                    </div>
                </div>
                <div class="project-card">
                    <div class="project-card-number">03</div>
                    <img src="{img_lapor}" alt="Laporan Fasilitas" class="project-card-img">
                    <div class="project-card-body">
                        <div class="project-card-category">Public Service</div>
                        <div class="project-card-title">WebGIS Pemetaan &amp; Pengaduan Fasilitas Publik</div>
                        <div class="project-card-desc">
                            Platform pelaporan dan pemetaan titik kerusakan fasilitas publik dengan pelacakan status penanganan.
                        </div>
                        <ul class="project-card-features">
                            <li>Formulir pengaduan dengan pin lokasi titik koordinat langsung</li>
                            <li>Filter multi-kategori kerusakan dan status penanganan</li>
                            <li>Dashboard admin untuk monitoring laporan masuk</li>
                        </ul>
                        <div class="project-card-footer">
                            <div class="project-card-tags">
                                <span class="mini-tag green">Leaflet</span>
                                <span class="mini-tag green">JS</span>
                                <span class="mini-tag green">Admin</span>
                            </div>
                            <a href="https://nizarnurfalah.github.io/pemetaan-laporan-fasilitas/" class="project-card-link">🔗 Live Demo</a>
                        </div>
                    </div>
                </div>
            </div>

            <div class="page-footer">
                <span>Portofolio Resmi &mdash; Muhamad Nizar Nurfalah, S.Kom.</span>
                <span class="page-num">02 / 03</span>
            </div>
        </div>
    </div>

    <!-- ==================== PAGE 3: MORE PROJECTS & PUBLICATIONS ==================== -->
    <div class="page">
        <div class="page-inner">
            <div class="page-top-bar">
                <div class="page-top-bar-title">Proyek <span class="highlight">Lainnya</span> &amp; Publikasi</div>
                <div class="page-top-bar-subtitle">Web Apps &amp; Media Humas</div>
            </div>

            <div class="compact-projects-row">
                <div class="compact-card">
                    <img src="{img_p2}" alt="Perhitungan Pipa" class="compact-card-img">
                    <div class="compact-card-body">
                        <div class="project-card-category">Engineering Tool</div>
                        <div class="compact-card-title">Kalkulator Perhitungan Pipa Teknis</div>
                        <div class="compact-card-desc">Kalkulator simulasi teknik untuk menghitung dimensi pipa, kecepatan aliran, dan kerugian tekanan (headloss) fluida secara presisi.</div>
                        <a href="https://nizarnurfalah.github.io/PerhitunganPipa/" class="compact-card-link">🔗 nizarnurfalah.github.io/PerhitunganPipa</a>
                    </div>
                </div>
                <div class="compact-card">
                    <img src="{img_p3}" alt="Jadwal Theater" class="compact-card-img">
                    <div class="compact-card-body">
                        <div class="project-card-category">Web Platform</div>
                        <div class="compact-card-title">Website Informasi Jadwal Teater Unisba</div>
                        <div class="compact-card-desc">Platform web katalog pementasan teater Unisba, informasi jadwal acara, dan registrasi pementasan seni budaya interaktif.</div>
                        <a href="https://nizarnurfalah.github.io/jadwaltheaterunisba/" class="compact-card-link">🔗 nizarnurfalah.github.io/jadwaltheaterunisba</a>
                    </div>
                </div>
            </div>

            <div>
                <div class="section-label">Media Publikasi</div>
                <div class="section-heading"><span class="accent-bar"></span> Artikel Rilis Pers — Diskominfo Kota Bandung</div>
            </div>

            <div class="humas-section">
                <div class="humas-grid">
                    <div class="humas-card">
                        <div class="humas-number">01</div>
                        <div class="humas-title">Penanganan Sampah TPS Gunung Batu Timur</div>
                        <div class="humas-desc">Liputan reaksi cepat penanganan TPS oleh aparat Kelurahan Sukagalih.</div>
                        <a href="https://www.bandung.go.id/news/read/12616/tumpukan-sampah-tps-gunung-batu-timur-menghilang-aparat-kelurahan-suk" class="humas-link">bandung.go.id/news/read/12616/...</a>
                    </div>
                    <div class="humas-card">
                        <div class="humas-number">02</div>
                        <div class="humas-title">RSUD Bandung Kiwari: Simulasi Gempa</div>
                        <div class="humas-desc">Kesiapsiagaan mitigasi bencana gempa bumi tenaga medis dan staf RS.</div>
                        <a href="https://www.bandung.go.id/news/read/12369/rsud-bandung-kiwari-tingkatkan-kesiapsiagaan-bencana-lewat-simulasi-pe" class="humas-link">bandung.go.id/news/read/12369/...</a>
                    </div>
                    <div class="humas-card">
                        <div class="humas-number">03</div>
                        <div class="humas-title">KDM Fest: Pemilihan Duta Dekranasda</div>
                        <div class="humas-desc">Promosi inovasi kerajinan kriya dan representasi duta Kota Bandung.</div>
                        <a href="https://www.bandung.go.id/news/read/12379/kembang-nusa-x-kdm-fest-dua-wakil-kota-bandung-bersaing-jadi-duta-dek" class="humas-link">bandung.go.id/news/read/12379/...</a>
                    </div>
                    <div class="humas-card">
                        <div class="humas-number">04</div>
                        <div class="humas-title">Bazar Gemar Ikan DKPP Kota Bandung</div>
                        <div class="humas-desc">Kampanye gizi protein ikan dan promosi pembudidaya ikan lokal.</div>
                        <a href="https://www.bandung.go.id/news/read/12499/azar-gemar-ikan-dkpp-kota-bandung-sukses-ajang-promobandung-city-depa" class="humas-link">bandung.go.id/news/read/12499/...</a>
                    </div>
                </div>
            </div>

            <div style="margin-top: 2mm;">
                <div class="section-label">Creative Media</div>
                <div class="section-heading" style="margin-bottom: 2mm;"><span class="accent-bar"></span> Video Konten Publikasi — Instagram Reels</div>
            </div>

            <div style="background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); border-radius: 12px; padding: 12px 14px; margin-bottom: 5mm;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <span style="font-family: 'Outfit', sans-serif; font-size: 8pt; font-weight: 700; color: #c4b5fd;">🎬 13 Video Reels diproduksi untuk @diskominfobdg</span>
                    <span style="font-size: 6.5pt; color: #94a3b8; font-weight: 600; background: rgba(255,255,255,0.06); padding: 2px 8px; border-radius: 10px;">Instagram Reels</span>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 5px;">
                    <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 6px; padding: 5px 7px;">
                        <div style="font-size: 6.5pt; font-weight: 700; color: #e2e8f0; line-height: 1.2; margin-bottom: 2px;">Liputan TPS &amp; Kebersihan</div>
                        <a href="https://www.instagram.com/reel/DRD3WZmEx2J/" style="font-size: 5.5pt; color: #a78bfa; text-decoration: none;">🔗 Lihat Reels</a>
                    </div>
                    <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 6px; padding: 5px 7px;">
                        <div style="font-size: 6.5pt; font-weight: 700; color: #e2e8f0; line-height: 1.2; margin-bottom: 2px;">Edukasi Program Diskominfo</div>
                        <a href="https://www.instagram.com/reel/DQ5-thk6RP/" style="font-size: 5.5pt; color: #a78bfa; text-decoration: none;">🔗 Lihat Reels</a>
                    </div>
                    <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 6px; padding: 5px 7px;">
                        <div style="font-size: 6.5pt; font-weight: 700; color: #e2e8f0; line-height: 1.2; margin-bottom: 2px;">Pelayanan Terpadu Warga</div>
                        <a href="https://www.instagram.com/reel/DQ3bBpxk1V_/" style="font-size: 5.5pt; color: #a78bfa; text-decoration: none;">🔗 Lihat Reels</a>
                    </div>
                    <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 6px; padding: 5px 7px;">
                        <div style="font-size: 6.5pt; font-weight: 700; color: #e2e8f0; line-height: 1.2; margin-bottom: 2px;">Tanggap Bencana Gempa</div>
                        <a href="https://www.instagram.com/reel/DQ29-tZE3y9/" style="font-size: 5.5pt; color: #a78bfa; text-decoration: none;">🔗 Lihat Reels</a>
                    </div>
                    <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 6px; padding: 5px 7px;">
                        <div style="font-size: 6.5pt; font-weight: 700; color: #e2e8f0; line-height: 1.2; margin-bottom: 2px;">Festival Dekranasda</div>
                        <a href="https://www.instagram.com/reel/DQas1yUExg1/" style="font-size: 5.5pt; color: #a78bfa; text-decoration: none;">🔗 Lihat Reels</a>
                    </div>
                    <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 6px; padding: 5px 7px;">
                        <div style="font-size: 6.5pt; font-weight: 700; color: #e2e8f0; line-height: 1.2; margin-bottom: 2px;">Pilah Sampah Mandiri</div>
                        <a href="https://www.instagram.com/reel/DQVdaIUE6vC/" style="font-size: 5.5pt; color: #a78bfa; text-decoration: none;">🔗 Lihat Reels</a>
                    </div>
                    <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 6px; padding: 5px 7px;">
                        <div style="font-size: 6.5pt; font-weight: 700; color: #e2e8f0; line-height: 1.2; margin-bottom: 2px;">Simulasi Darurat RSUD</div>
                        <a href="https://www.instagram.com/reel/DQDmgzxE2aM/" style="font-size: 5.5pt; color: #a78bfa; text-decoration: none;">🔗 Lihat Reels</a>
                    </div>
                    <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 6px; padding: 5px 7px;">
                        <div style="font-size: 6.5pt; font-weight: 700; color: #e2e8f0; line-height: 1.2; margin-bottom: 2px;">Citylight Carnival UMKM</div>
                        <a href="https://www.instagram.com/reel/DQBzL1fk9qg/" style="font-size: 5.5pt; color: #a78bfa; text-decoration: none;">🔗 Lihat Reels</a>
                    </div>
                    <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 6px; padding: 5px 7px;">
                        <div style="font-size: 6.5pt; font-weight: 700; color: #e2e8f0; line-height: 1.2; margin-bottom: 2px;">Floranimal Fest Komunitas</div>
                        <a href="https://www.instagram.com/reel/DP5a9Jsk23b/" style="font-size: 5.5pt; color: #a78bfa; text-decoration: none;">🔗 Lihat Reels</a>
                    </div>
                    <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 6px; padding: 5px 7px;">
                        <div style="font-size: 6.5pt; font-weight: 700; color: #e2e8f0; line-height: 1.2; margin-bottom: 2px;">Gemar Ikan Bersama DKPP</div>
                        <a href="https://www.instagram.com/reel/DP0F36Mk4jS/" style="font-size: 5.5pt; color: #a78bfa; text-decoration: none;">🔗 Lihat Reels</a>
                    </div>
                    <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 6px; padding: 5px 7px;">
                        <div style="font-size: 6.5pt; font-weight: 700; color: #e2e8f0; line-height: 1.2; margin-bottom: 2px;">Maggot Fest Inovasi Sampah</div>
                        <a href="https://www.instagram.com/reel/DPm6qAiEwZw/" style="font-size: 5.5pt; color: #a78bfa; text-decoration: none;">🔗 Lihat Reels</a>
                    </div>
                    <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 6px; padding: 5px 7px;">
                        <div style="font-size: 6.5pt; font-weight: 700; color: #e2e8f0; line-height: 1.2; margin-bottom: 2px;">Jajap Persib Heritage Tour</div>
                        <a href="https://www.instagram.com/reel/DPX0_SLkznm/" style="font-size: 5.5pt; color: #a78bfa; text-decoration: none;">🔗 Lihat Reels</a>
                    </div>
                </div>
                <div style="text-align: center; margin-top: 6px; font-size: 6pt; color: #64748b;">+ 1 video lainnya: Penyambutan Special Olympics Southeast Asia 2025 — <a href="https://www.instagram.com/reel/DPQNLVKk2na/" style="color: #a78bfa; text-decoration: none;">instagram.com/reel/DPQNLVKk2na</a></div>
            </div>

            <!-- CTA Footer -->
            <div class="cta-footer">
                <div>
                    <div class="cta-title">Siap Berkontribusi &amp; Berkolaborasi 🚀</div>
                    <div class="cta-sub">Terbuka untuk posisi Web Developer, WebGIS Specialist, Drafter, Creative Media, dan IT Staff.</div>
                </div>
                <div class="cta-right">
                    <div class="cta-name">Muhamad Nizar Nurfalah, S.Kom.</div>
                    <div class="cta-email">nizqrnurfalah@gmail.com</div>
                    <div class="cta-email">🌐 nizarnurfalah.github.io/PortofolioNizarNurfalah</div>
                </div>
            </div>

            <div class="page-footer">
                <span>Portofolio Resmi &mdash; Muhamad Nizar Nurfalah, S.Kom.</span>
                <span class="page-num">03 / 03</span>
            </div>
        </div>
    </div>

</body>
</html>
"""

with open("generate_portfolio_doc.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Creative 3-page portfolio HTML generated successfully!")
