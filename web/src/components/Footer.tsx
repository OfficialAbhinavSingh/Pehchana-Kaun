import React from "react";
import Link from "next/link";

export default function Footer() {
  return (
    <footer className="w-full border-t border-[#2B2B38] bg-[#101014] text-[#A1A1AA]">
      <div className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
        <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-8">
          {/* Brand + Mission */}
          <div>
            <Link
              href="/"
              className="text-lg font-bold tracking-tight text-[#F5F5F5] font-display hover:text-[#B8FF4D]"
            >
              Pehchana Kaun?
            </Link>
            <p className="mt-2 text-xs font-mono uppercase tracking-widest text-[#71717A]">
              An experiment in listening. Not a test of you.
            </p>
          </div>

          {/* Links */}
          <div className="flex flex-wrap items-center gap-6 font-mono text-xs uppercase tracking-wider">
            <Link href="/methodology#assignment" className="hover:text-[#F5F5F5] transition-colors">
              About
            </Link>
            <Link href="/methodology" className="hover:text-[#F5F5F5] transition-colors">
              Methodology
            </Link>
            <Link href="/methodology#privacy" className="hover:text-[#F5F5F5] transition-colors">
              Privacy & Consent
            </Link>
            <Link href="/leaderboard" className="hover:text-[#F5F5F5] transition-colors">
              Leaderboard
            </Link>
            <Link href="/play" className="text-[#B8FF4D] hover:underline">
              Play The Game ↗
            </Link>
          </div>
        </div>

        <div className="mt-8 pt-8 border-t border-[#2B2B38]/60 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs font-mono text-[#71717A]">
          <p>© 2026 Pehchaano Labs · Built for Bolna Symphony Buildathon</p>
          <div className="flex items-center gap-3">
            <span className="inline-block h-2 w-2 rounded-full bg-[#B8FF4D]" />
            <span>PHONE ONLY · HINDI + ENGLISH · NO BROWSER MIC</span>
            <span className="text-[#8B7CFF]">PK? / 01</span>
          </div>
        </div>
      </div>
    </footer>
  );
}
