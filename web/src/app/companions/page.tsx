import React from "react";
import Link from "next/link";

export default function CompanionsPage() {
  const maskedPhone = "+91 ••••• ••210 HINDI";

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
            <span className="text-[#B8FF4D]">Even when it&apos;s not a call.</span>
          </h1>
          <p className="mt-4 text-base text-[#A1A1AA] max-w-2xl leading-relaxed">
            Connection, recovery and post-call processing states. Identity remains hidden until a completed reveal is available.
          </p>
        </div>

        {/* 6 State Cards Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* State 1: Connecting */}
          <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7 space-y-4">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-[#8B7CFF] uppercase font-bold">CALL INITIATION / CONNECTING</span>
              <span className="text-[#71717A]">{maskedPhone}</span>
            </div>
            <div className="text-xs font-mono text-[#A1A1AA] uppercase">Connecting securely</div>
            <h3 className="text-2xl font-bold font-display text-[#F5F5F5]">
              Finding your mystery voice.
            </h3>
            <p className="text-sm text-[#A1A1AA] leading-relaxed">
              We&apos;re preparing your phone call. Keep this page open and your phone nearby. The participant&apos;s identity is hidden.
            </p>
            <div className="pt-3 border-t border-[#2B2B38] flex items-center gap-2 font-mono text-xs text-[#71717A]">
              <span className="h-2 w-2 rounded-full bg-[#8B7CFF] animate-spin" />
              <span>Preparing your call · No browser audio or microphone access is needed.</span>
            </div>
          </div>

          {/* State 2: Ringing */}
          <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7 space-y-4">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-[#B8FF4D] uppercase font-bold">CALL INITIATION / RINGING</span>
              <span className="text-[#71717A]">{maskedPhone}</span>
            </div>
            <div className="text-xs font-mono text-[#A1A1AA] uppercase">Your phone is ringing</div>
            <h3 className="text-2xl font-bold font-display text-[#F5F5F5]">
              Pick up. It&apos;s time.
            </h3>
            <p className="text-sm text-[#A1A1AA] leading-relaxed">
              Answer the incoming call on your phone. Your companion will show the timer after connection not before.
            </p>
            <div className="pt-3 border-t border-[#2B2B38] flex items-center gap-2 font-mono text-xs text-[#B8FF4D]">
              <span className="h-2 w-2 rounded-full bg-[#B8FF4D] animate-ping" />
              <span>Waiting for your answer · The conversation happens on your phone, not in this page.</span>
            </div>
          </div>

          {/* State 3: No Answer */}
          <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7 space-y-4">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-[#FFB547] uppercase font-bold">CALL INITIATION / NO ANSWER</span>
              <span className="text-[#71717A]">{maskedPhone}</span>
            </div>
            <div className="text-xs font-mono text-[#A1A1AA] uppercase">Call not answered</div>
            <h3 className="text-2xl font-bold font-display text-[#F5F5F5]">
              Missed the call? No problem.
            </h3>
            <p className="text-sm text-[#A1A1AA] leading-relaxed">
              No connected conversation was recorded for this attempt. Check your phone number and whether incoming calls are blocked.
            </p>
            <div className="pt-3 border-t border-[#2B2B38] flex items-center justify-between">
              <Link href="/play" className="font-mono text-xs text-[#B8FF4D] hover:underline font-bold">
                Try calling again ↗
              </Link>
              <span className="text-[11px] font-mono text-[#71717A]">
                You can return to setup to correct your number.
              </span>
            </div>
          </div>

          {/* State 4: Connection Error */}
          <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7 space-y-4">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-[#FF8C8C] uppercase font-bold">CALL INITIATION / CONNECTION ERROR</span>
              <span className="text-[#71717A]">{maskedPhone}</span>
            </div>
            <div className="text-xs font-mono text-[#A1A1AA] uppercase">We couldn&apos;t connect</div>
            <h3 className="text-2xl font-bold font-display text-[#F5F5F5]">
              Let&apos;s try that again.
            </h3>
            <p className="text-sm text-[#A1A1AA] leading-relaxed">
              The call could not be placed. Check your number and phone reception, then try again. No identity has been revealed.
            </p>
            <div className="pt-3 border-t border-[#2B2B38] flex items-center justify-between">
              <Link href="/play" className="font-mono text-xs text-[#B8FF4D] hover:underline font-bold">
                Retry call ↗
              </Link>
              <span className="text-[11px] font-mono text-[#71717A]">
                If this keeps happening, return to setup.
              </span>
            </div>
          </div>

          {/* State 5: Scoring Pending */}
          <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7 space-y-4">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-[#8B7CFF] uppercase font-bold">AFTER THE CALL / SCORING</span>
              <span className="text-[#71717A]">{maskedPhone}</span>
            </div>
            <div className="text-xs font-mono text-[#A1A1AA] uppercase">Call ended · result pending</div>
            <h3 className="text-2xl font-bold font-display text-[#F5F5F5]">
              The call&apos;s over. Hold that thought.
            </h3>
            <p className="text-sm text-[#A1A1AA] leading-relaxed">
              We&apos;re waiting for the post-call result. Your participant&apos;s identity and accusation timing aren&apos;t available yet.
            </p>
            <div className="pt-3 border-t border-[#2B2B38] flex items-center gap-2 font-mono text-xs text-[#8B7CFF]">
              <span className="h-2 w-2 rounded-full bg-[#8B7CFF] animate-pulse" />
              <span>Preparing your reveal · This is a processing state, not live transcription.</span>
            </div>
          </div>

          {/* State 6: Result Error */}
          <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7 space-y-4">
            <div className="flex items-center justify-between font-mono text-xs">
              <span className="text-[#FF8C8C] uppercase font-bold">AFTER THE CALL / RESULT ERROR</span>
              <span className="text-[#71717A]">{maskedPhone}</span>
            </div>
            <div className="text-xs font-mono text-[#A1A1AA] uppercase">Result unavailable</div>
            <h3 className="text-2xl font-bold font-display text-[#F5F5F5]">
              No verdict yet.
            </h3>
            <p className="text-sm text-[#A1A1AA] leading-relaxed">
              Your result couldn&apos;t be retrieved. We won&apos;t invent an identity, an accusation or a detection time while it&apos;s unavailable.
            </p>
            <div className="pt-3 border-t border-[#2B2B38] flex items-center justify-between">
              <Link href="/play" className="font-mono text-xs text-[#B8FF4D] hover:underline font-bold">
                Check result again ↗
              </Link>
              <span className="text-[11px] font-mono text-[#71717A]">
                Retry retrieves the result; it does not start another call.
              </span>
            </div>
          </div>
        </div>

        <div className="rounded-[4px] border border-[#2B2B38] bg-[#14141A] p-5 font-mono text-xs text-[#71717A]">
          Only call setup and retry actions start phone calls. No state on this website provides an in-browser mute or end-call control.
        </div>
      </div>
    </main>
  );
}
