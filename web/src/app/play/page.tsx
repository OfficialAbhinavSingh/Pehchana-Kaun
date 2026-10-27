"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import Waveform from "@/components/Waveform";

type Step = "consent" | "setup" | "call" | "reveal";
type CallStatus = "connecting" | "ringing" | "connected" | "no_answer" | "error" | "scoring";
type RevealOutcome = "ai_detected" | "human_control" | "undetected";

export default function PlayPage() {
  const [currentStep, setCurrentStep] = useState<Step>("consent");

  // Step 1: Consent state
  const [hasConsented, setHasConsented] = useState<boolean>(false);

  // Step 2: Call config
  const [language, setLanguage] = useState<"Hindi" | "English">("Hindi");
  const [phoneNumber, setPhoneNumber] = useState<string>("");
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

  // Formatter for timer MM:SS
  const formatTime = (totalSeconds: number) => {
    const mins = Math.floor(totalSeconds / 60);
    const secs = totalSeconds % 60;
    return `${mins.toString().padStart(2, "0")}:${secs.toString().padStart(2, "0")}`;
  };

  // Mask phone number
  const maskedPhone =
    phoneNumber.length >= 10
      ? `+91 ••••• ••${phoneNumber.slice(-3)}`
      : "+91 ••••• ••210";

  // Validate phone input
  const handlePhoneSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const cleanNumber = phoneNumber.replace(/\D/g, "");
    if (cleanNumber.length < 10) {
      setPhoneError("Enter a valid 10-digit Indian mobile number.");
      return;
    }
    setPhoneError("");
    setElapsedSeconds(0);
    setCallStatus("connecting");
    setCurrentStep("call");

    // Simulate connection flow: connecting -> ringing -> connected
    setTimeout(() => {
      setCallStatus("ringing");
      setTimeout(() => {
        setCallStatus("connected");
        setIsTimerRunning(true);
      }, 2500);
    }, 2000);
  };

  return (
    <main className="min-h-screen bg-[#101014] text-[#F5F5F5] px-4 py-12 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-4xl">
        {/* ─────────────────────────────────────────────────────────────
            PROGRESS STEPPER INDICATOR
           ───────────────────────────────────────────────────────────── */}
        <div className="mb-10 border-b border-[#2B2B38] pb-6">
          <div className="flex items-center justify-between font-mono text-xs uppercase tracking-wider text-[#71717A]">
            <div className="flex items-center gap-2 sm:gap-6">
              <span
                className={`flex items-center gap-1.5 ${
                  currentStep === "consent" ? "text-[#B8FF4D] font-bold" : "text-[#A1A1AA]"
                }`}
              >
                <span className="rounded-full bg-[#1B1B23] px-1.5 py-0.5 border border-[#2B2B38]">
                  01
                </span>
                The rules
              </span>
              <span>→</span>
              <span
                className={`flex items-center gap-1.5 ${
                  currentStep === "setup" ? "text-[#B8FF4D] font-bold" : "text-[#A1A1AA]"
                }`}
              >
                <span className="rounded-full bg-[#1B1B23] px-1.5 py-0.5 border border-[#2B2B38]">
                  02
                </span>
                Your phone
              </span>
              <span>→</span>
              <span
                className={`flex items-center gap-1.5 ${
                  currentStep === "call" ? "text-[#B8FF4D] font-bold" : "text-[#A1A1AA]"
                }`}
              >
                <span className="rounded-full bg-[#1B1B23] px-1.5 py-0.5 border border-[#2B2B38]">
                  03
                </span>
                The call
              </span>
              <span>→</span>
              <span
                className={`flex items-center gap-1.5 ${
                  currentStep === "reveal" ? "text-[#B8FF4D] font-bold" : "text-[#A1A1AA]"
                }`}
              >
                <span className="rounded-full bg-[#1B1B23] px-1.5 py-0.5 border border-[#2B2B38]">
                  04
                </span>
                The reveal
              </span>
            </div>

            <span className="hidden sm:inline-block text-[#8B7CFF]">PHONE EXPERIMENT</span>
          </div>
        </div>

        {/* ─────────────────────────────────────────────────────────────
            STEP 1: THE RULES & CONSENT
           ───────────────────────────────────────────────────────────── */}
        {currentStep === "consent" && (
          <div className="space-y-8 animate-fadeIn">
            <div>
              <span className="font-mono text-xs uppercase tracking-widest text-[#8B7CFF]">
                First, a Fair Warning
              </span>
              <h1 className="mt-2 text-4xl sm:text-6xl font-bold font-display uppercase tracking-tight text-[#F5F5F5]">
                You won&apos;t know
                <br />
                who&apos;s talking.
              </h1>
              <p className="mt-4 text-base text-[#A1A1AA]">
                That&apos;s the whole point. Here&apos;s what you&apos;re agreeing to before we call.
              </p>
            </div>

            {/* 3 Guidance Points */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-5">
                <span className="font-mono text-xs text-[#8B7CFF]">01</span>
                <h3 className="mt-2 text-base font-bold font-display text-[#F5F5F5]">
                  A blind connection
                </h3>
                <p className="mt-2 text-xs text-[#A1A1AA] leading-relaxed">
                  You&apos;ll be randomly matched with a human or an AI. Their identity stays hidden until after the call.
                </p>
              </div>

              <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-5">
                <span className="font-mono text-xs text-[#B8FF4D]">02</span>
                <h3 className="mt-2 text-base font-bold font-display text-[#F5F5F5]">
                  60–90 seconds, typically
                </h3>
                <p className="mt-2 text-xs text-[#A1A1AA] leading-relaxed">
                  Speak naturally in Hindi or English. If you suspect AI, say the exact phrase &ldquo;Tum bot ho!&rdquo; on the phone.
                </p>
              </div>

              <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-5">
                <span className="font-mono text-xs text-[#8B7CFF]">03</span>
                <h3 className="mt-2 text-base font-bold font-display text-[#F5F5F5]">
                  Your phone is the game
                </h3>
                <p className="mt-2 text-xs text-[#A1A1AA] leading-relaxed">
                  The browser is only a companion. To finish, hang up on your phone. Then return here for the reveal.
                </p>
              </div>
            </div>

            {/* Privacy & Recording Policy Box */}
            <div className="rounded-[4px] border border-[#2B2B38] bg-[#14141A] p-6 space-y-4">
              <div className="flex items-center justify-between">
                <span className="font-mono text-xs uppercase tracking-widest text-[#FFB547]">
                  A voice is personal.
                </span>
                <span className="font-mono text-[10px] text-[#71717A] uppercase">
                  RECORDING & RESEARCH
                </span>
              </div>
              <p className="text-sm text-[#A1A1AA] leading-relaxed">
                The proposed experiment records your call. Audio may be transcribed to identify valid accusations, calculate timing, and study conversational giveaways.
              </p>
              <p className="text-xs text-[#71717A] leading-relaxed">
                Don&apos;t share financial, health, or other sensitive personal information. Your phone number is for call delivery; it will never appear in public results.
              </p>
              <div className="pt-2">
                <Link
                  href="/methodology#privacy"
                  className="font-mono text-xs text-[#8B7CFF] hover:underline"
                >
                  Read proposed privacy & methodology ↗
                </Link>
              </div>
            </div>

            {/* Consent Form */}
            <div className="space-y-6 pt-2">
              <label className="flex items-start gap-3 cursor-pointer group">
                <input
                  type="checkbox"
                  checked={hasConsented}
                  onChange={(e) => setHasConsented(e.target.checked)}
                  className="mt-1 h-5 w-5 rounded-[4px] border-[#2B2B38] bg-[#1B1B23] text-[#B8FF4D] accent-[#B8FF4D] focus:ring-[#8B7CFF]"
                />
                <span className="text-sm text-[#F5F5F5] group-hover:text-[#B8FF4D] transition-colors leading-relaxed">
                  I consent to a blind phone conversation and its recording for transcription, scoring, and research under the proposed privacy terms.
                </span>
              </label>

              <div className="flex flex-col sm:flex-row sm:items-center gap-4">
                <button
                  type="button"
                  disabled={!hasConsented}
                  onClick={() => setCurrentStep("setup")}
                  className={`inline-flex h-13 items-center justify-center rounded-[4px] px-8 font-mono text-xs font-bold uppercase tracking-wider transition-all ${
                    hasConsented
                      ? "bg-[#B8FF4D] text-[#101014] hover:bg-[#CDFF7A] hover:shadow-[0_0_20px_rgba(184,255,77,0.3)]"
                      : "bg-[#1B1B23] text-[#71717A] border border-[#2B2B38] cursor-not-allowed"
                  }`}
                >
                  Continue to call setup ↗
                </button>
                <span className="text-xs font-mono text-[#71717A]">
                  Consent is required to continue. You can leave now without starting a call.
                </span>
              </div>

              <div className="pt-4">
                <Link href="/" className="font-mono text-xs text-[#A1A1AA] hover:text-[#F5F5F5]">
                  ← Back to home
                </Link>
              </div>
            </div>
          </div>
        )}

        {/* ─────────────────────────────────────────────────────────────
            STEP 2: PHONE & LANGUAGE SETUP
           ───────────────────────────────────────────────────────────── */}
        {currentStep === "setup" && (
          <div className="space-y-8 animate-fadeIn">
            <div>
              <span className="font-mono text-xs uppercase tracking-widest text-[#B8FF4D]">
                One Voice. No Clues.
              </span>
              <h1 className="mt-2 text-4xl sm:text-6xl font-bold font-display uppercase tracking-tight text-[#F5F5F5]">
                Your next call
                <br />
                is a question.
              </h1>
              <p className="mt-4 text-base text-[#A1A1AA]">
                Choose your language, enter your number and keep your phone nearby. We&apos;ll handle the mystery.
              </p>
              <div className="mt-3 flex items-center gap-2 font-mono text-xs text-[#8B7CFF]">
                <span>✓</span>
                <span>Consent recorded for this session</span>
              </div>
            </div>

            <form onSubmit={handlePhoneSubmit} className="space-y-6">
              <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6 space-y-6">
                <div className="font-mono text-xs uppercase tracking-wider text-[#71717A]">
                  CALL CONFIGURATION / 02
                </div>

                {/* Language Selector */}
                <div>
                  <label className="block text-sm font-medium text-[#F5F5F5] mb-2 font-mono">
                    Conversation language
                  </label>
                  <div className="grid grid-cols-2 gap-3 max-w-sm">
                    <button
                      type="button"
                      onClick={() => setLanguage("Hindi")}
                      className={`h-12 rounded-[4px] border font-mono text-xs font-bold uppercase transition-all flex items-center justify-between px-4 ${
                        language === "Hindi"
                          ? "border-[#B8FF4D] bg-[#B8FF4D]/10 text-[#B8FF4D]"
                          : "border-[#2B2B38] bg-[#14141A] text-[#A1A1AA] hover:text-[#F5F5F5]"
                      }`}
                    >
                      <span>Hindi</span>
                      <span className="text-[10px] text-[#71717A]">NAMASTE</span>
                    </button>
                    <button
                      type="button"
                      onClick={() => setLanguage("English")}
                      className={`h-12 rounded-[4px] border font-mono text-xs font-bold uppercase transition-all flex items-center justify-between px-4 ${
                        language === "English"
                          ? "border-[#B8FF4D] bg-[#B8FF4D]/10 text-[#B8FF4D]"
                          : "border-[#2B2B38] bg-[#14141A] text-[#A1A1AA] hover:text-[#F5F5F5]"
                      }`}
                    >
                      <span>English</span>
                      <span className="text-[10px] text-[#71717A]">HELLO</span>
                    </button>
                  </div>
                </div>

                {/* Phone Number Input */}
                <div>
                  <label className="block text-sm font-medium text-[#F5F5F5] mb-2 font-mono">
                    Mobile phone number
                  </label>
                  <div className="flex max-w-sm">
                    <span className="inline-flex items-center px-4 rounded-l-[4px] border border-r-0 border-[#2B2B38] bg-[#14141A] text-[#A1A1AA] font-mono text-sm">
                      +91
                    </span>
                    <input
                      type="tel"
                      value={phoneNumber}
                      onChange={(e) => setPhoneNumber(e.target.value)}
                      placeholder="98765 43210"
                      className="block w-full rounded-r-[4px] border border-[#2B2B38] bg-[#101014] px-4 py-3 text-sm font-mono text-[#F5F5F5] placeholder-[#71717A] focus:border-[#8B7CFF] focus:outline-none focus:ring-1 focus:ring-[#8B7CFF]"
                    />
                  </div>
                  {phoneError ? (
                    <p className="mt-2 text-xs font-mono text-[#FF8C8C]">{phoneError}</p>
                  ) : (
                    <p className="mt-2 text-xs font-mono text-[#71717A]">
                      We&apos;ll call this phone, not your browser. Number will be masked on results.
                    </p>
                  )}
                </div>

                {/* Preparation notice */}
                <div className="rounded-[4px] border border-[#2B2B38] bg-[#101014] p-4 text-xs font-mono text-[#A1A1AA] space-y-1">
                  <div className="text-[#FFB547] font-bold uppercase mb-1">Before you answer</div>
                  <p>• Use a quiet place.</p>
                  <p>• Don&apos;t share sensitive personal details.</p>
                  <p>• Participant identity remains locked until call end.</p>
                </div>
              </div>

              {/* Action Buttons */}
              <div className="flex flex-col sm:flex-row sm:items-center gap-4">
                <button
                  type="submit"
                  className="inline-flex h-13 items-center justify-center rounded-[4px] bg-[#B8FF4D] px-8 font-mono text-xs font-bold uppercase tracking-wider text-[#101014] hover:bg-[#CDFF7A] hover:shadow-[0_0_20px_rgba(184,255,77,0.3)]"
                >
                  Call my phone ↗
                </button>

                {/* Browser Web-Call Fallback (WS3 Bolna feature) */}
                <button
                  type="button"
                  onClick={() => {
                    setPhoneNumber("WEB-CALL");
                    setElapsedSeconds(0);
                    setCallStatus("connected");
                    setIsTimerRunning(true);
                    setCurrentStep("call");
                  }}
                  className="inline-flex h-13 items-center justify-center rounded-[4px] border border-[#8B7CFF]/50 bg-[#1B1B23] px-6 font-mono text-xs font-bold uppercase tracking-wider text-[#8B7CFF] hover:bg-[#8B7CFF]/10"
                >
                  Or Test via Web Call (AI Arm) ↗
                </button>
              </div>

              <div className="pt-2">
                <button
                  type="button"
                  onClick={() => setCurrentStep("consent")}
                  className="font-mono text-xs text-[#A1A1AA] hover:text-[#F5F5F5]"
                >
                  ← Review consent & rules
                </button>
              </div>
            </form>
          </div>
        )}

        {/* ─────────────────────────────────────────────────────────────
            STEP 3: LIVE CALL COMPANION
           ───────────────────────────────────────────────────────────── */}
        {currentStep === "call" && (
          <div className="space-y-8 animate-fadeIn">
            {/* Header / Mode Indicator */}
            <div className="flex items-center justify-between border-b border-[#2B2B38] pb-4 font-mono text-xs">
              <span className="flex items-center gap-2 text-[#B8FF4D]">
                <span className="h-2.5 w-2.5 rounded-full bg-[#B8FF4D] animate-ping" />
                Connected on your phone · {language.toUpperCase()}
              </span>
              <span className="text-[#8B7CFF]">{maskedPhone} · IDENTITY HIDDEN</span>
            </div>

            {/* In-Call Active State */}
            {callStatus === "connected" && (
              <div className="space-y-8">
                <div>
                  <h1 className="text-4xl sm:text-6xl font-bold font-display uppercase tracking-tight text-[#F5F5F5]">
                    Listen to the voice.
                    <br />
                    Trust your instinct.
                  </h1>
                </div>

                {/* Giant Live Elapsed Timer & Waveform */}
                <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-8 sm:p-12 text-center relative overflow-hidden">
                  <div className="font-mono text-xs uppercase tracking-widest text-[#71717A] mb-2">
                    ELAPSED SINCE CONNECTION
                  </div>
                  <div className="font-mono text-6xl sm:text-8xl lg:text-9xl font-bold tracking-tight text-[#B8FF4D]">
                    {formatTime(elapsedSeconds)}
                  </div>

                  {/* Audio Waveform Signal */}
                  <div className="mt-8 flex justify-center">
                    <Waveform active={true} size="lg" className="w-full max-w-md py-4" />
                  </div>
                  <div className="mt-2 text-xs font-mono text-[#71717A]">
                    DECORATIVE SIGNAL · NOT LIVE AUDIO
                  </div>
                </div>

                {/* Call Instruction Spotlight: "Tum bot ho!" */}
                <div className="rounded-[4px] border border-[#8B7CFF] bg-[#14141A] p-6 sm:p-8">
                  <div className="font-mono text-xs uppercase tracking-widest text-[#8B7CFF]">
                    YOUR SPECIAL MOVE
                  </div>
                  <div className="mt-2 text-3xl sm:text-4xl font-bold font-display text-[#B8FF4D]">
                    &ldquo;Tum bot ho!&rdquo;
                  </div>
                  <p className="mt-3 text-sm text-[#A1A1AA] leading-relaxed">
                    Think you&apos;re speaking to AI? Say the phrase out loud during your phone call. No button to press here.
                  </p>
                </div>

                {/* Ending / Reveal Trigger */}
                <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                  <div>
                    <h4 className="text-base font-bold font-display text-[#F5F5F5]">
                      Ready to finish? Hang up on your phone.
                    </h4>
                    <p className="text-xs text-[#A1A1AA] mt-1">
                      Use your phone&apos;s normal end-call control. We&apos;ll show the identity here after the call ends.
                    </p>
                  </div>

                  {/* Test helper button to proceed to Reveal screen */}
                  <button
                    type="button"
                    onClick={() => {
                      setIsTimerRunning(false);
                      setCallStatus("scoring");
                      setTimeout(() => {
                        setCurrentStep("reveal");
                      }, 1800);
                    }}
                    className="inline-flex h-12 items-center justify-center rounded-[4px] bg-[#B8FF4D] px-6 font-mono text-xs font-bold uppercase tracking-wider text-[#101014] hover:bg-[#CDFF7A]"
                  >
                    Simulate Call End & Reveal ↗
                  </button>
                </div>

                <div className="text-center font-mono text-xs text-[#71717A]">
                  Companion status only. The browser cannot hear or control this conversation.
                </div>
              </div>
            )}

            {/* Connecting State Preview */}
            {callStatus === "connecting" && (
              <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-10 text-center space-y-4">
                <span className="font-mono text-xs text-[#8B7CFF] uppercase">CALL INITIATION / CONNECTING</span>
                <h2 className="text-3xl font-bold font-display text-[#F5F5F5]">Finding your mystery voice...</h2>
                <p className="text-sm text-[#A1A1AA] max-w-md mx-auto">
                  We&apos;re preparing your phone call. Keep this page open and your phone nearby. The participant&apos;s identity is hidden.
                </p>
                <div className="pt-4 flex justify-center">
                  <div className="h-8 w-8 animate-spin rounded-full border-2 border-[#8B7CFF] border-t-transparent" />
                </div>
              </div>
            )}

            {/* Ringing State Preview */}
            {callStatus === "ringing" && (
              <div className="rounded-[4px] border border-[#B8FF4D] bg-[#1B1B23] p-10 text-center space-y-4">
                <span className="font-mono text-xs text-[#B8FF4D] uppercase">CALL INITIATION / RINGING</span>
                <h2 className="text-3xl font-bold font-display text-[#F5F5F5]">Your phone is ringing!</h2>
                <p className="text-sm text-[#A1A1AA] max-w-md mx-auto">
                  Pick up. It&apos;s time. Answer the incoming call on your phone. Your companion will show the timer after connection.
                </p>
                <div className="pt-2 font-mono text-sm text-[#B8FF4D] animate-pulse">
                  Waiting for your answer...
                </div>
              </div>
            )}

            {/* Scoring State Preview */}
            {callStatus === "scoring" && (
              <div className="rounded-[4px] border border-[#8B7CFF] bg-[#1B1B23] p-10 text-center space-y-4">
                <span className="font-mono text-xs text-[#8B7CFF] uppercase">AFTER THE CALL / SCORING</span>
                <h2 className="text-3xl font-bold font-display text-[#F5F5F5]">The call is over. Hold that thought.</h2>
                <p className="text-sm text-[#A1A1AA] max-w-md mx-auto">
                  We&apos;re processing the post-call recording to verify accusation timing. Your reveal is on its way...
                </p>
                <div className="pt-4 flex justify-center">
                  <div className="h-8 w-8 animate-spin rounded-full border-2 border-[#B8FF4D] border-t-transparent" />
                </div>
              </div>
            )}

            {/* State Switcher Drawer (to inspect all Journey Companion states from PDF) */}
            <div className="border-t border-[#2B2B38] pt-6 font-mono text-xs text-[#71717A]">
              <span className="block mb-2 font-semibold uppercase text-[#A1A1AA]">
                STATIC STATE SIMULATOR (FROM DESIGN SPEC):
              </span>
              <div className="flex flex-wrap gap-2">
                <button
                  type="button"
                  onClick={() => setCallStatus("connecting")}
                  className="rounded px-2.5 py-1 bg-[#1B1B23] border border-[#2B2B38] text-[#A1A1AA] hover:text-[#F5F5F5]"
                >
                  Connecting
                </button>
                <button
                  type="button"
                  onClick={() => setCallStatus("ringing")}
                  className="rounded px-2.5 py-1 bg-[#1B1B23] border border-[#2B2B38] text-[#A1A1AA] hover:text-[#F5F5F5]"
                >
                  Ringing
                </button>
                <button
                  type="button"
                  onClick={() => {
                    setCallStatus("connected");
                    setIsTimerRunning(true);
                  }}
                  className="rounded px-2.5 py-1 bg-[#1B1B23] border border-[#2B2B38] text-[#B8FF4D]"
                >
                  Connected
                </button>
                <button
                  type="button"
                  onClick={() => setCallStatus("scoring")}
                  className="rounded px-2.5 py-1 bg-[#1B1B23] border border-[#2B2B38] text-[#8B7CFF]"
                >
                  Scoring
                </button>
              </div>
            </div>
          </div>
        )}

        {/* ─────────────────────────────────────────────────────────────
            STEP 4: THE REVEAL SCREEN
           ───────────────────────────────────────────────────────────── */}
        {currentStep === "reveal" && (
          <div className="space-y-8 animate-fadeIn">
            {/* Header Badge */}
            <div className="flex items-center justify-between border-b border-[#2B2B38] pb-4 font-mono text-xs">
              <span className="text-[#B8FF4D] font-bold">
                CALL ENDED / IDENTITY UNLOCKED
              </span>
              <span className="text-[#A1A1AA]">Sample data · design preview</span>
            </div>

            {/* Reveal Verdict Hero */}
            {revealOutcome === "ai_detected" && (
              <div className="space-y-4">
                <div className="font-mono text-xs uppercase tracking-widest text-[#B8FF4D]">
                  VERDICT: CORRECT ACCUSATION
                </div>
                <h1 className="text-5xl sm:text-7xl font-bold font-display uppercase tracking-tight text-[#B8FF4D]">
                  That voice was AI.
                </h1>
                <p className="text-lg text-[#F5F5F5]">
                  You called it. You said &ldquo;Tum bot ho!&rdquo; at 38 seconds. Your first valid accusation was recorded.
                </p>
              </div>
            )}

            {revealOutcome === "human_control" && (
              <div className="space-y-4">
                <div className="font-mono text-xs uppercase tracking-widest text-[#FFB547]">
                  VERDICT: HUMAN FALSE ACCUSATION
                </div>
                <h1 className="text-5xl sm:text-7xl font-bold font-display uppercase tracking-tight text-[#FFB547]">
                  A human. Plot twist.
                </h1>
                <p className="text-lg text-[#F5F5F5]">
                  You guessed AI. This was a false accusation against a human, not an AI detection.
                </p>
              </div>
            )}

            {revealOutcome === "undetected" && (
              <div className="space-y-4">
                <div className="font-mono text-xs uppercase tracking-widest text-[#8B7CFF]">
                  VERDICT: RIGHT-CENSORED (NOT DETECTED)
                </div>
                <h1 className="text-5xl sm:text-7xl font-bold font-display uppercase tracking-tight text-[#8B7CFF]">
                  Not detected.
                </h1>
                <p className="text-lg text-[#F5F5F5]">
                  No valid accusation was recorded. Observed for 84s, then right-censored. No detection time is assigned.
                </p>
              </div>
            )}

            {/* CTAs */}
            <div className="flex flex-wrap items-center gap-4 pt-2">
              <button
                type="button"
                onClick={() => {
                  setElapsedSeconds(0);
                  setCurrentStep("setup");
                }}
                className="inline-flex h-12 items-center justify-center rounded-[4px] bg-[#B8FF4D] px-6 font-mono text-xs font-bold uppercase tracking-wider text-[#101014] hover:bg-[#CDFF7A]"
              >
                Play Again ↗
              </button>
              <Link
                href="/leaderboard"
                className="inline-flex h-12 items-center justify-center rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] px-6 font-mono text-xs font-bold uppercase tracking-wider text-[#F5F5F5] hover:border-[#8B7CFF]"
              >
                View Leaderboard ↗
              </Link>
            </div>

            {/* Metric Summary Grid */}
            <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6 sm:p-8 grid grid-cols-2 sm:grid-cols-3 gap-6 font-mono text-xs">
              <div>
                <span className="text-[#71717A] uppercase">THE TURING CLOCK / THIS CALL</span>
                <div className="mt-1 text-3xl font-bold text-[#B8FF4D]">
                  {revealOutcome === "ai_detected" ? "38s" : "—"}
                </div>
                <div className="text-[10px] text-[#A1A1AA]">Connection to accusation</div>
              </div>

              <div>
                <span className="text-[#71717A] uppercase">LANGUAGE</span>
                <div className="mt-1 text-2xl font-bold text-[#F5F5F5]">{language}</div>
                <div className="text-[10px] text-[#A1A1AA]">Selected mode</div>
              </div>

              <div>
                <span className="text-[#71717A] uppercase">TOTAL DURATION</span>
                <div className="mt-1 text-2xl font-bold text-[#F5F5F5]">84s</div>
                <div className="text-[10px] text-[#A1A1AA]">Call connected time</div>
              </div>

              <div>
                <span className="text-[#71717A] uppercase">MODEL / PROVIDER</span>
                <div className="mt-1 text-base font-bold text-[#8B7CFF]">
                  {revealOutcome === "human_control" ? "Human Volunteer" : "Aster / v1 (Orchid Labs)"}
                </div>
                <div className="text-[10px] text-[#A1A1AA]">Voice Stack</div>
              </div>

              <div>
                <span className="text-[#71717A] uppercase">VOICE NAME</span>
                <div className="mt-1 text-base font-bold text-[#F5F5F5]">
                  {revealOutcome === "human_control" ? "Volunteer #04" : "Nila"}
                </div>
                <div className="text-[10px] text-[#A1A1AA]">Persona identifier</div>
              </div>

              <div>
                <span className="text-[#71717A] uppercase">YOUR PHONE</span>
                <div className="mt-1 text-base font-bold text-[#A1A1AA]">{maskedPhone}</div>
                <div className="text-[10px] text-[#71717A]">Masked per privacy</div>
              </div>
            </div>

            {/* Timeline Recap */}
            <div className="rounded-[4px] border border-[#2B2B38] bg-[#14141A] p-6 space-y-4">
              <div className="flex items-center justify-between font-mono text-xs">
                <span className="text-[#71717A] uppercase font-bold">RECAP / NOT A TRANSCRIPT</span>
                <span className="text-[#A1A1AA]">00:00 ─── 00:38 · ACCUSED ─── 01:24</span>
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
              <p className="text-xs font-mono text-[#A1A1AA]">
                Example giveaway: <strong className="text-[#B8FF4D]">unnatural pauses</strong>. Illustrative coded insight, not a live assessment of your speech.
              </p>
            </div>

            {/* Switch outcomes to preview in design review */}
            <div className="border-t border-[#2B2B38] pt-6 font-mono text-xs text-[#71717A]">
              <span className="block mb-2 font-semibold uppercase text-[#A1A1AA]">
                PREVIEW ALTERNATE OUTCOMES (FROM DESIGN SPEC):
              </span>
              <div className="flex flex-wrap gap-2">
                <button
                  type="button"
                  onClick={() => setRevealOutcome("ai_detected")}
                  className={`rounded px-3 py-1 border ${
                    revealOutcome === "ai_detected"
                      ? "border-[#B8FF4D] text-[#B8FF4D]"
                      : "border-[#2B2B38] text-[#A1A1AA]"
                  }`}
                >
                  AI Detected (38s)
                </button>
                <button
                  type="button"
                  onClick={() => setRevealOutcome("human_control")}
                  className={`rounded px-3 py-1 border ${
                    revealOutcome === "human_control"
                      ? "border-[#FFB547] text-[#FFB547]"
                      : "border-[#2B2B38] text-[#A1A1AA]"
                  }`}
                >
                  Human Plot Twist (False Accusation)
                </button>
                <button
                  type="button"
                  onClick={() => setRevealOutcome("undetected")}
                  className={`rounded px-3 py-1 border ${
                    revealOutcome === "undetected"
                      ? "border-[#8B7CFF] text-[#8B7CFF]"
                      : "border-[#2B2B38] text-[#A1A1AA]"
                  }`}
                >
                  Not Detected (Right-censored)
                </button>
              </div>
            </div>
          </div>
        )}
      </div>
    </main>
  );
}
