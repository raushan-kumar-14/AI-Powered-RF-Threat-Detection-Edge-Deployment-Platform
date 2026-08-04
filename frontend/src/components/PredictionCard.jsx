import {
  FaBrain,
  FaShieldAlt,
  FaCheckCircle,
  FaChartLine,
} from "react-icons/fa";

export default function PredictionCard({ prediction }) {
  if (!prediction) {
    return (
      <div
        style={{
          marginTop: "30px",
          background: "rgba(255,255,255,0.05)",
          border: "1px solid rgba(255,255,255,0.08)",
          borderRadius: "20px",
          padding: "30px",
          color: "white",
        }}
      >
        <h2>Prediction Result</h2>
        <p>No prediction available.</p>
      </div>
    );
  }

  const confidence = Number(prediction.confidence);

  let threat = "Low";
  let threatColor = "#22c55e";

  if (confidence < 60) {
    threat = "Medium";
    threatColor = "#f59e0b";
  }

  if (confidence > 90) {
    threat = "High Confidence";
    threatColor = "#00d4ff";
  }

  return (
    <div
      style={{
        marginTop: "30px",
        background: "rgba(255,255,255,0.05)",
        border: "1px solid rgba(255,255,255,0.08)",
        borderRadius: "20px",
        padding: "30px",
        color: "white",
      }}
    >
      <h2 style={{ marginBottom: "25px" }}>
        <FaBrain color="#00d4ff" /> AI Prediction
      </h2>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit,minmax(220px,1fr))",
          gap: "20px",
        }}
      >
        <div>
          <p style={{ opacity: 0.7 }}>Detected Signal</p>

          <h1 style={{ color: "#00d4ff" }}>
            {prediction.class}
          </h1>
        </div>

        <div>
          <p style={{ opacity: 0.7 }}>Confidence</p>

          <h1>{confidence.toFixed(2)}%</h1>
        </div>

        <div>
          <p style={{ opacity: 0.7 }}>Threat Status</p>

          <h2 style={{ color: threatColor }}>
            <FaShieldAlt /> {threat}
          </h2>
        </div>

        <div>
          <p style={{ opacity: 0.7 }}>Recommendation</p>

          <h3 style={{ color: "#22c55e" }}>
            <FaCheckCircle /> Continue Monitoring
          </h3>
        </div>
      </div>

      <div style={{ marginTop: "35px" }}>
        <p style={{ marginBottom: "10px" }}>
          <FaChartLine /> Model Confidence
        </p>

        <div
          style={{
            width: "100%",
            height: "16px",
            background: "#23324d",
            borderRadius: "30px",
            overflow: "hidden",
          }}
        >
          <div
            style={{
              width: `${confidence}%`,
              height: "100%",
              background: "#00d4ff",
            }}
          />
        </div>
      </div>
    </div>
  );
}