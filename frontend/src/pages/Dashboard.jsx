import { useState } from "react";

import Header from "../components/Header";
import StatsCards from "../components/StatsCards";
import DronePanel from "../components/DronePanel";
import UploadCard from "../components/UploadCard";
import PredictionCard from "../components/PredictionCard";
import SpectrumChart from "../components/SpectrumChart";
import HistoryTable from "../components/HistoryTable";
import Footer from "../components/Footer";

export default function Dashboard() {
  const [prediction, setPrediction] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [history, setHistory] = useState([]);

  return (
    <div
      style={{
        minHeight: "100vh",
        padding: "40px",
        color: "white",
        maxWidth: "1500px",
        margin: "0 auto",
      }}
    >
      <Header />

      <StatsCards />

      <DronePanel />

      <div style={{ marginTop: "35px" }}>
        <UploadCard
          setPrediction={setPrediction}
          setImagePreview={setImagePreview}
          history={history}
          setHistory={setHistory}
      />
      </div>

      <div style={{ marginTop: "35px" }}>
        <PredictionCard prediction={prediction} />
      </div>

      <div style={{ marginTop: "35px" }}>
        <SpectrumChart imagePreview={imagePreview} />
      </div>

      <div style={{ marginTop: "35px" }}>
        <HistoryTable history={history} />
      </div>

      <Footer />
    </div>
  );
}