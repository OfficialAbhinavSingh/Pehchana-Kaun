import React from "react";
import Link from "next/link";

export default function CompanionsPage() {
  return (
    <main className="min-h-screen bg-[#f7f4fc] text-[#1f1b2e] px-4 py-12 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-7xl space-y-12">
        {/* Header */}
        <div className="border-b-2 border-[#1f1b2e] pb-8">
          <span className="font-mono text-xs uppercase tracking-widest text-[#5b45e0] font-semibold">
            JOURNEY COMPANIONS / STATIC STATE EXAMPLES
          </span>
          <h1 className="mt-2 text-4xl sm:text-6xl font-bold font-display uppercase tracking-tight text-[#1f1b2e]">
            A clear next step.
            <br />
            <span className="text-[#6a56e8]">Even when a session fails.</span>
          </h1>
          <p className="mt-4 text-base text-[#3b3552] max-w-2xl leading-relaxed">
            Browser-game connection and recovery states. The game only ever runs over phone calls
            (inbound, when the public number is live) or an AI voice in the browser; the site never
            places an outbound call.
          </p>
        </div>

        {/* State Cards Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* State 1: Connecting */}
          <div className="rounded-3xl border-2 border-[#1f1b2e] bg-[#ffffff] p-7 space-y-4">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-[#5b45e0] uppercase font-bold">BROWSER GAME / CONNECTING</span>
              <span className="text-[#5d5675]">POST /webcall/session</span>
            </div>
            <div className="text-xs font-mono text-[#3b3552] uppercase">Minting your session</div>
            <h3 className="text-2xl font-bold font-display text-[#1f1b2e]">
              Finding your mystery voice.
            </h3>
            <p className="text-sm text-[#3b3552] leading-relaxed">
              The browser is asking the backend for an AI voice session. Microphone access is
              requested once it&apos;s ready.
            </p>
            <div className="pt-3 border-t-2 border-[#1f1b2e] flex items-center gap-2 font-mono text-xs text-[#5d5675]">
              <span className="h-2 w-2 rounded-full bg-[#5b45e0] animate-spin" />
              <span>Usually under a second · AI voice only.</span>
            </div>
          </div>

          {/* State 2: Rate limited */}
          <div className="rounded-3xl border-2 border-[#1f1b2e] bg-[#ffffff] p-7 space-y-4">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-[#a8520a] uppercase font-bold">BROWSER GAME / 429</span>
              <span className="text-[#5d5675]">RATE LIMITED</span>
            </div>
            <div className="text-xs font-mono text-[#3b3552] uppercase">Too many sessions</div>
            <h3 className="text-2xl font-bold font-display text-[#1f1b2e]">
              Give it a few minutes.
            </h3>
            <p className="text-sm text-[#3b3552] leading-relaxed">
              Every session is a real call, so we cap sessions per network and in total per hour.
              The backend&apos;s own message is shown, not a generic error.
            </p>
            <div className="pt-3 border-t-2 border-[#1f1b2e] flex items-center justify-between">
              <Link href="/play" className="font-mono text-xs text-[#6a56e8] hover:underline font-bold">
                Try again later ↗
              </Link>
              <span className="text-[11px] font-mono text-[#5d5675]">No session was started.</span>
            </div>
          </div>

          {/* State 3: No arm available */}
          <div className="rounded-3xl border-2 border-[#1f1b2e] bg-[#ffffff] p-7 space-y-4">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-[#a8520a] uppercase font-bold">BROWSER GAME / 503</span>
              <span className="text-[#5d5675]">NO VOICE FREE</span>
            </div>
            <div className="text-xs font-mono text-[#3b3552] uppercase">Nothing to connect to</div>
            <h3 className="text-2xl font-bold font-display text-[#1f1b2e]">
              Every voice is busy.
            </h3>
            <p className="text-sm text-[#3b3552] leading-relaxed">
              No AI arm with a browser-call agent is eligible right now. This is rare and usually
              clears quickly.
            </p>
            <div className="pt-3 border-t-2 border-[#1f1b2e] flex items-center justify-between">
              <Link href="/play" className="font-mono text-xs text-[#6a56e8] hover:underline font-bold">
                Retry ↗
              </Link>
            </div>
          </div>

          {/* State 4: Mint failed */}
          <div className="rounded-3xl border-2 border-[#1f1b2e] bg-[#ffffff] p-7 space-y-4">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-[#c81e3a] uppercase font-bold">BROWSER GAME / 502</span>
              <span className="text-[#5d5675]">SESSION MINT FAILED</span>
            </div>
            <div className="text-xs font-mono text-[#3b3552] uppercase">We couldn&apos;t connect</div>
            <h3 className="text-2xl font-bold font-display text-[#1f1b2e]">
              Let&apos;s try that again.
            </h3>
            <p className="text-sm text-[#3b3552] leading-relaxed">
              The vendor call to start your session failed. No call is counted; nothing was
              recorded.
            </p>
            <div className="pt-3 border-t-2 border-[#1f1b2e] flex items-center justify-between">
              <Link href="/play" className="font-mono text-xs text-[#6a56e8] hover:underline font-bold">
                Retry ↗
              </Link>
            </div>
          </div>

          {/* State 5: Live session */}
          <div className="rounded-3xl border-2 border-[#1f1b2e] bg-[#ffffff] p-7 space-y-4">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-[#6a56e8] uppercase font-bold">BROWSER GAME / LIVE</span>
              <span className="text-[#5d5675]">SESSION MINTED</span>
            </div>
            <div className="text-xs font-mono text-[#3b3552] uppercase">Session active</div>
            <h3 className="text-2xl font-bold font-display text-[#1f1b2e]">
              Pick up. It&apos;s time.
            </h3>
            <p className="text-sm text-[#3b3552] leading-relaxed">
              Your browser microphone carries the call. Say &ldquo;Tum bot ho!&rdquo; if you suspect AI;
              there&apos;s no button for it.
            </p>
            <div className="pt-3 border-t-2 border-[#1f1b2e] flex items-center gap-2 font-mono text-xs text-[#6a56e8]">
              <span className="h-2 w-2 rounded-full bg-[#6a56e8] animate-ping" />
              <span>Sessions last about 2 minutes and are single-use.</span>
            </div>
          </div>

          {/* State 6: Not built yet */}
          <div className="rounded-3xl border-2 border-[#1f1b2e] bg-[#ffffff] p-7 space-y-4">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-[#5d5675] uppercase font-bold">BROWSER GAME / 501</span>
              <span className="text-[#5d5675]">NOT BUILT YET</span>
            </div>
            <div className="text-xs font-mono text-[#3b3552] uppercase">Browser game not ready</div>
            <h3 className="text-2xl font-bold font-display text-[#1f1b2e]">
              Not wired up yet.
            </h3>
            <p className="text-sm text-[#3b3552] leading-relaxed">
              The backend&apos;s Bolna web-call client isn&apos;t built yet. We won&apos;t invent a
              conversation or a verdict while it isn&apos;t.
            </p>
            <div className="pt-3 border-t-2 border-[#1f1b2e] flex items-center justify-between">
              <Link href="/leaderboard" className="font-mono text-xs text-[#6a56e8] hover:underline font-bold">
                See the leaderboard instead ↗
              </Link>
            </div>
          </div>
        </div>

        <div className="rounded-3xl border-2 border-[#1f1b2e] bg-[#ece6ff] p-5 font-mono text-xs text-[#5d5675]">
          This site never places an outbound call to your phone. A phone game means you call the
          public number; a browser game means your browser connects to an AI voice.
        </div>
      </div>
    </main>
  );
}
