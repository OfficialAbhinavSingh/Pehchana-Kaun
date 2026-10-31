import React from "react";
import Link from "next/link";

export default function DesignSystemPage() {
  const swatches = [
    { name: "Canvas", hex: "#f7f4fc", bg: "bg-[#f7f4fc]", text: "text-[#1f1b2e]" },
    { name: "Card", hex: "#ffffff", bg: "bg-[#ffffff]", text: "text-[#1f1b2e]" },
    { name: "Ink", hex: "#1f1b2e", bg: "bg-[#1f1b2e]", text: "text-[#f7f4fc]" },
    { name: "Accent", hex: "#6a56e8", bg: "bg-[#6a56e8]", text: "text-[#ffffff]" },
    { name: "Mint", hex: "#bdeedd", bg: "bg-[#bdeedd]", text: "text-[#1f1b2e]" },
    { name: "Peach", hex: "#ffd9c7", bg: "bg-[#ffd9c7]", text: "text-[#1f1b2e]" },
    { name: "Sky", hex: "#c8e4ff", bg: "bg-[#c8e4ff]", text: "text-[#1f1b2e]" },
    { name: "Lavender", hex: "#d9d0ff", bg: "bg-[#d9d0ff]", text: "text-[#1f1b2e]" },
  ];

  return (
    <main className="min-h-screen bg-[#f7f4fc] text-[#1f1b2e] px-4 py-12 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-7xl space-y-16">
        {/* Header */}
        <div className="border-b-2 border-[#1f1b2e] pb-10">
          <span className="font-mono text-xs uppercase tracking-widest text-[#5b45e0] font-semibold">
            PEHCHANA KAUN? / DESIGN SYSTEM 02
          </span>
          <h1 className="mt-2 text-4xl sm:text-6xl lg:text-7xl font-bold font-display tracking-tight text-[#1f1b2e] leading-[0.92]">
            A voice has a shape.
            <br />
            <span className="text-[#6a56e8]">So does trust.</span>
          </h1>
          <p className="mt-4 text-base sm:text-lg text-[#3b3552] max-w-2xl leading-relaxed">
            Cream ground, thick ink rules and one purple accent, set entirely in Archivo. Flat
            color blocks, hard offset shadows and rounded, huggable cards &mdash; a playful game
            skin over a serious research protocol.
          </p>
          <div className="mt-4 inline-flex items-center gap-2 rounded-full border-2 border-[#1f1b2e] bg-[#ffffff] px-3.5 py-1.5 font-mono text-xs text-[#5d5675]">
            <span>LIVE DESIGN SPECIFICATION &middot; ARCHIVO EVERYWHERE</span>
          </div>
        </div>

        {/* 01 / Visual Foundations */}
        <section className="space-y-8">
          <div className="border-b-2 border-[#1f1b2e] pb-4">
            <span className="font-mono text-xs uppercase tracking-widest text-[#6a56e8] font-bold">
              01 / VISUAL FOUNDATIONS
            </span>
            <h2 className="text-2xl sm:text-3xl font-bold font-display text-[#1f1b2e] mt-1">
              Color is a mono accent, not a rainbow.
            </h2>
          </div>

          {/* Color Palette */}
          <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-3">
            {swatches.map((s) => (
              <div key={s.name} className="rounded-2xl border-2 border-[#1f1b2e] bg-[#ffffff] p-3 space-y-3">
                <div className={`h-16 w-full rounded-xl border-2 border-[#1f1b2e] ${s.bg}`} />
                <div>
                  <div className="font-mono text-xs font-bold text-[#1f1b2e]">{s.name}</div>
                  <div className="font-mono text-[10px] text-[#5d5675] uppercase">{s.hex}</div>
                </div>
              </div>
            ))}
          </div>
          <p className="text-sm text-[#5d5675] max-w-2xl">
            Purple (#6a56e8) is the only accent &mdash; it carries every call to action. Mint, peach,
            sky and lavender are mood tints for stat cards and badges; they never compete with the
            accent for attention.
          </p>

          {/* Typography Specimens */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 pt-4">
            <div className="rounded-2xl border-2 border-[#1f1b2e] bg-[#ffffff] p-6 space-y-3">
              <span className="font-mono text-xs text-[#5b45e0] uppercase font-bold">
                ARCHIVO / 800&ndash;900 / &minus;3% TRACKING
              </span>
              <div className="text-4xl font-bold font-display text-[#1f1b2e]">Aa? 01</div>
              <h3 className="text-xl font-bold font-display text-[#6a56e8]">Pehchana Kaun?</h3>
              <p className="text-xs text-[#3b3552] leading-relaxed">
                Display 96&ndash;112 hero, 56&ndash;64 section, 28&ndash;36 heading. Tight leading
                (0.9&ndash;0.95), never tight touch targets.
              </p>
            </div>

            <div className="rounded-2xl border-2 border-[#1f1b2e] bg-[#ffffff] p-6 space-y-3">
              <span className="font-mono text-xs text-[#6a56e8] uppercase font-bold">
                ARCHIVO / 400&ndash;600 / BODY &amp; INTERFACE
              </span>
              <div className="text-2xl font-medium text-[#1f1b2e]">Aa Bb 12</div>
              <h3 className="text-base font-bold text-[#1f1b2e]">One phone call. One mystery voice.</h3>
              <p className="text-xs text-[#3b3552] leading-relaxed">
                Body 16&ndash;19 / 1.5&ndash;1.6 line height. One family does both display and body
                &mdash; weight is what separates them, not a second typeface.
              </p>
            </div>

            <div className="rounded-2xl border-2 border-[#1f1b2e] bg-[#ffffff] p-6 space-y-3">
              <span className="font-mono text-xs text-[#5b45e0] uppercase font-bold">
                ARCHIVO / 700&ndash;800 / METRICS &amp; LABELS
              </span>
              <div className="text-3xl font-mono font-bold text-[#1f1b2e]">00:42 &middot; 60%</div>
              <div className="font-mono text-xs text-[#5d5675] uppercase">STAT / TIMER FORMAT</div>
              <p className="text-xs font-mono text-[#3b3552] leading-relaxed">
                Labels 11&ndash;12 tracked wide. Data 24&ndash;56. Timers up to 96. Tabular figures
                across every table and stat tile.
              </p>
            </div>
          </div>
        </section>

        {/* 02 / Layout & Accessibility */}
        <section className="space-y-6">
          <div className="border-b-2 border-[#1f1b2e] pb-4">
            <span className="font-mono text-xs uppercase tracking-widest text-[#6a56e8] font-bold">
              02 / LAYOUT &amp; ACCESSIBILITY
            </span>
            <h2 className="text-2xl sm:text-3xl font-bold font-display text-[#1f1b2e] mt-1">
              Thick rules, round corners, a visible grid.
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="rounded-2xl border-2 border-[#1f1b2e] bg-[#ffffff] p-6 space-y-3 font-mono text-xs text-[#3b3552]">
              <div className="text-[#1f1b2e] font-bold uppercase mb-2">ACCESSIBILITY RULES</div>
              <p>&bull; Minimum 44px touch targets; primary actions 48&ndash;56px.</p>
              <p>&bull; Visible 2px accent keyboard focus ring on all interactive elements.</p>
              <p>&bull; Color is always paired with text and a state label.</p>
              <p>&bull; Accent fills use white text; pastel fills keep ink text.</p>
              <p>&bull; Readable labels and errors; never placeholder-only inputs.</p>
              <p>&bull; Decorative motion respects prefers-reduced-motion.</p>
              <p>&bull; Reflow content; do not shrink desktop screens to mobile.</p>
            </div>

            <div className="rounded-2xl border-2 border-[#1f1b2e] bg-[#ffffff] p-6 space-y-3 font-mono text-xs text-[#3b3552]">
              <div className="text-[#1f1b2e] font-bold uppercase mb-2">SPACING &amp; GEOMETRY SYSTEM</div>
              <div className="flex gap-2 text-xs font-bold text-[#6a56e8]">
                <span>4</span> <span>8</span> <span>12</span> <span>16</span> <span>24</span> <span>32</span> <span>48</span> <span>80px</span>
              </div>
              <p>&bull; Desktop: 1280&ndash;1440px, 56&ndash;64px margins, 24px gutters.</p>
              <p>&bull; Mobile: 390px, 16&ndash;20px margins.</p>
              <p>&bull; Cards: 20&ndash;32px inset padding, 20&ndash;28px corner radius.</p>
              <p>&bull; Corners: generous and rounded &mdash; nothing sharp, nothing fully pill except badges.</p>
              <p>&bull; Rules at 2px solid #1f1b2e &mdash; always ink, never a hairline.</p>
            </div>
          </div>
        </section>

        {/* 03 / Navigation & Interactive Actions */}
        <section className="space-y-6">
          <div className="border-b-2 border-[#1f1b2e] pb-4">
            <span className="font-mono text-xs uppercase tracking-widest text-[#6a56e8] font-bold">
              03 / NAVIGATION &amp; ACTIONS
            </span>
            <h2 className="text-2xl sm:text-3xl font-bold font-display text-[#1f1b2e] mt-1">
              Buttons push down. They don&apos;t just glow.
            </h2>
          </div>

          <div className="rounded-2xl border-2 border-[#1f1b2e] bg-[#ffffff] p-6 space-y-6">
            <div className="flex flex-wrap items-center gap-4 font-mono text-xs">
              <div>
                <span className="block text-[10px] text-[#5d5675] mb-1">DEFAULT PRIMARY</span>
                <button type="button" className="btn-pop shadow-hard h-12 px-6 rounded-2xl border-2 border-[#1f1b2e] bg-[#6a56e8] text-[#ffffff] font-bold uppercase">
                  Play the Game &#8599;
                </button>
              </div>

              <div>
                <span className="block text-[10px] text-[#5d5675] mb-1">HOVER (LIFTS, SHADOW GROWS)</span>
                <button type="button" className="shadow-hard-lg h-12 px-6 rounded-2xl border-2 border-[#1f1b2e] bg-[#5640d8] text-[#ffffff] font-bold uppercase -translate-x-0.5 -translate-y-0.5">
                  Play the Game &#8599;
                </button>
              </div>

              <div>
                <span className="block text-[10px] text-[#5d5675] mb-1">SECONDARY</span>
                <button type="button" className="btn-pop shadow-hard h-12 px-6 rounded-2xl border-2 border-[#1f1b2e] bg-[#ffffff] text-[#1f1b2e] font-bold uppercase">
                  View Leaderboard
                </button>
              </div>

              <div>
                <span className="block text-[10px] text-[#5d5675] mb-1">DISABLED</span>
                <button type="button" disabled className="h-12 px-6 rounded-2xl border-2 border-[#1f1b2e] bg-[#ece6ff] text-[#5d5675] font-bold uppercase cursor-not-allowed">
                  Continue to call setup
                </button>
              </div>

              <div>
                <span className="block text-[10px] text-[#5d5675] mb-1">PILL TAG</span>
                <span className="inline-flex rounded-full border-2 border-[#1f1b2e] bg-[#bdeedd] px-4 py-2 font-bold uppercase text-[11px]">
                  Live
                </span>
              </div>
            </div>
          </div>
        </section>

        {/* Footer Navigation Back */}
        <div className="pt-6 border-t-2 border-[#1f1b2e] flex items-center justify-between font-mono text-xs">
          <Link href="/" className="text-[#5b45e0] hover:underline">
            &larr; Back to Landing Page
          </Link>
          <Link href="/companions" className="text-[#6a56e8] hover:underline font-bold">
            View Journey Companions &#8599;
          </Link>
        </div>
      </div>
    </main>
  );
}
