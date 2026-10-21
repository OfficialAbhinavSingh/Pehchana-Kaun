// Placeholder landing page. Owner: WS3. Real design + copy: see docs/plan.md (Day 4-5).
export default function Home() {
  return (
    <main className="mx-auto flex min-h-screen max-w-2xl flex-col justify-center gap-6 px-4 py-16">
      <p className="text-sm font-semibold uppercase tracking-widest text-foreground/60">
        Bolna Symphony Buildathon 2026
      </p>
      <h1 className="text-5xl font-bold tracking-tight">Pehchana Kaun?</h1>
      <p className="text-lg text-foreground/80">
        Call a number. Chat for two minutes. Real person or AI? The moment you&apos;re
        sure, say <span className="font-semibold">&ldquo;tum bot ho!&rdquo;</span>
      </p>
      <p className="rounded-lg border border-foreground/15 p-4 text-sm text-foreground/70">
        Scaffold only. The landing page, leaderboard and web-call fallback are built in
        WS3. API contract: <code>src/lib/api.ts</code>.
      </p>
    </main>
  );
}
