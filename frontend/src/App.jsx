import { BrowserRouter, Routes, Route } from "react-router-dom";
import { HeroSection } from "./Components/landing/HeroSection";
import Login from "./Components/Login/Login";


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HeroSection />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
