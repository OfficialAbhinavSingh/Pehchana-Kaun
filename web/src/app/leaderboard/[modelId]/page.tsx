import React from "react";
import Link from "next/link";
import SurvivalChart from "@/components/SurvivalChart";
import GiveawayBar from "@/components/GiveawayBar";
import { SAMPLE_ARMS, SAMPLE_ASTER_CURVE } from "@/lib/sampleData";

export function generateStaticParams() {
  return SAMPLE_ARMS.map((arm) => ({
    modelId: arm.arm_id,
  }));
}

export default async function ModelProfilePage({
  params,
}: {
  params: Promise<{ modelId: string }>;
}) {
  const { modelId } = await params;
  const arm = SAMPLE_ARMS.find((a) => a.arm_id === modelId) ?? SAMPLE_ARMS[1];

  const giveaways = arm.top_giveaways.length > 0 ? arm.top_giveaways : [
    { tag: "Unnatural pauses", count: 63 },
    { tag: "Overly polished replies", count: 51 },
    { tag: "Missed context", count: 36 },
  ];

  return (
    <main className="min-h-screen bg-[#101014] text-[#F5F5F5] px-4 py-12 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-7xl space-y-10">
        {/* Navigation & breadcrumb */}
        <div className="flex items-center justify-between border-b border-[#2B2B38] pb-4 font-mono text-xs">
          <Link
            href="/leaderboard"
            className="text-[#8B7CFF] hover:underline flex items-center gap-1.5"
          >
            ← Public leaderboard
          </Link>
          <span className="text-[#B8FF4D]">Sample data · design preview</span>
        </div>

        {/* Model Profile Title */}
        <div className="space-y-4">
          <div className="font-mono text-xs uppercase tracking-widest text-[#8B7CFF]">
            MODEL PROFILE / VOICE EVALUATION
          </div>
          <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-6">
            <div>
              <h1 className="text-4xl sm:text-6xl font-bold font-display uppercase tracking-tight text-[#F5F5F5]">
                {arm.display_name}
              </h1>
              <p className="mt-2 text-base text-[#A1A1AA]">
                Voice display name: <strong className="text-[#F5F5F5]">Nila</strong> (Hinglish Conversational Voice)
              </p>
            </div>
            <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] px-4 py-2 font-mono text-xs text-[#71717A]">
              PHONE ONLY · HINDI + ENGLISH · EDITORIAL VOICE MARK
            </div>
          </div>
        </div>

        {/* 4 Primary KPIs */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6">
            <span className="font-mono text-xs uppercase tracking-wider text-[#71717A]">
              AI PHONE CALLS
            </span>
            <div className="mt-3 text-4xl font-bold font-mono text-[#F5F5F5]">
              {arm.n_calls}
            </div>
            <p className="mt-2 text-xs font-mono text-[#A1A1AA]">
              150 Hindi · 150 English
            </p>
          </div>

          <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6">
            <span className="font-mono text-xs uppercase tracking-wider text-[#71717A]">
              AI ACCUSATION RATE
            </span>
            <div className="mt-3 text-4xl font-bold font-mono text-[#B8FF4D]">
              {Math.round(arm.accusation_rate * 100)}%
            </div>
            <p className="mt-2 text-xs font-mono text-[#A1A1AA]">
              {arm.n_accused} detections / {arm.n_calls} calls
            </p>
          </div>

          <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6">
            <span className="font-mono text-xs uppercase tracking-wider text-[#71717A]">
              MEDIAN TURING CLOCK
            </span>
            <div className="mt-3 text-4xl font-bold font-mono text-[#8B7CFF]">
              {arm.median_turing_clock_s ? `${arm.median_turing_clock_s}s` : "—"}
            </div>
            <p className="mt-2 text-xs font-mono text-[#A1A1AA]">
              Among {arm.n_accused} detected calls only
            </p>
          </div>

          <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6">
            <span className="font-mono text-xs uppercase tracking-wider text-[#71717A]">
              NOT DETECTED
            </span>
            <div className="mt-3 text-4xl font-bold font-mono text-[#F5F5F5]">
              {arm.n_calls - arm.n_accused}
            </div>
            <p className="mt-2 text-xs font-mono text-[#A1A1AA]">
              {Math.round(((arm.n_calls - arm.n_accused) / arm.n_calls) * 100)}% right-censored at 90s
            </p>
          </div>
        </div>

        {/* Charts & Giveaways */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <div className="lg:col-span-7">
            <SurvivalChart
              curve={arm.curve.length > 0 ? arm.curve : SAMPLE_ASTER_CURVE}
              title={`How long does ${arm.display_name} last?`}
              subtitle={`Estimated share of calls remaining unaccused over time (n=${arm.n_calls}).`}
            />
          </div>

          <div className="lg:col-span-5">
            <GiveawayBar
              items={giveaways}
              totalDetected={arm.n_accused}
              title="What gave it away?"
              subtitle={`Coded giveaway themes among ${arm.n_accused} detected calls.`}
            />
          </div>
        </div>

        {/* Language Comparison Section */}
        <div className="rounded-[4px] border border-[#2B2B38] bg-[#14141A] p-6 sm:p-8 space-y-6">
          <div>
            <span className="font-mono text-xs uppercase tracking-widest text-[#B8FF4D]">
              LANGUAGE IS PART OF THE EXPERIMENT
            </span>
            <h3 className="text-2xl sm:text-3xl font-bold font-display text-[#F5F5F5] mt-1">
              The same voice. Different conversations.
            </h3>
            <p className="text-xs text-[#A1A1AA] mt-1">
              Differences are descriptive across accents and turn-taking styles, not evidence of a language advantage.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Hindi Card */}
            <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6 space-y-4">
              <div className="flex items-center justify-between font-mono text-xs">
                <span className="text-base font-bold text-[#F5F5F5] font-display">Hindi</span>
                <span className="text-[#71717A]">150 AI PHONE CALLS</span>
              </div>
              <div className="flex items-baseline gap-6 font-mono">
                <div>
                  <div className="text-3xl font-bold text-[#B8FF4D]">54%</div>
                  <div className="text-[11px] text-[#A1A1AA]">81 / 150 accused</div>
                </div>
                <div>
                  <div className="text-3xl font-bold text-[#8B7CFF]">36s</div>
                  <div className="text-[11px] text-[#A1A1AA]">Median clock (detected)</div>
                </div>
              </div>
              <p className="text-xs font-mono text-[#71717A] border-t border-[#2B2B38] pt-3">
                69 calls not detected · right-censored at 90s.
              </p>
            </div>

            {/* English Card */}
            <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6 space-y-4">
              <div className="flex items-center justify-between font-mono text-xs">
                <span className="text-base font-bold text-[#F5F5F5] font-display">English</span>
                <span className="text-[#71717A]">150 AI PHONE CALLS</span>
              </div>
              <div className="flex items-baseline gap-6 font-mono">
                <div>
                  <div className="text-3xl font-bold text-[#B8FF4D]">46%</div>
                  <div className="text-[11px] text-[#A1A1AA]">69 / 150 accused</div>
                </div>
                <div>
                  <div className="text-3xl font-bold text-[#8B7CFF]">40s</div>
                  <div className="text-[11px] text-[#A1A1AA]">Median clock (detected)</div>
                </div>
              </div>
              <p className="text-xs font-mono text-[#71717A] border-t border-[#2B2B38] pt-3">
                81 calls not detected · right-censored at 90s.
              </p>
            </div>
          </div>

          <div className="pt-2">
            <Link
              href="/methodology"
              className="font-mono text-xs uppercase tracking-wider text-[#8B7CFF] hover:underline"
            >
              Explore the methodology ↗
            </Link>
          </div>
        </div>
      </div>
    </main>
  );
}
