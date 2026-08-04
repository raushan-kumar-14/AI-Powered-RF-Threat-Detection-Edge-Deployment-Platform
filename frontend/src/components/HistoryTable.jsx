export default function HistoryTable({ history }) {
  return (
    <div
      style={{
        background: "rgba(255,255,255,0.05)",
        border: "1px solid rgba(255,255,255,0.08)",
        borderRadius: "20px",
        padding: "25px",
        marginTop: "30px",
        color: "white",
      }}
    >
      <h2>Detection History</h2>

      {history.length === 0 ? (
        <p style={{ opacity: 0.7 }}>
          No previous detections available.
        </p>
      ) : (
        <table
          style={{
            width: "100%",
            marginTop: "20px",
            borderCollapse: "collapse",
          }}
        >
          <thead>
            <tr>
              <th style={thStyle}>Time</th>
              <th style={thStyle}>Signal</th>
              <th style={thStyle}>Confidence</th>
              <th style={thStyle}>Status</th>
            </tr>
          </thead>

          <tbody>
            {history.map((item) => (
              <tr key={item.id}>
                <td style={tdStyle}>{item.time}</td>

                <td style={tdStyle}>{item.signal}</td>

                <td style={tdStyle}>
                  {Number(item.confidence).toFixed(2)}%
                </td>

                <td style={tdStyle}>
                  {item.confidence > 90
                    ? "High"
                    : item.confidence > 50
                    ? "Medium"
                    : "Low"}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

const thStyle = {
  textAlign: "left",
  padding: "12px",
  borderBottom: "1px solid rgba(255,255,255,0.15)",
};

const tdStyle = {
  padding: "12px",
  borderBottom: "1px solid rgba(255,255,255,0.08)",
};