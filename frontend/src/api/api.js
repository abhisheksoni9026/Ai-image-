import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

const API = axios.create({
  baseURL: API_BASE_URL,
});

export const generateImage = async (data) => {
  const response = await API.post("/generate", data);
  return response.data;
};

export const getHistory = async () => {
  const response = await API.get("/history");
  return response.data;
};
