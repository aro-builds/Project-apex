export default function Sidebar() {
  return (
    <aside className="w-64 bg-slate-900 border-r border-slate-700 p-5">
      <p className="font-semibold mb-4">Navigation</p>

      <ul className="space-y-3">
        <li>Dashboard</li>
        <li>Projects</li>
        <li>Workflow</li>
        <li>Video Engine</li>
        <li>Voice Engine</li>
      </ul>
    </aside>
  );
}