import Navbar from "./Navbar";
import Sidebar from "./Sidebar";
import StatusBar from "./StatusBar";

interface MainLayoutProps {
  children: React.ReactNode;
}

export default function MainLayout({ children }: MainLayoutProps) {
  return (
    <div className="min-h-screen bg-slate-950 text-white flex flex-col">
      <Navbar />

      <div className="flex flex-1">
        <Sidebar />

        <main className="flex-1 p-6">
          {children}
        </main>
      </div>

      <StatusBar />
    </div>
  );
}