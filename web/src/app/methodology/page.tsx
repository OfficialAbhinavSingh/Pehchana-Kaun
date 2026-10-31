import React from "react";
import Link from "next/link";

export default function MethodologyPage() {
  const protocolNotes = [
    {
      id: "assignment",
      num: "01",
      title: "A blind conversation, randomly assigned.",
      content:
        "Pehchana Kaun? asks whether people can distinguish a human from an AI in a short, natural phone conversation. A participant type is randomly assigned for each call, and its identity is concealed until the call ends. The participant type and AI provider must never appear in setup or the active companion. Random assignment is not a promise of an exact 50/50 split in every small cohort.",
    },
    {
      id: "accusations",
      num: "02",
      title: "An accusation is a spoken decision.",
      content:
        "The game instruction is to say the exact phrase \"Tum bot ho!\" to accuse the other participant of being AI. The first valid accusation during the connected phone conversation is the event used for timing. Proposed scoring distinguishes an intentional accusation from a quoted example, a negated phrase or uncertain transcription. An accusation against a human is a false accusation, never an AI detection.",
    },
    {
      id: "clock",
      num: "03",
      title: "The Turing Clock starts at connection.",
      content:
        "Detection time runs from call connection to the first valid accusation on an AI call. The displayed median Turing Clock is conditional: it includes detected AI calls only. The AI accusation rate uses all eligible AI calls as its denominator. We report total eligible calls, detected calls, and undetected calls alongside time statistics. Human false-accusation rate is human calls with a valid accusation divided by eligible human calls.",
    },
    {
      id: "censoring",
      num: "04",
      title: "Not detected does not mean zero seconds.",
      content:
        "If an AI call ends without a valid accusation, its observation is right-censored at the call's observed end time. It has no detection time. We cannot know whether that caller would have accused the AI later. Survival curves estimate the share of AI calls remaining unaccused over time and incorporate censoring. Show the observation horizon, sample sizes and censor marks. No accusation is not proof that a caller believed the voice was human.",
    },
    {
      id: "workflow",
      num: "05",
      title: "Scoring must be inspectable, not magical.",
      content:
        "The proposed workflow is: capture a consented recording and connection timestamps; transcribe audio with Deepgram Nova-3; identify candidate accusation phrases; validate intent and timing; aggregate de-identified events. Transcription can miss words, accents and code-switching. Ambiguous events and incomplete calls need documented review and exclusion rules before any public reporting.",
    },
    {
      id: "limitations",
      num: "06",
      title: "A benchmark with boundaries.",
      content:
        "Volunteers are self-selected. They may be unusually curious about AI, familiar with the game, or returning players. Short calls, phone quality, latency, conversation topics and expectations can all affect accusations. Hindi and English are not interchangeable test conditions. Accent, dialect and code-switching coverage may differ. Small cohorts and conditional medians are unstable; do not treat differences as causal, or claim one model is more human from a single ranking.",
    },
    {
      id: "privacy",
      num: "07",
      title: "Recording and privacy need explicit consent.",
      content:
        "The proposed experiment records calls for transcription, scoring and research. Consent must be explicit and initially unchecked, with clear information before a real call starts. Phone numbers are for routing only and must never be published in results. Design principles: minimize collection; limit access; separate contact details from research events; aggregate public results; avoid publishing identifiable audio or transcripts without separate permission.",
    },
    {
      id: "deletion",
      num: "08",
      title: "Deletion is a policy, not a promise we invent.",
      content:
        "Storage location, security controls, authorized access, retention periods, deletion request channels and handling of already aggregated results remain strictly governed. Participants may request deletion of their call recording and associated metadata at any time by contacting the operators. If withdrawal cannot be honored cleanly, call collection does not proceed.",
    },
  ];

  return (
    <main className="min-h-screen bg-[#f7f4fc] text-[#1f1b2e] px-4 py-12 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-7xl">
        {/* Header */}
        <div className="border-b-2 border-[#1f1b2e] pb-10">
          <span className="font-mono text-xs uppercase tracking-widest text-[#5b45e0]">
            About / Methodology / Privacy
          </span>
          <h1 className="mt-2 text-4xl sm:text-6xl lg:text-7xl font-bold font-display uppercase tracking-tight text-[#1f1b2e]">
            Listen closely.
            <br />
            <span className="text-[#6a56e8]">Measure honestly.</span>
          </h1>
          <p className="mt-4 text-base sm:text-lg text-[#3b3552] max-w-2xl leading-relaxed">
            A playful question about voice. A serious responsibility to explain what the answers do and don&apos;t mean.
          </p>
          <div className="mt-4 inline-flex items-center gap-2 rounded-3xl border-2 border-[#1f1b2e] bg-[#ffffff] px-3 py-1 font-mono text-xs text-[#5d5675]">
            <span>PROTOTYPE RESEARCH PROTOCOL · METHODS & OPERATIONAL POLICIES</span>
          </div>
        </div>

        {/* Content Layout: Sticky Table of Contents + Protocol Sections */}
        <div className="mt-12 grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
          {/* Sticky Sidebar */}
          <aside className="lg:col-span-4 sticky top-24 rounded-3xl border-2 border-[#1f1b2e] bg-[#ffffff] p-6 space-y-4">
            <div className="font-mono text-xs uppercase tracking-widest text-[#5b45e0] font-bold">
              IN THIS DOCUMENT
            </div>
            <nav className="space-y-2 font-mono text-xs">
              {protocolNotes.map((note) => (
                <a
                  key={note.id}
                  href={`#${note.id}`}
                  className="block text-[#3b3552] hover:text-[#6a56e8] transition-colors py-1 border-b-2 border-[#1f1b2e]/40"
                >
                  <span className="text-[#5d5675] mr-2">{note.num} /</span>
                  {note.title.split(",")[0].split(".")[0]}
                </a>
              ))}
            </nav>

            <div className="pt-4 border-t-2 border-[#1f1b2e] font-mono text-[11px] text-[#5d5675] space-y-2">
              <strong className="text-[#1f1b2e] block">METHODOLOGY, NOT RESULTS</strong>
              <p>
                This page explains the protocol. For live numbers, see the{" "}
                <Link href="/leaderboard" className="text-[#5b45e0] hover:underline">
                  leaderboard
                </Link>
                .
              </p>
            </div>
          </aside>

          {/* Protocol Notes Stream */}
          <div className="lg:col-span-8 space-y-10">
            {protocolNotes.map((note) => (
              <section
                key={note.id}
                id={note.id}
                className="scroll-mt-24 rounded-3xl border-2 border-[#1f1b2e] bg-[#ffffff] p-8 space-y-4 hover:border-[#5b45e0]/50 transition-colors"
              >
                <div className="flex items-center justify-between font-mono text-xs">
                  <span className="text-[#5b45e0] uppercase font-bold">
                    {note.num} / PROTOCOL NOTE
                  </span>
                  <span className="text-[#5d5675]">RESEARCH STANDARD</span>
                </div>
                <h2 className="text-2xl font-bold font-display text-[#1f1b2e]">
                  {note.title}
                </h2>
                <p className="text-sm sm:text-base text-[#3b3552] leading-relaxed">
                  {note.content}
                </p>
              </section>
            ))}

            {/* Curiosity Callout Banner */}
            <div className="rounded-3xl border-2 border-[#6a56e8] bg-[#ece6ff] p-8 space-y-4">
              <span className="font-mono text-xs uppercase tracking-widest text-[#6a56e8] font-bold">
                CURIOSITY, NOT CERTAINTY.
              </span>
              <h3 className="text-2xl font-bold font-display text-[#1f1b2e]">
                Accusation is an observable behavior.
              </h3>
              <p className="text-sm text-[#3b3552] leading-relaxed">
                Human-likeness is a much bigger claim. Read the rates, the curve, and the limitations together.
              </p>
              <div className="pt-2">
                <Link
                  href="/leaderboard"
                  className="inline-flex h-11 items-center justify-center rounded-2xl bg-[#6a56e8] px-6 font-mono text-xs font-bold uppercase tracking-wider text-[#f7f4fc] hover:bg-[#5640d8]"
                >
                  Back to the leaderboard ↗
                </Link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
