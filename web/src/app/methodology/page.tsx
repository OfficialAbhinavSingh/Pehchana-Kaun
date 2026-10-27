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
    <main className="min-h-screen bg-[#101014] text-[#F5F5F5] px-4 py-12 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-7xl">
        {/* Header */}
        <div className="border-b border-[#2B2B38] pb-10">
          <span className="font-mono text-xs uppercase tracking-widest text-[#8B7CFF]">
            About / Methodology / Privacy
          </span>
          <h1 className="mt-2 text-4xl sm:text-6xl lg:text-7xl font-bold font-display uppercase tracking-tight text-[#F5F5F5]">
            Listen closely.
            <br />
            <span className="text-[#B8FF4D]">Measure honestly.</span>
          </h1>
          <p className="mt-4 text-base sm:text-lg text-[#A1A1AA] max-w-2xl leading-relaxed">
            A playful question about voice. A serious responsibility to explain what the answers do and don&apos;t mean.
          </p>
          <div className="mt-4 inline-flex items-center gap-2 rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] px-3 py-1 font-mono text-xs text-[#71717A]">
            <span>PROTOTYPE RESEARCH PROTOCOL · METHODS & OPERATIONAL POLICIES</span>
          </div>
        </div>

        {/* Content Layout: Sticky Table of Contents + Protocol Sections */}
        <div className="mt-12 grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
          {/* Sticky Sidebar */}
          <aside className="lg:col-span-4 sticky top-24 rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-6 space-y-4">
            <div className="font-mono text-xs uppercase tracking-widest text-[#8B7CFF] font-bold">
              IN THIS DOCUMENT
            </div>
            <nav className="space-y-2 font-mono text-xs">
              {protocolNotes.map((note) => (
                <a
                  key={note.id}
                  href={`#${note.id}`}
                  className="block text-[#A1A1AA] hover:text-[#B8FF4D] transition-colors py-1 border-b border-[#2B2B38]/40"
                >
                  <span className="text-[#71717A] mr-2">{note.num} /</span>
                  {note.title.split(",")[0].split(".")[0]}
                </a>
              ))}
            </nav>

            <div className="pt-4 border-t border-[#2B2B38] font-mono text-[11px] text-[#71717A] space-y-2">
              <strong className="text-[#F5F5F5] block">NOT LIVE RESEARCH RESULTS</strong>
              <p>
                All preview metrics shown are sample data. Real data will be exported on 29 Oct at the data freeze.
              </p>
            </div>
          </aside>

          {/* Protocol Notes Stream */}
          <div className="lg:col-span-8 space-y-10">
            {protocolNotes.map((note) => (
              <section
                key={note.id}
                id={note.id}
                className="scroll-mt-24 rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-8 space-y-4 hover:border-[#8B7CFF]/50 transition-colors"
              >
                <div className="flex items-center justify-between font-mono text-xs">
                  <span className="text-[#8B7CFF] uppercase font-bold">
                    {note.num} / PROTOCOL NOTE
                  </span>
                  <span className="text-[#71717A]">RESEARCH STANDARD</span>
                </div>
                <h2 className="text-2xl font-bold font-display text-[#F5F5F5]">
                  {note.title}
                </h2>
                <p className="text-sm sm:text-base text-[#A1A1AA] leading-relaxed">
                  {note.content}
                </p>
              </section>
            ))}

            {/* Curiosity Callout Banner */}
            <div className="rounded-[4px] border border-[#B8FF4D] bg-[#14141A] p-8 space-y-4">
              <span className="font-mono text-xs uppercase tracking-widest text-[#B8FF4D] font-bold">
                CURIOSITY, NOT CERTAINTY.
              </span>
              <h3 className="text-2xl font-bold font-display text-[#F5F5F5]">
                Accusation is an observable behavior.
              </h3>
              <p className="text-sm text-[#A1A1AA] leading-relaxed">
                Human-likeness is a much bigger claim. Read the rates, the curve, and the limitations together.
              </p>
              <div className="pt-2">
                <Link
                  href="/leaderboard"
                  className="inline-flex h-11 items-center justify-center rounded-[4px] bg-[#B8FF4D] px-6 font-mono text-xs font-bold uppercase tracking-wider text-[#101014] hover:bg-[#CDFF7A]"
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
