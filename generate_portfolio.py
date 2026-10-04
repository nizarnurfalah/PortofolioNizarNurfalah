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
img_cad = get_base64_image("images/thumbnail_autocad.jpg")

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
            font-size: 8.5pt;
            line-height: 1.45;
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

        .cover-hero {{
            background: linear-gradient(145deg, #090a16 0%, #111326 40%, #1a153b 70%, #25124d 100%);
            padding: 26mm 20mm 18mm 20mm;
            position: relative;
            flex-shrink: 0;
        }}

        .cover-hero::before {{
            content: '';
            position: absolute;
            top: -30px;
            right: -20px;
            width: 180px;
            height: 180px;
            border: 2px solid rgba(139, 92, 246, 0.15);
            border-radius: 50%;
        }}
        .cover-hero::after {{
            content: '';
            position: absolute;
            bottom: 20px;
            right: 40px;
            width: 70px;
            height: 70px;
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.12), rgba(168, 85, 247, 0.08));
            border-radius: 12px;
            transform: rotate(45deg);
        }}

        .cover-accent-line {{
            position: absolute;
            top: 12mm;
            left: 20mm;
            right: 20mm;
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
            font-size: 7.5pt;
            color: rgba(255,255,255,0.45);
            text-transform: uppercase;
            letter-spacing: 3px;
            font-weight: 700;
        }}

        .cover-profile {{
            display: flex;
            align-items: center;
            gap: 20px;
            position: relative;
            z-index: 2;
        }}

        .cover-avatar-wrap {{
            position: relative;
            flex-shrink: 0;
        }}
        .cover-avatar {{
            width: 105px;
            height: 105px;
            border-radius: 20px;
            object-fit: cover;
            border: 3px solid rgba(139, 92, 246, 0.6);
            box-shadow: 0 8px 32px rgba(139, 92, 246, 0.35);
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
            font-size: 21pt;
            font-weight: 800;
            color: #ffffff;
            letter-spacing: -0.5px;
            line-height: 1.1;
            margin-bottom: 4px;
        }}
        .cover-tagline {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 10pt;
            color: #a78bfa;
            font-weight: 600;
            letter-spacing: 0.3px;
            margin-bottom: 10px;
        }}
        .cover-contacts {{
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
        }}
        .cover-contact-chip {{
            display: inline-flex;
            align-items: center;
            gap: 4px;
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.1);
            padding: 3px 9px;
            border-radius: 20px;
            font-size: 6.8pt;
            color: #cbd5e1;
        }}
        .cover-contact-chip .icon {{
            font-size: 8pt;
        }}
        .cover-contact-chip.badge-avail {{
            background: rgba(34, 197, 94, 0.15);
            border-color: rgba(34, 197, 94, 0.3);
            color: #86efac;
            font-weight: 600;
        }}

        .cover-body {{
            background: #ffffff;
            flex: 1;
            padding: 14mm 20mm 12mm 20mm;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        .section-label {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 7.5pt;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: #8b5cf6;
            margin-bottom: 3px;
        }}
        .section-heading {{
            font-family: 'Outfit', sans-serif;
            font-size: 11.5pt;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .section-heading .accent-bar {{
            width: 4px;
            height: 14px;
            background: #8b5cf6;
            border-radius: 2px;
        }}

        .profile-summary {{
            font-size: 8.5pt;
            color: #334155;
            line-height: 1.6;
            background: #f8fafc;
            border-left: 3px solid #8b5cf6;
            padding: 10px 14px;
            border-radius: 0 8px 8px 0;
            margin-bottom: 10px;
        }}

        .skills-row {{
            display: grid;
            grid-template-columns: 1.2fr 1fr 1fr;
            gap: 10px;
            margin-bottom: 10px;
        }}
        .skill-group {{
            background: #f8fafc;
            border-radius: 8px;
            padding: 9px 11px;
            border: 1px solid #e2e8f0;
        }}
        .skill-group.purple {{ border-top: 3px solid #8b5cf6; }}
        .skill-group.blue {{ border-top: 3px solid #3b82f6; }}
        .skill-group.emerald {{ border-top: 3px solid #10b981; }}
        .skill-group-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 8.5pt;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 6px;
        }}
        .skill-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 4px;
        }}
        .skill-tag {{
            font-size: 6.8pt;
            font-weight: 600;
            background: #ede9fe;
            color: #6d28d9;
            padding: 2px 6px;
            border-radius: 4px;
        }}
        .skill-group.blue .skill-tag {{
            background: #dbeafe;
            color: #1d4ed8;
        }}
        .skill-group.emerald .skill-tag {{
            background: #d1fae5;
            color: #047857;
        }}

        .timeline {{
            display: flex;
            flex-direction: column;
            gap: 8px;
        }}
        .timeline-item {{
            position: relative;
            padding-left: 18px;
            border-left: 2px solid #e2e8f0;
        }}
        .timeline-item::before {{
            content: '';
            position: absolute;
            left: -5px;
            top: 4px;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #8b5cf6;
        }}
        .timeline-role {{
            font-family: 'Outfit', sans-serif;
            font-size: 8.8pt;
            font-weight: 700;
            color: #0f172a;
        }}
        .timeline-company {{
            font-size: 7.5pt;
            color: #64748b;
            font-weight: 600;
            margin-bottom: 2px;
        }}
        .timeline-desc {{
            font-size: 7.8pt;
            color: #475569;
            line-height: 1.4;
        }}

        .cover-footer {{
            border-top: 1px solid #e2e8f0;
            padding-top: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 7pt;
            color: #94a3b8;
        }}

        /* ======== PAGES 2 & 3 ======== */
        .page-inner {{
            padding: 16mm 20mm 14mm 20mm;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        .page-top-bar {{
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            border-bottom: 2px solid #0f172a;
            padding-bottom: 6px;
            margin-bottom: 12px;
        }}
        .page-top-bar-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 15pt;
            font-weight: 800;
            color: #0f172a;
            letter-spacing: -0.5px;
        }}
        .page-top-bar-title .highlight {{
            color: #8b5cf6;
        }}
        .page-top-bar-subtitle {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 7.5pt;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            font-weight: 600;
        }}

        /* Featured Project (Skripsi) */
        .featured-project {{
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
            border-radius: 12px;
            padding: 14px 16px;
            color: #ffffff;
            position: relative;
            overflow: hidden;
            margin-bottom: 11px;
            box-shadow: 0 4px 20px rgba(15, 23, 42, 0.15);
        }}
        .featured-project::after {{
            content: 'SKRIPSI / CASE STUDY';
            position: absolute;
            top: 10px;
            right: 14px;
            background: linear-gradient(135deg, #ec4899, #8b5cf6);
            color: #ffffff;
            font-family: 'Space Grotesk', sans-serif;
            font-size: 6pt;
            font-weight: 700;
            letter-spacing: 1px;
            padding: 3px 8px;
            border-radius: 4px;
        }}
        .featured-header-wrap {{
            display: flex;
            gap: 14px;
            margin-bottom: 9px;
        }}
        .featured-thumb {{
            width: 145px;
            height: 96px;
            border-radius: 8px;
            object-fit: cover;
            border: 1px solid rgba(255,255,255,0.15);
            flex-shrink: 0;
        }}
        .featured-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 11.5pt;
            font-weight: 800;
            color: #ffffff;
            line-height: 1.25;
            margin-bottom: 4px;
            padding-right: 110px;
        }}
        .featured-meta {{
            font-size: 7.2pt;
            color: #94a3b8;
            margin-bottom: 5px;
        }}
        .featured-desc {{
            font-size: 7.6pt;
            color: #cbd5e1;
            line-height: 1.45;
        }}
        .case-study-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 8px;
            padding: 8px 10px;
            margin-bottom: 9px;
        }}
        .case-box-title {{
            font-size: 6.8pt;
            font-weight: 700;
            color: #a78bfa;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 2px;
        }}
        .case-box-text {{
            font-size: 7.2pt;
            color: #e2e8f0;
            line-height: 1.35;
        }}
        .featured-footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .featured-tags {{
            display: flex;
            gap: 4px;
            flex-wrap: wrap;
        }}
        .featured-tag {{
            font-size: 6.2pt;
            font-weight: 600;
            background: rgba(139, 92, 246, 0.25);
            color: #c4b5fd;
            padding: 2px 7px;
            border-radius: 4px;
            border: 1px solid rgba(139, 92, 246, 0.4);
        }}
        .project-links-wrap {{
            display: flex;
            gap: 8px;
        }}
        .featured-link {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 6.8pt;
            color: #a78bfa;
            text-decoration: none;
            font-weight: 700;
            background: rgba(255,255,255,0.08);
            padding: 3px 8px;
            border-radius: 4px;
        }}

        /* 2 Project Cards Grid on Page 2 */
        .projects-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-bottom: 4px;
        }}
        .project-card {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            box-shadow: 0 2px 10px rgba(0,0,0,0.04);
            position: relative;
        }}
        .project-card-number {{
            position: absolute;
            top: 7px;
            right: 8px;
            font-family: 'Space Grotesk', sans-serif;
            font-size: 7.5pt;
            font-weight: 800;
            color: #ffffff;
            background: rgba(15, 23, 42, 0.7);
            backdrop-filter: blur(4px);
            padding: 2px 7px;
            border-radius: 4px;
            z-index: 2;
        }}
        .project-card-img {{
            width: 100%;
            height: 90px;
            object-fit: cover;
            border-bottom: 1px solid #e2e8f0;
        }}
        .project-card-body {{
            padding: 10px 12px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            flex: 1;
        }}
        .project-card-category {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 6.5pt;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #8b5cf6;
            margin-bottom: 2px;
        }}
        .project-card-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 9.5pt;
            font-weight: 700;
            color: #0f172a;
            line-height: 1.25;
            margin-bottom: 4px;
        }}
        .project-card-desc {{
            font-size: 7.4pt;
            color: #475569;
            line-height: 1.35;
            margin-bottom: 6px;
        }}
        .project-card-features {{
            list-style: none;
            margin-bottom: 8px;
            font-size: 7pt;
            color: #334155;
        }}
        .project-card-features li {{
            position: relative;
            padding-left: 11px;
            margin-bottom: 2px;
            line-height: 1.3;
        }}
        .project-card-features li::before {{
            content: '•';
            position: absolute;
            left: 2px;
            color: #8b5cf6;
            font-weight: bold;
        }}
        .project-card-footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid #f1f5f9;
            padding-top: 6px;
        }}
        .project-card-tags {{
            display: flex;
            gap: 3px;
        }}
        .mini-tag {{
            font-size: 6pt;
            font-weight: 600;
            background: #ede9fe;
            color: #6d28d9;
            padding: 1px 5px;
            border-radius: 3px;
        }}
        .mini-tag.blue {{ background: #dbeafe; color: #1d4ed8; }}
        .mini-tag.green {{ background: #d1fae5; color: #047857; }}
        .project-card-link {{
            font-size: 6.8pt;
            color: #8b5cf6;
            text-decoration: none;
            font-weight: 700;
        }}

        /* Page 3 Styles */
        .cad-highlight-card {{
            background: #f8fafc;
            border: 1px solid #cbd5e1;
            border-top: 3px solid #0284c7;
            border-radius: 10px;
            padding: 10px 12px;
            display: flex;
            gap: 12px;
            margin-bottom: 10px;
        }}
        .cad-thumb {{
            width: 125px;
            height: 80px;
            object-fit: cover;
            border-radius: 6px;
            border: 1px solid #cbd5e1;
            flex-shrink: 0;
            background: #fff;
        }}
        .cad-body {{
            flex: 1;
        }}
        .cad-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 9.5pt;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 3px;
        }}
        .cad-desc {{
            font-size: 7.5pt;
            color: #334155;
            line-height: 1.35;
            margin-bottom: 5px;
        }}
        .cad-badges {{
            display: flex;
            gap: 4px;
            flex-wrap: wrap;
        }}
        .cad-badge {{
            font-size: 6.2pt;
            font-weight: 600;
            background: #e0f2fe;
            color: #0369a1;
            padding: 1px 6px;
            border-radius: 3px;
        }}

        .compact-projects-row {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-bottom: 9px;
        }}
        .compact-card {{
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 8px 10px;
            display: flex;
            gap: 9px;
            align-items: center;
        }}
        .compact-card-img {{
            width: 60px;
            height: 48px;
            border-radius: 6px;
            object-fit: cover;
            flex-shrink: 0;
        }}
        .compact-card-body {{
            flex: 1;
            min-width: 0;
        }}
        .compact-card-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 8pt;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 2px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}
        .compact-card-desc {{
            font-size: 6.8pt;
            color: #64748b;
            line-height: 1.25;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}
        .compact-card-link {{
            font-size: 6.2pt;
            color: #8b5cf6;
            text-decoration: none;
            font-weight: 600;
            display: block;
            margin-top: 2px;
        }}

        .humas-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr 1fr 1fr;
            gap: 7px;
            margin-bottom: 9px;
        }}
        .humas-card {{
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            padding: 7px 8px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        .humas-number {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 6.2pt;
            font-weight: 700;
            color: #8b5cf6;
            margin-bottom: 2px;
        }}
        .humas-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 7.2pt;
            font-weight: 700;
            color: #0f172a;
            line-height: 1.2;
            margin-bottom: 3px;
        }}
        .humas-desc {{
            font-size: 6.2pt;
            color: #64748b;
            line-height: 1.25;
            margin-bottom: 4px;
        }}
        .humas-link {{
            font-size: 5.8pt;
            color: #8b5cf6;
            text-decoration: none;
            font-weight: 600;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}

        .cta-footer {{
            background: linear-gradient(135deg, #090a16 0%, #17153b 100%);
            border-radius: 10px;
            padding: 10px 14px;
            color: #ffffff;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: auto;
        }}
        .cta-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 9.5pt;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 2px;
        }}
        .cta-sub {{
            font-size: 7pt;
            color: #cbd5e1;
            line-height: 1.3;
        }}
        .cta-right {{
            text-align: right;
            font-size: 7pt;
            flex-shrink: 0;
        }}
        .cta-name {{
            font-weight: 700;
            color: #c4b5fd;
            font-size: 8pt;
        }}
        .cta-email {{
            color: #94a3b8;
            font-size: 6.8pt;
        }}

        .page-footer {{
            border-top: 1px solid #e2e8f0;
            padding-top: 6px;
            margin-top: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 6.8pt;
            color: #94a3b8;
        }}
        .page-footer .page-num {{
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            color: #8b5cf6;
            font-size: 7.5pt;
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
                    <div class="label">Portfolio 2026</div>
                </div>
                <div class="cover-profile">
                    <div class="cover-avatar-wrap">
                        <img src="{img_avatar}" alt="Nizar" class="cover-avatar">
                        <div class="cover-avatar-badge">S.Kom</div>
                    </div>
                    <div>
                        <div class="cover-name">MUHAMAD NIZAR<br>NURFALAH</div>
                        <div class="cover-tagline">WebGIS &amp; Frontend Developer &bull; AutoCAD Technical Drafter &bull; Creative Media</div>
                        <div class="cover-contacts">
                            <span class="cover-contact-chip"><span class="icon">📍</span> Bandung, Jawa Barat</span>
                            <span class="cover-contact-chip badge-avail"><span class="icon">🟢</span> Full-time (Bandung / Jabodetabek &bull; Hybrid / Remote)</span>
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
                        Lulusan <strong>S1 Sistem Informasi STMIK AMIK Bandung</strong> dengan spesialisasi utama pada <strong>WebGIS &amp; Frontend Development</strong>, pemrosesan data spasial, dan perancangan antarmuka web interaktif. Memiliki kemampuan komplementer di bidang <strong>AutoCAD Technical Drafting (Telekomunikasi)</strong> serta <strong>Creative Media &amp; Kehumasan</strong>. Berpengalaman magang &plusmn;10 bulan di PT Nexwave (proyek operator Indosat &amp; XL Axiata) dan Diskominfo Kota Bandung, mencakup pemetaan analisis spasial, penyusunan gambar teknik blueprint, serta publikasi warta berita dan video kreatif.
                    </div>
                </div>

                <div>
                    <div class="section-label">Keahlian</div>
                    <div class="section-heading"><span class="accent-bar"></span> Tech Stack &amp; Kompetensi Inti</div>
                    <div class="skills-row">
                        <div class="skill-group purple">
                            <div class="skill-group-title">🌐 WebGIS &amp; Frontend (Utama)</div>
                            <div class="skill-tags">
                                <span class="skill-tag">WebGIS</span>
                                <span class="skill-tag">Leaflet.js</span>
                                <span class="skill-tag">JavaScript (ES6+)</span>
                                <span class="skill-tag">Spatial Analysis</span>
                                <span class="skill-tag">GeoJSON</span>
                                <span class="skill-tag">React.js</span>
                                <span class="skill-tag">HTML5 / CSS3</span>
                                <span class="skill-tag">Tailwind CSS</span>
                            </div>
                        </div>
                        <div class="skill-group blue">
                            <div class="skill-group-title">📐 Technical Drafting &amp; Telecom</div>
                            <div class="skill-tags">
                                <span class="skill-tag">AutoCAD 2D</span>
                                <span class="skill-tag">Site Layout Plan</span>
                                <span class="skill-tag">Monopole Elevation</span>
                                <span class="skill-tag">SID Survey</span>
                                <span class="skill-tag">Cable Tray Routing</span>
                                <span class="skill-tag">As-Built Drawing</span>
                            </div>
                        </div>
                        <div class="skill-group emerald">
                            <div class="skill-group-title">🎬 Media &amp; Professional Tools</div>
                            <div class="skill-tags">
                                <span class="skill-tag">Warta Berita Rilis</span>
                                <span class="skill-tag">Video Reels</span>
                                <span class="skill-tag">Git / GitHub</span>
                                <span class="skill-tag">QGIS</span>
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
                            <div class="timeline-role">Drafter Telekomunikasi &mdash; PT Nexwave</div>
                            <div class="timeline-company">Magang Industri &bull; Proyek Operator Indosat Ooredoo Hutchison &amp; XL Axiata</div>
                            <div class="timeline-desc">Menyusun dokumen gambar teknik blueprint AutoCAD (Site Layout Plan, tiang monopole, rute kabel feeder, elevasi antena, dan as-built drawing) dengan standar format industri telekomunikasi.</div>
                        </div>
                        <div class="timeline-item">
                            <div class="timeline-role">Humas &amp; Creative Media &mdash; Diskominfo Kota Bandung</div>
                            <div class="timeline-company">Magang Kedinasan &bull; Bidang Informasi &amp; Komunikasi Publik</div>
                            <div class="timeline-desc">Menulis dan menerbitkan 11 artikel warta berita di portal resmi bandung.go.id serta memproduksi 13 video reels Instagram (@diskominfobdg) untuk publikasi kegiatan dan edukasi program kota.</div>
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
                <div class="page-top-bar-title">Showcase <span class="highlight">Proyek WebGIS</span></div>
                <div class="page-top-bar-subtitle">Geospatial Solutions &bull; Case Studies</div>
            </div>

            <!-- Featured Project: Skripsi -->
            <div class="featured-project">
                <div class="featured-header-wrap">
                    <img src="{img_p1}" alt="WebGIS Longsor" class="featured-thumb">
                    <div>
                        <div class="featured-title">WebGIS Analisis &amp; Pemetaan Kerawanan Longsor Kab. Kuningan</div>
                        <div class="featured-meta">Studi Kasus Mitigasi Bencana &bull; Skripsi S1 Sistem Informasi STMIK AMIK Bandung</div>
                        <div class="featured-desc">
                            Pengembangan sistem informasi geografis interaktif berbasis web untuk memetakan zonasi kerawanan longsor di lereng Gunung Ciremai berdasarkan data BPBD Kuningan (tren lonjakan 121 kejadian di 2021 hingga &gt;150 kejadian/tahun).
                        </div>
                    </div>
                </div>

                <div class="case-study-grid">
                    <div>
                        <div class="case-box-title">📊 Multi-Sumber Data Spasial Resmi:</div>
                        <div class="case-box-text">
                            DEMNAS BIG 8.25m (kemiringan lereng), Curah Hujan CHIRPS (UC Santa Barbara 2021&ndash;2025), Peta Geologi &amp; Jenis Tanah BAPPEDA Kuningan, Peta Tutupan Lahan BIG, serta validasi data historis BPBD Kuningan.
                        </div>
                    </div>
                    <div>
                        <div class="case-box-title">🎯 Metode Analisis &amp; Temuan Kunci:</div>
                        <div class="case-box-text">
                            Metode <strong>Weighted Overlay &amp; Skoring</strong> parameter spasial menghasilkan 5 tingkat kerawanan (didominasi Sedang 41.96% &amp; Tinggi 36.94%). Zona <strong>Sangat Tinggi</strong> terkonsentrasi di 5 kecamatan: <em>Cigugur, Jalaksana, Darma, Mandirancan, dan Cilebak</em>.
                        </div>
                    </div>
                </div>

                <div class="featured-footer">
                    <div class="featured-tags">
                        <span class="featured-tag">Leaflet.js</span>
                        <span class="featured-tag">Spatial Analysis</span>
                        <span class="featured-tag">Weighted Overlay</span>
                        <span class="featured-tag">GeoJSON</span>
                        <span class="featured-tag">JavaScript (ES6)</span>
                    </div>
                    <div class="project-links-wrap">
                        <a href="https://nizarnurfalah.github.io/webgis_longsor_kuningan/" class="featured-link">🌐 Live Demo</a>
                        <a href="https://github.com/nizarnurfalah/webgis_longsor_kuningan" class="featured-link">💻 Source Code</a>
                    </div>
                </div>
            </div>

            <!-- 2 Project Cards Grid -->
            <div class="projects-grid">
                <div class="project-card">
                    <div class="project-card-number">02</div>
                    <img src="{img_tower}" alt="Microwave Tower" class="project-card-img">
                    <div class="project-card-body">
                        <div>
                            <div class="project-card-category">GIS &amp; Telecom Simulation (Solo Project)</div>
                            <div class="project-card-title">WebGIS Prediksi Radius Pancaran Microwave Tower BTS</div>
                            <div class="project-card-desc">
                                Aplikasi web simulasi mandiri untuk estimasi dan prediksi radius jangkauan gelombang mikro antena serta visualisasi interkoneksi jarak antar menara BTS.
                            </div>
                            <ul class="project-card-features">
                                <li>Simulasi kalkulasi estimasi radius jangkauan sinyal microwave</li>
                                <li>Visualisasi interkoneksi jarak spasial antar koordinat BTS</li>
                                <li>Fitur uji titik lokasi dalam radius jangkauan antena terdekat</li>
                            </ul>
                        </div>
                        <div class="project-card-footer">
                            <div class="project-card-tags">
                                <span class="mini-tag">Leaflet</span>
                                <span class="mini-tag blue">Telecom GIS</span>
                                <span class="mini-tag blue">Bootstrap</span>
                            </div>
                            <div class="project-links-wrap">
                                <a href="https://nizarnurfalah.github.io/pancaranradius_microwave/" class="project-card-link">🌐 Demo</a>
                                <a href="https://github.com/nizarnurfalah/pancaranradius_microwave" class="project-card-link">💻 Repo</a>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="project-card">
                    <div class="project-card-number">03</div>
                    <img src="{img_lapor}" alt="Laporan Fasilitas" class="project-card-img">
                    <div class="project-card-body">
                        <div>
                            <div class="project-card-category">Public Service &amp; Smart City</div>
                            <div class="project-card-title">WebGIS Sistem Pelaporan &amp; Pemetaan Fasilitas Publik</div>
                            <div class="project-card-desc">
                                Platform WebGIS interaktif pemetaan titik kerusakan fasilitas publik (jalan, PJU, drainase, jembatan) dengan filter status tindak lanjut penanganan.
                            </div>
                            <ul class="project-card-features">
                                <li>Formulir pengaduan dengan pin lokasi koordinat otomatis</li>
                                <li>Filter multi-kategori kerusakan dan status penanganan real-time</li>
                                <li>Dashboard admin &amp; optimasi demo client-side mock storage</li>
                            </ul>
                        </div>
                        <div class="project-card-footer">
                            <div class="project-card-tags">
                                <span class="mini-tag green">Leaflet</span>
                                <span class="mini-tag green">Mock Data</span>
                                <span class="mini-tag green">WebGIS</span>
                            </div>
                            <div class="project-links-wrap">
                                <a href="https://nizarnurfalah.github.io/pemetaan-laporan-fasilitas/" class="project-card-link">🌐 Demo</a>
                                <a href="https://github.com/nizarnurfalah/pemetaan-laporan-fasilitas" class="project-card-link">💻 Repo</a>
                            </div>
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

    <!-- ==================== PAGE 3: DRAFTING, WEB APPS & PUBLICATIONS ==================== -->
    <div class="page">
        <div class="page-inner">
            <div class="page-top-bar">
                <div class="page-top-bar-title">Drafting, Apps <span class="highlight">&amp; Publikasi</span></div>
                <div class="page-top-bar-subtitle">AutoCAD &bull; Web Engineering &bull; Media Humas</div>
            </div>

            <!-- AutoCAD Section with Real Blueprint Preview -->
            <div class="cad-highlight-card">
                <img src="{img_cad}" alt="AutoCAD Drawing Blueprint" class="cad-thumb">
                <div class="cad-body">
                    <div class="section-label" style="color: #0284c7;">AutoCAD Technical Drafting &bull; PT Nexwave</div>
                    <div class="cad-title">Dokumentasi Gambar Teknik Telekomunikasi (Indosat &amp; XL Axiata)</div>
                    <div class="cad-desc">
                        Penyusunan berkas gambar kerja blueprint AutoCAD 2D untuk 10+ site telekomunikasi wilayah Jawa Barat, mencakup Site Layout Plan, elevasi menara monopole, rancangan fondasi, rute cable tray feeder, serta verifikasi As-Built Drawing.
                    </div>
                    <div class="cad-badges">
                        <span class="cad-badge">Site Layout Plan</span>
                        <span class="cad-badge">Monopole 20m/30m</span>
                        <span class="cad-badge">Cable Tray Routing</span>
                        <span class="cad-badge">As-Built Drawing</span>
                        <span class="cad-badge">Operator: Indosat &amp; XL</span>
                    </div>
                </div>
            </div>

            <!-- Compact Web Apps -->
            <div class="compact-projects-row">
                <div class="compact-card">
                    <img src="{img_p2}" alt="Perhitungan Pipa" class="compact-card-img">
                    <div class="compact-card-body">
                        <div class="project-card-category">Engineering Tool</div>
                        <div class="compact-card-title">Kalkulator Perhitungan Pipa Teknis</div>
                        <div class="compact-card-desc">Simulasi kalkulator teknik untuk menghitung estimasi dimensi pipa, debit aliran fluida, dan kehilangan tekanan (headloss).</div>
                        <a href="https://nizarnurfalah.github.io/PerhitunganPipa/" class="compact-card-link">🌐 Live Demo &bull; PerhitunganPipa</a>
                    </div>
                </div>
                <div class="compact-card">
                    <img src="{img_p3}" alt="Jadwal Theater" class="compact-card-img">
                    <div class="compact-card-body">
                        <div class="project-card-category">Web Platform</div>
                        <div class="compact-card-title">Website Jadwal &amp; Info Teater Unisba</div>
                        <div class="compact-card-desc">Platform web katalog pementasan teater Unisba, informasi jadwal kegiatan, dan publikasi agenda seni budaya kampus.</div>
                        <a href="https://nizarnurfalah.github.io/jadwaltheaterunisba/" class="compact-card-link">🌐 Live Demo &bull; jadwaltheaterunisba</a>
                    </div>
                </div>
            </div>

            <!-- Artikel Diskominfo -->
            <div>
                <div class="section-label">Media Publikasi &bull; Diskominfo Kota Bandung</div>
                <div class="section-heading" style="margin-bottom: 5px;"><span class="accent-bar"></span> 4 Artikel Warta Berita Terpilih (dari 11 artikel di bandung.go.id)</div>
            </div>

            <div class="humas-grid">
                <div class="humas-card">
                    <div class="humas-number">01 / Warta</div>
                    <div class="humas-title">Penanganan Sampah TPS Gn. Batu</div>
                    <div class="humas-desc">Reaksi cepat penanganan timbunan TPS oleh Kelurahan Sukagalih.</div>
                    <a href="https://www.bandung.go.id/news/read/12616/tumpukan-sampah-tps-gunung-batu-timur-menghilang-aparat-kelurahan-suk" class="humas-link">🔗 bandung.go.id/news/read/12616</a>
                </div>
                <div class="humas-card">
                    <div class="humas-number">02 / Warta</div>
                    <div class="humas-title">RSUD Bandung Kiwari: Gempa</div>
                    <div class="humas-desc">Kesiapsiagaan mitigasi bencana gempa bumi tenaga medis RS.</div>
                    <a href="https://www.bandung.go.id/news/read/12369/rsud-bandung-kiwari-tingkatkan-kesiapsiagaan-bencana-lewat-simulasi-pe" class="humas-link">🔗 bandung.go.id/news/read/12369</a>
                </div>
                <div class="humas-card">
                    <div class="humas-number">03 / Warta</div>
                    <div class="humas-title">KDM Fest &amp; Duta Dekranasda</div>
                    <div class="humas-desc">Promosi inovasi kerajinan kriya representasi Kota Bandung.</div>
                    <a href="https://www.bandung.go.id/news/read/12379/kembang-nusa-x-kdm-fest-dua-wakil-kota-bandung-bersaing-jadi-duta-dek" class="humas-link">🔗 bandung.go.id/news/read/12379</a>
                </div>
                <div class="humas-card">
                    <div class="humas-number">04 / Warta</div>
                    <div class="humas-title">Bazar Gemar Ikan DKPP Bandung</div>
                    <div class="humas-desc">Kampanye gizi protein ikan dan promosi pembudidaya lokal.</div>
                    <a href="https://www.bandung.go.id/news/read/12499/azar-gemar-ikan-dkpp-kota-bandung-sukses-ajang-promobandung-city-depa" class="humas-link">🔗 bandung.go.id/news/read/12499</a>
                </div>
            </div>

            <!-- Video Reels -->
            <div style="background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); border-radius: 10px; padding: 9px 12px; margin-bottom: 6px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <span style="font-family: 'Outfit', sans-serif; font-size: 7.8pt; font-weight: 700; color: #c4b5fd;">🎬 13 Video Reels Kreatif diproduksi untuk @diskominfobdg</span>
                    <span style="font-size: 6.2pt; color: #94a3b8; font-weight: 600; background: rgba(255,255,255,0.06); padding: 1px 7px; border-radius: 8px;">Instagram Reels</span>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 4px;">
                    <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 5px; padding: 4px 6px;">
                        <div style="font-size: 6.2pt; font-weight: 700; color: #e2e8f0; line-height: 1.2;">Liputan TPS &amp; Kebersihan</div>
                        <a href="https://www.instagram.com/reel/DRD3WZmEx2J/" style="font-size: 5.4pt; color: #a78bfa; text-decoration: none;">🔗 Lihat Reels</a>
                    </div>
                    <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 5px; padding: 4px 6px;">
                        <div style="font-size: 6.2pt; font-weight: 700; color: #e2e8f0; line-height: 1.2;">Edukasi Program Diskominfo</div>
                        <a href="https://www.instagram.com/reel/DQ5-thk6RP/" style="font-size: 5.4pt; color: #a78bfa; text-decoration: none;">🔗 Lihat Reels</a>
                    </div>
                    <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 5px; padding: 4px 6px;">
                        <div style="font-size: 6.2pt; font-weight: 700; color: #e2e8f0; line-height: 1.2;">Pelayanan Terpadu Warga</div>
                        <a href="https://www.instagram.com/reel/DQ3bBpxk1V_/" style="font-size: 5.4pt; color: #a78bfa; text-decoration: none;">🔗 Lihat Reels</a>
                    </div>
                    <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 5px; padding: 4px 6px;">
                        <div style="font-size: 6.2pt; font-weight: 700; color: #e2e8f0; line-height: 1.2;">Tanggap Bencana Gempa</div>
                        <a href="https://www.instagram.com/reel/DQ29-tZE3y9/" style="font-size: 5.4pt; color: #a78bfa; text-decoration: none;">🔗 Lihat Reels</a>
                    </div>
                    <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 5px; padding: 4px 6px;">
                        <div style="font-size: 6.2pt; font-weight: 700; color: #e2e8f0; line-height: 1.2;">Festival Dekranasda</div>
                        <a href="https://www.instagram.com/reel/DQas1yUExg1/" style="font-size: 5.4pt; color: #a78bfa; text-decoration: none;">🔗 Lihat Reels</a>
                    </div>
                    <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 5px; padding: 4px 6px;">
                        <div style="font-size: 6.2pt; font-weight: 700; color: #e2e8f0; line-height: 1.2;">Pilah Sampah Mandiri</div>
                        <a href="https://www.instagram.com/reel/DQVdaIUE6vC/" style="font-size: 5.4pt; color: #a78bfa; text-decoration: none;">🔗 Lihat Reels</a>
                    </div>
                </div>
                <div style="text-align: center; margin-top: 5px; font-size: 5.8pt; color: #94a3b8;">+ 7 reels lainnya (Simulasi RSUD, UMKM Carnival, Floranimal Fest, Maggot Fest, Jajap Persib, dll. di instagram.com/diskominfobdg)</div>
            </div>

            <!-- CTA Footer -->
            <div class="cta-footer">
                <div>
                    <div class="cta-title">Siap Berkontribusi &amp; Berkolaborasi 🚀</div>
                    <div class="cta-sub">Terbuka untuk posisi WebGIS Developer, Frontend Web Developer, AutoCAD Drafter, dan IT Staff.</div>
                </div>
                <div class="cta-right">
                    <div class="cta-name">Muhamad Nizar Nurfalah, S.Kom.</div>
                    <div class="cta-email">✉️ nizqrnurfalah@gmail.com</div>
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
