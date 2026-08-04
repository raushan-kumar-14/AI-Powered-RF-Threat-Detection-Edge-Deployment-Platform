export default function SpectrumChart({ imagePreview }) {
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
      <h2>Signal Spectrum</h2>

      {!imagePreview ? (
        <p style={{ opacity: 0.7 }}>
          Spectrum visualization will appear here.
        </p>
      ) : (
        <div
          style={{
            marginTop: "20px",
            textAlign: "center",
          }}
        >
          <img
            src={imagePreview}
            alt="RF Spectrum"
            style={{
              width: "100%",
              maxHeight: "500px",
              objectFit: "contain",
              borderRadius: "15px",
              border: "2px solid #00d4ff",
            }}
          />
        </div>
      )}
    </div>
  );
}