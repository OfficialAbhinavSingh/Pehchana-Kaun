"use client";

import React, { useEffect, useState } from "react";
import Link from "next/link";
import Waveform from "@/components/Waveform";
import { ArmStats, Leaderboard, getLeaderboard } from "@/lib/api";

function pct(n: number): string {
  return `${Math.round(n * 100)}%`;
}

function clock(s: number | null): string {
  if (s === null) return "—";
  const whole = Math.round(s);
  return `${Math.floor(whole / 60)}:${(whole % 60).toString().padStart(2, "0")}`;
}

export default function Home() {
  const [board, setBoard] = useState<Leaderboard | null>(null);

  useEffect(() => {
    getLeaderboard()
      .then(setBoard)
      .catch(() => setBoard(null));
  }, []);

  const aiArms: ArmStats[] = (board?.arms ?? []).filter((a) => a.kind === "ai");
  const rankedAi = aiArms.filter((a) => a.ranked);
  const human = board?.arms.find((a) => a.kind === "human");
  const aiCalls = aiArms.reduce((s, a) => s + a.n_calls, 0);
  const aiAccused = aiArms.reduce((s, a) => s + a.n_accused, 0);
  const bestArm = rankedAi[0];

  return (
    <main className="min-h-screen bg-[#f3f2f2] text-[#201e1d]">
      {/* ─────────────────────────────────────────────────────────────
          HERO SECTION
         ───────────────────────────────────────────────────────────── */}
      <section className="relative overflow-hidden border-b-2 border-[#201e1d] px-4 pt-14 pb-16 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          {/* Eyebrow badge */}
          <div className="inline-flex items-center gap-2 border-2 border-[#201e1d] bg-[#ffffff] px-3.5 py-1.5 font-mono text-[11px] uppercase tracking-widest text-[#605d5d]">
            <span className="h-2 w-2 bg-[#ec3013]" />
            <span>The Voice Identity Experiment</span>
            <span className="text-[#7d7979]">·</span>
            <span>Call or play in browser / Hindi + English / 60–90 Sec</span>
          </div>

          {/* Main Title & Hero Visual */}
          <div className="mt-8 grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            <div className="lg:col-span-8">
              <h1 className="text-5xl sm:text-7xl lg:text-8xl font-bold font-display uppercase tracking-tight leading-[0.92] text-[#201e1d]">
                Human or AI?
                <br />
                Think you
                <br />
                <span className="text-[#ec3013]">can tell?</span>
              </h1>

              <p className="mt-6 text-lg sm:text-xl text-[#605d5d] max-w-2xl leading-relaxed">
                One call. One mystery voice. Talk to a randomly assigned human or AI and trust your
                ears.
              </p>

              <div className="mt-8 flex flex-wrap items-center gap-4">
                <Link
                  href="/play"
                  className="inline-flex h-[52px] items-center justify-center bg-[#ec3013] px-8 font-mono text-sm font-bold uppercase tracking-wider text-[#f3f2f2] transition-all hover:bg-[#dd2b0f] hover:shadow-[6px_6px_0_#201e1d] active:translate-y-[1px]"
                >
                  Play the Game ↗
                </Link>
                <Link
                  href="/leaderboard"
                  className="inline-flex h-[52px] items-center justify-center border-2 border-[#201e1d] bg-[#ffffff] px-8 font-mono text-sm font-bold uppercase tracking-wider text-[#201e1d] transition-all hover:border-[#ae1800] hover:bg-[#fff2ef]"
                >
                  View Leaderboard ↗
                </Link>
              </div>
            </div>

            {/* Audio Waveform & Badge */}
            <div className="lg:col-span-4 flex justify-start lg:justify-end">
              <div className="w-full max-w-sm border-2 border-[#201e1d] bg-[#ffffff] p-6 shadow-2xl relative overflow-hidden">
                <div className="flex items-center justify-between mb-4">
                  <div className="flex items-center gap-2 font-mono text-xs text-[#ec3013]">
                    <span className="h-2.5 w-2.5 bg-[#ec3013] animate-pulse" />
                    <span>SIGNAL MONITOR</span>
                  </div>
                  <span className=" bg-[#ae1800]/20 px-2 py-0.5 font-mono text-xs font-bold text-[#ae1800]">
                    ?
                  </span>
                </div>

                <div className="py-4">
                  <Waveform active={true} size="md" />
                </div>

                <div className="mt-4 pt-3 border-t-2 border-[#201e1d] flex items-center justify-between text-[11px] font-mono text-[#7d7979]">
                  <span>48 kHz STEREO</span>
                  <span>DECORATIVE SIGNAL</span>
                </div>
              </div>
            </div>
          </div>

          {/* Two Identity Teaser Cards */}
          <div className="mt-12 grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className=" border-2 border-[#201e1d] bg-[#ffffff] p-6 sm:p-7 hover:border-[#ae1800] transition-colors">
              <div className="font-mono text-xs text-[#ae1800] uppercase font-bold tracking-wider mb-2">
                01 / HUMAN?
              </div>
              <h3 className="text-xl sm:text-2xl font-bold font-display text-[#201e1d]">
                Identity revealed only after the call
              </h3>
              <p className="mt-2 text-sm text-[#605d5d] leading-relaxed">
                Volunteers are on shift. You might be speaking to an ordinary person in India.
              </p>
            </div>

            <div className=" border-2 border-[#201e1d] bg-[#ffffff] p-6 sm:p-7 hover:border-[#ec3013] transition-colors">
              <div className="font-mono text-xs text-[#ec3013] uppercase font-bold tracking-wider mb-2">
                02 / AI?
              </div>
              <h3 className="text-xl sm:text-2xl font-bold font-display text-[#201e1d]">
                Think it&apos;s AI? Say &ldquo;Tum bot ho!&rdquo;
              </h3>
              <p className="mt-2 text-sm text-[#605d5d] leading-relaxed">
                Keep talking. Find out who it was when you hang up.
              </p>
            </div>
          </div>

          {/* Ticker / Banner Strip */}
          <div className="mt-8 border-2 border-[#201e1d] bg-[#fff2ef] px-5 py-3.5 flex flex-wrap items-center justify-between gap-4 font-mono text-xs uppercase tracking-wider text-[#605d5d]">
            <div className="flex items-center gap-2 text-[#201e1d] font-semibold">
              <span className="h-2 w-2 bg-[#ec3013]" />
              <span>CALL IN, OR PLAY IN YOUR BROWSER</span>
            </div>
            <div className="text-[#7d7979]">HIDDEN IDENTITY · HI / EN</div>
            <Link href="/methodology" className="text-[#ae1800] hover:underline">
              LESS SCROLLING. MORE SECOND GUESSING. ↗
            </Link>
          </div>
        </div>
      </section>

      {/* ─────────────────────────────────────────────────────────────
          SECTION 01: THE RULES ARE SIMPLE
         ───────────────────────────────────────────────────────────── */}
      <section id="rules" className="border-b-2 border-[#201e1d] px-4 py-20 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <div className="flex flex-col md:flex-row md:items-end justify-between gap-4 mb-12">
            <div>
              <span className="font-mono text-xs uppercase tracking-widest text-[#ae1800] font-semibold">
                01 / The Rules Are Simple
              </span>
              <h2 className="text-3xl sm:text-5xl font-bold font-display tracking-tight text-[#201e1d] mt-2">
                A conversation. Not an interrogation.
              </h2>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {/* Step 01 */}
            <div className=" border-2 border-[#201e1d] bg-[#ffffff] p-7 flex flex-col justify-between">
              <div>
                <span className="font-mono text-3xl font-bold text-[#ec3013]">01</span>
                <h3 className="mt-4 text-xl font-bold font-display text-[#201e1d] leading-snug">
                  Pick a language.
                  <br />
                  Call or play in browser.
                </h3>
                <p className="mt-3 text-sm text-[#605d5d] leading-relaxed">
                  Choose Hindi or English. Dial in if the number is live, or start the game from
                  this site with your browser&apos;s microphone.
                </p>
              </div>
              <div className="mt-6 pt-4 border-t-2 border-[#201e1d] text-[11px] font-mono text-[#7d7979]">
                YOU START THE CALL
              </div>
            </div>

            {/* Step 02 */}
            <div className=" border-2 border-[#201e1d] bg-[#ffffff] p-7 flex flex-col justify-between">
              <div>
                <span className="font-mono text-3xl font-bold text-[#ae1800]">02</span>
                <h3 className="mt-4 text-xl font-bold font-display text-[#201e1d] leading-snug">
                  Meet a voice.
                  <br />
                  Not an identity.
                </h3>
                <p className="mt-3 text-sm text-[#605d5d] leading-relaxed">
                  A human or an AI is randomly assigned. Chat naturally for a typical 60–90 seconds. Their identity stays hidden.
                </p>
              </div>
              <div className="mt-6 pt-4 border-t-2 border-[#201e1d] text-[11px] font-mono text-[#7d7979]">
                RANDOMIZED BLIND CONTROL
              </div>
            </div>

            {/* Step 03 */}
            <div className=" border-2 border-[#201e1d] bg-[#ffffff] p-7 flex flex-col justify-between">
              <div>
                <span className="font-mono text-3xl font-bold text-[#ec3013]">03</span>
                <h3 className="mt-4 text-xl font-bold font-display text-[#201e1d] leading-snug">
                  Make the call.
                  <br />
                  Then see the reveal.
                </h3>
                <p className="mt-3 text-sm text-[#605d5d] leading-relaxed">
                  If you suspect AI, say &ldquo;Tum bot ho!&rdquo; End the call to discover who you spoke to.
                </p>
              </div>
              <div className="mt-6 pt-4 border-t-2 border-[#201e1d] text-[11px] font-mono text-[#7d7979]">
                ACCUSATION VERIFICATION
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ─────────────────────────────────────────────────────────────
          SECTION 02: YOUR ONLY SPECIAL MOVE
         ───────────────────────────────────────────────────────────── */}
      <section className="border-b-2 border-[#201e1d] bg-[#fff2ef] px-4 py-20 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <div className=" border-2 border-[#ae1800]/50 bg-[#ffffff] p-8 sm:p-14 relative overflow-hidden">
            <span className="font-mono text-xs uppercase tracking-widest text-[#ec3013] font-bold">
              02 / Your Only Special Move
            </span>

            <div className="mt-4 flex flex-wrap items-baseline gap-4">
              <h2 className="text-4xl sm:text-6xl lg:text-7xl font-bold font-display text-[#ec3013]">
                &ldquo;Tum bot ho!&rdquo;
              </h2>
              <span className="font-mono text-xs uppercase tracking-wider text-[#605d5d]">
                TRANSLATION: &ldquo;YOU ARE A BOT!&rdquo;
              </span>
            </div>

            <div className="mt-8 max-w-3xl space-y-4">
              <h3 className="text-2xl sm:text-3xl font-bold font-display text-[#201e1d]">
                Suspicious? Say it out loud.
              </h3>

              <p className="text-base text-[#605d5d] leading-relaxed">
                Say the exact phrase during the call, in Hindi or English. Your first valid
                accusation starts the scoring story.
              </p>

              <p className="text-sm text-[#7d7979] leading-relaxed">
                The voice won&apos;t be unmasked mid-call. Your instinct gets a verdict only after you hang up.
              </p>
            </div>

            <div className="mt-10 flex flex-wrap items-center gap-6">
              <Link
                href="/play"
                className="inline-flex h-12 items-center justify-center bg-[#ec3013] px-7 font-mono text-xs font-bold uppercase tracking-wider text-[#f3f2f2] hover:bg-[#dd2b0f]"
              >
                Play the Game ↗
              </Link>
              <Link
                href="/methodology#accusations"
                className="font-mono text-xs uppercase tracking-wider text-[#ae1800] hover:underline"
              >
                Learn the rules ↗
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* ─────────────────────────────────────────────────────────────
          SECTION 03: INSTINCT, MEET EVIDENCE
         ───────────────────────────────────────────────────────────── */}
      <section className="border-b-2 border-[#201e1d] px-4 py-20 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4 mb-8">
            <div>
              <span className="font-mono text-xs uppercase tracking-widest text-[#ae1800] font-semibold">
                03 / Instinct, Meet Evidence
              </span>
              <h2 className="text-3xl sm:text-5xl font-bold font-display text-[#201e1d] mt-2">
                Every conversation asks a bigger question.
              </h2>
            </div>
            {board && (
              <span className=" border-2 border-[#201e1d] bg-[#ffffff] px-3.5 py-1.5 font-mono text-xs text-[#ec3013]">
                {board.includes_demo_data ? "Includes seeded demo data" : "Live results"}
              </span>
            )}
          </div>

          <p className="text-sm text-[#605d5d] max-w-2xl mb-8 leading-relaxed">
            What makes a voice feel human? Numbers below come straight from the public
            leaderboard, not a mockup.
          </p>

          {board && board.total_calls > 0 ? (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
              <div className=" border-2 border-[#201e1d] bg-[#ffffff] p-6">
                <span className="font-mono text-xs uppercase tracking-wider text-[#7d7979]">
                  TOTAL PHONE CALLS
                </span>
                <div className="mt-3 text-4xl sm:text-5xl font-bold font-mono text-[#201e1d]">
                  {board.total_calls}
                </div>
                <p className="mt-2 text-xs font-mono text-[#605d5d]">
                  {aiCalls} AI · {human?.n_calls ?? 0} human
                </p>
              </div>

              <div className=" border-2 border-[#201e1d] bg-[#ffffff] p-6">
                <span className="font-mono text-xs uppercase tracking-wider text-[#7d7979]">
                  AI ACCUSATION RATE
                </span>
                <div className="mt-3 text-4xl sm:text-5xl font-bold font-mono text-[#ec3013]">
                  {aiCalls > 0 ? pct(aiAccused / aiCalls) : "—"}
                </div>
                <p className="mt-2 text-xs font-mono text-[#605d5d]">
                  {aiAccused} of {aiCalls} AI calls
                </p>
              </div>

              <div className=" border-2 border-[#201e1d] bg-[#ffffff] p-6">
                <span className="font-mono text-xs uppercase tracking-wider text-[#7d7979]">
                  FASTEST MEDIAN TURING CLOCK¹
                </span>
                <div className="mt-3 text-4xl sm:text-5xl font-bold font-mono text-[#ae1800]">
                  {bestArm ? clock(bestArm.median_turing_clock_s) : "—"}
                </div>
                <p className="mt-2 text-xs font-mono text-[#605d5d]">
                  {bestArm ? bestArm.display_name : "no voice ranked yet"}
                </p>
              </div>

              <div className=" border-2 border-[#201e1d] bg-[#ffffff] p-6">
                <span className="font-mono text-xs uppercase tracking-wider text-[#7d7979]">
                  HUMAN FALSE ACCUSATIONS
                </span>
                <div className="mt-3 text-4xl sm:text-5xl font-bold font-mono text-[#a8520a]">
                  {human ? pct(human.accusation_rate) : "—"}
                </div>
                <p className="mt-2 text-xs font-mono text-[#605d5d]">
                  {human ? `${human.n_accused} of ${human.n_calls} human calls` : "no human calls yet"}
                </p>
              </div>
            </div>
          ) : (
            <div className=" border-2 border-[#201e1d] bg-[#ffffff] p-8 text-center font-mono text-sm text-[#605d5d]">
              Abhi shuru hua hai. Pehle callers mein se ek bano.
              <br />
              Just started. Be one of the first callers.
            </div>
          )}
        </div>
      </section>

      {/* ─────────────────────────────────────────────────────────────
          SECTION 04: THE PUBLIC SCOREBOARD
         ───────────────────────────────────────────────────────────── */}
      <section className="border-b-2 border-[#201e1d] px-4 py-20 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4 mb-6">
            <div>
              <span className="font-mono text-xs uppercase tracking-widest text-[#ec3013] font-semibold">
                04 / The Public Scoreboard
              </span>
              <h2 className="text-3xl sm:text-5xl font-bold font-display text-[#201e1d] mt-2">
                Which voices keep you guessing?
              </h2>
              <p className="mt-2 text-sm text-[#605d5d] max-w-2xl leading-relaxed">
                Compare accusation rates, detection times and the calls that ended without an accusation. A single rank can&apos;t tell the whole story.
              </p>
            </div>
            <Link
              href="/leaderboard"
              className="inline-flex h-11 items-center justify-center border-2 border-[#201e1d] bg-[#ffffff] px-6 font-mono text-xs font-bold uppercase tracking-wider text-[#201e1d] hover:border-[#ae1800]"
            >
              View Leaderboard ↗
            </Link>
          </div>

          <div className="flex items-center justify-between text-xs font-mono text-[#7d7979] mb-3">
            <span>VOICE NAMES ONLY · NO VENDOR NAMES</span>
            <span>LOWER ACCUSATION ≠ BETTER IN EVERY CONTEXT</span>
          </div>

          <div className="overflow-x-auto border-2 border-[#201e1d] bg-[#ffffff]">
            <table className="w-full text-left font-mono text-xs">
              <thead className="border-b-2 border-[#201e1d] bg-[#fff2ef] text-[#7d7979] uppercase tracking-wider">
                <tr>
                  <th className="py-4 px-6">Voice</th>
                  <th className="py-4 px-6">AI Calls</th>
                  <th className="py-4 px-6">Accused</th>
                  <th className="py-4 px-6">Clock¹</th>
                </tr>
              </thead>
              <tbody className="divide-y-2 divide-[#201e1d] text-[#201e1d]">
                {aiArms.length === 0 ? (
                  <tr>
                    <td className="py-4 px-6 text-[#7d7979]" colSpan={4}>
                      No AI calls yet. Be the first to play.
                    </td>
                  </tr>
                ) : (
                  aiArms.map((a) => (
                    <tr key={a.arm_id} className="hover:bg-[#fff2ef] transition-colors">
                      <td className="py-4 px-6">
                        <Link
                          href={`/leaderboard/${a.arm_id}`}
                          className="font-bold text-[#201e1d] hover:text-[#ec3013]"
                        >
                          {a.display_name} ↗
                        </Link>
                      </td>
                      <td className="py-4 px-6">{a.n_calls}</td>
                      <td className="py-4 px-6">
                        <span className="font-bold text-[#ec3013]">{pct(a.accusation_rate)}</span>
                        <span className="block text-[11px] text-[#605d5d]">
                          {a.n_accused} / {a.n_calls}
                        </span>
                      </td>
                      <td className="py-4 px-6 font-bold text-[#201e1d]">
                        {clock(a.median_turing_clock_s)}{" "}
                        <span className="text-[11px] font-normal text-[#7d7979] block">
                          detected only
                        </span>
                      </td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>

          <div className="mt-4 text-[11px] font-mono text-[#7d7979]">
            ¹ Median Turing Clock among detected AI calls only. Undetected calls are not 0s.
          </div>
        </div>
      </section>

      {/* ─────────────────────────────────────────────────────────────
          SECTION 05: A GAME WITH A RESEARCH QUESTION
         ───────────────────────────────────────────────────────────── */}
      <section className="border-b-2 border-[#201e1d] px-4 py-20 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <div className="max-w-3xl">
            <span className="font-mono text-xs uppercase tracking-widest text-[#ae1800] font-semibold">
              05 / A Game with a Research Question
            </span>
            <h2 className="text-3xl sm:text-5xl font-bold font-display text-[#201e1d] mt-2">
              How long can a voice stay a mystery?
            </h2>
            <div className="mt-6 space-y-4 text-base text-[#605d5d] leading-relaxed">
              <p>
                We call it the <strong className="text-[#201e1d]">Turing Clock</strong>: time from connection to your first valid &ldquo;Tum bot ho!&rdquo;
              </p>
              <p>
                Some calls end without detection. Those are right-censored observations, not zero-second detections. We report them separately and use a survival curve to show the fuller picture.
              </p>
              <p className="text-sm text-[#7d7979]">
                Random assignment helps keep identity hidden. It does not remove selection bias, differences between languages, or the limits of a short call.
              </p>
            </div>
            <div className="mt-8">
              <Link
                href="/methodology"
                className="font-mono text-xs uppercase tracking-wider text-[#ec3013] hover:underline"
              >
                Read the methodology ↗
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* ─────────────────────────────────────────────────────────────
          SECTION 06: BEFORE YOU PICK UP
         ───────────────────────────────────────────────────────────── */}
      <section className="border-b-2 border-[#201e1d] px-4 py-20 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <div className="max-w-3xl">
            <span className="font-mono text-xs uppercase tracking-widest text-[#a8520a] font-semibold">
              06 / Before You Pick Up
            </span>
            <h2 className="text-3xl sm:text-5xl font-bold font-display text-[#201e1d] mt-2">
              Your voice is personal.
              <br />
              Consent is essential.
            </h2>
            <div className="mt-6 space-y-4 text-base text-[#605d5d] leading-relaxed">
              <p>
                The call is recorded for transcription, accusation scoring and research. You&apos;ll
                hear the consent notice before anyone picks up, and you must stay on the line to
                agree.
              </p>
              <p className="text-sm text-[#7d7979]">
                We never keep your phone number: only a one-way hash, so repeat callers can be
                counted. Don&apos;t share sensitive personal information in a conversation.
              </p>
            </div>
            <div className="mt-8">
              <Link
                href="/methodology#privacy"
                className="font-mono text-xs uppercase tracking-wider text-[#ae1800] hover:underline"
              >
                Recording & privacy ↗
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* ─────────────────────────────────────────────────────────────
          SECTION 07: GOOD QUESTIONS
         ───────────────────────────────────────────────────────────── */}
      <section className="border-b-2 border-[#201e1d] px-4 py-20 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <div className="mb-12">
            <span className="font-mono text-xs uppercase tracking-widest text-[#ae1800] font-semibold">
              07 / Good Questions
            </span>
            <h2 className="text-3xl sm:text-5xl font-bold font-display text-[#201e1d] mt-2">
              A little less mystery about the game.
            </h2>
            <p className="text-sm font-mono text-[#605d5d] mt-2">
              The participant stays a mystery. The process shouldn&apos;t.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className=" border-2 border-[#201e1d] bg-[#ffffff] p-7">
              <h3 className="text-lg font-bold font-display text-[#201e1d]">
                Do I need my browser microphone?
              </h3>
              <p className="mt-3 text-sm text-[#605d5d] leading-relaxed">
                Only if you play in browser. Calling the game&apos;s number uses your phone, and this
                site never listens through your browser in that mode. Playing in browser uses your
                browser&apos;s microphone for the call itself.
              </p>
            </div>

            <div className=" border-2 border-[#201e1d] bg-[#ffffff] p-7">
              <h3 className="text-lg font-bold font-display text-[#201e1d]">
                Can I play in Hindi or English?
              </h3>
              <p className="mt-3 text-sm text-[#605d5d] leading-relaxed">
                Yes. Choose one language before the call. In either mode, use the exact accusation phrase &ldquo;Tum bot ho!&rdquo; if you think you&apos;re talking to AI.
              </p>
            </div>

            <div className=" border-2 border-[#201e1d] bg-[#ffffff] p-7">
              <h3 className="text-lg font-bold font-display text-[#201e1d]">
                What if I accuse a human?
              </h3>
              <p className="mt-3 text-sm text-[#605d5d] leading-relaxed">
                A recorded accusation against a human counts as a false accusation, not an AI
                detection. Overall results are on the leaderboard for everyone.
              </p>
            </div>

            <div className=" border-2 border-[#201e1d] bg-[#ffffff] p-7">
              <h3 className="text-lg font-bold font-display text-[#201e1d]">
                Are the leaderboard numbers real?
              </h3>
              <p className="mt-3 text-sm text-[#605d5d] leading-relaxed">
                Yes, read live from <code className="text-[#ae1800]">GET /leaderboard</code>. Vendor
                names are hidden unless explicitly revealed; voices are labeled Voice A/B/C. A demo
                banner shows if seeded demo data is ever mixed in.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* ─────────────────────────────────────────────────────────────
          SECTION 08: YOUR EARS. YOUR INSTINCT.
         ───────────────────────────────────────────────────────────── */}
      <section className="bg-[#ec3013] text-[#f3f2f2] px-4 py-20 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl flex flex-col md:flex-row md:items-end justify-between gap-8">
          <div>
            <span className="font-mono text-xs uppercase tracking-widest text-[#f3f2f2]/70 font-bold">
              08 / Your Ears. Your Instinct.
            </span>
            <h2 className="text-4xl sm:text-6xl lg:text-7xl font-bold font-display uppercase tracking-tight leading-[0.92] mt-2">
              Don&apos;t guess from here.
              <br />
              Pick up.
            </h2>
            <p className="mt-4 text-base sm:text-lg text-[#f3f2f2]/80 max-w-xl font-medium">
              A human or an AI is waiting on the other side. You won&apos;t know which until it&apos;s over.
            </p>
          </div>

          <div className="flex flex-col items-start md:items-end gap-3">
            <Link
              href="/play"
              className="inline-flex h-14 items-center justify-center bg-[#f3f2f2] px-9 font-mono text-sm font-bold uppercase tracking-wider text-[#201e1d] transition-all hover:bg-[#fff2ef] active:translate-y-[1px]"
            >
              Play the Game ↗
            </Link>
            <span className="font-mono text-[11px] uppercase tracking-wider text-[#f3f2f2]/70 font-semibold">
              CALL OR BROWSER · HINDI / ENGLISH · CONSENT FIRST
            </span>
          </div>
        </div>
      </section>
    </main>
  );
}
