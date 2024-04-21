import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./Layout";
import Schedule from "./pages/Schedule";
import Login from "./pages/Login";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout/>}>
          <Route path="/timely" element={<App/>} />
          <Route index element={<Login/>} />
          <Route path="/schedule" element={<Schedule/>} />
        </Route>
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
