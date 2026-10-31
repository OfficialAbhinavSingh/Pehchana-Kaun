import React from "react";
import Link from "next/link";

export default function CompanionsPage() {
  return (
    <main className="min-h-screen bg-[#f3f2f2] text-[#201e1d] px-4 py-12 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-7xl space-y-12">
        {/* Header */}
        <div className="border-b-2 border-[#201e1d] pb-8">
          <span className="font-mono text-xs uppercase tracking-widest text-[#ae1800] font-semibold">
            JOURNEY COMPANIONS / STATIC STATE EXAMPLES
          </span>
          <h1 className="mt-2 text-4xl sm:text-6xl font-bold font-display uppercase tracking-tight text-[#201e1d]">
            A clear next step.
            <br />
            <span className="text-[#ec3013]">Even when a session fails.</span>
          </h1>
          <p className="mt-4 text-base text-[#605d5d] max-w-2xl leading-relaxed">
            Browser-game connection and recovery states. The game only ever runs over phone calls
            (inbound, when the public number is live) or an AI voice in the browser; the site never
            places an outbound call.
          </p>
        </div>

        {/* State Cards Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* State 1: Connecting */}
          <div className=" border-2 border-[#201e1d] bg-[#ffffff] p-7 space-y-4">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-[#ae1800] uppercase font-bold">BROWSER GAME / CONNECTING</span>
              <span className="text-[#7d7979]">POST /webcall/session</span>
            </div>
            <div className="text-xs font-mono text-[#605d5d] uppercase">Minting your session</div>
            <h3 className="text-2xl font-bold font-display text-[#201e1d]">
              Finding your mystery voice.
            </h3>
            <p className="text-sm text-[#605d5d] leading-relaxed">
              The browser is asking the backend for an AI voice session. Microphone access is
              requested once it&apos;s ready.
            </p>
            <div className="pt-3 border-t-2 border-[#201e1d] flex items-center gap-2 font-mono text-xs text-[#7d7979]">
              <span className="h-2 w-2 bg-[#ae1800] animate-spin" />
              <span>Usually under a second · AI voice only.</span>
            </div>
          </div>

          {/* State 2: Rate limited */}
          <div className=" border-2 border-[#201e1d] bg-[#ffffff] p-7 space-y-4">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-[#a8520a] uppercase font-bold">BROWSER GAME / 429</span>
              <span className="text-[#7d7979]">RATE LIMITED</span>
            </div>
            <div className="text-xs font-mono text-[#605d5d] uppercase">Too many sessions</div>
            <h3 className="text-2xl font-bold font-display text-[#201e1d]">
              Give it a few minutes.
            </h3>
            <p className="text-sm text-[#605d5d] leading-relaxed">
              Every session is a real call, so we cap sessions per network and in total per hour.
              The backend&apos;s own message is shown, not a generic error.
            </p>
            <div className="pt-3 border-t-2 border-[#201e1d] flex items-center justify-between">
              <Link href="/play" className="font-mono text-xs text-[#ec3013] hover:underline font-bold">
                Try again later ↗
              </Link>
              <span className="text-[11px] font-mono text-[#7d7979]">No session was started.</span>
            </div>
          </div>

          {/* State 3: No arm available */}
          <div className=" border-2 border-[#201e1d] bg-[#ffffff] p-7 space-y-4">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-[#a8520a] uppercase font-bold">BROWSER GAME / 503</span>
              <span className="text-[#7d7979]">NO VOICE FREE</span>
            </div>
            <div className="text-xs font-mono text-[#605d5d] uppercase">Nothing to connect to</div>
            <h3 className="text-2xl font-bold font-display text-[#201e1d]">
              Every voice is busy.
            </h3>
            <p className="text-sm text-[#605d5d] leading-relaxed">
              No AI arm with a browser-call agent is eligible right now. This is rare and usually
              clears quickly.
            </p>
            <div className="pt-3 border-t-2 border-[#201e1d] flex items-center justify-between">
              <Link href="/play" className="font-mono text-xs text-[#ec3013] hover:underline font-bold">
                Retry ↗
              </Link>
            </div>
          </div>

          {/* State 4: Mint failed */}
          <div className=" border-2 border-[#201e1d] bg-[#ffffff] p-7 space-y-4">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-[#c81e3a] uppercase font-bold">BROWSER GAME / 502</span>
              <span className="text-[#7d7979]">SESSION MINT FAILED</span>
            </div>
            <div className="text-xs font-mono text-[#605d5d] uppercase">We couldn&apos;t connect</div>
            <h3 className="text-2xl font-bold font-display text-[#201e1d]">
              Let&apos;s try that again.
            </h3>
            <p className="text-sm text-[#605d5d] leading-relaxed">
              The vendor call to start your session failed. No call is counted; nothing was
              recorded.
            </p>
            <div className="pt-3 border-t-2 border-[#201e1d] flex items-center justify-between">
              <Link href="/play" className="font-mono text-xs text-[#ec3013] hover:underline font-bold">
                Retry ↗
              </Link>
            </div>
          </div>

          {/* State 5: Live session */}
          <div className=" border-2 border-[#201e1d] bg-[#ffffff] p-7 space-y-4">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-[#ec3013] uppercase font-bold">BROWSER GAME / LIVE</span>
              <span className="text-[#7d7979]">SESSION MINTED</span>
            </div>
            <div className="text-xs font-mono text-[#605d5d] uppercase">Session active</div>
            <h3 className="text-2xl font-bold font-display text-[#201e1d]">
              Pick up. It&apos;s time.
            </h3>
            <p className="text-sm text-[#605d5d] leading-relaxed">
              Your browser microphone carries the call. Say &ldquo;Tum bot ho!&rdquo; if you suspect AI;
              there&apos;s no button for it.
            </p>
            <div className="pt-3 border-t-2 border-[#201e1d] flex items-center gap-2 font-mono text-xs text-[#ec3013]">
              <span className="h-2 w-2 bg-[#ec3013] animate-ping" />
              <span>Sessions last about 2 minutes and are single-use.</span>
            </div>
          </div>

          {/* State 6: Not built yet */}
          <div className=" border-2 border-[#201e1d] bg-[#ffffff] p-7 space-y-4">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-[#7d7979] uppercase font-bold">BROWSER GAME / 501</span>
              <span className="text-[#7d7979]">NOT BUILT YET</span>
            </div>
            <div className="text-xs font-mono text-[#605d5d] uppercase">Browser game not ready</div>
            <h3 className="text-2xl font-bold font-display text-[#201e1d]">
              Not wired up yet.
            </h3>
            <p className="text-sm text-[#605d5d] leading-relaxed">
              The backend&apos;s Bolna web-call client isn&apos;t built yet. We won&apos;t invent a
              conversation or a verdict while it isn&apos;t.
            </p>
            <div className="pt-3 border-t-2 border-[#201e1d] flex items-center justify-between">
              <Link href="/leaderboard" className="font-mono text-xs text-[#ec3013] hover:underline font-bold">
                See the leaderboard instead ↗
              </Link>
            </div>
          </div>
        </div>

        <div className=" border-2 border-[#201e1d] bg-[#fff2ef] p-5 font-mono text-xs text-[#7d7979]">
          This site never places an outbound call to your phone. A phone game means you call the
          public number; a browser game means your browser connects to an AI voice.
        </div>
      </div>
    </main>
  );
}
