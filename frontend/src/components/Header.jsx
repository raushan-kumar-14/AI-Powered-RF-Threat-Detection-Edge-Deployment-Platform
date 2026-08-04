import { FaSatelliteDish, FaShieldAlt } from "react-icons/fa";
import "./Header.css";

export default function Header() {
  return (
    <header className="hero">

      <div className="hero-left">

        <div className="logo-circle">
          <FaSatelliteDish />
        </div>

        <div>

          <h1>
            RF Threat Detection Platform
          </h1>

          <p>
            AI Powered Spectrum Intelligence & Drone Signal Recognition
          </p>

        </div>

      </div>

      <div className="hero-right">

        <div className="status">

          <FaShieldAlt />

          <span>System Online</span>

        </div>

      </div>

    </header>
  );
}