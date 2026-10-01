import React, { useEffect, useState, useCallback } from "react";
import PropTypes from "prop-types";
import SwipeableViews from "react-swipeable-views";
import { useTheme } from "@mui/material/styles";
import AppBar from "@mui/material/AppBar";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import AOS from "aos";
import "aos/dist/aos.css";
import { Code, Award, Boxes, Newspaper, Compass, Video, Sparkles } from "lucide-react";

import CardProject from "../components/CardProject";
import TechStackIcon from "../components/TechStackIcon";
import Certificate from "../components/Certificate";
import ArticleCard from "../components/ArticleCard";
import VideoCard from "../components/VideoCard";
import AutoCADCard from "../components/AutoCADCard";

import {
  INITIAL_PROJECTS,
  INITIAL_CERTIFICATES,
  HUMAS_ARTICLES,
  HUMAS_VIDEOS,
  AUTOCAD_PROJECTS,
  TECH_STACKS,
} from "../data/portfolioData";
import { supabase } from "../supabase";

const ToggleButton = ({ onClick, isShowingMore }) => (
  <button
    onClick={onClick}
    className="
      px-4 py-2
      text-slate-300 
      hover:text-white 
      text-sm 
      font-medium 
      transition-all 
      duration-300 
      ease-in-out
      flex 
      items-center 
      gap-2
      bg-white/5 
      hover:bg-white/10
      rounded-lg
      border 
      border-white/10
      hover:border-purple-500/40
      backdrop-blur-sm
      group
      relative
      overflow-hidden
    "
  >
    <span className="relative z-10 flex items-center gap-2">
      {isShowingMore ? "Lihat Lebih Sedikit" : "Tampilkan Semua"}
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="16"
        height="16"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
        className={`
          transition-transform 
          duration-300 
          ${isShowingMore ? "group-hover:-translate-y-0.5" : "group-hover:translate-y-0.5"}
        `}
      >
        <polyline points={isShowingMore ? "18 15 12 9 6 15" : "6 9 12 15 18 9"}></polyline>
      </svg>
    </span>
    <span className="absolute bottom-0 left-0 w-0 h-0.5 bg-purple-500 transition-all duration-300 group-hover:w-full"></span>
  </button>
);

function TabPanel({ children, value, index, ...other }) {
  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`full-width-tabpanel-${index}`}
      aria-labelledby={`full-width-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: { xs: 1, sm: 3 } }}>
          <Typography component="div">{children}</Typography>
        </Box>
      )}
    </div>
  );
}

TabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.number.isRequired,
  value: PropTypes.number.isRequired,
};

function a11yProps(index) {
  return {
    id: `full-width-tab-${index}`,
    "aria-controls": `full-width-tabpanel-${index}`,
  };
}

export default function FullWidthTabs() {
  const theme = useTheme();
  const [value, setValue] = useState(0);

  // Data states with guaranteed fallbacks
  const [projects, setProjects] = useState(INITIAL_PROJECTS);
  const [certificates, setCertificates] = useState(INITIAL_CERTIFICATES);
  const [articles] = useState(HUMAS_ARTICLES);
  const [videos] = useState(HUMAS_VIDEOS);
  const [autocadList] = useState(AUTOCAD_PROJECTS);

  // Sub-filter state for Media Humas tab: 'articles' | 'videos'
  const [mediaFilter, setMediaFilter] = useState("articles");

  // Show more states
  const [showAllProjects, setShowAllProjects] = useState(false);
  const [showAllCertificates, setShowAllCertificates] = useState(false);
  const [showAllArticles, setShowAllArticles] = useState(false);
  const [showAllVideos, setShowAllVideos] = useState(false);
  const [showAllAutocad, setShowAllAutocad] = useState(false);

  const initialItems = 6;

  useEffect(() => {
    AOS.init({
      once: false,
    });
  }, []);

  // Sync initial data to localStorage immediately for stats & details
  useEffect(() => {
    localStorage.setItem("projects", JSON.stringify(INITIAL_PROJECTS));
    setProjects(INITIAL_PROJECTS);
    localStorage.setItem("certificates", JSON.stringify(INITIAL_CERTIFICATES));
    setCertificates(INITIAL_CERTIFICATES);

    window.dispatchEvent(new Event("portfolioDataUpdated"));
  }, []);

  const fetchData = useCallback(async () => {
    try {
      if (!supabase) return;

      const [projectsResponse, certificatesResponse] = await Promise.all([
        supabase.from("projects").select("*").order("id", { ascending: false }),
        supabase.from("certificates").select("*").order("id", { ascending: false }),
      ]);

      if (projectsResponse.data && projectsResponse.data.length > 0) {
        setProjects(projectsResponse.data);
        localStorage.setItem("projects", JSON.stringify(projectsResponse.data));
      }
      if (certificatesResponse.data && certificatesResponse.data.length > 0) {
        setCertificates(certificatesResponse.data);
        localStorage.setItem("certificates", JSON.stringify(certificatesResponse.data));
      }

      window.dispatchEvent(new Event("portfolioDataUpdated"));
    } catch (error) {
      console.warn("Using fallback local data:", error.message);
    }
  }, []);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  const displayedProjects = showAllProjects ? projects : projects.slice(0, initialItems);
  const displayedCertificates = showAllCertificates ? certificates : certificates.slice(0, initialItems);
  const displayedArticles = showAllArticles ? articles : articles.slice(0, initialItems);
  const displayedVideos = showAllVideos ? videos : videos.slice(0, initialItems);
  const displayedAutocad = showAllAutocad ? autocadList : autocadList.slice(0, initialItems);

  return (
    <div className="md:px-[10%] px-[5%] w-full sm:mt-0 mt-[3rem] bg-[#030014] overflow-hidden" id="Portofolio">
      {/* Header section */}
      <div className="text-center pb-10" data-aos="fade-up" data-aos-duration="1000">
        <h2 className="inline-block text-3xl md:text-5xl font-bold text-center mx-auto text-transparent bg-clip-text bg-gradient-to-r from-[#6366f1] to-[#a855f7]">
          <span
            style={{
              color: "#6366f1",
              backgroundImage: "linear-gradient(45deg, #6366f1 10%, #a855f7 93%)",
              WebkitBackgroundClip: "text",
              backgroundClip: "text",
              WebkitTextFillColor: "transparent",
            }}
          >
            Portfolio & Karya
          </span>
        </h2>
        <p className="text-slate-400 max-w-2xl mx-auto text-sm md:text-base mt-2">
          Jelajahi rekam jejak pengalaman magang, publikasi media humas, gambar teknik, proyek pengembangan web, dan sertifikasi.
        </p>
      </div>

      <Box sx={{ width: "100%" }}>
        {/* AppBar and Tabs */}
        <AppBar
          position="static"
          elevation={0}
          sx={{
            bgcolor: "transparent",
            border: "1px solid rgba(255, 255, 255, 0.1)",
            borderRadius: "20px",
            position: "relative",
            overflow: "hidden",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            "&::before": {
              content: '""',
              position: "absolute",
              top: 0,
              left: 0,
              right: 0,
              bottom: 0,
              background: "linear-gradient(180deg, rgba(139, 92, 246, 0.05) 0%, rgba(59, 130, 246, 0.05) 100%)",
              backdropFilter: "blur(12px)",
              zIndex: 0,
            },
          }}
          className="w-full px-2"
        >
          <Tabs
            value={value}
            onChange={handleChange}
            textColor="secondary"
            indicatorColor="secondary"
            variant="scrollable"
            scrollButtons="auto"
            allowScrollButtonsMobile
            sx={{
              minHeight: "72px",
              width: "100%",
              "& .MuiTabs-scroller": {
                display: { xs: "block", md: "flex" },
                justifyContent: { xs: "flex-start", md: "center" },
              },
              "& .MuiTabs-flexContainer": {
                justifyContent: { xs: "flex-start", md: "center" },
                minWidth: { xs: "max-content", md: "100%" },
              },
              "& .MuiTabScrollButton-root": {
                color: "#c084fc",
                "&.Mui-disabled": {
                  opacity: 0.2,
                },
              },
              "& .MuiTab-root": {
                fontSize: { xs: "0.85rem", md: "0.95rem" },
                fontWeight: "600",
                color: "#94a3b8",
                textTransform: "none",
                transition: "all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
                padding: { xs: "12px 16px", md: "16px 20px" },
                zIndex: 1,
                margin: "6px 4px",
                borderRadius: "14px",
                "&:hover": {
                  color: "#ffffff",
                  backgroundColor: "rgba(139, 92, 246, 0.12)",
                  transform: "translateY(-2px)",
                },
                "&.Mui-selected": {
                  color: "#fff",
                  background: "linear-gradient(135deg, rgba(139, 92, 246, 0.25), rgba(59, 130, 246, 0.25))",
                  boxShadow: "0 4px 15px -3px rgba(139, 92, 246, 0.25)",
                  border: "1px solid rgba(168, 85, 247, 0.3)",
                  "& .lucide": {
                    color: "#c084fc",
                  },
                },
              },
              "& .MuiTabs-indicator": {
                height: 0,
              },
            }}
          >
            <Tab
              icon={<Newspaper className="mb-1 w-5 h-5 transition-all duration-300" />}
              label="Media Humas (24)"
              {...a11yProps(0)}
            />
            <Tab
              icon={<Compass className="mb-1 w-5 h-5 transition-all duration-300" />}
              label="Drafter CAD (10)"
              {...a11yProps(1)}
            />
            <Tab
              icon={<Code className="mb-1 w-5 h-5 transition-all duration-300" />}
              label="Web Projects (3)"
              {...a11yProps(2)}
            />
            <Tab
              icon={<Award className="mb-1 w-5 h-5 transition-all duration-300" />}
              label="Certificates (12)"
              {...a11yProps(3)}
            />
            <Tab
              icon={<Boxes className="mb-1 w-5 h-5 transition-all duration-300" />}
              label="Tech Stack (15)"
              {...a11yProps(4)}
            />
          </Tabs>
        </AppBar>

        <SwipeableViews
          axis={theme.direction === "rtl" ? "x-reverse" : "x"}
          index={value}
          onChangeIndex={setValue}
        >
          {/* TAB 0: MEDIA HUMAS (11 RILIS ATAU 13 VIDEO) */}
          <TabPanel value={value} index={0} dir={theme.direction}>
            <div className="container mx-auto space-y-8">
              {/* Media Filter Tabs: Only Artikel Rilis and Video Reels */}
              <div className="flex flex-wrap items-center justify-center gap-4 pt-2">
                <button
                  onClick={() => setMediaFilter("articles")}
                  className={`px-6 py-3 rounded-xl text-sm font-semibold transition-all duration-300 flex items-center gap-2.5 ${
                    mediaFilter === "articles"
                      ? "bg-gradient-to-r from-purple-600 to-indigo-600 text-white shadow-lg shadow-purple-600/30 scale-105 border border-purple-400/40"
                      : "bg-white/5 text-gray-400 hover:text-white hover:bg-white/10 border border-white/10"
                  }`}
                >
                  <Newspaper className="w-4 h-4 text-purple-300" />
                  Artikel Rilis ({articles.length})
                </button>
                <button
                  onClick={() => setMediaFilter("videos")}
                  className={`px-6 py-3 rounded-xl text-sm font-semibold transition-all duration-300 flex items-center gap-2.5 ${
                    mediaFilter === "videos"
                      ? "bg-gradient-to-r from-pink-600 to-rose-600 text-white shadow-lg shadow-pink-600/30 scale-105 border border-pink-400/40"
                      : "bg-white/5 text-gray-400 hover:text-white hover:bg-white/10 border border-white/10"
                  }`}
                >
                  <Video className="w-4 h-4 text-pink-300" />
                  Video Reels ({videos.length})
                </button>
              </div>

              {/* Rilis Berita Section */}
              {mediaFilter === "articles" && (
                <div className="space-y-6 pt-2">
                  <div className="flex items-center justify-between border-b border-white/10 pb-3">
                    <div className="flex items-center gap-2">
                      <Newspaper className="w-5 h-5 text-purple-400" />
                      <h3 className="text-xl font-bold text-white">Artikel Rilis Pers — Diskominfo Kota Bandung</h3>
                    </div>
                    <span className="text-xs text-purple-300 px-3 py-1 rounded-full bg-purple-500/10 border border-purple-500/20">
                      {articles.length} Artikel
                    </span>
                  </div>

                  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {displayedArticles.map((article, index) => (
                      <div
                        key={article.id}
                        data-aos="fade-up"
                        data-aos-duration={800 + (index % 3) * 200}
                      >
                        <ArticleCard {...article} />
                      </div>
                    ))}
                  </div>

                  {articles.length > initialItems && (
                    <div className="mt-8 flex justify-center">
                      <ToggleButton
                        onClick={() => setShowAllArticles((prev) => !prev)}
                        isShowingMore={showAllArticles}
                      />
                    </div>
                  )}
                </div>
              )}

              {/* Video Reels Section */}
              {mediaFilter === "videos" && (
                <div className="space-y-6 pt-2">
                  <div className="flex items-center justify-between border-b border-white/10 pb-3">
                    <div className="flex items-center gap-2">
                      <Video className="w-5 h-5 text-pink-400" />
                      <h3 className="text-xl font-bold text-white">Video Konten Publikasi — Instagram Reels</h3>
                    </div>
                    <span className="text-xs text-pink-300 px-3 py-1 rounded-full bg-pink-500/10 border border-pink-500/20">
                      {videos.length} Video Konten
                    </span>
                  </div>

                  <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
                    {displayedVideos.map((video, index) => (
                      <div
                        key={video.id}
                        data-aos="fade-up"
                        data-aos-duration={800 + (index % 4) * 150}
                      >
                        <VideoCard {...video} />
                      </div>
                    ))}
                  </div>

                  {videos.length > initialItems && (
                    <div className="mt-8 flex justify-center">
                      <ToggleButton
                        onClick={() => setShowAllVideos((prev) => !prev)}
                        isShowingMore={showAllVideos}
                      />
                    </div>
                  )}
                </div>
              )}
            </div>
          </TabPanel>

          {/* TAB 1: DRAFTER TELEKOMUNIKASI (10 AUTOCAD BLUEPRINT) */}
          <TabPanel value={value} index={1} dir={theme.direction}>
            <div className="container mx-auto space-y-6">
              <div className="bg-gradient-to-r from-cyan-950/40 via-slate-900/60 to-blue-950/40 p-5 rounded-2xl border border-cyan-500/20 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
                <div>
                  <h3 className="text-lg font-bold text-white flex items-center gap-2">
                    <Compass className="w-5 h-5 text-cyan-400" />
                    Drafter Telekomunikasi — PT Nexwave
                  </h3>
                  <p className="text-xs md:text-sm text-gray-400 mt-1">
                    Dokumen gambar kerja teknis (SID, Pole Project Q2, As-Built Drawing, dan Rooftop Antenna Layout) berformat PDF & DWG.
                  </p>
                </div>
                <span className="px-3 py-1.5 rounded-full text-xs font-semibold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 whitespace-nowrap">
                  10 Dokumen Blueprint
                </span>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {displayedAutocad.map((cad, index) => (
                  <div
                    key={cad.id}
                    data-aos="fade-up"
                    data-aos-duration={800 + (index % 3) * 200}
                  >
                    <AutoCADCard {...cad} />
                  </div>
                ))}
              </div>

              {autocadList.length > initialItems && (
                <div className="mt-6 flex justify-center">
                  <ToggleButton
                    onClick={() => setShowAllAutocad((prev) => !prev)}
                    isShowingMore={showAllAutocad}
                  />
                </div>
              )}
            </div>
          </TabPanel>

          {/* TAB 2: WEB PROJECTS (3 PROYEK UTAMA) */}
          <TabPanel value={value} index={2} dir={theme.direction}>
            <div className="container mx-auto flex flex-col justify-center items-center overflow-hidden">
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6 w-full max-w-6xl">
                {displayedProjects.map((project, index) => (
                  <div
                    key={project.id || index}
                    data-aos="fade-up"
                    data-aos-duration={800 + index * 150}
                  >
                    <CardProject
                      Img={project.Img}
                      Title={project.Title}
                      Description={project.Description}
                      Link={project.Link}
                      id={project.id}
                    />
                  </div>
                ))}
              </div>

              {projects.length > initialItems && (
                <div className="mt-6 w-full flex justify-start">
                  <ToggleButton
                    onClick={() => setShowAllProjects((prev) => !prev)}
                    isShowingMore={showAllProjects}
                  />
                </div>
              )}
            </div>
          </TabPanel>

          {/* TAB 3: CERTIFICATES (12 SERTIFIKAT) */}
          <TabPanel value={value} index={3} dir={theme.direction}>
            <div className="container mx-auto flex flex-col justify-center items-center overflow-hidden">
              <div className="grid grid-cols-1 md:grid-cols-3 md:gap-6 gap-4 w-full">
                {displayedCertificates.map((certificate, index) => (
                  <div
                    key={certificate.id || index}
                    data-aos="fade-up"
                    data-aos-duration={800 + (index % 3) * 200}
                  >
                    <div className="space-y-2">
                      <Certificate ImgSertif={certificate.Img} />
                      {certificate.Title && (
                        <div className="px-1">
                          <p className="text-sm font-semibold text-white truncate">{certificate.Title}</p>
                          <p className="text-xs text-purple-400">{certificate.Issuer}</p>
                        </div>
                      )}
                    </div>
                  </div>
                ))}
              </div>

              {certificates.length > initialItems && (
                <div className="mt-8 w-full flex justify-center">
                  <ToggleButton
                    onClick={() => setShowAllCertificates((prev) => !prev)}
                    isShowingMore={showAllCertificates}
                  />
                </div>
              )}
            </div>
          </TabPanel>

          {/* TAB 4: TECH STACK */}
          <TabPanel value={value} index={4} dir={theme.direction}>
            <div className="container mx-auto flex justify-center items-center overflow-hidden pb-[5%]">
              <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-6 w-full max-w-5xl">
                {TECH_STACKS.map((stack, index) => (
                  <div
                    key={index}
                    data-aos="fade-up"
                    data-aos-duration={700 + (index % 5) * 150}
                  >
                    <TechStackIcon TechStackIcon={stack.icon} Language={stack.language} />
                  </div>
                ))}
              </div>
            </div>
          </TabPanel>
        </SwipeableViews>
      </Box>
    </div>
  );
}