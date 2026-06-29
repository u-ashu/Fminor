import WorkspaceLayout from "../layouts/WorkspaceLayout";

export default function Workspace() {
  return (
    <WorkspaceLayout>
      <div className="flex h-full items-center justify-center">
        <h1 className="text-5xl font-bold">
          Welcome to PaperMind AI 🚀
        </h1>
      </div>
    </WorkspaceLayout>
  );
}