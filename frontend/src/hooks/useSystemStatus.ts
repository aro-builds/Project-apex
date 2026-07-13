import { useEffect, useState } from "react";
import { getSystemStatus } from "../api/system";

export function useSystemStatus() {
  const [status, setStatus] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getSystemStatus()
      .then(setStatus)
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  return {
    status,
    loading,
  };
}