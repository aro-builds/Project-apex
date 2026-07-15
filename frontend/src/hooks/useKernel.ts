import { useEffect, useState } from "react";
import { getAgents } from "../api/kernel";

export function useKernel() {

    const [agents, setAgents] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {

        getAgents()
            .then(setAgents)
            .finally(() => setLoading(false));

    }, []);

    return { agents, loading };

}