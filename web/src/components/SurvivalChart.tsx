"use client";

import React, { useState } from "react";
import { SurvivalPoint } from "@/lib/api";

interface SurvivalChartProps {
  curve: SurvivalPoint[];
  title?: string;
  subtitle?: string;
  maxT?: number;
}

export default function SurvivalChart({
  curve,
  title = "How long does the illusion last?",
  subtitle = "Estimated share of AI calls with no valid accusation yet.",
  maxT = 90,
}: SurvivalChartProps) {
  const [hoveredPoint, setHoveredPoint] = useState<SurvivalPoint | null>(null);

  // SVG dimensions
  const width = 640;
  const height = 240;
  const padding = { top: 20, right: 30, bottom: 40, left: 50 };
  const chartWidth = width - padding.left - padding.right;
  const chartHeight = height - padding.top - padding.bottom;

  const points = curve && curve.length > 0 ? curve : [
    { t: 0, survival: 1.0, at_risk: 300, events: 0, ci_low: null, ci_high: null },
    { t: 90, survival: 0.5, at_risk: 150, events: 150, ci_low: 0.45, ci_high: 0.55 },
  ];

  // Helper coordinate mappers
  const getX = (t: number) => padding.left + (Math.min(t, maxT) / maxT) * chartWidth;
  const getY = (s: number) => padding.top + (1 - s) * chartHeight;

  // Build SVG path for step-wise Kaplan-Meier curve
  let stepPath = `M ${getX(points[0].t)} ${getY(points[0].survival)}`;
  for (let i = 1; i < points.length; i++) {
    const prev = points[i - 1];
    const curr = points[i];
    // Step horizontal then down
    stepPath += ` L ${getX(curr.t)} ${getY(prev.survival)} L ${getX(curr.t)} ${getY(curr.survival)}`;
  }

  // Build CI confidence band path if present
  let ciPath = "";
  const pointsWithCI = points.filter((p) => p.ci_low !== null && p.ci_high !== null);
  if (pointsWithCI.length > 1) {
    const topPoints = pointsWithCI.map((p) => `${getX(p.t)},${getY(p.ci_high!)}`).join(" L ");
    const bottomPoints = [...pointsWithCI].reverse().map((p) => `${getX(p.t)},${getY(p.ci_low!)}`).join(" L ");
    ciPath = `M ${topPoints} L ${bottomPoints} Z`;
  }

  const endSurvivalPercent = Math.round(points[points.length - 1].survival * 100);

  return (
    <div className="rounded-3xl border-2 border-[#1f1b2e] bg-[#ffffff] p-5 sm:p-6 text-[#1f1b2e]">
      {/* Chart Header */}
      <div className="flex flex-col sm:flex-row sm:items-baseline justify-between gap-2 border-b-2 border-[#1f1b2e] pb-4">
        <div>
          <h4 className="text-base font-bold font-display text-[#1f1b2e]">{title}</h4>
          <p className="text-xs text-[#3b3552]">{subtitle}</p>
        </div>
        <div className="flex items-center gap-3 font-mono text-xs">
          <span className="flex items-center gap-1.5 text-[#6a56e8]">
            <span className="inline-block h-2 w-2 rounded-full bg-[#6a56e8]" />
            Survival Curve
          </span>
          <span className="flex items-center gap-1.5 text-[#5b45e0]">
            <span>+</span> Right-censored
          </span>
        </div>
      </div>

      {/* SVG Canvas */}
      <div className="relative mt-4 w-full overflow-hidden">
        <svg
          viewBox={`0 0 ${width} ${height}`}
          className="w-full h-auto overflow-visible select-none"
        >
          {/* Grid lines */}
          {[1.0, 0.75, 0.5, 0.25, 0].map((s) => (
            <g key={s}>
              <line
                x1={padding.left}
                y1={getY(s)}
                x2={width - padding.right}
                y2={getY(s)}
                stroke="#1f1b2e"
                strokeDasharray="3 3"
                strokeWidth="1"
              />
              <text
                x={padding.left - 8}
                y={getY(s) + 4}
                textAnchor="end"
                className="fill-[#5d5675] text-[10px] font-mono"
              >
                {Math.round(s * 100)}%
              </text>
            </g>
          ))}

          {/* X Axis ticks */}
          {[0, 30, 60, 90].map((t) => (
            <g key={t}>
              <line
                x1={getX(t)}
                y1={padding.top}
                x2={getX(t)}
                y2={height - padding.bottom}
                stroke="#1f1b2e"
                strokeDasharray="2 2"
                strokeWidth="1"
              />
              <text
                x={getX(t)}
                y={height - padding.bottom + 18}
                textAnchor="middle"
                className="fill-[#3b3552] text-[11px] font-mono"
              >
                {t}s
              </text>
            </g>
          ))}

          {/* 95% Greenwood Confidence Interval Band */}
          {ciPath && (
            <path
              d={ciPath}
              fill="#5b45e0"
              fillOpacity="0.12"
              stroke="none"
            />
          )}

          {/* Stepped Kaplan-Meier Survival Line */}
          <path
            d={stepPath}
            fill="none"
            stroke="#6a56e8"
            strokeWidth="2.5"
            strokeLinecap="round"
            strokeLinejoin="round"
          />

          {/* Right-censored marks '+' on the line */}
          {points.map((p, i) => {
            if (p.t === 0 || p.events === 0) return null;
            return (
              <g
                key={i}
                transform={`translate(${getX(p.t)}, ${getY(p.survival)})`}
                onMouseEnter={() => setHoveredPoint(p)}
                onMouseLeave={() => setHoveredPoint(null)}
                className="cursor-pointer group"
              >
                <circle
                  r="4"
                  fill="#ffffff"
                  stroke="#5b45e0"
                  strokeWidth="2"
                  className="transition-transform group-hover:scale-150"
                />
                <text
                  y="-8"
                  textAnchor="middle"
                  className="fill-[#5b45e0] text-[9px] font-mono font-bold"
                >
                  +
                </text>
              </g>
            );
          })}
        </svg>

        {/* Hover inspect card */}
        {hoveredPoint && (
          <div className="absolute top-2 right-4 rounded-xl border-2 border-[#5b45e0] bg-[#f7f4fc]/95 p-2 font-mono text-xs shadow-lg backdrop-blur-md">
            <div className="text-[#6a56e8] font-bold">t = {hoveredPoint.t}s</div>
            <div className="text-[#1f1b2e]">
              Survival: {Math.round(hoveredPoint.survival * 100)}%
            </div>
            <div className="text-[#3b3552]">At Risk: {hoveredPoint.at_risk}</div>
            {hoveredPoint.ci_low !== null && (
              <div className="text-[#5d5675] text-[10px]">
                95% CI: [{Math.round(hoveredPoint.ci_low * 100)}% -{" "}
                {Math.round(hoveredPoint.ci_high! * 100)}%]
              </div>
            )}
          </div>
        )}
      </div>

      {/* Chart Footer description */}
      <div className="mt-4 flex flex-col sm:flex-row items-start sm:items-center justify-between border-t-2 border-[#1f1b2e] pt-3 text-[11px] font-mono text-[#3b3552]">
        <div>
          Kaplan-Meier estimate · <span className="text-[#5b45e0] font-bold">+</span> indicates right-censoring at observed call end
        </div>
        <div className="text-[#6a56e8] font-bold mt-1 sm:mt-0">
          {endSurvivalPercent}% unaccused at 90s
        </div>
      </div>
    </div>
  );
}
