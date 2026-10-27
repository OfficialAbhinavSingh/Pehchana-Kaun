"use client";

import React, { useEffect, useState } from "react";
import Link from "next/link";
import Waveform from "@/components/Waveform";

type Step = "consent" | "start" | "connecting" | "live" | "error";

// Set once the public number from #1 is live. Until then, browser play is the only way in.
const GAME_NUMBER = process.env.NEXT_PUBLIC_GAME_NUMBER ?? "";
const API_URL =
  process.env.NEXT_PUBLIC_API_URL ?? process.env.API_URL ?? "http://localhost:8000";

type SessionInfo = {
  expires_in?: number;
  [key: string]: unknown;
};

export default function PlayPage() {
  const [step, setStep] = useState<Step>("consent");
  const [hasConsented, setHasConsented] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string>("");
  const [secondsLeft, setSecondsLeft] = useState<number | null>(null);

  useEffect(() => {
    if (step !== "live" || secondsLeft === null) return;
    if (secondsLeft <= 0) return;
    const id = setTimeout(() => setSecondsLeft((s) => (s === null ? null : s - 1)), 1000);
    return () => clearTimeout(id);
  }, [step, secondsLeft]);

  const startBrowserGame = async () => {
    setStep("connecting");
    setErrorMessage("");
    try {
      const res = await fetch(`${API_URL}/webcall/session`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ consent: true }),
      });
      if (!res.ok) {
        const body = await res.json().catch(() => ({ detail: `request failed (${res.status})` }));
        setErrorMessage(body.detail ?? `request failed (${res.status})`);
        setStep("error");
        return;
      }
      const data = (await res.json()) as SessionInfo;
      setSecondsLeft(typeof data.expires_in === "number" ? data.expires_in : null);
      setStep("live");
    } catch {
      setErrorMessage("Could not reach the game server. Check your connection and try again.");
      setStep("error");
    }
  };

  return (
    <main className="min-h-screen bg-[#101014] text-[#F5F5F5] px-4 py-10 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-7xl">
        {/* PROGRESS STEPPER INDICATOR */}
        <div className="mb-10 border-b border-[#2B2B38] pb-5">
          <div className="flex items-center justify-between font-mono text-xs uppercase tracking-wider">
            <div className="flex flex-wrap items-center gap-3 sm:gap-8">
              <span
                className={`flex items-center gap-2 ${
                  step === "consent" ? "text-[#B8FF4D] font-bold" : "text-[#71717A]"
                }`}
              >
                <span className="text-[#8B7CFF]">01</span> The rules
              </span>
              <span className="text-[#2B2B38]">/</span>
              <span
                className={`flex items-center gap-2 ${
                  step === "start" || step === "connecting" || step === "error"
                    ? "text-[#B8FF4D] font-bold"
                    : "text-[#71717A]"
                }`}
              >
                <span className="text-[#8B7CFF]">02</span> Start the call
              </span>
              <span className="text-[#2B2B38]">/</span>
              <span
                className={`flex items-center gap-2 ${
                  step === "live" ? "text-[#B8FF4D] font-bold" : "text-[#71717A]"
                }`}
              >
                <span className="text-[#8B7CFF]">03</span> The call
              </span>
            </div>
          </div>
        </div>

        {/* STEP 1: THE RULES & CONSENT */}
        {step === "consent" && (
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
            <div className="lg:col-span-7 space-y-6">
              <div>
                <span className="font-mono text-xs uppercase tracking-widest text-[#8B7CFF] font-semibold">
                  FIRST, A FAIR WARNING.
                </span>
                <h1 className="mt-2 text-4xl sm:text-6xl font-bold font-display uppercase tracking-tight text-[#F5F5F5] leading-[0.95]">
                  You won&apos;t know
                  <br />
                  who&apos;s talking.
                </h1>
                <p className="mt-4 text-base text-[#A1A1AA] leading-relaxed">
                  That&apos;s the whole point. Here&apos;s what you&apos;re agreeing to before we start.
                </p>
              </div>

              <div className="space-y-4 pt-2">
                <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6">
                  <div className="font-mono text-xs text-[#8B7CFF] font-bold">01</div>
                  <h3 className="mt-2 text-lg font-bold font-display text-[#F5F5F5]">
                    A blind connection
                  </h3>
                  <p className="mt-1 text-sm text-[#A1A1AA] leading-relaxed">
                    Browser play always reaches an AI voice. You can never be talking to a human in
                    this mode.
                  </p>
                </div>

                <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6">
                  <div className="font-mono text-xs text-[#B8FF4D] font-bold">02</div>
                  <h3 className="mt-2 text-lg font-bold font-display text-[#F5F5F5]">
                    60–90 seconds, typically
                  </h3>
                  <p className="mt-1 text-sm text-[#A1A1AA] leading-relaxed">
                    Speak naturally in Hindi or English. If you suspect AI, say the exact phrase
                    &ldquo;Tum bot ho!&rdquo; out loud.
                  </p>
                </div>

                <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6">
                  <div className="font-mono text-xs text-[#8B7CFF] font-bold">03</div>
                  <h3 className="mt-2 text-lg font-bold font-display text-[#F5F5F5]">
                    Your browser microphone is used
                  </h3>
                  <p className="mt-1 text-sm text-[#A1A1AA] leading-relaxed">
                    Playing in browser needs microphone access for the call itself, the browser is
                    not just a companion screen in this mode.
                  </p>
                </div>
              </div>
            </div>

            <div className="lg:col-span-5 space-y-6">
              <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7 space-y-5">
                <div>
                  <span className="font-mono text-xs uppercase tracking-widest text-[#FFB547] font-semibold">
                    A VOICE IS PERSONAL.
                  </span>
                  <h3 className="mt-1 text-xl font-bold font-display text-[#F5F5F5]">
                    Recording & research
                  </h3>
                </div>

                <p className="text-sm text-[#A1A1AA] leading-relaxed">
                  The call is recorded. Audio may be transcribed to identify valid accusations,
                  calculate timing and study conversational giveaways.
                </p>

                <p className="text-xs text-[#71717A] leading-relaxed">
                  Don&apos;t share financial, health or other sensitive personal information. We never
                  keep your phone number; only a one-way hash for repeat-caller counting.
                </p>

                <div className="pt-2">
                  <Link
                    href="/methodology#privacy"
                    className="font-mono text-xs text-[#8B7CFF] hover:underline"
                  >
                    Read privacy & methodology ↗
                  </Link>
                </div>

                <div className="pt-4 border-t border-[#2B2B38] space-y-4">
                  <label className="flex items-start gap-3 cursor-pointer group">
                    <input
                      type="checkbox"
                      checked={hasConsented}
                      onChange={(e) => setHasConsented(e.target.checked)}
                      className="mt-1 h-5 w-5 rounded-[4px] border-[#2B2B38] bg-[#101014] text-[#B8FF4D] accent-[#B8FF4D] focus:ring-[#8B7CFF]"
                    />
                    <span className="text-xs sm:text-sm text-[#F5F5F5] group-hover:text-[#B8FF4D] transition-colors leading-relaxed">
                      I consent to a blind conversation and its recording for transcription,
                      scoring and research.
                    </span>
                  </label>

                  <button
                    type="button"
                    disabled={!hasConsented}
                    onClick={() => setStep("start")}
                    className={`flex h-12 w-full items-center justify-center rounded-[4px] px-6 font-mono text-xs font-bold uppercase tracking-wider transition-all ${
                      hasConsented
                        ? "bg-[#B8FF4D] text-[#101014] hover:bg-[#CDFF7A] shadow-[0_0_20px_rgba(184,255,77,0.3)]"
                        : "bg-[#14141A] text-[#71717A] border border-[#2B2B38] cursor-not-allowed"
                    }`}
                  >
                    Continue
                  </button>

                  <div className="text-[11px] font-mono text-[#71717A] text-center">
                    Consent is required to continue. You can leave now without starting a call.
                  </div>
                </div>
              </div>

              <div className="text-left">
                <Link href="/" className="font-mono text-xs text-[#A1A1AA] hover:text-[#F5F5F5]">
                  ← Back to home
                </Link>
              </div>
            </div>
          </div>
        )}

        {/* STEP 2: START THE CALL */}
        {(step === "start" || step === "connecting" || step === "error") && (
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
            <div className="lg:col-span-6 space-y-6">
              <div>
                <span className="font-mono text-xs uppercase tracking-widest text-[#B8FF4D] font-semibold">
                  ONE VOICE. NO CLUES.
                </span>
                <h1 className="mt-2 text-4xl sm:text-6xl font-bold font-display uppercase tracking-tight text-[#F5F5F5] leading-[0.95]">
                  Your next call
                  <br />
                  is a question.
                </h1>
                <p className="mt-4 text-base text-[#A1A1AA] leading-relaxed">
                  {GAME_NUMBER
                    ? "Call the number for a chance at a human or an AI, or play in your browser against an AI voice."
                    : "The public phone line isn't live yet. Play in your browser against an AI voice."}
                </p>
              </div>

              <div className="inline-flex items-center gap-2 rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] px-3.5 py-1.5 font-mono text-xs text-[#8B7CFF]">
                <span>↙</span>
                <span>Consent recorded for this session</span>
              </div>
            </div>

            <div className="lg:col-span-6 space-y-6">
              {GAME_NUMBER && (
                <a
                  href={`tel:${GAME_NUMBER}`}
                  className="flex h-16 w-full items-center justify-center gap-3 rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] px-6 font-mono text-sm font-bold uppercase tracking-wider text-[#F5F5F5] hover:border-[#B8FF4D]"
                >
                  Call {GAME_NUMBER} ↗
                </a>
              )}

              <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7 space-y-5">
                <div className="font-mono text-xs uppercase tracking-wider text-[#71717A] border-b border-[#2B2B38] pb-3">
                  BROWSER GAME / AI VOICES ONLY
                </div>
                <p className="text-sm text-[#A1A1AA] leading-relaxed">
                  Your browser will ask for microphone access. The call happens over your browser,
                  no app or download needed.
                </p>

                {step === "error" && (
                  <div className="rounded-[4px] border border-[#FF8C8C] bg-[#1B1B23] p-4 font-mono text-xs text-[#FF8C8C]">
                    {errorMessage}
                  </div>
                )}

                <button
                  type="button"
                  disabled={step === "connecting"}
                  onClick={startBrowserGame}
                  className="flex h-13 w-full items-center justify-center rounded-[4px] bg-[#B8FF4D] font-mono text-xs font-bold uppercase tracking-wider text-[#101014] hover:bg-[#CDFF7A] shadow-[0_0_20px_rgba(184,255,77,0.3)] disabled:opacity-60"
                >
                  {step === "connecting" ? "Connecting…" : "Play in browser ↗"}
                </button>

                <div className="pt-2 border-t border-[#2B2B38]">
                  <button
                    type="button"
                    onClick={() => setStep("consent")}
                    className="font-mono text-xs text-[#A1A1AA] hover:text-[#F5F5F5]"
                  >
                    ← Review consent & rules
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* STEP 3: LIVE */}
        {step === "live" && (
          <div className="space-y-8">
            <div className="flex items-center justify-between font-mono text-xs border-b border-[#2B2B38] pb-4">
              <span className="flex items-center gap-2 text-[#B8FF4D] font-bold">
                <span className="h-2.5 w-2.5 rounded-full bg-[#B8FF4D] animate-ping" />
                Session minted
              </span>
              <span className="text-[#8B7CFF]">BROWSER · AI VOICE · IDENTITY HIDDEN</span>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
              <div className="lg:col-span-7 space-y-8">
                <h1 className="text-4xl sm:text-6xl font-bold font-display uppercase tracking-tight text-[#F5F5F5] leading-[0.95]">
                  Listen to the voice.
                  <br />
                  Trust your instinct.
                </h1>

                <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-8 sm:p-12 text-center">
                  <div className="font-mono text-5xl sm:text-7xl font-bold tracking-tight text-[#F5F5F5]">
                    {secondsLeft !== null ? `${secondsLeft}s` : "—"}
                  </div>
                  <div className="mt-2 font-mono text-xs uppercase tracking-widest text-[#71717A]">
                    SESSION TIME REMAINING
                  </div>

                  <div className="mt-8">
                    <Waveform active={true} size="lg" className="w-full max-w-md mx-auto" />
                  </div>
                  <div className="mt-3 font-mono text-[11px] text-[#71717A]">
                    DECORATIVE SIGNAL · NOT LIVE AUDIO
                  </div>
                </div>

                <div className="font-mono text-xs text-[#71717A]">
                  The in-browser audio call itself is wired through the Bolna Web Call SDK, tracked
                  separately. This screen confirms a session was minted for your game.
                </div>
              </div>

              <div className="lg:col-span-5 space-y-6">
                <div className="rounded-[4px] border border-[#8B7CFF] bg-[#1B1B23] p-7 space-y-4">
                  <div className="font-mono text-xs uppercase tracking-widest text-[#8B7CFF] font-bold">
                    YOUR SPECIAL MOVE
                  </div>
                  <h2 className="text-3xl sm:text-4xl font-bold font-display text-[#B8FF4D]">
                    &ldquo;Tum bot ho!&rdquo;
                  </h2>
                  <p className="text-sm text-[#A1A1AA] leading-relaxed">
                    Say the phrase out loud during the call. There&apos;s no button here, it&apos;s part
                    of the conversation.
                  </p>
                </div>

                <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7 space-y-3">
                  <h3 className="text-lg font-bold font-display text-[#F5F5F5]">
                    Your result goes on the leaderboard
                  </h3>
                  <p className="text-sm text-[#A1A1AA] leading-relaxed">
                    This site never shows a per-call verdict for you specifically; results are
                    counted into the public, anonymous leaderboard.
                  </p>
                </div>

                <Link
                  href="/leaderboard"
                  className="flex h-12 w-full items-center justify-center rounded-[4px] bg-[#B8FF4D] font-mono text-xs font-bold uppercase tracking-wider text-[#101014] hover:bg-[#CDFF7A]"
                >
                  View Leaderboard ↗
                </Link>
              </div>
            </div>
          </div>
        )}
      </div>
    </main>
  );
}
