import React from "react";
import Link from "next/link";

export default function Footer() {
  return (
    <footer className="w-full border-t-2 border-[#1f1b2e] bg-[#f7f4fc] text-[#3b3552]">
      <div className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
        <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-8">
          {/* Brand + Mission */}
          <div>
            <Link
              href="/"
              className="text-lg font-bold tracking-tight text-[#1f1b2e] font-display hover:text-[#6a56e8]"
            >
              Pehchana Kaun?
            </Link>
            <p className="mt-2 text-xs font-mono uppercase tracking-widest text-[#5d5675]">
              An experiment in listening. Not a test of you.
            </p>
          </div>

          {/* Links */}
          <div className="flex flex-wrap items-center gap-6 font-mono text-xs uppercase tracking-wider">
            <Link href="/methodology#assignment" className="hover:text-[#1f1b2e] transition-colors">
              About
            </Link>
            <Link href="/methodology" className="hover:text-[#1f1b2e] transition-colors">
              Methodology
            </Link>
            <Link href="/methodology#privacy" className="hover:text-[#1f1b2e] transition-colors">
              Privacy & Consent
            </Link>
            <Link href="/leaderboard" className="hover:text-[#1f1b2e] transition-colors">
              Leaderboard
            </Link>
            <Link href="/play" className="text-[#6a56e8] hover:underline">
              Play The Game ↗
            </Link>
          </div>
        </div>

        <div className="mt-8 pt-8 border-t-2 border-[#1f1b2e]/60 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs font-mono text-[#5d5675]">
          <p>© 2026 Pehchaano Labs · Built for Bolna Symphony Buildathon</p>
          <div className="flex items-center gap-3">
            <span className="inline-block h-2 w-2 rounded-full bg-[#6a56e8]" />
            <span>CALL OR BROWSER · HINDI + ENGLISH</span>
            <span className="text-[#5b45e0]">PK? / 01</span>
          </div>
        </div>
      </div>
    </footer>
  );
}
