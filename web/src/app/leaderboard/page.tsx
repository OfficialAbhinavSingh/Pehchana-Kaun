"use client";

import React, { useState } from "react";
import Link from "next/link";
import SurvivalChart from "@/components/SurvivalChart";
import GiveawayBar from "@/components/GiveawayBar";
import { SAMPLE_LEADERBOARD, SAMPLE_OVERALL_CURVE } from "@/lib/sampleData";

export default function LeaderboardPage() {
  const [languageFilter, setLanguageFilter] = useState<"all" | "hi" | "en">("all");

  const data = SAMPLE_LEADERBOARD;
  const arms = languageFilter === "all" ? data.arms : (data.by_language[languageFilter] ?? data.arms);
  const aiArms = arms.filter((a) => a.kind === "ai");
  const humanArm = arms.find((a) => a.kind === "human") ?? data.arms[0];

  // Aggregate metrics
  const totalCalls = languageFilter === "all" ? 1200 : 600;
  const aiCalls = languageFilter === "all" ? 900 : 450;
  const humanCalls = languageFilter === "all" ? 300 : 150;
  const detectedCalls = languageFilter === "all" ? 540 : 270;
  const falseHumanAccusations = languageFilter === "all" ? 45 : 22;
  const medianClock = languageFilter === "hi" ? "30s" : languageFilter === "en" ? "34s" : "32s";

  const topGiveaways = [
    { tag: "Unnatural pauses", count: 63 },
    { tag: "Overly polished replies", count: 51 },
    { tag: "Missed context", count: 36 },
    { tag: "Robotic pitch / cadence", count: 32 },
    { tag: "Pronoun confusion", count: 28 },
  ];

  return (
    <main className="min-h-screen bg-[#101014] text-[#F5F5F5] px-4 py-12 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-7xl space-y-12">
        {/* ─────────────────────────────────────────────────────────────
            HEADER & COHORT CONTEXT
           ───────────────────────────────────────────────────────────── */}
        <div className="border-b border-[#2B2B38] pb-8">
          <div className="flex flex-col md:flex-row md:items-end justify-between gap-4">
            <div>
              <span className="font-mono text-xs uppercase tracking-widest text-[#8B7CFF]">
                The Public Experiment / 01
              </span>
              <h1 className="mt-2 text-4xl sm:text-6xl lg:text-7xl font-bold font-display uppercase tracking-tight text-[#F5F5F5]">
                The voices.
                <br />
                The doubt.
                <br />
                <span className="text-[#B8FF4D]">The data.</span>
              </h1>
              <p className="mt-4 text-base text-[#A1A1AA] max-w-xl">
                A scoreboard for questions, not a final verdict on intelligence.
              </p>
            </div>

            <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-4 text-xs font-mono text-[#A1A1AA] space-y-1">
              <span className="text-[#B8FF4D] font-bold block mb-1">SAMPLE DATA · DESIGN PREVIEW</span>
              <div>Cohort: 1,200 completed phone calls</div>
              <div>Channel: Phone Only · No Browser Audio</div>
              <div className="text-[#8B7CFF]">
                <Link href="/methodology" className="hover:underline">
                  How we measure ↗
                </Link>
              </div>
            </div>
          </div>

          {/* Filter Bar */}
          <div className="mt-8 flex flex-wrap items-center justify-between gap-4">
            <div className="flex items-center gap-2">
              <span className="text-xs font-mono text-[#71717A] uppercase mr-2">Language:</span>
              <button
                type="button"
                onClick={() => setLanguageFilter("all")}
                className={`h-9 rounded-[4px] border px-4 font-mono text-xs font-bold uppercase transition-all ${
                  languageFilter === "all"
                    ? "border-[#B8FF4D] bg-[#B8FF4D]/10 text-[#B8FF4D]"
                    : "border-[#2B2B38] bg-[#1B1B23] text-[#A1A1AA] hover:text-[#F5F5F5]"
                }`}
              >
                All Languages
              </button>
              <button
                type="button"
                onClick={() => setLanguageFilter("hi")}
                className={`h-9 rounded-[4px] border px-4 font-mono text-xs font-bold uppercase transition-all ${
                  languageFilter === "hi"
                    ? "border-[#B8FF4D] bg-[#B8FF4D]/10 text-[#B8FF4D]"
                    : "border-[#2B2B38] bg-[#1B1B23] text-[#A1A1AA] hover:text-[#F5F5F5]"
                }`}
              >
                Hindi
              </button>
              <button
                type="button"
                onClick={() => setLanguageFilter("en")}
                className={`h-9 rounded-[4px] border px-4 font-mono text-xs font-bold uppercase transition-all ${
                  languageFilter === "en"
                    ? "border-[#B8FF4D] bg-[#B8FF4D]/10 text-[#B8FF4D]"
                    : "border-[#2B2B38] bg-[#1B1B23] text-[#A1A1AA] hover:text-[#F5F5F5]"
                }`}
              >
                English
              </button>
            </div>

            <div className="text-xs font-mono text-[#71717A]">
              Phone-only dataset. Web-call sessions segregated.
            </div>
          </div>
        </div>

        {/* ─────────────────────────────────────────────────────────────
            SUMMARY KPIS
           ───────────────────────────────────────────────────────────── */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6">
            <span className="font-mono text-xs uppercase tracking-wider text-[#71717A]">
              TOTAL CALLS
            </span>
            <div className="mt-3 text-4xl sm:text-5xl font-bold font-mono text-[#F5F5F5]">
              {totalCalls.toLocaleString()}
            </div>
            <p className="mt-2 text-xs font-mono text-[#A1A1AA]">
              {aiCalls} AI · {humanCalls} human
            </p>
          </div>

          <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6">
            <span className="font-mono text-xs uppercase tracking-wider text-[#71717A]">
              AI ACCUSATION RATE
            </span>
            <div className="mt-3 text-4xl sm:text-5xl font-bold font-mono text-[#B8FF4D]">
              60%
            </div>
            <p className="mt-2 text-xs font-mono text-[#A1A1AA]">
              {detectedCalls} / {aiCalls} AI calls accused
            </p>
          </div>

          <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6">
            <span className="font-mono text-xs uppercase tracking-wider text-[#71717A]">
              MEDIAN TURING CLOCK
            </span>
            <div className="mt-3 text-4xl sm:text-5xl font-bold font-mono text-[#8B7CFF]">
              {medianClock}
            </div>
            <p className="mt-2 text-xs font-mono text-[#A1A1AA]">
              Conditional on {detectedCalls} detections
            </p>
          </div>

          <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6">
            <span className="font-mono text-xs uppercase tracking-wider text-[#71717A]">
              HUMAN FALSE ACCUSATIONS
            </span>
            <div className="mt-3 text-4xl sm:text-5xl font-bold font-mono text-[#FFB547]">
              15%
            </div>
            <p className="mt-2 text-xs font-mono text-[#A1A1AA]">
              {falseHumanAccusations} / {humanCalls} human control calls
            </p>
          </div>
        </div>

        <div className="rounded-[4px] border border-[#2B2B38] bg-[#14141A] p-4 text-xs font-mono text-[#A1A1AA]">
          <strong className="text-[#B8FF4D]">360 AI calls were not detected.</strong> Their observation ends are right-censored, never scored as 0s.
        </div>

        {/* ─────────────────────────────────────────────────────────────
            "A CLOSER LISTEN": SCOREBOARD TABLE
           ───────────────────────────────────────────────────────────── */}
        <div className="space-y-4">
          <div className="flex items-baseline justify-between">
            <div>
              <span className="font-mono text-xs uppercase tracking-widest text-[#B8FF4D]">
                A closer listen.
              </span>
              <h3 className="text-2xl font-bold font-display text-[#F5F5F5] mt-1">
                Model & Provider Breakdown
              </h3>
            </div>
            <span className="text-xs font-mono text-[#71717A]">
              LOWER ACCUSATION ≠ BETTER IN EVERY CONTEXT
            </span>
          </div>

          <div className="overflow-x-auto rounded-[4px] border border-[#2B2B38] bg-[#1B1B23]">
            <table className="w-full text-left font-mono text-xs">
              <thead className="border-b border-[#2B2B38] bg-[#14141A] text-[#71717A] uppercase tracking-wider">
                <tr>
                  <th className="py-4 px-6">Model / Provider</th>
                  <th className="py-4 px-6">Calls</th>
                  <th className="py-4 px-6">Accused Rate</th>
                  <th className="py-4 px-6">Median Clock¹</th>
                  <th className="py-4 px-6">Survival @ 60s</th>
                  <th className="py-4 px-6 text-right">Profile</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-[#2B2B38] text-[#F5F5F5]">
                {/* Control Human Arm */}
                <tr className="bg-[#14141A]/50 hover:bg-[#22222D] transition-colors">
                  <td className="py-4 px-6">
                    <span className="font-bold text-[#FFB547]">
                      {humanArm.display_name}
                    </span>
                    <span className="block text-[11px] text-[#A1A1AA]">
                      Control Arm · Human Volunteers
                    </span>
                  </td>
                  <td className="py-4 px-6">{humanArm.n_calls}</td>
                  <td className="py-4 px-6 text-[#FFB547]">
                    {Math.round(humanArm.accusation_rate * 100)}%{" "}
                    <span className="text-[10px] text-[#71717A]">(False Accusations)</span>
                  </td>
                  <td className="py-4 px-6 text-[#71717A]">N/A (Control)</td>
                  <td className="py-4 px-6 font-bold text-[#F5F5F5]">85%</td>
                  <td className="py-4 px-6 text-right text-[#71717A]">Baseline</td>
                </tr>

                {/* AI Arms */}
                {aiArms.map((arm) => (
                  <tr key={arm.arm_id} className="hover:bg-[#22222D] transition-colors">
                    <td className="py-4 px-6">
                      <span className="font-bold text-[#F5F5F5]">{arm.display_name}</span>
                      <span className="block text-[11px] text-[#A1A1AA]">
                        AI Voice Agent · Hinglish LiD
                      </span>
                    </td>
                    <td className="py-4 px-6">{arm.n_calls}</td>
                    <td className="py-4 px-6 text-[#B8FF4D]">
                      {Math.round(arm.accusation_rate * 100)}%{" "}
                      <span className="text-[11px] text-[#A1A1AA]">
                        ({arm.n_accused}/{arm.n_calls})
                      </span>
                    </td>
                    <td className="py-4 px-6 font-bold text-[#F5F5F5]">
                      {arm.median_turing_clock_s ? `${arm.median_turing_clock_s}s` : "—"}{" "}
                      {arm.median_ci_low_s && (
                        <span className="text-[10px] text-[#71717A] block font-normal">
                          95% CI: [{arm.median_ci_low_s}s–{arm.median_ci_high_s}s]
                        </span>
                      )}
                    </td>
                    <td className="py-4 px-6 text-[#8B7CFF]">
                      {arm.fooled_at_60s ? `${Math.round(arm.fooled_at_60s * 100)}%` : "—"}
                    </td>
                    <td className="py-4 px-6 text-right">
                      <Link
                        href={`/leaderboard/${arm.arm_id}`}
                        className="text-[#8B7CFF] hover:underline"
                      >
                        Profile ↗
                      </Link>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <p className="text-[11px] font-mono text-[#71717A]">
            ¹ Median Turing Clock among detected AI calls only. Undetected calls are not 0s. Accused is the share of AI calls with at least one valid accusation.
          </p>
        </div>

        {/* ─────────────────────────────────────────────────────────────
            SURVIVAL CHART & GIVEAWAYS SPLIT
           ───────────────────────────────────────────────────────────── */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <div className="lg:col-span-7">
            <SurvivalChart
              curve={SAMPLE_OVERALL_CURVE}
              title="How long does the illusion last?"
              subtitle="Estimated share of AI calls with no valid accusation yet (All AI Arms)."
            />
          </div>

          <div className="lg:col-span-5">
            <GiveawayBar
              items={topGiveaways}
              totalDetected={540}
              title="What gave it away?"
              subtitle="Coded conversational themes across all detected AI calls."
            />
          </div>
        </div>

        {/* ─────────────────────────────────────────────────────────────
            METHODOLOGY CALLOUT
           ───────────────────────────────────────────────────────────── */}
        <div className="rounded-[4px] border border-[#2B2B38] bg-[#14141A] p-6 sm:p-8 flex flex-col md:flex-row md:items-center justify-between gap-6">
          <div>
            <span className="font-mono text-xs uppercase tracking-widest text-[#8B7CFF]">
              SCIENTIFIC HONESTY
            </span>
            <h4 className="text-xl font-bold font-display text-[#F5F5F5] mt-1">
              Read both measures together
            </h4>
            <p className="text-xs text-[#A1A1AA] max-w-2xl mt-2 leading-relaxed">
              The survival curve includes censored calls. The median Turing Clock does not. Neither metric alone ranks a model fairly across different callers, languages, or call lengths.
            </p>
          </div>
          <Link
            href="/methodology"
            className="inline-flex h-11 shrink-0 items-center justify-center rounded-[4px] border border-[#8B7CFF] px-6 font-mono text-xs font-bold uppercase tracking-wider text-[#8B7CFF] hover:bg-[#8B7CFF]/10"
          >
            Read All Limitations ↗
          </Link>
        </div>
      </div>
    </main>
  );
}
