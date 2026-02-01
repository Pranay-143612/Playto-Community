import './HeroSection.css';
import video from './herobg.mp4';
import { Link } from "react-router-dom";

const Button = ({ children, className = '', ...props }) => (
  <button className={className} {...props}>
    {children}
  </button>
);

export const HeroSection = () => {
  return (
    <section className="hero">
      <video
        className="hero-video"
        src={video}
        autoPlay
        loop
        muted
        playsInline
      />

      {/* Overlay */}
      <div className="hero-overlay"></div>

      {/* Content */}
      <div className="hero-content">
        {/* Left */}
        <div className="hero-left">
          <div className="logo">
            <span className="logo-text">Playto <span style={{ color: "#fff" }}>Community</span></span>
          </div>

          <h1>Welcome to your professional community</h1>
          <p>Connect. Share. Grow.</p>

          <div className="hero-buttons">
            <Link to="/login">
              <Button className="btn btn-primary">Sign in</Button>
            </Link>

            <Link to="/login">
              <Button className="btn btn-outline">Join now</Button>
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
};
