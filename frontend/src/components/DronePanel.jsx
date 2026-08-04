import {
  FaSatelliteDish,
  FaBroadcastTower,
  FaShieldAlt,
  FaCrosshairs,
} from "react-icons/fa";

export default function DronePanel() {
  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: "2fr 1fr",
        gap: "25px",
        marginBottom: "35px",
      }}
    >
      {/* Left Panel */}

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
          RF Intelligence Center
        </h2>

        <div
          style={{
            fontSize: "90px",
            textAlign: "center",
            marginBottom: "25px",
          }}
        >
          📡
        </div>

        <p
          style={{
            color: "#bcd3ea",
            lineHeight: "1.8",
            fontSize: "17px",
          }}
        >
          AI continuously analyzes uploaded RF spectrograms to classify
          communication signals using a CNN model optimized with ONNX Runtime.
          The platform is designed for spectrum intelligence, RF monitoring,
          and drone threat detection.
        </p>
      </div>

      {/* Right Panel */}

      <div
        style={{
          display: "flex",
          flexDirection: "column",
          gap: "18px",
        }}
      >
        {[
          {
            icon: <FaSatelliteDish />,
            title: "Radar",
            value: "Scanning",
            color: "#00d4ff",
          },
          {
            icon: <FaBroadcastTower />,
            title: "Signals",
            value: "11 Classes",
            color: "#00ff99",
          },
          {
            icon: <FaShieldAlt />,
            title: "Threat",
            value: "Low",
            color: "#ffcc00",
          },
          {
            icon: <FaCrosshairs />,
            title: "Detection",
            value: "Ready",
            color: "#ff4d6d",
          },
        ].map((item) => (
          <div
            key={item.title}
            style={{
              background: "rgba(255,255,255,.05)",
              borderRadius: "16px",
              padding: "18px",
              border: "1px solid rgba(255,255,255,.08)",
            }}
          >
            <div
              style={{
                fontSize: "28px",
                color: item.color,
                marginBottom: "8px",
              }}
            >
              {item.icon}
            </div>

            <div
              style={{
                color: "#9db6d1",
                fontSize: "14px",
              }}
            >
              {item.title}
            </div>

            <div
              style={{
                fontWeight: "700",
                fontSize: "22px",
                marginTop: "5px",
              }}
            >
              {item.value}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}