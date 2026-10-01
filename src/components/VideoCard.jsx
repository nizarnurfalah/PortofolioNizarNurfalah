import React from "react";
import { Instagram, Play, ExternalLink, Video } from "lucide-react";

const VideoCard = ({ title, url, tag, id }) => {
  return (
    <div className="group relative w-full h-full flex flex-col justify-between rounded-2xl bg-gradient-to-br from-slate-900/90 to-slate-800/90 backdrop-blur-lg border border-white/10 p-5 shadow-xl transition-all duration-300 hover:scale-[1.03] hover:border-pink-500/40 hover:shadow-pink-500/20">
      <div className="absolute inset-0 bg-gradient-to-br from-pink-500/10 via-rose-500/10 to-purple-500/10 opacity-40 group-hover:opacity-75 rounded-2xl transition-opacity duration-300 pointer-events-none"></div>

      <div className="relative z-10 space-y-4">
        {/* Reel Header Visual */}
        <div className="relative w-full h-40 rounded-xl bg-gradient-to-tr from-purple-950 via-slate-900 to-pink-950/80 border border-white/10 flex flex-col items-center justify-center overflow-hidden group-hover:border-pink-500/30 transition-all">
          <div className="absolute top-3 left-3 flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-black/60 backdrop-blur-md text-[11px] font-medium text-pink-300 border border-pink-500/30">
            <Instagram className="w-3.5 h-3.5 text-pink-400" />
            <span>Reel #{id}</span>
          </div>

          <div className="w-14 h-14 rounded-full bg-gradient-to-tr from-pink-500 to-purple-600 flex items-center justify-center text-white shadow-lg shadow-pink-500/30 group-hover:scale-110 transition-transform duration-300">
            <Play className="w-6 h-6 fill-current ml-1" />
          </div>

          <div className="absolute bottom-3 right-3 text-[11px] text-gray-400 px-2 py-0.5 rounded bg-black/40">
            Instagram Media
          </div>
        </div>

        <div>
          <span className="inline-block text-[11px] font-semibold text-pink-400 uppercase tracking-wider mb-1">
            {tag}
          </span>
          <h4 className="text-base font-semibold text-white group-hover:text-pink-200 transition-colors duration-200 line-clamp-2">
            {title}
          </h4>
        </div>
      </div>

      <div className="relative z-10 pt-4 mt-3 border-t border-white/10 flex items-center justify-between">
        <span className="text-xs text-gray-400 flex items-center gap-1">
          <Video className="w-3.5 h-3.5 text-pink-400" />
          Diskominfo Reel
        </span>
        <a
          href={url}
          target="_blank"
          rel="noopener noreferrer"
          className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg bg-gradient-to-r from-pink-600 to-rose-600 hover:from-pink-500 hover:to-rose-500 text-white text-xs font-semibold shadow-md transition-all duration-200 hover:scale-105 active:scale-95"
        >
          <span>Tonton Video</span>
          <ExternalLink className="w-3.5 h-3.5" />
        </a>
      </div>
    </div>
  );
};

export default VideoCard;
