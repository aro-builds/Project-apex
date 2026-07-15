import api from "../lib/api";

export async function getAgents() {
    const response = await api.get("/v1/kernel/agents");
    return response.data;
}