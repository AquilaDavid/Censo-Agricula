import { BrowserRouter, Routes, Route } from "react-router-dom";
import Users from "../pages/Users";

export default function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Users />} />
      </Routes>
    </BrowserRouter>
  );
}
