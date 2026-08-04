import { useState } from "react";
import axios from "axios";
import { FaCloudUploadAlt, FaImage } from "react-icons/fa";

export default function UploadCard({
    setPrediction,
    setImagePreview,
    history,
    setHistory,
  }) {
  const [loading, setLoading] = useState(false);
  const [selectedFile, setSelectedFile] = useState(null);

  function handleFileChange(e) {
      const file = e.target.files[0];

      setSelectedFile(file);

      if (file) {
          setImagePreview(URL.createObjectURL(file));
      }
  }

  async function handleUpload() {

      if (!selectedFile) {
          alert("Please select an image first.");
          return;
      }

      const formData = new FormData();
      formData.append("file", selectedFile);

      setLoading(true);

      try {

          const response = await axios.post(
              "http://127.0.0.1:8000/predict",
              formData
          );
          console.log(response.data);

          setPrediction(response.data);

          const newDetection = {
            id: Date.now(),
            signal: response.data.class,
            confidence: response.data.confidence,
            time: new Date().toLocaleTimeString(),
          };

          setHistory([newDetection, ...history]);

      } catch (err) {

          console.error(err);
          alert("Prediction Failed");

      }

      setLoading(false);
  }

  return (
    <div
      style={{
        background: "rgba(255,255,255,.05)",
        border: "1px solid rgba(255,255,255,.08)",
        borderRadius: "20px",
        padding: "30px",
        backdropFilter: "blur(12px)",
        boxShadow: "0 15px 30px rgba(0,0,0,.35)",
      }}
    >
      <h2
        style={{
          marginTop: 0,
          marginBottom: "25px",
          color: "#00d4ff",
        }}
      >
        Upload RF Spectrogram
      </h2>

      <div
        style={{
          border: "2px dashed #00d4ff",
          borderRadius: "18px",
          padding: "40px",
          textAlign: "center",
          background: "rgba(0,212,255,.05)",
        }}
      >
        <FaCloudUploadAlt
          style={{
            fontSize: "70px",
            color: "#00d4ff",
          }}
        />

        <h3>Select Spectrogram Image</h3>

        <p style={{ color: "#9db6d1" }}>
          Upload PNG or JPG spectrogram generated from SDR IQ samples
        </p>

        <input
          type="file"
          accept="image/*"
          onChange={handleFileChange}
          style={{
            marginTop: "15px",
          }}
        />

        {selectedFile && (
          <div
            style={{
              marginTop: "20px",
              color: "#00ff99",
              fontWeight: "600",
            }}
          >
            <FaImage /> {selectedFile.name}
          </div>
        )}

        <button
          onClick={handleUpload}
          disabled={loading}
          style={{
              marginTop: "25px",
              background: "#00d4ff",
              color: "#08131f",
              border: "none",
              padding: "14px 28px",
              borderRadius: "10px",
              fontWeight: "700",
              cursor: loading ? "not-allowed" : "pointer",
              opacity: loading ? 0.7 : 1,
              fontSize: "16px",
          }}
      >
          {loading ? "Analyzing RF Signal..." : "Analyze Signal"}
        </button>
      </div>
    </div>
  );
}