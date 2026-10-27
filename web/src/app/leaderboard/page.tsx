"use client";

import React, { useState } from "react";
import Link from "next/link";
import SurvivalChart from "@/components/SurvivalChart";
import GiveawayBar from "@/components/GiveawayBar";
import { SAMPLE_OVERALL_CURVE } from "@/lib/sampleData";

export default function LeaderboardPage() {
  const [activeTab, setActiveTab] = useState<"all" | "hindi" | "english">("all");

  const topGiveaways = [
    { tag: "Unnatural pauses", count: 63 },
    { tag: "Overly polished replies", count: 51 },
    { tag: "Missed context", count: 36 },
  ];

  return (
    <main className="min-h-screen bg-[#101014] text-[#F5F5F5] px-4 py-12 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-7xl space-y-10">
        {/* Header Section */}
        <div className="border-b border-[#2B2B38] pb-8">
          <div className="flex flex-col md:flex-row md:items-end justify-between gap-6">
            <div>
              <span className="font-mono text-xs uppercase tracking-widest text-[#8B7CFF] font-semibold">
                THE PUBLIC EXPERIMENT / 01
              </span>
              <h1 className="mt-2 text-5xl sm:text-7xl font-bold font-display uppercase tracking-tight text-[#F5F5F5] leading-[0.92]">
                The voices.
                <br />
                The doubt.
                <br />
                <span className="text-[#B8FF4D]">The data.</span>
              </h1>
              <p className="mt-4 text-base text-[#A1A1AA]">
                A scoreboard for questions, not a final verdict on intelligence.
              </p>
            </div>

            <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-5 font-mono text-xs text-[#A1A1AA] space-y-2 max-w-sm">
              <span className="text-[#B8FF4D] font-bold block uppercase">
                Sample data · design preview
              </span>
              <p className="text-[11px] text-[#71717A] leading-relaxed">
                Illustrative cohort of 1,200 completed phone calls. Fictional models, not real provider performance. No live results are shown.
              </p>
              <div className="pt-2 border-t border-[#2B2B38] flex items-center justify-between text-[11px]">
                <span className="text-[#71717A]">CHANNEL / PHONE ONLY</span>
                <Link href="/methodology" className="text-[#8B7CFF] hover:underline">
                  How we measure ↗
                </Link>
              </div>
            </div>
          </div>

          {/* Filter Tabs */}
          <div className="mt-8 flex flex-wrap items-center justify-between gap-4">
            <div className="flex items-center gap-2">
              <button
                type="button"
                onClick={() => setActiveTab("all")}
                className={`h-9 rounded-[4px] border px-4 font-mono text-xs font-bold uppercase transition-all ${
                  activeTab === "all"
                    ? "border-[#B8FF4D] bg-[#B8FF4D]/10 text-[#B8FF4D]"
                    : "border-[#2B2B38] bg-[#1B1B23] text-[#A1A1AA]"
                }`}
              >
                All
              </button>
              <button
                type="button"
                onClick={() => setActiveTab("hindi")}
                className={`h-9 rounded-[4px] border px-4 font-mono text-xs font-bold uppercase transition-all ${
                  activeTab === "hindi"
                    ? "border-[#B8FF4D] bg-[#B8FF4D]/10 text-[#B8FF4D]"
                    : "border-[#2B2B38] bg-[#1B1B23] text-[#A1A1AA]"
                }`}
              >
                Hindi
              </button>
              <button
                type="button"
                onClick={() => setActiveTab("english")}
                className={`h-9 rounded-[4px] border px-4 font-mono text-xs font-bold uppercase transition-all ${
                  activeTab === "english"
                    ? "border-[#B8FF4D] bg-[#B8FF4D]/10 text-[#B8FF4D]"
                    : "border-[#2B2B38] bg-[#1B1B23] text-[#A1A1AA]"
                }`}
              >
                English
              </button>
            </div>

            <div className="font-mono text-xs text-[#71717A]">
              COHORT / {activeTab.toUpperCase()}
            </div>
          </div>
        </div>

        {/* 4 KPI Summary Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6">
            <span className="font-mono text-xs uppercase tracking-wider text-[#71717A]">
              TOTAL CALLS
            </span>
            <div className="mt-3 text-4xl sm:text-5xl font-bold font-mono text-[#F5F5F5]">
              1,200
            </div>
            <p className="mt-2 text-xs font-mono text-[#A1A1AA]">
              900 AI · 300 human
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
              540 / 900 AI calls
            </p>
          </div>

          <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6">
            <span className="font-mono text-xs uppercase tracking-wider text-[#71717A]">
              MEDIAN TURING CLOCK
            </span>
            <div className="mt-3 text-4xl sm:text-5xl font-bold font-mono text-[#8B7CFF]">
              32s
            </div>
            <p className="mt-2 text-xs font-mono text-[#A1A1AA]">
              Conditional on 540 detections
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
              45 / 300 human calls
            </p>
          </div>
        </div>

        <div className="rounded-[4px] border border-[#2B2B38] bg-[#14141A] p-4 font-mono text-xs text-[#A1A1AA]">
          <strong className="text-[#F5F5F5]">360 AI calls were not detected.</strong> Their observation ends are right-censored, never scored as 0s.
        </div>

        {/* Section: A closer listen */}
        <div className="space-y-4">
          <div className="flex flex-col sm:flex-row sm:items-baseline justify-between gap-2">
            <div>
              <span className="font-mono text-xs uppercase tracking-widest text-[#B8FF4D] font-semibold">
                A closer listen.
              </span>
              <h3 className="text-2xl font-bold font-display text-[#F5F5F5] mt-1">
                Model Performance Breakdown
              </h3>
            </div>
            <span className="font-mono text-xs text-[#71717A]">
              FICTIONAL PROVIDERS / LOWER ACCUSATION ≠ BETTER IN EVERY CONTEXT
            </span>
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
                    <span className="block text-[11px] text-[#A1A1AA]">150 / 300 detected only</span>
                  </td>
                  <td className="py-4 px-6 font-bold text-[#F5F5F5]">38s</td>
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
                    <span className="block text-[11px] text-[#A1A1AA]">180 / 300 detected only</span>
                  </td>
                  <td className="py-4 px-6 font-bold text-[#F5F5F5]">32s</td>
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
                    <span className="block text-[11px] text-[#A1A1AA]">210 / 300 detected only</span>
                  </td>
                  <td className="py-4 px-6 font-bold text-[#F5F5F5]">26s</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div className="space-y-1 text-[11px] font-mono text-[#71717A]">
            <p>¹ Median Turing Clock among detected AI calls only. Undetected calls are not 0s. All models and providers are fictional.</p>
            <p>Accused is the share of AI calls with at least one valid accusation. Turing Clock is the median time only among those detected — it can look fast even when many calls go undetected.</p>
          </div>
        </div>

        {/* Two-Column: Survival Curve & Giveaways */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <div className="lg:col-span-7">
            <SurvivalChart
              curve={SAMPLE_OVERALL_CURVE}
              title="How long does the illusion last?"
              subtitle="Estimated share of AI calls with no valid accusation yet. ALL AI / n=900 · 540 DETECTED · 360 CENSORED"
            />
          </div>

          <div className="lg:col-span-5 space-y-4">
            <GiveawayBar
              items={topGiveaways}
              totalDetected={150}
              title="What gave it away?"
              subtitle="Example coded themes among 150 detected Aster calls. One primary theme per call."
            />
            <div className="text-right">
              <Link href="/methodology#limitations" className="font-mono text-xs text-[#8B7CFF] hover:underline">
                Read all limitations ↗
              </Link>
            </div>
          </div>
        </div>

        {/* Read both measures together Card */}
        <div className="rounded-[4px] border border-[#2B2B38] bg-[#14141A] p-7">
          <h4 className="text-lg font-bold font-display text-[#F5F5F5]">
            Read both measures together
          </h4>
          <p className="mt-2 text-sm text-[#A1A1AA] leading-relaxed">
            The curve includes censored calls. The 32s Turing Clock does not. Neither metric alone ranks a model fairly across different callers, languages or call lengths.
          </p>
        </div>
      </div>
    </main>
  );
}
