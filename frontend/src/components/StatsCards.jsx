import {
  FaRobot,
  FaSignal,
  FaChartBar,
  FaBolt,
} from "react-icons/fa";

const cards = [
  {
    title: "AI Model",
    value: "CNN + ONNX",
    icon: <FaRobot />,
    color: "#00d4ff",
  },
  {
    title: "Signal Classes",
    value: "11",
    icon: <FaSignal />,
    color: "#00ff99",
  },
  {
    title: "Predictions",
    value: "Live",
    icon: <FaChartBar />,
    color: "#ffcc00",
  },
  {
    title: "System",
    value: "Online",
    icon: <FaBolt />,
    color: "#ff4d6d",
  },
];

export default function StatsCards() {
  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: "repeat(auto-fit,minmax(240px,1fr))",
        gap: "20px",
        marginBottom: "35px",
      }}
    >
      {cards.map((card) => (
        <div
          key={card.title}
          style={{
            background: "rgba(255,255,255,0.05)",
            border: "1px solid rgba(255,255,255,0.08)",
            borderRadius: "18px",
            padding: "25px",
            backdropFilter: "blur(12px)",
            boxShadow: "0 10px 25px rgba(0,0,0,.35)",
          }}
        >
          <div
            style={{
              fontSize: "32px",
              color: card.color,
              marginBottom: "18px",
            }}
          >
            {card.icon}
          </div>

          <div
            style={{
              color: "#9db6d1",
              fontSize: "15px",
            }}
          >
            {card.title}
          </div>

          <div
            style={{
              fontSize: "28px",
              fontWeight: "700",
              marginTop: "8px",
            }}
          >
            {card.value}
          </div>
        </div>
      ))}
    </div>
  );
}