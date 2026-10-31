import React from "react";
import Link from "next/link";

export default function NotFound() {
  return (
    <main className="min-h-screen bg-[#f3f2f2] text-[#201e1d] px-4 py-24 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-3xl text-center">
        <span className="font-mono text-xs uppercase tracking-widest text-[#ae1800] font-semibold">
          404 / NOT FOUND
        </span>
        <h1 className="mt-4 text-5xl sm:text-7xl font-bold font-display text-[#201e1d] leading-[0.92]">
          No voice at
          <br />
          <span className="text-[#ec3013]">this address.</span>
        </h1>
        <p className="mt-4 text-base text-[#605d5d] max-w-md mx-auto">
          The page you&apos;re looking for doesn&apos;t exist. Maybe it hung up early.
        </p>
        <div className="mt-8 flex flex-wrap items-center justify-center gap-4">
          <Link
            href="/"
            className="btn-pop shadow-hard inline-flex h-12 items-center justify-center border-2 border-[#201e1d] bg-[#ec3013] px-7 font-mono text-sm font-bold uppercase tracking-wider text-[#ffffff]"
          >
            Back to home
          </Link>
          <Link
            href="/play"
            className="btn-pop shadow-hard inline-flex h-12 items-center justify-center border-2 border-[#201e1d] bg-[#ffffff] px-7 font-mono text-sm font-bold uppercase tracking-wider text-[#201e1d]"
          >
            Play the game
          </Link>
        </div>
      </div>
    </main>
  );
}
