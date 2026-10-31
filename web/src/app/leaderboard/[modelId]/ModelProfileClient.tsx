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

export default function ModelProfileClient({ modelId }: { modelId: string }) {
  const [board, setBoard] = useState<Leaderboard | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getLeaderboard()
      .then(setBoard)
      .catch(() => setError("Could not load the leaderboard. Try again in a bit."));
  }, []);

  if (error) {
    return (
      <main className="min-h-screen bg-[#f7f4fc] text-[#1f1b2e] px-4 py-24 text-center font-mono text-sm text-[#3b3552]">
        {error}
      </main>
    );
  }

  if (!board) {
    return (
      <main className="min-h-screen bg-[#f7f4fc] text-[#1f1b2e] px-4 py-24 text-center font-mono text-sm text-[#3b3552]">
        Loading…
      </main>
    );
  }

  const arm = board.arms.find((a) => a.arm_id === modelId && a.kind === "ai");
  if (!arm) {
    return (
      <main className="min-h-screen bg-[#f7f4fc] text-[#1f1b2e] px-4 py-24 text-center font-mono text-sm text-[#3b3552] space-y-4">
        <p>No voice called &ldquo;{modelId}&rdquo; on the leaderboard.</p>
        <Link href="/leaderboard" className="text-[#5b45e0] hover:underline">
          ← Back to the leaderboard
        </Link>
      </main>
    );
  }

  const byLanguage = Object.entries(board.by_language)
    .map(([lang, arms]) => [lang, arms.find((a) => a.arm_id === arm.arm_id)] as const)
    .filter((entry): entry is [string, ArmStats] => entry[1] !== undefined);

  return (
    <main className="min-h-screen bg-[#f7f4fc] text-[#1f1b2e] px-4 py-12 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-7xl space-y-10">
        {/* Navigation & breadcrumb */}
        <div className="flex items-center justify-between border-b-2 border-[#1f1b2e] pb-4 font-mono text-xs">
          <Link
            href="/leaderboard"
            className="text-[#5b45e0] hover:underline flex items-center gap-1.5"
          >
            ← Public leaderboard
          </Link>
          <span className="text-[#5d5675]">
            {board.includes_demo_data ? "Includes seeded demo data" : "Live results"}
          </span>
        </div>

        {/* Model Profile Title */}
        <div className="space-y-4">
          <div className="font-mono text-xs uppercase tracking-widest text-[#5b45e0]">
            VOICE PROFILE / EVALUATION
          </div>
          <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-6">
            <div>
              <h1 className="text-4xl sm:text-6xl font-bold font-display uppercase tracking-tight text-[#1f1b2e]">
                {arm.display_name}
              </h1>
              {!arm.ranked && (
                <p className="mt-2 text-sm text-[#a8520a]">
                  Below {board.min_calls_for_ranking} calls: shown, not ranked yet.
                </p>
              )}
            </div>
            <div className="rounded-3xl border-2 border-[#1f1b2e] bg-[#ffffff] px-4 py-2 font-mono text-xs text-[#5d5675]">
              PHONE ONLY · HIDDEN IDENTITY UNTIL REVEAL_VENDORS
            </div>
          </div>
        </div>

        {/* 4 Primary KPIs */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="rounded-3xl border-2 border-[#1f1b2e] bg-[#ffffff] p-6">
            <span className="font-mono text-xs uppercase tracking-wider text-[#5d5675]">
              AI PHONE CALLS
            </span>
            <div className="mt-3 text-4xl font-bold font-mono text-[#1f1b2e]">{arm.n_calls}</div>
            <p className="mt-2 text-xs font-mono text-[#3b3552]">
              {byLanguage.map(([lang, a]) => `${a.n_calls} ${lang}`).join(" · ") || "—"}
            </p>
          </div>

          <div className="rounded-3xl border-2 border-[#1f1b2e] bg-[#ffffff] p-6">
            <span className="font-mono text-xs uppercase tracking-wider text-[#5d5675]">
              AI ACCUSATION RATE
            </span>
            <div className="mt-3 text-4xl font-bold font-mono text-[#6a56e8]">
              {pct(arm.accusation_rate)}
            </div>
            <p className="mt-2 text-xs font-mono text-[#3b3552]">
              {arm.n_accused} detections / {arm.n_calls} calls
            </p>
          </div>

          <div className="rounded-3xl border-2 border-[#1f1b2e] bg-[#ffffff] p-6">
            <span className="font-mono text-xs uppercase tracking-wider text-[#5d5675]">
              MEDIAN TURING CLOCK
            </span>
            <div className="mt-3 text-4xl font-bold font-mono text-[#5b45e0]">
              {clock(arm.median_turing_clock_s)}
            </div>
            <p className="mt-2 text-xs font-mono text-[#3b3552]">
              Among {arm.n_accused} detected calls only
            </p>
          </div>

          <div className="rounded-3xl border-2 border-[#1f1b2e] bg-[#ffffff] p-6">
            <span className="font-mono text-xs uppercase tracking-wider text-[#5d5675]">
              NOT DETECTED
            </span>
            <div className="mt-3 text-4xl font-bold font-mono text-[#1f1b2e]">
              {arm.n_calls - arm.n_accused}
            </div>
            <p className="mt-2 text-xs font-mono text-[#3b3552]">
              {arm.n_calls > 0
                ? `${Math.round(((arm.n_calls - arm.n_accused) / arm.n_calls) * 100)}% right-censored`
                : "—"}
            </p>
          </div>
        </div>

        {/* Charts & Giveaways */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <div className="lg:col-span-7">
            <SurvivalChart
              curve={arm.curve}
              title={`How long does ${arm.display_name} last?`}
              subtitle={`Estimated share of calls remaining unaccused over time (n=${arm.n_calls}).`}
            />
          </div>

          <div className="lg:col-span-5">
            <GiveawayBar
              items={arm.top_giveaways}
              totalDetected={arm.n_accused}
              title="What gave it away?"
              subtitle={`Coded giveaway themes among ${arm.n_accused} detected calls.`}
            />
          </div>
        </div>

        {/* Language Comparison Section */}
        {byLanguage.length > 0 && (
          <div className="rounded-3xl border-2 border-[#1f1b2e] bg-[#ece6ff] p-6 sm:p-8 space-y-6">
            <div>
              <span className="font-mono text-xs uppercase tracking-widest text-[#6a56e8]">
                LANGUAGE IS PART OF THE EXPERIMENT
              </span>
              <h3 className="text-2xl sm:text-3xl font-bold font-display text-[#1f1b2e] mt-1">
                The same voice. Different conversations.
              </h3>
              <p className="text-xs text-[#3b3552] mt-1">
                Differences are descriptive across accents and turn-taking styles, not evidence of
                a language advantage.
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {byLanguage.map(([lang, a]) => (
                <div key={lang} className="rounded-3xl border-2 border-[#1f1b2e] bg-[#ffffff] p-6 space-y-4">
                  <div className="flex items-center justify-between font-mono text-xs">
                    <span className="text-base font-bold text-[#1f1b2e] font-display uppercase">
                      {lang}
                    </span>
                    <span className="text-[#5d5675]">{a.n_calls} AI PHONE CALLS</span>
                  </div>
                  <div className="flex items-baseline gap-6 font-mono">
                    <div>
                      <div className="text-3xl font-bold text-[#6a56e8]">{pct(a.accusation_rate)}</div>
                      <div className="text-[11px] text-[#3b3552]">
                        {a.n_accused} / {a.n_calls} accused
                      </div>
                    </div>
                    <div>
                      <div className="text-3xl font-bold text-[#5b45e0]">{clock(a.median_turing_clock_s)}</div>
                      <div className="text-[11px] text-[#3b3552]">Median clock (detected)</div>
                    </div>
                  </div>
                  <p className="text-xs font-mono text-[#5d5675] border-t-2 border-[#1f1b2e] pt-3">
                    {a.n_calls - a.n_accused} calls not detected · right-censored.
                  </p>
                </div>
              ))}
            </div>

            <div className="pt-2">
              <Link
                href="/methodology"
                className="font-mono text-xs uppercase tracking-wider text-[#5b45e0] hover:underline"
              >
                Explore the methodology ↗
              </Link>
            </div>
          </div>
        )}
      </div>
    </main>
  );
}
