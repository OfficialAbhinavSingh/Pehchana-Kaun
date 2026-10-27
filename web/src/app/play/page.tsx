"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import Waveform from "@/components/Waveform";

type Step = "consent" | "setup" | "call" | "reveal";
type CallStatus = "connecting" | "ringing" | "connected" | "scoring";
type RevealOutcome = "ai_detected" | "human_control" | "undetected";

export default function PlayPage() {
  const [currentStep, setCurrentStep] = useState<Step>("consent");

  // Step 1: Consent state
  const [hasConsented, setHasConsented] = useState<boolean>(false);

  // Step 2: Call config
  const [language, setLanguage] = useState<"Hindi" | "English">("Hindi");
  const [phoneNumber, setPhoneNumber] = useState<string>("+91 98765 43210");
  const [phoneError, setPhoneError] = useState<string>("");

  // Step 3: In-call companion state
  const [callStatus, setCallStatus] = useState<CallStatus>("connected");
  const [elapsedSeconds, setElapsedSeconds] = useState<number>(42);
  const [isTimerRunning, setIsTimerRunning] = useState<boolean>(true);

  // Step 4: Reveal outcome state
  const [revealOutcome, setRevealOutcome] = useState<RevealOutcome>("ai_detected");

  // Timer effect for live connected companion
  useEffect(() => {
    let interval: NodeJS.Timeout;
    if (currentStep === "call" && callStatus === "connected" && isTimerRunning) {
      interval = setInterval(() => {
        setElapsedSeconds((prev) => prev + 1);
      }, 1000);
    }
    return () => clearInterval(interval);
  }, [currentStep, callStatus, isTimerRunning]);

  const formatTime = (totalSeconds: number) => {
    const mins = Math.floor(totalSeconds / 60);
    const secs = totalSeconds % 60;
    return `${mins.toString().padStart(2, "0")}:${secs.toString().padStart(2, "0")}`;
  };

  const maskedPhone = "+91 ••••• ••210";

  const handlePhoneSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!phoneNumber || phoneNumber.trim().length < 6) {
      setPhoneError("Enter a valid Indian mobile number.");
      return;
    }
    setPhoneError("");
    setElapsedSeconds(42);
    setCallStatus("connected");
    setIsTimerRunning(true);
    setCurrentStep("call");
  };

  return (
    <main className="min-h-screen bg-[#101014] text-[#F5F5F5] px-4 py-10 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-7xl">
        {/* ─────────────────────────────────────────────────────────────
            PROGRESS STEPPER INDICATOR
           ───────────────────────────────────────────────────────────── */}
        <div className="mb-10 border-b border-[#2B2B38] pb-5">
          <div className="flex items-center justify-between font-mono text-xs uppercase tracking-wider">
            <div className="flex flex-wrap items-center gap-3 sm:gap-8">
              <span
                className={`flex items-center gap-2 ${
                  currentStep === "consent"
                    ? "text-[#B8FF4D] font-bold"
                    : "text-[#71717A]"
                }`}
              >
                <span className="text-[#8B7CFF]">01</span> The rules
              </span>
              <span className="text-[#2B2B38]">/</span>
              <span
                className={`flex items-center gap-2 ${
                  currentStep === "setup"
                    ? "text-[#B8FF4D] font-bold"
                    : "text-[#71717A]"
                }`}
              >
                <span className="text-[#8B7CFF]">02</span> Your phone
              </span>
              <span className="text-[#2B2B38]">/</span>
              <span
                className={`flex items-center gap-2 ${
                  currentStep === "call"
                    ? "text-[#B8FF4D] font-bold"
                    : "text-[#71717A]"
                }`}
              >
                <span className="text-[#8B7CFF]">03</span> The call
              </span>
              <span className="text-[#2B2B38]">/</span>
              <span
                className={`flex items-center gap-2 ${
                  currentStep === "reveal"
                    ? "text-[#B8FF4D] font-bold"
                    : "text-[#71717A]"
                }`}
              >
                <span className="text-[#8B7CFF]">04</span> The reveal
              </span>
            </div>

            <span className="hidden sm:inline-block text-[#8B7CFF] font-mono text-xs">
              PHONE ONLY EXPERIMENT
            </span>
          </div>
        </div>

        {/* ─────────────────────────────────────────────────────────────
            STEP 1: THE RULES & CONSENT (EXACT TWO-COLUMN LAYOUT FROM PDF)
           ───────────────────────────────────────────────────────────── */}
        {currentStep === "consent" && (
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
            {/* Left Column: Warning & 3 Rule Cards */}
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
                  That&apos;s the whole point. Here&apos;s what you&apos;re agreeing to before we call.
                </p>
              </div>

              <div className="space-y-4 pt-2">
                <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6">
                  <div className="font-mono text-xs text-[#8B7CFF] font-bold">01</div>
                  <h3 className="mt-2 text-lg font-bold font-display text-[#F5F5F5]">
                    A blind connection
                  </h3>
                  <p className="mt-1 text-sm text-[#A1A1AA] leading-relaxed">
                    You&apos;ll be randomly matched with a human or an AI. Their identity stays hidden until after the call.
                  </p>
                </div>

                <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6">
                  <div className="font-mono text-xs text-[#B8FF4D] font-bold">02</div>
                  <h3 className="mt-2 text-lg font-bold font-display text-[#F5F5F5]">
                    60–90 seconds, typically
                  </h3>
                  <p className="mt-1 text-sm text-[#A1A1AA] leading-relaxed">
                    Speak naturally in Hindi or English. If you suspect AI, say the exact phrase &ldquo;Tum bot ho!&rdquo; on the phone.
                  </p>
                </div>

                <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6">
                  <div className="font-mono text-xs text-[#8B7CFF] font-bold">03</div>
                  <h3 className="mt-2 text-lg font-bold font-display text-[#F5F5F5]">
                    Your phone is the game
                  </h3>
                  <p className="mt-1 text-sm text-[#A1A1AA] leading-relaxed">
                    The browser is only a companion. To finish, hang up on your phone. Then return here for the reveal.
                  </p>
                </div>
              </div>
            </div>

            {/* Right Column: Research Notice & Consent Box */}
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
                  The proposed experiment records your call. Audio may be transcribed to identify valid accusations, calculate timing and study conversational giveaways.
                </p>

                <p className="text-xs text-[#71717A] leading-relaxed">
                  Don&apos;t share financial, health or other sensitive personal information. Your phone number is for call delivery; it must not appear in public results.
                </p>

                <div className="pt-2 border-t border-[#2B2B38]">
                  <div className="font-mono text-xs text-[#F5F5F5] font-semibold mb-1">
                    Prototype policy pending confirmation
                  </div>
                  <p className="text-xs text-[#71717A] leading-relaxed">
                    Who can access recordings, where they&apos;re stored, retention periods and how deletion requests are handled are not yet finalized. Final terms must be published before real calls launch.
                  </p>
                </div>

                <div className="pt-2">
                  <Link
                    href="/methodology#privacy"
                    className="font-mono text-xs text-[#8B7CFF] hover:underline"
                  >
                    Read proposed privacy & methodology ↗
                  </Link>
                </div>

                {/* Consent Checkbox */}
                <div className="pt-4 border-t border-[#2B2B38] space-y-4">
                  <label className="flex items-start gap-3 cursor-pointer group">
                    <input
                      type="checkbox"
                      checked={hasConsented}
                      onChange={(e) => setHasConsented(e.target.checked)}
                      className="mt-1 h-5 w-5 rounded-[4px] border-[#2B2B38] bg-[#101014] text-[#B8FF4D] accent-[#B8FF4D] focus:ring-[#8B7CFF]"
                    />
                    <span className="text-xs sm:text-sm text-[#F5F5F5] group-hover:text-[#B8FF4D] transition-colors leading-relaxed">
                      I consent to a blind phone conversation and its recording for transcription, scoring and research under the proposed privacy terms.
                    </span>
                  </label>

                  <button
                    type="button"
                    disabled={!hasConsented}
                    onClick={() => setCurrentStep("setup")}
                    className={`flex h-12 w-full items-center justify-center rounded-[4px] px-6 font-mono text-xs font-bold uppercase tracking-wider transition-all ${
                      hasConsented
                        ? "bg-[#B8FF4D] text-[#101014] hover:bg-[#CDFF7A] shadow-[0_0_20px_rgba(184,255,77,0.3)]"
                        : "bg-[#14141A] text-[#71717A] border border-[#2B2B38] cursor-not-allowed"
                    }`}
                  >
                    Continue to call setup
                  </button>

                  <div className="text-[11px] font-mono text-[#71717A] text-center">
                    Consent is required to continue. You can leave now without starting a call.
                  </div>
                </div>
              </div>

              <div className="text-left">
                <Link
                  href="/"
                  className="font-mono text-xs text-[#A1A1AA] hover:text-[#F5F5F5]"
                >
                  ← Back to home
                </Link>
              </div>
            </div>
          </div>
        )}

        {/* ─────────────────────────────────────────────────────────────
            STEP 2: PHONE CONFIGURATION (EXACT TWO-COLUMN LAYOUT FROM PDF)
           ───────────────────────────────────────────────────────────── */}
        {currentStep === "setup" && (
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
            {/* Left Column: Heading & Context */}
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
                  Choose your language, enter your number and keep your phone nearby. We&apos;ll handle the mystery.
                </p>
              </div>

              <div className="inline-flex items-center gap-2 rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] px-3.5 py-1.5 font-mono text-xs text-[#8B7CFF]">
                <span>↙</span>
                <span>Consent recorded for this session</span>
              </div>

              <div className="rounded-[4px] border border-[#2B2B38] bg-[#14141A] p-6 space-y-2">
                <h4 className="text-base font-bold font-display text-[#F5F5F5]">
                  Answer on your phone.
                </h4>
                <p className="text-sm text-[#A1A1AA] leading-relaxed">
                  The conversation happens over a phone call. Leave this page open for call status and your result. No browser microphone access is needed.
                </p>
              </div>
            </div>

            {/* Right Column: Call Configuration Card */}
            <div className="lg:col-span-6 space-y-6">
              <form onSubmit={handlePhoneSubmit} className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7 space-y-6">
                <div className="font-mono text-xs uppercase tracking-wider text-[#71717A] border-b border-[#2B2B38] pb-3">
                  CALL CONFIGURATION / 02
                </div>

                {/* Language Selector */}
                <div>
                  <label className="block text-xs font-mono uppercase tracking-wider text-[#F5F5F5] mb-2 font-semibold">
                    Conversation language
                  </label>
                  <div className="grid grid-cols-2 gap-3">
                    <button
                      type="button"
                      onClick={() => setLanguage("Hindi")}
                      className={`h-12 rounded-[4px] border px-4 font-mono text-xs font-bold uppercase transition-all flex items-center justify-between ${
                        language === "Hindi"
                          ? "border-[#B8FF4D] bg-[#B8FF4D]/10 text-[#B8FF4D]"
                          : "border-[#2B2B38] bg-[#101014] text-[#A1A1AA]"
                      }`}
                    >
                      <span>Hindi {language === "Hindi" && "✓"}</span>
                      <span className="text-[10px] text-[#71717A]">NAMASTE</span>
                    </button>
                    <button
                      type="button"
                      onClick={() => setLanguage("English")}
                      className={`h-12 rounded-[4px] border px-4 font-mono text-xs font-bold uppercase transition-all flex items-center justify-between ${
                        language === "English"
                          ? "border-[#B8FF4D] bg-[#B8FF4D]/10 text-[#B8FF4D]"
                          : "border-[#2B2B38] bg-[#101014] text-[#A1A1AA]"
                      }`}
                    >
                      <span>English {language === "English" && "✓"}</span>
                      <span className="text-[10px] text-[#71717A]">HELLO</span>
                    </button>
                  </div>
                </div>

                {/* Phone Number Input */}
                <div>
                  <label className="block text-xs font-mono uppercase tracking-wider text-[#F5F5F5] mb-2 font-semibold">
                    Mobile phone number
                  </label>
                  <input
                    type="tel"
                    value={phoneNumber}
                    onChange={(e) => setPhoneNumber(e.target.value)}
                    className="block w-full rounded-[4px] border border-[#2B2B38] bg-[#101014] px-4 py-3 text-sm font-mono text-[#F5F5F5] focus:border-[#8B7CFF] focus:outline-none"
                  />
                  {phoneError ? (
                    <p className="mt-1 text-xs font-mono text-[#FF8C8C]">{phoneError}</p>
                  ) : (
                    <p className="mt-1 text-xs font-mono text-[#71717A]">
                      Example number. We&apos;ll call this phone, not your browser.
                    </p>
                  )}
                </div>

                {/* Notice Box: Before you answer */}
                <div className="rounded-[4px] border border-[#2B2B38] bg-[#101014] p-4 font-mono text-xs text-[#A1A1AA] space-y-1">
                  <div className="text-[#F5F5F5] font-bold mb-1">Before you answer</div>
                  <p>Use a quiet place. Don&apos;t share sensitive information. Your participant&apos;s identity will stay hidden until the call has ended.</p>
                </div>

                <div className="space-y-3 pt-2">
                  <button
                    type="submit"
                    className="flex h-13 w-full items-center justify-center rounded-[4px] bg-[#B8FF4D] font-mono text-xs font-bold uppercase tracking-wider text-[#101014] hover:bg-[#CDFF7A] shadow-[0_0_20px_rgba(184,255,77,0.3)]"
                  >
                    Call my phone ↗
                  </button>
                  <p className="text-[11px] font-mono text-[#71717A] text-center leading-relaxed">
                    This starts an incoming phone call to the number above. Your number will be masked on companion and result screens.
                  </p>
                </div>

                <div className="pt-2 border-t border-[#2B2B38] flex items-center justify-between">
                  <button
                    type="button"
                    onClick={() => setCurrentStep("consent")}
                    className="font-mono text-xs text-[#A1A1AA] hover:text-[#F5F5F5]"
                  >
                    ← Review consent & rules
                  </button>

                  <button
                    type="button"
                    onClick={() => {
                      setPhoneNumber("WEB-CALL");
                      setCurrentStep("call");
                    }}
                    className="font-mono text-xs text-[#8B7CFF] hover:underline"
                  >
                    Or Web Call Fallback ↗
                  </button>
                </div>
              </form>
            </div>
          </div>
        )}

        {/* ─────────────────────────────────────────────────────────────
            STEP 3: LIVE CONNECTED COMPANION (EXACT LAYOUT FROM PDF)
           ───────────────────────────────────────────────────────────── */}
        {currentStep === "call" && (
          <div className="space-y-8">
            <div className="flex items-center justify-between font-mono text-xs border-b border-[#2B2B38] pb-4">
              <span className="flex items-center gap-2 text-[#B8FF4D] font-bold">
                <span className="h-2.5 w-2.5 rounded-full bg-[#B8FF4D] animate-ping" />
                Connected on your phone {language === "Hindi" ? "HI" : "EN"}
              </span>
              <span className="text-[#8B7CFF]">{maskedPhone} · IDENTITY HIDDEN</span>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
              {/* Left Column: Heading, Giant Timer, Waveform */}
              <div className="lg:col-span-7 space-y-8">
                <div>
                  <h1 className="text-4xl sm:text-6xl font-bold font-display uppercase tracking-tight text-[#F5F5F5] leading-[0.95]">
                    Listen to the voice.
                    <br />
                    Trust your instinct.
                  </h1>
                </div>

                {/* Giant Timer */}
                <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-8 sm:p-12 text-center">
                  <div className="font-mono text-7xl sm:text-9xl font-bold tracking-tight text-[#F5F5F5]">
                    {formatTime(elapsedSeconds)}
                  </div>
                  <div className="mt-2 font-mono text-xs uppercase tracking-widest text-[#71717A]">
                    ELAPSED SINCE CONNECTION
                  </div>

                  <div className="mt-8">
                    <Waveform active={true} size="lg" className="w-full max-w-md mx-auto" />
                  </div>
                  <div className="mt-3 font-mono text-[11px] text-[#71717A]">
                    DECORATIVE SIGNAL · NOT LIVE AUDIO
                  </div>
                </div>

                <div className="font-mono text-xs text-[#71717A]">
                  Companion status only. The browser cannot hear or control this conversation.
                </div>
              </div>

              {/* Right Column: Special Move & Hangup Control */}
              <div className="lg:col-span-5 space-y-6">
                <div className="rounded-[4px] border border-[#8B7CFF] bg-[#1B1B23] p-7 space-y-4">
                  <div className="font-mono text-xs uppercase tracking-widest text-[#8B7CFF] font-bold">
                    YOUR SPECIAL MOVE
                  </div>
                  <h2 className="text-3xl sm:text-4xl font-bold font-display text-[#B8FF4D]">
                    &ldquo;Tum bot ho!&rdquo;
                  </h2>
                  <p className="text-sm text-[#A1A1AA] leading-relaxed">
                    Think you&apos;re speaking to AI? Say the phrase out loud during your phone call. No button to press here.
                  </p>
                </div>

                <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7 space-y-4">
                  <h3 className="text-lg font-bold font-display text-[#F5F5F5]">
                    Ready to finish? Hang up on your phone.
                  </h3>
                  <p className="text-sm text-[#A1A1AA] leading-relaxed">
                    Use your phone&apos;s normal end-call control. We&apos;ll show the identity here after the call ends. The website cannot end the call.
                  </p>
                  <p className="text-xs text-[#71717A] leading-relaxed border-t border-[#2B2B38] pt-3">
                    There&apos;s no live transcript on this page. Accusations are assessed after the conversation under the proposed scoring workflow.
                  </p>
                </div>

                <button
                  type="button"
                  onClick={() => {
                    setIsTimerRunning(false);
                    setCurrentStep("reveal");
                  }}
                  className="flex h-12 w-full items-center justify-center rounded-[4px] bg-[#B8FF4D] font-mono text-xs font-bold uppercase tracking-wider text-[#101014] hover:bg-[#CDFF7A]"
                >
                  Simulate Call End & Reveal ↗
                </button>
              </div>
            </div>
          </div>
        )}

        {/* ─────────────────────────────────────────────────────────────
            STEP 4: REVEAL SCREEN (EXACT LAYOUT FROM PDF)
           ───────────────────────────────────────────────────────────── */}
        {currentStep === "reveal" && (
          <div className="space-y-8">
            <div className="flex items-center justify-between font-mono text-xs border-b border-[#2B2B38] pb-4">
              <span className="text-[#A1A1AA]">Sample data · design preview</span>
              <span className="text-[#B8FF4D] font-bold uppercase tracking-wider">
                CALL ENDED / IDENTITY UNLOCKED
              </span>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
              {/* Left Column: Verdict Title & Outcomes */}
              <div className="lg:col-span-7 space-y-8">
                {revealOutcome === "ai_detected" && (
                  <div>
                    <h1 className="text-5xl sm:text-7xl font-bold font-display uppercase tracking-tight text-[#F5F5F5] leading-[0.92]">
                      That voice was
                      <br />
                      <span className="text-[#B8FF4D]">AI.</span>
                    </h1>
                    <h3 className="mt-4 text-xl font-bold font-display text-[#F5F5F5]">
                      You called it. Correct accusation.
                    </h3>
                    <p className="mt-2 text-base text-[#A1A1AA] leading-relaxed">
                      You said &ldquo;Tum bot ho!&rdquo; at 38 seconds. Your first valid accusation was recorded.
                    </p>
                  </div>
                )}

                {revealOutcome === "human_control" && (
                  <div>
                    <h1 className="text-5xl sm:text-7xl font-bold font-display uppercase tracking-tight text-[#FFB547] leading-[0.92]">
                      A human.
                      <br />
                      Plot twist.
                    </h1>
                    <h3 className="mt-4 text-xl font-bold font-display text-[#F5F5F5]">
                      You guessed AI. This was a false accusation.
                    </h3>
                    <p className="mt-2 text-base text-[#A1A1AA] leading-relaxed">
                      This was a false accusation against a human, not an AI detection. Language: English.
                    </p>
                  </div>
                )}

                {revealOutcome === "undetected" && (
                  <div>
                    <h1 className="text-5xl sm:text-7xl font-bold font-display uppercase tracking-tight text-[#8B7CFF] leading-[0.92]">
                      Not detected.
                    </h1>
                    <p className="mt-4 text-base text-[#A1A1AA] leading-relaxed">
                      No valid accusation was recorded. Observed for 84s, then right-censored. No detection time is assigned.
                    </p>
                  </div>
                )}

                <div className="flex flex-wrap items-center gap-4 pt-2">
                  <button
                    type="button"
                    onClick={() => {
                      setElapsedSeconds(42);
                      setCurrentStep("setup");
                    }}
                    className="inline-flex h-12 items-center justify-center rounded-[4px] bg-[#B8FF4D] px-7 font-mono text-xs font-bold uppercase tracking-wider text-[#101014] hover:bg-[#CDFF7A]"
                  >
                    Play Again ↗
                  </button>
                  <Link
                    href="/leaderboard"
                    className="inline-flex h-12 items-center justify-center rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] px-7 font-mono text-xs font-bold uppercase tracking-wider text-[#F5F5F5] hover:border-[#8B7CFF]"
                  >
                    View Leaderboard ↗
                  </Link>
                </div>

                {/* Alternate Outcomes selector from PDF */}
                <div className="pt-6 border-t border-[#2B2B38] space-y-3">
                  <span className="font-mono text-xs uppercase tracking-wider text-[#71717A] block font-semibold">
                    ALTERNATE OUTCOMES / SAMPLE RESULT STATES
                  </span>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    <button
                      type="button"
                      onClick={() => setRevealOutcome("human_control")}
                      className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-4 text-left hover:border-[#FFB547]"
                    >
                      <div className="text-xs font-mono text-[#FFB547] uppercase font-bold">CALL ENDED / HUMAN</div>
                      <div className="text-sm font-bold font-display text-[#F5F5F5] mt-1">A human. Plot twist.</div>
                      <div className="text-[11px] font-mono text-[#71717A] mt-1">A REAL PERSON. AN UNEXPECTED ANSWER.</div>
                    </button>

                    <button
                      type="button"
                      onClick={() => setRevealOutcome("undetected")}
                      className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-4 text-left hover:border-[#8B7CFF]"
                    >
                      <div className="text-xs font-mono text-[#8B7CFF] uppercase font-bold">CALL ENDED / AI</div>
                      <div className="text-sm font-bold font-display text-[#F5F5F5] mt-1">Not detected.</div>
                      <div className="text-[11px] font-mono text-[#71717A] mt-1">HINDI · ASTER / v1 · NILA · FICTIONAL</div>
                    </button>
                  </div>
                </div>
              </div>

              {/* Right Column: Turing Clock Metrics */}
              <div className="lg:col-span-5 space-y-6">
                <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7 space-y-5 font-mono text-xs">
                  <div>
                    <span className="text-[#71717A] uppercase tracking-wider block">THE TURING CLOCK / THIS CALL</span>
                    <div className="mt-1 text-5xl font-bold text-[#B8FF4D]">38s</div>
                    <div className="text-[11px] text-[#A1A1AA] mt-1">From connection to first valid accusation.</div>
                  </div>

                  <div className="grid grid-cols-2 gap-4 border-t border-[#2B2B38] pt-4">
                    <div>
                      <span className="text-[#71717A] uppercase block">LANGUAGE</span>
                      <div className="text-lg font-bold text-[#F5F5F5] mt-0.5">Hindi</div>
                    </div>
                    <div>
                      <span className="text-[#71717A] uppercase block">TOTAL DURATION</span>
                      <div className="text-lg font-bold text-[#F5F5F5] mt-0.5">84 seconds</div>
                    </div>
                  </div>

                  <div className="border-t border-[#2B2B38] pt-4">
                    <span className="text-[#71717A] uppercase block">MODEL / FICTIONAL PROVIDER</span>
                    <div className="text-sm font-bold text-[#8B7CFF] mt-0.5">Aster / v1 · Orchid Labs</div>
                  </div>

                  <div className="grid grid-cols-2 gap-4 border-t border-[#2B2B38] pt-4">
                    <div>
                      <span className="text-[#71717A] uppercase block">VOICE NAME</span>
                      <div className="text-sm font-bold text-[#F5F5F5] mt-0.5">Nila</div>
                    </div>
                    <div>
                      <span className="text-[#71717A] uppercase block">YOUR PHONE</span>
                      <div className="text-sm font-bold text-[#A1A1AA] mt-0.5">{maskedPhone}</div>
                    </div>
                  </div>

                  <div className="pt-2 border-t border-[#2B2B38]">
                    <Link href="/leaderboard/aster-v1" className="text-[#8B7CFF] hover:underline block text-center">
                      Explore this fictional model ↗
                    </Link>
                  </div>
                </div>
              </div>
            </div>

            {/* Bottom Full-Width Timeline Recap */}
            <div className="rounded-[4px] border border-[#2B2B38] bg-[#14141A] p-6 space-y-3 font-mono text-xs">
              <div className="flex items-center justify-between text-[#71717A]">
                <span className="uppercase font-bold">RECAP / NOT A TRANSCRIPT</span>
                <span>00:00 ──── 00:38 · ACCUSED ──── 01:24</span>
              </div>
              <div className="relative h-2 w-full rounded-full bg-[#1B1B23]">
                <div
                  className="absolute left-0 top-0 h-full rounded-full bg-[#B8FF4D]"
                  style={{ width: "45%" }}
                />
                <div
                  className="absolute top-1/2 h-4 w-4 -translate-y-1/2 rounded-full border-2 border-[#101014] bg-[#8B7CFF]"
                  style={{ left: "45%" }}
                />
              </div>
              <p className="text-[#A1A1AA]">
                Example giveaway: <strong className="text-[#B8FF4D]">unnatural pauses</strong>. Illustrative coded insight, not a live assessment of your speech.
              </p>
            </div>
          </div>
        )}
      </div>
    </main>
  );
}
