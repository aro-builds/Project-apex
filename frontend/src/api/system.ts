import api from "../lib/api";

export async function getSystemStatus() {
  const response = await api.get("/system/status");
  return response.data;
}