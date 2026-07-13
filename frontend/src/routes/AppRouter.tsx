import { BrowserRouter, Routes, Route } from "react-router-dom";

import MainLayout from "../layouts/MainLayout";
import Dashboard from "../pages/Dashboard";

export default function AppRouter() {
  return (
    <BrowserRouter>
      <MainLayout>
        <Routes>
          <Route path="/" element={<Dashboard />} />
        </Routes>
      </MainLayout>
    </BrowserRouter>
  );
}