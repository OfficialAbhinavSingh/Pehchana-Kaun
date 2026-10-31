"use client";

import React from "react";

interface WaveformProps {
  active?: boolean;
  size?: "sm" | "md" | "lg";
  className?: string;
}

export default function Waveform({
  active = true,
  size = "md",
  className = "",
}: WaveformProps) {
  // Height profile mimicking voice frequency bands
  const heights = [
    24, 45, 78, 52, 90, 65, 40, 85, 100, 72,
    48, 88, 60, 95, 80, 50, 70, 42, 60, 35,
    55, 75, 92, 68, 82, 45, 62, 38, 50, 28,
  ];

  const barWidth = size === "sm" ? 2 : size === "md" ? 3 : 4;
  const barGap = size === "sm" ? 2 : size === "md" ? 3 : 4;
  const maxHeight = size === "sm" ? 32 : size === "md" ? 48 : 80;

  return (
    <div
      className={`flex items-center justify-center gap-[${barGap}px] ${className}`}
      aria-hidden="true"
    >
      {heights.map((h, i) => {
        const scaledHeight = (h / 100) * maxHeight;
        // Stagger animation delays for natural organic wave motion
        const delay = (i % 7) * 0.15;
        const duration = 0.8 + ((i % 5) * 0.2);

        return (
          <span
            key={i}
            className="rounded-full transition-all"
            style={{
              width: `${barWidth}px`,
              height: `${Math.max(4, scaledHeight)}px`,
              backgroundColor:
                i % 4 === 0
                  ? "#6a56e8" // Electric lime
                  : i % 3 === 0
                  ? "#5b45e0" // Identity violet
                  : "#b9aee0", // Muted neutral
              opacity: active ? 1 : 0.4,
              animation: active
                ? `pulseBar ${duration}s ease-in-out ${delay}s infinite alternate`
                : "none",
            }}
          />
        );
      })}

      <style jsx>{`
        @keyframes pulseBar {
          0% {
            transform: scaleY(0.35);
          }
          100% {
            transform: scaleY(1.15);
          }
        }
      `}</style>
    </div>
  );
}
