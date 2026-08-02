import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const generateImage = async (data) => {
  const response = await API.post("/generate", data);
  return response.data;
};

export const getHistory = async () => {
  const response = await API.get("/history");
  return response.data;
};