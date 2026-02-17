import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://localhost:5000", // backend Flask
});

export default apiClient;
