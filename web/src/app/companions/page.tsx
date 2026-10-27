import React from "react";
import Link from "next/link";

export default function CompanionsPage() {
  return (
    <main className="min-h-screen bg-[#101014] text-[#F5F5F5] px-4 py-12 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-7xl space-y-12">
        {/* Header */}
        <div className="border-b border-[#2B2B38] pb-8">
          <span className="font-mono text-xs uppercase tracking-widest text-[#8B7CFF] font-semibold">
            JOURNEY COMPANIONS / STATIC STATE EXAMPLES
          </span>
          <h1 className="mt-2 text-4xl sm:text-6xl font-bold font-display uppercase tracking-tight text-[#F5F5F5]">
            A clear next step.
            <br />
            <span className="text-[#B8FF4D]">Even when a session fails.</span>
          </h1>
          <p className="mt-4 text-base text-[#A1A1AA] max-w-2xl leading-relaxed">
            Browser-game connection and recovery states. The game only ever runs over phone calls
            (inbound, when the public number is live) or an AI voice in the browser; the site never
            places an outbound call.
          </p>
        </div>

        {/* State Cards Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* State 1: Connecting */}
          <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7 space-y-4">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-[#8B7CFF] uppercase font-bold">BROWSER GAME / CONNECTING</span>
              <span className="text-[#71717A]">POST /webcall/session</span>
            </div>
            <div className="text-xs font-mono text-[#A1A1AA] uppercase">Minting your session</div>
            <h3 className="text-2xl font-bold font-display text-[#F5F5F5]">
              Finding your mystery voice.
            </h3>
            <p className="text-sm text-[#A1A1AA] leading-relaxed">
              The browser is asking the backend for an AI voice session. Microphone access is
              requested once it&apos;s ready.
            </p>
            <div className="pt-3 border-t border-[#2B2B38] flex items-center gap-2 font-mono text-xs text-[#71717A]">
              <span className="h-2 w-2 rounded-full bg-[#8B7CFF] animate-spin" />
              <span>Usually under a second · AI voice only.</span>
            </div>
          </div>

          {/* State 2: Rate limited */}
          <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7 space-y-4">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-[#FFB547] uppercase font-bold">BROWSER GAME / 429</span>
              <span className="text-[#71717A]">RATE LIMITED</span>
            </div>
            <div className="text-xs font-mono text-[#A1A1AA] uppercase">Too many sessions</div>
            <h3 className="text-2xl font-bold font-display text-[#F5F5F5]">
              Give it a few minutes.
            </h3>
            <p className="text-sm text-[#A1A1AA] leading-relaxed">
              Every session is a real call, so we cap sessions per network and in total per hour.
              The backend&apos;s own message is shown, not a generic error.
            </p>
            <div className="pt-3 border-t border-[#2B2B38] flex items-center justify-between">
              <Link href="/play" className="font-mono text-xs text-[#B8FF4D] hover:underline font-bold">
                Try again later ↗
              </Link>
              <span className="text-[11px] font-mono text-[#71717A]">No session was started.</span>
            </div>
          </div>

          {/* State 3: No arm available */}
          <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7 space-y-4">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-[#FFB547] uppercase font-bold">BROWSER GAME / 503</span>
              <span className="text-[#71717A]">NO VOICE FREE</span>
            </div>
            <div className="text-xs font-mono text-[#A1A1AA] uppercase">Nothing to connect to</div>
            <h3 className="text-2xl font-bold font-display text-[#F5F5F5]">
              Every voice is busy.
            </h3>
            <p className="text-sm text-[#A1A1AA] leading-relaxed">
              No AI arm with a browser-call agent is eligible right now. This is rare and usually
              clears quickly.
            </p>
            <div className="pt-3 border-t border-[#2B2B38] flex items-center justify-between">
              <Link href="/play" className="font-mono text-xs text-[#B8FF4D] hover:underline font-bold">
                Retry ↗
              </Link>
            </div>
          </div>

          {/* State 4: Mint failed */}
          <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7 space-y-4">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-[#FF8C8C] uppercase font-bold">BROWSER GAME / 502</span>
              <span className="text-[#71717A]">SESSION MINT FAILED</span>
            </div>
            <div className="text-xs font-mono text-[#A1A1AA] uppercase">We couldn&apos;t connect</div>
            <h3 className="text-2xl font-bold font-display text-[#F5F5F5]">
              Let&apos;s try that again.
            </h3>
            <p className="text-sm text-[#A1A1AA] leading-relaxed">
              The vendor call to start your session failed. No call is counted; nothing was
              recorded.
            </p>
            <div className="pt-3 border-t border-[#2B2B38] flex items-center justify-between">
              <Link href="/play" className="font-mono text-xs text-[#B8FF4D] hover:underline font-bold">
                Retry ↗
              </Link>
            </div>
          </div>

          {/* State 5: Live session */}
          <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7 space-y-4">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-[#B8FF4D] uppercase font-bold">BROWSER GAME / LIVE</span>
              <span className="text-[#71717A]">SESSION MINTED</span>
            </div>
            <div className="text-xs font-mono text-[#A1A1AA] uppercase">Session active</div>
            <h3 className="text-2xl font-bold font-display text-[#F5F5F5]">
              Pick up. It&apos;s time.
            </h3>
            <p className="text-sm text-[#A1A1AA] leading-relaxed">
              Your browser microphone carries the call. Say &ldquo;Tum bot ho!&rdquo; if you suspect AI;
              there&apos;s no button for it.
            </p>
            <div className="pt-3 border-t border-[#2B2B38] flex items-center gap-2 font-mono text-xs text-[#B8FF4D]">
              <span className="h-2 w-2 rounded-full bg-[#B8FF4D] animate-ping" />
              <span>Sessions last about 2 minutes and are single-use.</span>
            </div>
          </div>

          {/* State 6: Not built yet */}
          <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7 space-y-4">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-[#71717A] uppercase font-bold">BROWSER GAME / 501</span>
              <span className="text-[#71717A]">NOT BUILT YET</span>
            </div>
            <div className="text-xs font-mono text-[#A1A1AA] uppercase">Browser game not ready</div>
            <h3 className="text-2xl font-bold font-display text-[#F5F5F5]">
              Not wired up yet.
            </h3>
            <p className="text-sm text-[#A1A1AA] leading-relaxed">
              The backend&apos;s Bolna web-call client isn&apos;t built yet. We won&apos;t invent a
              conversation or a verdict while it isn&apos;t.
            </p>
            <div className="pt-3 border-t border-[#2B2B38] flex items-center justify-between">
              <Link href="/leaderboard" className="font-mono text-xs text-[#B8FF4D] hover:underline font-bold">
                See the leaderboard instead ↗
              </Link>
            </div>
          </div>
        </div>

        <div className="rounded-[4px] border border-[#2B2B38] bg-[#14141A] p-5 font-mono text-xs text-[#71717A]">
          This site never places an outbound call to your phone. A phone game means you call the
          public number; a browser game means your browser connects to an AI voice.
        </div>
      </div>
    </main>
  );
}
