"use client";

import React, { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";

export default function Navbar() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const pathname = usePathname();

  const navLinks = [
    { href: "/#rules", label: "How it works" },
    { href: "/leaderboard", label: "Leaderboard" },
    { href: "/methodology", label: "Methodology" },
    { href: "/companions", label: "Companions" },
    { href: "/design-system", label: "Design System" },
  ];

  return (
    <header className="sticky top-0 z-50 w-full border-b border-[#2B2B38] bg-[#101014]/90 backdrop-blur-md">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
        {/* Brand / Logo */}
        <Link
          href="/"
          className="flex items-center gap-2 text-xl font-bold tracking-tight text-[#F5F5F5] transition-colors hover:text-[#B8FF4D]"
        >
          <span className="font-display tracking-tight">Pehchana Kaun?</span>
          <span className="rounded-[4px] bg-[#8B7CFF]/20 px-1.5 py-0.5 font-mono text-[10px] font-semibold tracking-wider text-[#8B7CFF]">
            EXP·01
          </span>
        </Link>

        {/* Desktop Navigation Links */}
        <nav className="hidden lg:flex items-center gap-7">
          {navLinks.map((link) => {
            const isActive = pathname === link.href;
            return (
              <Link
                key={link.href}
                href={link.href}
                className={`text-xs font-mono uppercase tracking-wider transition-colors hover:text-[#F5F5F5] ${
                  isActive ? "text-[#B8FF4D] font-bold" : "text-[#A1A1AA]"
                }`}
              >
                {link.label}
              </Link>
            );
          })}
        </nav>

        {/* CTA + Mobile Menu Button */}
        <div className="flex items-center gap-4">
          <Link
            href="/play"
            className="inline-flex h-10 items-center justify-center rounded-[4px] bg-[#B8FF4D] px-4 font-mono text-xs font-bold uppercase tracking-wider text-[#101014] transition-all hover:bg-[#CDFF7A] hover:shadow-[0_0_20px_rgba(184,255,77,0.3)] active:translate-y-[1px]"
          >
            Play the Game ↗
          </Link>

          {/* Hamburger toggle for mobile */}
          <button
            type="button"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            className="lg:hidden flex h-10 w-10 items-center justify-center rounded-[4px] border border-[#2B2B38] text-[#F5F5F5] hover:bg-[#1B1B23]"
            aria-label="Toggle navigation menu"
            aria-expanded={mobileMenuOpen}
          >
            {mobileMenuOpen ? (
              <svg className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            ) : (
              <svg className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
              </svg>
            )}
          </button>
        </div>
      </div>

      {/* Mobile Drawer Menu */}
      {mobileMenuOpen && (
        <div className="lg:hidden border-b border-[#2B2B38] bg-[#1B1B23] px-4 py-5">
          <div className="flex flex-col gap-4 font-mono text-xs uppercase tracking-wider">
            {navLinks.map((link) => (
              <Link
                key={link.href}
                href={link.href}
                onClick={() => setMobileMenuOpen(false)}
                className="text-[#F5F5F5] hover:text-[#B8FF4D] py-1"
              >
                {link.label}
              </Link>
            ))}
            <div className="pt-3 border-t border-[#2B2B38]">
              <Link
                href="/play"
                onClick={() => setMobileMenuOpen(false)}
                className="flex h-11 w-full items-center justify-center rounded-[4px] bg-[#B8FF4D] font-mono text-xs font-bold uppercase tracking-wider text-[#101014]"
              >
                Play the Game ↗
              </Link>
            </div>
          </div>
        </div>
      )}
    </header>
  );
}
