"use client";

import React, { useEffect, useState } from "react";
import Link from "next/link";
import SurvivalChart from "@/components/SurvivalChart";
import GiveawayBar from "@/components/GiveawayBar";
import { ArmStats, Leaderboard, getLeaderboard } from "@/lib/api";

function pct(n: number): string {
  return `${Math.round(n * 100)}%`;
}

function clock(s: number | null): string {
  if (s === null) return "—";
  const whole = Math.round(s);
  return `${Math.floor(whole / 60)}:${(whole % 60).toString().padStart(2, "0")}`;
}

export default function LeaderboardPage() {
  const [board, setBoard] = useState<Leaderboard | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState<string>("all");

  useEffect(() => {
    getLeaderboard()
      .then(setBoard)
      .catch(() => setError("Could not load the leaderboard. Try again in a bit."));
  }, []);

  if (error) {
    return (
      <main className="min-h-screen bg-[#f3f2f2] text-[#201e1d] px-4 py-24 text-center font-mono text-sm text-[#605d5d]">
        {error}
      </main>
    );
  }

  if (!board) {
    return (
      <main className="min-h-screen bg-[#f3f2f2] text-[#201e1d] px-4 py-24 text-center font-mono text-sm text-[#605d5d]">
        Loading the leaderboard…
      </main>
    );
  }

  const languages = Object.keys(board.by_language);
  const arms: ArmStats[] = activeTab === "all" ? board.arms : board.by_language[activeTab] ?? [];
  const human = arms.find((a) => a.kind === "human");
  const aiArms = arms.filter((a) => a.kind === "ai");
  const aiCalls = aiArms.reduce((s, a) => s + a.n_calls, 0);
  const aiAccused = aiArms.reduce((s, a) => s + a.n_accused, 0);
  const topArm = aiArms.find((a) => a.ranked) ?? aiArms[0];

  return (
    <main className="min-h-screen bg-[#f3f2f2] text-[#201e1d] px-4 py-12 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-7xl space-y-10">
        {/* Header Section */}
        <div className="border-b-2 border-[#201e1d] pb-8">
          <div className="flex flex-col md:flex-row md:items-end justify-between gap-6">
            <div>
              <span className="font-mono text-xs uppercase tracking-widest text-[#ae1800] font-semibold">
                THE PUBLIC EXPERIMENT / 01
              </span>
              <h1 className="mt-2 text-5xl sm:text-7xl font-bold font-display uppercase tracking-tight text-[#201e1d] leading-[0.92]">
                The voices.
                <br />
                The doubt.
                <br />
                <span className="text-[#ec3013]">The data.</span>
              </h1>
              <p className="mt-4 text-base text-[#605d5d]">
                A scoreboard for questions, not a final verdict on intelligence.
              </p>
            </div>

            <div className=" border-2 border-[#201e1d] bg-[#ffffff] p-5 font-mono text-xs text-[#605d5d] space-y-2 max-w-sm">
              {board.includes_demo_data ? (
                <span className="text-[#a8520a] font-bold block uppercase">
                  Includes seeded demo data
                </span>
              ) : (
                <span className="text-[#ec3013] font-bold block uppercase">Live results</span>
              )}
              <p className="text-[11px] text-[#7d7979] leading-relaxed">
                Real phone calls only. Voice names only (no vendor names). Updated{" "}
                {new Date(board.generated_at).toLocaleString()}.
              </p>
              <div className="pt-2 border-t-2 border-[#201e1d] flex items-center justify-between text-[11px]">
                <span className="text-[#7d7979]">CHANNEL / PHONE ONLY</span>
                <Link href="/methodology" className="text-[#ae1800] hover:underline">
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
                className={`h-9 border px-4 font-mono text-xs font-bold uppercase transition-all ${
                  activeTab === "all"
                    ? "border-[#ec3013] bg-[#ec3013]/10 text-[#ec3013]"
                    : "border-[#201e1d] bg-[#ffffff] text-[#605d5d]"
                }`}
              >
                All
              </button>
              {languages.map((lang) => (
                <button
                  key={lang}
                  type="button"
                  onClick={() => setActiveTab(lang)}
                  className={`h-9 border px-4 font-mono text-xs font-bold uppercase transition-all ${
                    activeTab === lang
                      ? "border-[#ec3013] bg-[#ec3013]/10 text-[#ec3013]"
                      : "border-[#201e1d] bg-[#ffffff] text-[#605d5d]"
                  }`}
                >
                  {lang}
                </button>
              ))}
            </div>

            <div className="font-mono text-xs text-[#7d7979]">
              COHORT / {activeTab.toUpperCase()}
            </div>
          </div>
        </div>

        {/* 4 KPI Summary Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <div className=" border-2 border-[#201e1d] bg-[#ffffff] p-6">
            <span className="font-mono text-xs uppercase tracking-wider text-[#7d7979]">
              TOTAL CALLS
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
              {aiAccused} / {aiCalls} AI calls
            </p>
          </div>

          <div className=" border-2 border-[#201e1d] bg-[#ffffff] p-6">
            <span className="font-mono text-xs uppercase tracking-wider text-[#7d7979]">
              FASTEST MEDIAN TURING CLOCK
            </span>
            <div className="mt-3 text-4xl sm:text-5xl font-bold font-mono text-[#ae1800]">
              {topArm ? clock(topArm.median_turing_clock_s) : "—"}
            </div>
            <p className="mt-2 text-xs font-mono text-[#605d5d]">
              {topArm ? `${topArm.display_name}, n=${topArm.n_calls}` : "not enough calls yet"}
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
              {human ? `${human.n_accused} / ${human.n_calls} human calls` : "no human-arm calls yet"}
            </p>
          </div>
        </div>

        <div className=" border-2 border-[#201e1d] bg-[#fff2ef] p-4 font-mono text-xs text-[#605d5d]">
          <strong className="text-[#201e1d]">
            {aiCalls - aiAccused} AI calls were not detected.
          </strong>{" "}
          Their observation ends are right-censored, never scored as 0s.
        </div>

        {/* Section: A closer listen */}
        <div className="space-y-4">
          <div className="flex flex-col sm:flex-row sm:items-baseline justify-between gap-2">
            <div>
              <span className="font-mono text-xs uppercase tracking-widest text-[#ec3013] font-semibold">
                A closer listen.
              </span>
              <h3 className="text-2xl font-bold font-display text-[#201e1d] mt-1">
                Model Performance Breakdown
              </h3>
            </div>
            <span className="font-mono text-xs text-[#7d7979]">
              VOICE NAMES ONLY / LOWER ACCUSATION ≠ BETTER IN EVERY CONTEXT
            </span>
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
                {aiArms.length === 0 && (
                  <tr>
                    <td className="py-4 px-6 text-[#7d7979]" colSpan={4}>
                      No AI calls in this cohort yet.
                    </td>
                  </tr>
                )}
                {aiArms.map((a) => (
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
                        {a.n_accused} / {a.n_calls} {a.ranked ? "" : "· below ranking minimum"}
                      </span>
                    </td>
                    <td className="py-4 px-6 font-bold text-[#201e1d]">
                      {clock(a.median_turing_clock_s)}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <div className="space-y-1 text-[11px] font-mono text-[#7d7979]">
            <p>
              ¹ Median Turing Clock among detected AI calls only. Undetected calls are not 0s.
              Vendor names are hidden; voice labels are consistent across the game.
            </p>
            <p>
              Accused is the share of AI calls with at least one valid accusation. Turing Clock is
              the median time only among those detected — it can look fast even when many calls go
              undetected.
            </p>
          </div>
        </div>

        {/* Two-Column: Survival Curve & Giveaways */}
        {topArm && (
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            <div className="lg:col-span-7">
              <SurvivalChart
                curve={topArm.curve}
                title={`How long does ${topArm.display_name} last?`}
                subtitle={`Estimated share of ${topArm.display_name} calls with no valid accusation yet. n=${topArm.n_calls} · ${topArm.n_accused} detected · ${topArm.n_calls - topArm.n_accused} censored.`}
              />
            </div>

            <div className="lg:col-span-5 space-y-4">
              <GiveawayBar
                items={topArm.top_giveaways}
                totalDetected={topArm.n_accused}
                title="What gave it away?"
                subtitle={`Coded themes among ${topArm.n_accused} detected ${topArm.display_name} calls. One primary theme per call.`}
              />
              <div className="text-right">
                <Link href="/methodology#limitations" className="font-mono text-xs text-[#ae1800] hover:underline">
                  Read all limitations ↗
                </Link>
              </div>
            </div>
          </div>
        )}

        {/* Read both measures together Card */}
        <div className=" border-2 border-[#201e1d] bg-[#fff2ef] p-7">
          <h4 className="text-lg font-bold font-display text-[#201e1d]">
            Read both measures together
          </h4>
          <p className="mt-2 text-sm text-[#605d5d] leading-relaxed">
            The curve includes censored calls. The median Turing Clock does not. Neither metric
            alone ranks a voice fairly across different callers, languages or call lengths.
          </p>
        </div>
      </div>
    </main>
  );
}
