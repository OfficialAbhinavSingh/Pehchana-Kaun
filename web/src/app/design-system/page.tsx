import React from "react";
import Link from "next/link";

export default function DesignSystemPage() {
  const swatches = [
    { name: "Canvas", hex: "#f3f2f2", bg: "bg-[#f3f2f2]", text: "text-[#201e1d]" },
    { name: "Card", hex: "#ffffff", bg: "bg-[#ffffff]", text: "text-[#201e1d]" },
    { name: "Ink", hex: "#201e1d", bg: "bg-[#201e1d]", text: "text-[#f3f2f2]" },
    { name: "Accent", hex: "#ec3013", bg: "bg-[#ec3013]", text: "text-[#ffffff]" },
    { name: "Accent tint", hex: "#fff2ef", bg: "bg-[#fff2ef]", text: "text-[#201e1d]" },
    { name: "Accent deep", hex: "#ae1800", bg: "bg-[#ae1800]", text: "text-[#ffffff]" },
    { name: "Neutral", hex: "#d7d3d3", bg: "bg-[#d7d3d3]", text: "text-[#201e1d]" },
    { name: "Neutral deep", hex: "#605d5d", bg: "bg-[#605d5d]", text: "text-[#ffffff]" },
  ];

  return (
    <main className="min-h-screen bg-[#f3f2f2] text-[#201e1d] px-4 py-12 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-7xl space-y-16">
        {/* Header */}
        <div className="border-b-2 border-[#201e1d] pb-10">
          <span className="font-mono text-xs uppercase tracking-widest text-[#ae1800] font-semibold">
            PEHCHANA KAUN? / DESIGN SYSTEM 02
          </span>
          <h1 className="mt-2 text-4xl sm:text-6xl lg:text-7xl font-bold font-display tracking-tight text-[#201e1d] leading-[0.92]">
            A voice has a shape.
            <br />
            <span className="text-[#ec3013]">So does trust.</span>
          </h1>
          <p className="mt-4 text-base sm:text-lg text-[#605d5d] max-w-2xl leading-relaxed">
            Flat, architectural and near-mono: a light grey ground, thick ink rules, zero corner
            radius and one red accent, set entirely in Archivo &mdash; a serious research protocol
            that reads as exactly that.
          </p>
          <div className="mt-4 inline-flex items-center gap-2 border-2 border-[#201e1d] bg-[#ffffff] px-3.5 py-1.5 font-mono text-xs text-[#7d7979]">
            <span>LIVE DESIGN SPECIFICATION &middot; ARCHIVO EVERYWHERE</span>
          </div>
        </div>

        {/* 01 / Visual Foundations */}
        <section className="space-y-8">
          <div className="border-b-2 border-[#201e1d] pb-4">
            <span className="font-mono text-xs uppercase tracking-widest text-[#ec3013] font-bold">
              01 / VISUAL FOUNDATIONS
            </span>
            <h2 className="text-2xl sm:text-3xl font-bold font-display text-[#201e1d] mt-1">
              Color is a mono accent, not a rainbow.
            </h2>
          </div>

          {/* Color Palette */}
          <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-3">
            {swatches.map((s) => (
              <div key={s.name} className="border-2 border-[#201e1d] bg-[#ffffff] p-3 space-y-3">
                <div className={`h-16 w-full border-2 border-[#201e1d] ${s.bg}`} />
                <div>
                  <div className="font-mono text-xs font-bold text-[#201e1d]">{s.name}</div>
                  <div className="font-mono text-[10px] text-[#7d7979] uppercase">{s.hex}</div>
                </div>
              </div>
            ))}
          </div>
          <p className="text-sm text-[#7d7979] max-w-2xl">
            Red (#ec3013) is the only accent &mdash; it carries every call to action and nothing
            else. No second brand color: variety comes from the neutral ramp (light grey tints to
            deep ink), never from a rainbow of card colors.
          </p>

          {/* Typography Specimens */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 pt-4">
            <div className="border-2 border-[#201e1d] bg-[#ffffff] p-6 space-y-3">
              <span className="font-mono text-xs text-[#ae1800] uppercase font-bold">
                ARCHIVO / 800&ndash;900 / &minus;3% TRACKING
              </span>
              <div className="text-4xl font-bold font-display text-[#201e1d]">Aa? 01</div>
              <h3 className="text-xl font-bold font-display text-[#ec3013]">Pehchana Kaun?</h3>
              <p className="text-xs text-[#605d5d] leading-relaxed">
                Display 96&ndash;112 hero, 56&ndash;64 section, 28&ndash;36 heading. Tight leading
                (0.9&ndash;0.95), never tight touch targets.
              </p>
            </div>

            <div className="border-2 border-[#201e1d] bg-[#ffffff] p-6 space-y-3">
              <span className="font-mono text-xs text-[#ec3013] uppercase font-bold">
                ARCHIVO / 400&ndash;600 / BODY &amp; INTERFACE
              </span>
              <div className="text-2xl font-medium text-[#201e1d]">Aa Bb 12</div>
              <h3 className="text-base font-bold text-[#201e1d]">One phone call. One mystery voice.</h3>
              <p className="text-xs text-[#605d5d] leading-relaxed">
                Body 16&ndash;19 / 1.5&ndash;1.6 line height. One family does both display and body
                &mdash; weight is what separates them, not a second typeface.
              </p>
            </div>

            <div className="border-2 border-[#201e1d] bg-[#ffffff] p-6 space-y-3">
              <span className="font-mono text-xs text-[#ae1800] uppercase font-bold">
                ARCHIVO / 700&ndash;800 / METRICS &amp; LABELS
              </span>
              <div className="text-3xl font-mono font-bold text-[#201e1d]">00:42 &middot; 60%</div>
              <div className="font-mono text-xs text-[#7d7979] uppercase">STAT / TIMER FORMAT</div>
              <p className="text-xs font-mono text-[#605d5d] leading-relaxed">
                Labels 11&ndash;12 tracked wide. Data 24&ndash;56. Timers up to 96. Tabular figures
                across every table and stat tile.
              </p>
            </div>
          </div>
        </section>

        {/* 02 / Layout & Accessibility */}
        <section className="space-y-6">
          <div className="border-b-2 border-[#201e1d] pb-4">
            <span className="font-mono text-xs uppercase tracking-widest text-[#ec3013] font-bold">
              02 / LAYOUT &amp; ACCESSIBILITY
            </span>
            <h2 className="text-2xl sm:text-3xl font-bold font-display text-[#201e1d] mt-1">
              Thick rules, square corners, a visible grid.
            </h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="border-2 border-[#201e1d] bg-[#ffffff] p-6 space-y-3 font-mono text-xs text-[#605d5d]">
              <div className="text-[#201e1d] font-bold uppercase mb-2">ACCESSIBILITY RULES</div>
              <p>&bull; Minimum 44px touch targets; primary actions 48&ndash;56px.</p>
              <p>&bull; Visible 2px accent keyboard focus ring on all interactive elements.</p>
              <p>&bull; Color is always paired with text and a state label.</p>
              <p>&bull; Accent fills use white text; tinted fills keep ink text.</p>
              <p>&bull; Readable labels and errors; never placeholder-only inputs.</p>
              <p>&bull; Decorative motion respects prefers-reduced-motion.</p>
              <p>&bull; Reflow content; do not shrink desktop screens to mobile.</p>
            </div>

            <div className="border-2 border-[#201e1d] bg-[#ffffff] p-6 space-y-3 font-mono text-xs text-[#605d5d]">
              <div className="text-[#201e1d] font-bold uppercase mb-2">SPACING &amp; GEOMETRY SYSTEM</div>
              <div className="flex gap-2 text-xs font-bold text-[#ec3013]">
                <span>4</span> <span>8</span> <span>12</span> <span>16</span> <span>24</span> <span>32</span> <span>48</span> <span>80px</span>
              </div>
              <p>&bull; Desktop: 1280&ndash;1440px, 56&ndash;64px margins, 24px gutters.</p>
              <p>&bull; Mobile: 390px, 16&ndash;20px margins.</p>
              <p>&bull; Cards: 20&ndash;32px inset padding.</p>
              <p>&bull; Corners: 0px, on purpose &mdash; nothing rounded anywhere, not even badges.</p>
              <p>&bull; Rules at 2px solid #201e1d &mdash; always ink, never a hairline.</p>
            </div>
          </div>
        </section>

        {/* 03 / Navigation & Interactive Actions */}
        <section className="space-y-6">
          <div className="border-b-2 border-[#201e1d] pb-4">
            <span className="font-mono text-xs uppercase tracking-widest text-[#ec3013] font-bold">
              03 / NAVIGATION &amp; ACTIONS
            </span>
            <h2 className="text-2xl sm:text-3xl font-bold font-display text-[#201e1d] mt-1">
              Buttons push down. They don&apos;t just glow.
            </h2>
          </div>

          <div className="border-2 border-[#201e1d] bg-[#ffffff] p-6 space-y-6">
            <div className="flex flex-wrap items-center gap-4 font-mono text-xs">
              <div>
                <span className="block text-[10px] text-[#7d7979] mb-1">DEFAULT PRIMARY</span>
                <button type="button" className="btn-pop shadow-hard h-12 px-6 border-2 border-[#201e1d] bg-[#ec3013] text-[#ffffff] font-bold uppercase">
                  Play the Game &#8599;
                </button>
              </div>

              <div>
                <span className="block text-[10px] text-[#7d7979] mb-1">HOVER (LIFTS, SHADOW GROWS)</span>
                <button type="button" className="shadow-hard-lg h-12 px-6 border-2 border-[#201e1d] bg-[#dd2b0f] text-[#ffffff] font-bold uppercase -translate-x-0.5 -translate-y-0.5">
                  Play the Game &#8599;
                </button>
              </div>

              <div>
                <span className="block text-[10px] text-[#7d7979] mb-1">SECONDARY</span>
                <button type="button" className="btn-pop shadow-hard h-12 px-6 border-2 border-[#201e1d] bg-[#ffffff] text-[#201e1d] font-bold uppercase">
                  View Leaderboard
                </button>
              </div>

              <div>
                <span className="block text-[10px] text-[#7d7979] mb-1">DISABLED</span>
                <button type="button" disabled className="h-12 px-6 border-2 border-[#201e1d] bg-[#fff2ef] text-[#7d7979] font-bold uppercase cursor-not-allowed">
                  Continue to call setup
                </button>
              </div>

              <div>
                <span className="block text-[10px] text-[#7d7979] mb-1">TAG</span>
                <span className="inline-flex border-2 border-[#201e1d] bg-[#fff2ef] px-4 py-2 font-bold uppercase text-[11px]">
                  Live
                </span>
              </div>
            </div>
          </div>
        </section>

        {/* Footer Navigation Back */}
        <div className="pt-6 border-t-2 border-[#201e1d] flex items-center justify-between font-mono text-xs">
          <Link href="/" className="text-[#ae1800] hover:underline">
            &larr; Back to Landing Page
          </Link>
          <Link href="/companions" className="text-[#ec3013] hover:underline font-bold">
            View Journey Companions &#8599;
          </Link>
        </div>
      </div>
    </main>
  );
}
