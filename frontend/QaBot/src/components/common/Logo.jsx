export default function Logo() {
  return (
    <div className="flex items-center gap-3">
      <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-violet-600 font-bold text-xl">
        P
      </div>

      <div>
        <h1 className="text-xl font-bold">PaperMind</h1>

        <p className="text-xs text-slate-400">
          AI Research Assistant
        </p>
      </div>
    </div>
  );
}