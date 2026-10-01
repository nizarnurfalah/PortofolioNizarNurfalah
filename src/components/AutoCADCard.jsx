import React, { useState } from "react";
import { FileText, ExternalLink, Download, Maximize2, X, Compass, Layers } from "lucide-react";
import { Modal, Box, IconButton, Backdrop } from "@mui/material";

const AutoCADCard = ({ siteId, title, category, description, pdfUrl }) => {
  const [openModal, setOpenModal] = useState(false);

  return (
    <>
      <div className="group relative w-full h-full flex flex-col justify-between rounded-2xl bg-gradient-to-br from-slate-900/90 to-slate-800/90 backdrop-blur-lg border border-white/10 p-6 shadow-xl transition-all duration-300 hover:scale-[1.02] hover:border-cyan-500/40 hover:shadow-cyan-500/20">
        <div className="absolute inset-0 bg-gradient-to-br from-cyan-500/10 via-blue-500/10 to-indigo-500/10 opacity-40 group-hover:opacity-75 rounded-2xl transition-opacity duration-300 pointer-events-none"></div>

        <div className="relative z-10 space-y-4">
          <div className="flex items-center justify-between gap-2">
            <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">
              <Compass className="w-3.5 h-3.5" />
              Site: {siteId}
            </span>
            <span className="text-xs text-gray-400 flex items-center gap-1">
              <Layers className="w-3.5 h-3.5 text-cyan-400" />
              {category}
            </span>
          </div>

          <div className="relative w-full h-32 rounded-xl bg-slate-950/80 border border-cyan-500/20 p-4 flex flex-col justify-between overflow-hidden group-hover:border-cyan-500/40 transition-colors">
            {/* Grid pattern mimicking CAD blueprint */}
            <div className="absolute inset-0 opacity-15 bg-[radial-gradient(#06b6d4_1px,transparent_1px)] [background-size:12px_12px]" />
            <div className="flex items-center justify-between">
              <span className="text-[10px] font-mono text-cyan-400 tracking-wider">AUTOCAD DWG/PDF</span>
              <span className="text-[10px] font-mono text-gray-400">PT NEXWAVE</span>
            </div>
            <div className="flex items-center gap-2">
              <FileText className="w-7 h-7 text-cyan-400 shrink-0" />
              <div className="overflow-hidden">
                <p className="text-xs font-mono text-gray-200 truncate">{pdfUrl.replace('/autocad/', '')}</p>
                <p className="text-[10px] text-gray-400">Engineering Drawing Spec</p>
              </div>
            </div>
          </div>

          <div>
            <h4 className="text-base font-semibold text-white group-hover:text-cyan-200 transition-colors duration-200 line-clamp-1">
              {title}
            </h4>
            <p className="text-gray-300/80 text-sm leading-relaxed mt-1 line-clamp-2">
              {description}
            </p>
          </div>
        </div>

        <div className="relative z-10 pt-5 mt-4 border-t border-white/10 flex items-center justify-between gap-2">
          <button
            onClick={() => setOpenModal(true)}
            className="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-lg bg-cyan-600/80 hover:bg-cyan-500 text-white text-xs font-semibold transition-all duration-200 hover:scale-105 active:scale-95"
          >
            <Maximize2 className="w-3.5 h-3.5" />
            <span>Preview</span>
          </button>

          <a
            href={pdfUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-lg bg-white/5 hover:bg-white/15 text-cyan-300 hover:text-white text-xs font-semibold border border-cyan-500/20 transition-all duration-200 hover:scale-105 active:scale-95"
          >
            <span>Buka PDF</span>
            <ExternalLink className="w-3.5 h-3.5" />
          </a>
        </div>
      </div>

      {/* PDF Modal Viewer */}
      <Modal
        open={openModal}
        onClose={() => setOpenModal(false)}
        BackdropComponent={Backdrop}
        BackdropProps={{
          timeout: 300,
          sx: {
            backgroundColor: "rgba(3, 0, 20, 0.92)",
            backdropFilter: "blur(8px)",
          },
        }}
        sx={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          p: 2,
        }}
      >
        <Box
          sx={{
            position: "relative",
            width: "95vw",
            maxWidth: "1100px",
            height: "85vh",
            bgcolor: "#0b0f19",
            border: "1px solid rgba(6, 182, 212, 0.3)",
            borderRadius: "16px",
            overflow: "hidden",
            display: "flex",
            flexDirection: "column",
            boxShadow: "0 0 50px rgba(6, 182, 212, 0.2)",
            outline: "none",
          }}
        >
          {/* Header */}
          <div className="flex items-center justify-between px-5 py-3 bg-slate-900 border-b border-white/10">
            <div className="flex items-center gap-2">
              <Compass className="w-5 h-5 text-cyan-400" />
              <div>
                <h3 className="text-white text-sm font-semibold">{title}</h3>
                <p className="text-xs text-gray-400 font-mono">Site ID: {siteId} | PT Nexwave</p>
              </div>
            </div>
            <div className="flex items-center gap-3">
              <a
                href={pdfUrl}
                download
                className="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white text-xs font-semibold transition"
              >
                <Download className="w-3.5 h-3.5" />
                <span>Unduh</span>
              </a>
              <IconButton
                onClick={() => setOpenModal(false)}
                sx={{ color: "#94a3b8", "&:hover": { color: "#ffffff" } }}
              >
                <X className="w-5 h-5" />
              </IconButton>
            </div>
          </div>

          {/* PDF Viewer using object tag */}
          <div className="flex-1 w-full h-full bg-slate-950 relative overflow-hidden">
            <object
              data={`${pdfUrl}#toolbar=1&navpanes=0`}
              type="application/pdf"
              className="w-full h-full border-none"
            >
              <div className="flex flex-col items-center justify-center h-full gap-4 text-center p-6 bg-slate-950">
                <FileText className="w-14 h-14 text-cyan-400 animate-pulse" />
                <div className="space-y-1">
                  <p className="text-white font-semibold text-base">Preview Dokumen Blueprint</p>
                  <p className="text-gray-400 text-xs max-w-md">
                    Browser Anda diatur untuk mengunduh PDF secara otomatis. Klik tombol di bawah untuk membuka blueprint langsung di tab baru.
                  </p>
                </div>
                <a
                  href={pdfUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="px-5 py-2.5 bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-500 hover:to-blue-500 text-white text-xs font-semibold rounded-xl flex items-center gap-2 shadow-lg transition-all"
                >
                  <ExternalLink className="w-4 h-4" />
                  <span>Buka Blueprint di Tab Baru</span>
                </a>
              </div>
            </object>
          </div>
        </Box>
      </Modal>
    </>
  );
};

export default AutoCADCard;
