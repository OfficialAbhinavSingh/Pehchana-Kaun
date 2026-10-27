import React from "react";
import Link from "next/link";

export default function DesignSystemPage() {
  const swatches = [
    { name: "Canvas", hex: "#101014", bg: "bg-[#101014]", text: "text-[#F5F5F5]" },
    { name: "Card", hex: "#1B1B23", bg: "bg-[#1B1B23]", text: "text-[#F5F5F5]" },
    { name: "Action", hex: "#B8FF4D", bg: "bg-[#B8FF4D]", text: "text-[#101014]" },
    { name: "Identity", hex: "#8B7CFF", bg: "bg-[#8B7CFF]", text: "text-[#101014]" },
    { name: "Primary", hex: "#F5F5F5", bg: "bg-[#F5F5F5]", text: "text-[#101014]" },
    { name: "Muted", hex: "#A1A1AA", bg: "bg-[#A1A1AA]", text: "text-[#101014]" },
    { name: "Warning", hex: "#FFB547", bg: "bg-[#FFB547]", text: "text-[#101014]" },
    { name: "Error", hex: "#FF8C8C", bg: "bg-[#FF8C8C]", text: "text-[#101014]" },
  ];

  return (
    <main className="min-h-screen bg-[#101014] text-[#F5F5F5] px-4 py-12 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-7xl space-y-16">
        {/* Header */}
        <div className="border-b border-[#2B2B38] pb-10">
          <span className="font-mono text-xs uppercase tracking-widest text-[#8B7CFF] font-semibold">
            PEHCHANA KAUN? / DESIGN SYSTEM 01
          </span>
          <h1 className="mt-2 text-4xl sm:text-6xl lg:text-7xl font-bold font-display uppercase tracking-tight text-[#F5F5F5] leading-[0.92]">
            Voice has a shape.
            <br />
            <span className="text-[#B8FF4D]">Trust has a system.</span>
          </h1>
          <p className="mt-4 text-base sm:text-lg text-[#A1A1AA] max-w-2xl leading-relaxed">
            Dark editorial rhythm. Electric-lime actions. Violet identity signals. Native, editable frame examples for a phone-first experiment.
          </p>
          <div className="mt-4 inline-flex items-center gap-2 rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] px-3.5 py-1.5 font-mono text-xs text-[#71717A]">
            <span>STATIC DESIGN SPECIFICATION · FIGMA CANONICAL</span>
          </div>
        </div>

        {/* 01 / Visual Foundations */}
        <section className="space-y-8">
          <div className="border-b border-[#2B2B38] pb-4">
            <span className="font-mono text-xs uppercase tracking-widest text-[#B8FF4D] font-bold">
              01 / VISUAL FOUNDATIONS
            </span>
            <h2 className="text-2xl sm:text-3xl font-bold font-display text-[#F5F5F5] mt-1">
              Color is functional, not decorative.
            </h2>
          </div>

          {/* Color Palette */}
          <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-3">
            {swatches.map((s) => (
              <div key={s.name} className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-3 space-y-3">
                <div className={`h-16 w-full rounded-[3px] border border-[#2B2B38] ${s.bg}`} />
                <div>
                  <div className="font-mono text-xs font-bold text-[#F5F5F5]">{s.name}</div>
                  <div className="font-mono text-[10px] text-[#71717A] uppercase">{s.hex}</div>
                </div>
              </div>
            ))}
          </div>

          {/* Typography Specimens */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 pt-4">
            {/* Space Grotesk */}
            <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6 space-y-3">
              <span className="font-mono text-xs text-[#8B7CFF] uppercase font-bold">
                SPACE GROTESK / 700 / −2% TRACKING
              </span>
              <div className="text-4xl font-bold font-display text-[#F5F5F5]">Aa? 01</div>
              <h3 className="text-xl font-bold font-display text-[#B8FF4D]">A voice, not a face.</h3>
              <p className="text-xs text-[#A1A1AA] leading-relaxed">
                Display 116 / 106 hero mobile 56 page 80 / 48 section 56 / 38 heading 28 / 24. Use tight leading, never tight touch targets.
              </p>
            </div>

            {/* Inter */}
            <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6 space-y-3">
              <span className="font-mono text-xs text-[#B8FF4D] uppercase font-bold">
                INTER / BODY & INTERFACE
              </span>
              <div className="text-2xl font-medium text-[#F5F5F5]">Aa Bb 12</div>
              <h3 className="text-base font-bold text-[#F5F5F5]">One phone call. One mystery voice.</h3>
              <p className="text-xs text-[#A1A1AA] leading-relaxed">
                Body 16 / 1.6 line height. Supporting copy 14 / 1.6. Keep explanations complete and phone-only constraints unmistakable.
              </p>
            </div>

            {/* JetBrains Mono */}
            <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6 space-y-3">
              <span className="font-mono text-xs text-[#8B7CFF] uppercase font-bold">
                JETBRAINS MONO / METRICS & TECHNICAL LABELS
              </span>
              <div className="text-3xl font-mono font-bold text-[#F5F5F5]">00:42 / 60%</div>
              <div className="font-mono text-xs text-[#71717A] uppercase">STAT / TIMER FORMAT</div>
              <p className="text-xs font-mono text-[#A1A1AA] leading-relaxed">
                Labels 11 / 1.5. Data 24–40. Timers 76–112. No all-caps paragraphs. Tabular figures across all tables.
              </p>
            </div>
          </div>
        </section>

        {/* 02 / Layout & Accessibility */}
        <section className="space-y-6">
          <div className="border-b border-[#2B2B38] pb-4">
            <span className="font-mono text-xs uppercase tracking-widest text-[#B8FF4D] font-bold">
              02 / LAYOUT & ACCESSIBILITY
            </span>
            <h2 className="text-2xl sm:text-3xl font-bold font-display text-[#F5F5F5] mt-1">
              A disciplined beat. Clear beats clever.
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6 space-y-3 font-mono text-xs text-[#A1A1AA]">
              <div className="text-[#F5F5F5] font-bold uppercase mb-2">ACCESSIBILITY RULES</div>
              <p>• Minimum 44px touch targets; primary actions 52px.</p>
              <p>• Visible 3px violet keyboard focus ring on all interactive elements.</p>
              <p>• Color is always paired with text and state indicators.</p>
              <p>• Lime uses dark ink; violet text uses a lighter tint.</p>
              <p>• Readable labels and errors; never placeholder-only inputs.</p>
              <p>• Decorative waveforms respect prefers-reduced-motion.</p>
              <p>• Reflow content; do not shrink desktop screens to mobile.</p>
            </div>

            <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6 space-y-3 font-mono text-xs text-[#A1A1AA]">
              <div className="text-[#F5F5F5] font-bold uppercase mb-2">SPACING & GEOMETRY SYSTEM</div>
              <div className="flex gap-2 text-xs font-bold text-[#B8FF4D]">
                <span>4</span> <span>8</span> <span>12</span> <span>16</span> <span>24</span> <span>32</span> <span>48</span> <span>80px</span>
              </div>
              <p>• Desktop: 1440px, 64px margins, 24–32px gutters.</p>
              <p>• Mobile: 390px, 20px margins.</p>
              <p>• Cards: 20–32px inset padding.</p>
              <p>• Corners: 4px, not bubbly.</p>
              <p>• Column rules at 1px solid #2B2B38.</p>
            </div>
          </div>
        </section>

        {/* 03 / Navigation & Interactive Actions */}
        <section className="space-y-6">
          <div className="border-b border-[#2B2B38] pb-4">
            <span className="font-mono text-xs uppercase tracking-widest text-[#B8FF4D] font-bold">
              03 / NAVIGATION & ACTIONS
            </span>
            <h2 className="text-2xl sm:text-3xl font-bold font-display text-[#F5F5F5] mt-1">
              Interactive States
            </h2>
          </div>

          <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6 space-y-6">
            <div className="flex flex-wrap items-center gap-4 font-mono text-xs">
              <div>
                <span className="block text-[10px] text-[#71717A] mb-1">DEFAULT PRIMARY</span>
                <button type="button" className="h-12 px-6 rounded-[4px] bg-[#B8FF4D] text-[#101014] font-bold uppercase">
                  Play the Game ↗
                </button>
              </div>

              <div>
                <span className="block text-[10px] text-[#71717A] mb-1">HOVER</span>
                <button type="button" className="h-12 px-6 rounded-[4px] bg-[#CDFF7A] text-[#101014] font-bold uppercase shadow-[0_0_20px_rgba(184,255,77,0.3)]">
                  Play the Game ↗
                </button>
              </div>

              <div>
                <span className="block text-[10px] text-[#71717A] mb-1">SECONDARY</span>
                <button type="button" className="h-12 px-6 rounded-[4px] border border-[#2B2B38] bg-[#14141A] text-[#F5F5F5] font-bold uppercase">
                  View Leaderboard ↗
                </button>
              </div>

              <div>
                <span className="block text-[10px] text-[#71717A] mb-1">DISABLED</span>
                <button type="button" disabled className="h-12 px-6 rounded-[4px] border border-[#2B2B38] bg-[#14141A] text-[#71717A] font-bold uppercase cursor-not-allowed">
                  Continue to call setup
                </button>
              </div>
            </div>
          </div>
        </section>

        {/* Footer Navigation Back */}
        <div className="pt-6 border-t border-[#2B2B38] flex items-center justify-between font-mono text-xs">
          <Link href="/" className="text-[#8B7CFF] hover:underline">
            ← Back to Landing Page
          </Link>
          <Link href="/companions" className="text-[#B8FF4D] hover:underline">
            View Journey Companions ↗
          </Link>
        </div>
      </div>
    </main>
  );
}
