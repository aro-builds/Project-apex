import { useSystemStatus } from "../hooks/useSystemStatus";

export default function SystemStatusCard() {
  const { status, loading } = useSystemStatus();

  if (loading) {
    return (
      <div className="rounded-xl border border-slate-700 bg-slate-900 p-6">
        Loading system status...
      </div>
    );
  }

  return (
    <div className="rounded-xl border border-slate-700 bg-slate-900 p-6">
      <h2 className="mb-4 text-2xl font-bold">
        System Status
      </h2>

      <div className="space-y-2">
        <p>Backend: {status.data.services.backend}</p>
        <p>Ollama: {status.data.services.ollama}</p>
        <p>Workflow: {status.data.services.workflow_engine}</p>
        <p>Video: {status.data.services.video_engine}</p>
        <p>Voice: {status.data.services.voice_engine}</p>
      </div>
    </div>
  );
}