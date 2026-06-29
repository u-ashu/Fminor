import Sidebar from "../components/layout/Sidebar";
import Header from "../components/layout/Header";

export default function WorkspaceLayout({ children }) {
  return (
    <div className="flex h-screen overflow-hidden bg-[#070B16] text-white">
      <Sidebar />

      <div className="flex flex-1 min-w-0 flex-col">
        <Header />

        <main className="flex-1 overflow-y-auto">
          {children}
        </main>
      </div>
    </div>
  );
}