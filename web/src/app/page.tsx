import React from "react";
import Link from "next/link";
import Waveform from "@/components/Waveform";

export default function Home() {
  return (
    <main className="min-h-screen bg-[#101014] text-[#F5F5F5]">
      {/* ─────────────────────────────────────────────────────────────
          HERO SECTION
         ───────────────────────────────────────────────────────────── */}
      <section className="relative overflow-hidden border-b border-[#2B2B38] px-4 pt-14 pb-16 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          {/* Eyebrow badge */}
          <div className="inline-flex items-center gap-2 rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] px-3.5 py-1.5 font-mono text-[11px] uppercase tracking-widest text-[#A1A1AA]">
            <span className="h-2 w-2 rounded-full bg-[#B8FF4D]" />
            <span>The Voice Identity Experiment</span>
            <span className="text-[#71717A]">·</span>
            <span>Phone Only / Hindi + English / 60–90 Sec</span>
          </div>

          {/* Main Title & Hero Visual */}
          <div className="mt-8 grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            <div className="lg:col-span-8">
              <h1 className="text-5xl sm:text-7xl lg:text-8xl font-bold font-display uppercase tracking-tight leading-[0.92] text-[#F5F5F5]">
                Human or AI?
                <br />
                Think you
                <br />
                <span className="text-[#B8FF4D]">can tell?</span>
              </h1>

              <p className="mt-6 text-lg sm:text-xl text-[#A1A1AA] max-w-2xl leading-relaxed">
                One phone call. One mystery voice. Talk to a randomly assigned human or AI and trust your ears.
              </p>

              <div className="mt-8 flex flex-wrap items-center gap-4">
                <Link
                  href="/play"
                  className="inline-flex h-[52px] items-center justify-center rounded-[4px] bg-[#B8FF4D] px-8 font-mono text-sm font-bold uppercase tracking-wider text-[#101014] transition-all hover:bg-[#CDFF7A] hover:shadow-[0_0_24px_rgba(184,255,77,0.4)] active:translate-y-[1px]"
                >
                  Play the Game ↗
                </Link>
                <Link
                  href="/leaderboard"
                  className="inline-flex h-[52px] items-center justify-center rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] px-8 font-mono text-sm font-bold uppercase tracking-wider text-[#F5F5F5] transition-all hover:border-[#8B7CFF] hover:bg-[#22222D]"
                >
                  View Leaderboard ↗
                </Link>
              </div>
            </div>

            {/* Audio Waveform & Badge */}
            <div className="lg:col-span-4 flex justify-start lg:justify-end">
              <div className="w-full max-w-sm rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6 shadow-2xl relative overflow-hidden">
                <div className="flex items-center justify-between mb-4">
                  <div className="flex items-center gap-2 font-mono text-xs text-[#B8FF4D]">
                    <span className="h-2.5 w-2.5 rounded-full bg-[#B8FF4D] animate-pulse" />
                    <span>SIGNAL MONITOR</span>
                  </div>
                  <span className="rounded-[4px] bg-[#8B7CFF]/20 px-2 py-0.5 font-mono text-xs font-bold text-[#8B7CFF]">
                    ?
                  </span>
                </div>

                <div className="py-4">
                  <Waveform active={true} size="md" />
                </div>

                <div className="mt-4 pt-3 border-t border-[#2B2B38] flex items-center justify-between text-[11px] font-mono text-[#71717A]">
                  <span>48 kHz STEREO</span>
                  <span>DECORATIVE SIGNAL</span>
                </div>
              </div>
            </div>
          </div>

          {/* Two Identity Teaser Cards */}
          <div className="mt-12 grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6 sm:p-7 hover:border-[#8B7CFF] transition-colors">
              <div className="font-mono text-xs text-[#8B7CFF] uppercase font-bold tracking-wider mb-2">
                01 / HUMAN?
              </div>
              <h3 className="text-xl sm:text-2xl font-bold font-display text-[#F5F5F5]">
                Identity revealed only after the call
              </h3>
              <p className="mt-2 text-sm text-[#A1A1AA] leading-relaxed">
                Volunteers are on shift. You might be speaking to an ordinary person in India.
              </p>
            </div>

            <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6 sm:p-7 hover:border-[#B8FF4D] transition-colors">
              <div className="font-mono text-xs text-[#B8FF4D] uppercase font-bold tracking-wider mb-2">
                02 / AI?
              </div>
              <h3 className="text-xl sm:text-2xl font-bold font-display text-[#F5F5F5]">
                Think it’s AI? Say &ldquo;Tum bot ho!&rdquo; on your phone.
              </h3>
              <p className="mt-2 text-sm text-[#A1A1AA] leading-relaxed">
                Keep talking. Find out who it was when you hang up.
              </p>
            </div>
          </div>

          {/* Ticker / Banner Strip */}
          <div className="mt-8 rounded-[4px] border border-[#2B2B38] bg-[#14141A] px-5 py-3.5 flex flex-wrap items-center justify-between gap-4 font-mono text-xs uppercase tracking-wider text-[#A1A1AA]">
            <div className="flex items-center gap-2 text-[#F5F5F5] font-semibold">
              <span className="h-2 w-2 rounded-full bg-[#B8FF4D]" />
              <span>NO BROWSER MIC. JUST YOUR PHONE.</span>
            </div>
            <div className="text-[#71717A]">REAL PHONE CALLS · HIDDEN IDENTITY · HI / EN</div>
            <Link href="/methodology" className="text-[#8B7CFF] hover:underline">
              LESS SCROLLING. MORE SECOND GUESSING. ↗
            </Link>
          </div>
        </div>
      </section>

      {/* ─────────────────────────────────────────────────────────────
          SECTION 01: THE RULES ARE SIMPLE
         ───────────────────────────────────────────────────────────── */}
      <section id="rules" className="border-b border-[#2B2B38] px-4 py-20 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <div className="flex flex-col md:flex-row md:items-end justify-between gap-4 mb-12">
            <div>
              <span className="font-mono text-xs uppercase tracking-widest text-[#8B7CFF] font-semibold">
                01 / The Rules Are Simple
              </span>
              <h2 className="text-3xl sm:text-5xl font-bold font-display tracking-tight text-[#F5F5F5] mt-2">
                A conversation. Not an interrogation.
              </h2>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {/* Step 01 */}
            <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7 flex flex-col justify-between">
              <div>
                <span className="font-mono text-3xl font-bold text-[#B8FF4D]">01</span>
                <h3 className="mt-4 text-xl font-bold font-display text-[#F5F5F5] leading-snug">
                  Pick a language.
                  <br />
                  Answer your phone.
                </h3>
                <p className="mt-3 text-sm text-[#A1A1AA] leading-relaxed">
                  Choose Hindi or English and enter your number. We&apos;ll call your phone to start the experiment.
                </p>
              </div>
              <div className="mt-6 pt-4 border-t border-[#2B2B38] text-[11px] font-mono text-[#71717A]">
                PHONE-FIRST ARCHITECTURE
              </div>
            </div>

            {/* Step 02 */}
            <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7 flex flex-col justify-between">
              <div>
                <span className="font-mono text-3xl font-bold text-[#8B7CFF]">02</span>
                <h3 className="mt-4 text-xl font-bold font-display text-[#F5F5F5] leading-snug">
                  Meet a voice.
                  <br />
                  Not an identity.
                </h3>
                <p className="mt-3 text-sm text-[#A1A1AA] leading-relaxed">
                  A human or an AI is randomly assigned. Chat naturally for a typical 60–90 seconds. Their identity stays hidden.
                </p>
              </div>
              <div className="mt-6 pt-4 border-t border-[#2B2B38] text-[11px] font-mono text-[#71717A]">
                RANDOMIZED BLIND CONTROL
              </div>
            </div>

            {/* Step 03 */}
            <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7 flex flex-col justify-between">
              <div>
                <span className="font-mono text-3xl font-bold text-[#B8FF4D]">03</span>
                <h3 className="mt-4 text-xl font-bold font-display text-[#F5F5F5] leading-snug">
                  Make the call.
                  <br />
                  Then see the reveal.
                </h3>
                <p className="mt-3 text-sm text-[#A1A1AA] leading-relaxed">
                  If you suspect AI, say &ldquo;Tum bot ho!&rdquo; End the call on your phone to discover who you spoke to.
                </p>
              </div>
              <div className="mt-6 pt-4 border-t border-[#2B2B38] text-[11px] font-mono text-[#71717A]">
                ACCUSATION VERIFICATION
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ─────────────────────────────────────────────────────────────
          SECTION 02: YOUR ONLY SPECIAL MOVE
         ───────────────────────────────────────────────────────────── */}
      <section className="border-b border-[#2B2B38] bg-[#14141A] px-4 py-20 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <div className="rounded-[4px] border border-[#8B7CFF]/50 bg-[#1B1B23] p-8 sm:p-14 relative overflow-hidden">
            <span className="font-mono text-xs uppercase tracking-widest text-[#B8FF4D] font-bold">
              02 / Your Only Special Move
            </span>

            <div className="mt-4 flex flex-wrap items-baseline gap-4">
              <h2 className="text-4xl sm:text-6xl lg:text-7xl font-bold font-display text-[#B8FF4D]">
                &ldquo;Tum bot ho!&rdquo;
              </h2>
              <span className="font-mono text-xs uppercase tracking-wider text-[#A1A1AA]">
                TRANSLATION: &ldquo;YOU ARE A BOT!&rdquo;
              </span>
            </div>

            <div className="mt-8 max-w-3xl space-y-4">
              <h3 className="text-2xl sm:text-3xl font-bold font-display text-[#F5F5F5]">
                Suspicious? Say it out loud.
              </h3>

              <p className="text-base text-[#A1A1AA] leading-relaxed">
                Say the exact phrase during your phone call in Hindi or English mode. Your first valid accusation starts the scoring story. The website doesn&apos;t listen through your browser.
              </p>

              <p className="text-sm text-[#71717A] leading-relaxed">
                The voice won&apos;t be unmasked mid-call. Your instinct gets a verdict only after you hang up.
              </p>
            </div>

            <div className="mt-10 flex flex-wrap items-center gap-6">
              <Link
                href="/play"
                className="inline-flex h-12 items-center justify-center rounded-[4px] bg-[#B8FF4D] px-7 font-mono text-xs font-bold uppercase tracking-wider text-[#101014] hover:bg-[#CDFF7A]"
              >
                Play the Game ↗
              </Link>
              <Link
                href="/methodology#accusations"
                className="font-mono text-xs uppercase tracking-wider text-[#8B7CFF] hover:underline"
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
      <section className="border-b border-[#2B2B38] px-4 py-20 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4 mb-8">
            <div>
              <span className="font-mono text-xs uppercase tracking-widest text-[#8B7CFF] font-semibold">
                03 / Instinct, Meet Evidence
              </span>
              <h2 className="text-3xl sm:text-5xl font-bold font-display text-[#F5F5F5] mt-2">
                Every conversation asks a bigger question.
              </h2>
            </div>
            <span className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] px-3.5 py-1.5 font-mono text-xs text-[#B8FF4D]">
              Sample data · design preview
            </span>
          </div>

          <p className="text-sm text-[#A1A1AA] max-w-2xl mb-8 leading-relaxed">
            What makes a voice feel human? This is a preview of how the public experiment will report results — not live performance.
          </p>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            {/* Metric 1 */}
            <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6">
              <span className="font-mono text-xs uppercase tracking-wider text-[#71717A]">
                TOTAL PHONE CALLS
              </span>
              <div className="mt-3 text-4xl sm:text-5xl font-bold font-mono text-[#F5F5F5]">
                1,200
              </div>
              <p className="mt-2 text-xs font-mono text-[#A1A1AA]">
                900 AI · 300 human
              </p>
            </div>

            {/* Metric 2 */}
            <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6">
              <span className="font-mono text-xs uppercase tracking-wider text-[#71717A]">
                AI ACCUSATION RATE
              </span>
              <div className="mt-3 text-4xl sm:text-5xl font-bold font-mono text-[#B8FF4D]">
                60%
              </div>
              <p className="mt-2 text-xs font-mono text-[#A1A1AA]">
                540 of 900 AI calls
              </p>
            </div>

            {/* Metric 3 */}
            <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6">
              <span className="font-mono text-xs uppercase tracking-wider text-[#71717A]">
                MEDIAN TURING CLOCK¹
              </span>
              <div className="mt-3 text-4xl sm:text-5xl font-bold font-mono text-[#8B7CFF]">
                32s
              </div>
              <p className="mt-2 text-xs font-mono text-[#A1A1AA]">
                Among 540 detected AI calls only
              </p>
            </div>

            {/* Metric 4 */}
            <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6">
              <span className="font-mono text-xs uppercase tracking-wider text-[#71717A]">
                HUMAN FALSE ACCUSATIONS
              </span>
              <div className="mt-3 text-4xl sm:text-5xl font-bold font-mono text-[#FFB547]">
                15%
              </div>
              <p className="mt-2 text-xs font-mono text-[#A1A1AA]">
                45 of 300 human calls
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* ─────────────────────────────────────────────────────────────
          SECTION 04: THE PUBLIC SCOREBOARD
         ───────────────────────────────────────────────────────────── */}
      <section className="border-b border-[#2B2B38] px-4 py-20 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4 mb-6">
            <div>
              <span className="font-mono text-xs uppercase tracking-widest text-[#B8FF4D] font-semibold">
                04 / The Public Scoreboard
              </span>
              <h2 className="text-3xl sm:text-5xl font-bold font-display text-[#F5F5F5] mt-2">
                Which voices keep you guessing?
              </h2>
              <p className="mt-2 text-sm text-[#A1A1AA] max-w-2xl leading-relaxed">
                Compare accusation rates, detection times and the calls that ended without an accusation. A single rank can&apos;t tell the whole story.
              </p>
            </div>
            <Link
              href="/leaderboard"
              className="inline-flex h-11 items-center justify-center rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] px-6 font-mono text-xs font-bold uppercase tracking-wider text-[#F5F5F5] hover:border-[#8B7CFF]"
            >
              View Leaderboard ↗
            </Link>
          </div>

          <div className="flex items-center justify-between text-xs font-mono text-[#71717A] mb-3">
            <span>SAMPLE DATA · DESIGN PREVIEW</span>
            <span>FICTIONAL PROVIDERS / LOWER ACCUSATION ≠ BETTER IN EVERY CONTEXT</span>
          </div>

          <div className="overflow-x-auto rounded-[4px] border border-[#2B2B38] bg-[#1B1B23]">
            <table className="w-full text-left font-mono text-xs">
              <thead className="border-b border-[#2B2B38] bg-[#14141A] text-[#71717A] uppercase tracking-wider">
                <tr>
                  <th className="py-4 px-6">Model / Provider</th>
                  <th className="py-4 px-6">AI Calls</th>
                  <th className="py-4 px-6">Accused</th>
                  <th className="py-4 px-6">Clock¹</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-[#2B2B38] text-[#F5F5F5]">
                {/* Aster */}
                <tr className="hover:bg-[#22222D] transition-colors">
                  <td className="py-4 px-6">
                    <Link href="/leaderboard/aster-v1" className="font-bold text-[#F5F5F5] hover:text-[#B8FF4D]">
                      Aster / v1 ↗
                    </Link>
                    <span className="block text-[11px] text-[#A1A1AA]">Orchid Labs</span>
                  </td>
                  <td className="py-4 px-6">300</td>
                  <td className="py-4 px-6">
                    <span className="font-bold text-[#B8FF4D]">50%</span>
                    <span className="block text-[11px] text-[#A1A1AA]">150 / 300</span>
                  </td>
                  <td className="py-4 px-6 font-bold text-[#F5F5F5]">
                    38s <span className="text-[11px] font-normal text-[#71717A] block">detected only</span>
                  </td>
                </tr>

                {/* Echo */}
                <tr className="hover:bg-[#22222D] transition-colors">
                  <td className="py-4 px-6">
                    <Link href="/leaderboard" className="font-bold text-[#F5F5F5] hover:text-[#B8FF4D]">
                      Echo / v2 ↗
                    </Link>
                    <span className="block text-[11px] text-[#A1A1AA]">Fable Audio</span>
                  </td>
                  <td className="py-4 px-6">300</td>
                  <td className="py-4 px-6">
                    <span className="font-bold text-[#B8FF4D]">60%</span>
                    <span className="block text-[11px] text-[#A1A1AA]">180 / 300</span>
                  </td>
                  <td className="py-4 px-6 font-bold text-[#F5F5F5]">
                    32s <span className="text-[11px] font-normal text-[#71717A] block">detected only</span>
                  </td>
                </tr>

                {/* Mica */}
                <tr className="hover:bg-[#22222D] transition-colors">
                  <td className="py-4 px-6">
                    <Link href="/leaderboard" className="font-bold text-[#F5F5F5] hover:text-[#B8FF4D]">
                      Mica / v1 ↗
                    </Link>
                    <span className="block text-[11px] text-[#A1A1AA]">Loom Voice</span>
                  </td>
                  <td className="py-4 px-6">300</td>
                  <td className="py-4 px-6">
                    <span className="font-bold text-[#B8FF4D]">70%</span>
                    <span className="block text-[11px] text-[#A1A1AA]">210 / 300</span>
                  </td>
                  <td className="py-4 px-6 font-bold text-[#F5F5F5]">
                    26s <span className="text-[11px] font-normal text-[#71717A] block">detected only</span>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <div className="mt-4 text-[11px] font-mono text-[#71717A]">
            ¹ Median Turing Clock among detected AI calls only. Undetected calls are not 0s. All models and providers are fictional.
          </div>
        </div>
      </section>

      {/* ─────────────────────────────────────────────────────────────
          SECTION 05: A GAME WITH A RESEARCH QUESTION
         ───────────────────────────────────────────────────────────── */}
      <section className="border-b border-[#2B2B38] px-4 py-20 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <div className="max-w-3xl">
            <span className="font-mono text-xs uppercase tracking-widest text-[#8B7CFF] font-semibold">
              05 / A Game with a Research Question
            </span>
            <h2 className="text-3xl sm:text-5xl font-bold font-display text-[#F5F5F5] mt-2">
              How long can a voice stay a mystery?
            </h2>
            <div className="mt-6 space-y-4 text-base text-[#A1A1AA] leading-relaxed">
              <p>
                We call it the <strong className="text-[#F5F5F5]">Turing Clock</strong>: time from connection to your first valid &ldquo;Tum bot ho!&rdquo;
              </p>
              <p>
                Some calls end without detection. Those are right-censored observations, not zero-second detections. We report them separately and use a survival curve to show the fuller picture.
              </p>
              <p className="text-sm text-[#71717A]">
                Random assignment helps keep identity hidden. It does not remove selection bias, differences between languages, or the limits of a short phone call.
              </p>
            </div>
            <div className="mt-8">
              <Link
                href="/methodology"
                className="font-mono text-xs uppercase tracking-wider text-[#B8FF4D] hover:underline"
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
      <section className="border-b border-[#2B2B38] px-4 py-20 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <div className="max-w-3xl">
            <span className="font-mono text-xs uppercase tracking-widest text-[#FFB547] font-semibold">
              06 / Before You Pick Up
            </span>
            <h2 className="text-3xl sm:text-5xl font-bold font-display text-[#F5F5F5] mt-2">
              Your voice is personal.
              <br />
              Consent is essential.
            </h2>
            <div className="mt-6 space-y-4 text-base text-[#A1A1AA] leading-relaxed">
              <p>
                The proposed experiment records calls for transcription, accusation scoring and research. You must explicitly agree before continuing.
              </p>
              <p className="text-sm text-[#71717A]">
                This is a prototype. Storage, retention, access and deletion procedures are pending policy confirmation. Final terms must be available before real calls launch. Don&apos;t share sensitive personal information in a conversation.
              </p>
            </div>
            <div className="mt-8">
              <Link
                href="/methodology#privacy"
                className="font-mono text-xs uppercase tracking-wider text-[#8B7CFF] hover:underline"
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
      <section className="border-b border-[#2B2B38] px-4 py-20 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <div className="mb-12">
            <span className="font-mono text-xs uppercase tracking-widest text-[#8B7CFF] font-semibold">
              07 / Good Questions
            </span>
            <h2 className="text-3xl sm:text-5xl font-bold font-display text-[#F5F5F5] mt-2">
              A little less mystery about the game.
            </h2>
            <p className="text-sm font-mono text-[#A1A1AA] mt-2">
              The participant stays a mystery. The process shouldn&apos;t.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7">
              <h3 className="text-lg font-bold font-display text-[#F5F5F5]">
                Do I need to speak to my browser?
              </h3>
              <p className="mt-3 text-sm text-[#A1A1AA] leading-relaxed">
                No. You&apos;ll receive a real phone call. This page only shows call status and the reveal; it has no browser microphone, transcript or call controls.
              </p>
            </div>

            <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7">
              <h3 className="text-lg font-bold font-display text-[#F5F5F5]">
                Can I play in Hindi or English?
              </h3>
              <p className="mt-3 text-sm text-[#A1A1AA] leading-relaxed">
                Yes. Choose one language before the call. In either mode, use the exact accusation phrase &ldquo;Tum bot ho!&rdquo; if you think you&apos;re talking to AI.
              </p>
            </div>

            <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7">
              <h3 className="text-lg font-bold font-display text-[#F5F5F5]">
                What if I accuse a human?
              </h3>
              <p className="mt-3 text-sm text-[#A1A1AA] leading-relaxed">
                You&apos;ll see that after the call. A recorded accusation against a human counts as a false accusation, not an AI detection.
              </p>
            </div>

            <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-7">
              <h3 className="text-lg font-bold font-display text-[#F5F5F5]">
                Are the leaderboard numbers real?
              </h3>
              <p className="mt-3 text-sm text-[#A1A1AA] leading-relaxed">
                Not in this design preview. Every metric is sample data, and all provider names are fictional. Public research results should include cohort sizes and limitations.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* ─────────────────────────────────────────────────────────────
          SECTION 08: YOUR EARS. YOUR INSTINCT.
         ───────────────────────────────────────────────────────────── */}
      <section className="bg-[#B8FF4D] text-[#101014] px-4 py-20 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl flex flex-col md:flex-row md:items-end justify-between gap-8">
          <div>
            <span className="font-mono text-xs uppercase tracking-widest text-[#101014]/70 font-bold">
              08 / Your Ears. Your Instinct.
            </span>
            <h2 className="text-4xl sm:text-6xl lg:text-7xl font-bold font-display uppercase tracking-tight leading-[0.92] mt-2">
              Don&apos;t guess from here.
              <br />
              Pick up.
            </h2>
            <p className="mt-4 text-base sm:text-lg text-[#101014]/80 max-w-xl font-medium">
              A human or an AI is waiting on the other side. You won&apos;t know which until it&apos;s over.
            </p>
          </div>

          <div className="flex flex-col items-start md:items-end gap-3">
            <Link
              href="/play"
              className="inline-flex h-14 items-center justify-center rounded-[4px] bg-[#101014] px-9 font-mono text-sm font-bold uppercase tracking-wider text-[#F5F5F5] transition-all hover:bg-[#22222D] active:translate-y-[1px]"
            >
              Play the Game ↗
            </Link>
            <span className="font-mono text-[11px] uppercase tracking-wider text-[#101014]/70 font-semibold">
              PHONE ONLY · HINDI / ENGLISH · CONSENT FIRST
            </span>
          </div>
        </div>
      </section>
    </main>
  );
}
