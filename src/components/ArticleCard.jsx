import React from "react";
import { ExternalLink, Newspaper, Calendar, Building2 } from "lucide-react";

const ArticleCard = ({ title, summary, url, category, source }) => {
  return (
    <div className="group relative w-full h-full flex flex-col justify-between rounded-2xl bg-gradient-to-br from-slate-900/90 to-slate-800/90 backdrop-blur-lg border border-white/10 p-6 shadow-xl transition-all duration-300 hover:scale-[1.02] hover:border-purple-500/40 hover:shadow-purple-500/20">
      <div className="absolute inset-0 bg-gradient-to-br from-indigo-500/10 via-purple-500/10 to-pink-500/10 opacity-40 group-hover:opacity-70 rounded-2xl transition-opacity duration-300 pointer-events-none"></div>

      <div className="relative z-10 space-y-4">
        <div className="flex items-center justify-between gap-2">
          <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-purple-500/20 text-purple-300 border border-purple-500/30">
            <Newspaper className="w-3.5 h-3.5" />
            {category}
          </span>
          <span className="text-xs text-gray-400 flex items-center gap-1">
            <Building2 className="w-3.5 h-3.5 text-blue-400" />
            {source}
          </span>
        </div>

        <h3 className="text-lg font-semibold text-white group-hover:text-purple-200 transition-colors duration-200 line-clamp-2">
          {title}
        </h3>

        <p className="text-gray-300/80 text-sm leading-relaxed line-clamp-3">
          {summary}
        </p>
      </div>

      <div className="relative z-10 pt-5 mt-4 border-t border-white/10 flex items-center justify-between">
        <span className="text-xs text-gray-400">Portal Resmi Kota Bandung</span>
        <a
          href={url}
          target="_blank"
          rel="noopener noreferrer"
          className="inline-flex items-center gap-2 px-4 py-2 rounded-lg bg-gradient-to-r from-purple-600/80 to-indigo-600/80 hover:from-purple-600 hover:to-indigo-600 text-white text-xs font-semibold shadow-md transition-all duration-200 hover:scale-105 active:scale-95"
        >
          <span>Baca Berita</span>
          <ExternalLink className="w-3.5 h-3.5" />
        </a>
      </div>
    </div>
  );
};

export default ArticleCard;
