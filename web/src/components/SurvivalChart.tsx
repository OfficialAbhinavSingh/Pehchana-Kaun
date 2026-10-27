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
    <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-5 sm:p-6 text-[#F5F5F5]">
      {/* Chart Header */}
      <div className="flex flex-col sm:flex-row sm:items-baseline justify-between gap-2 border-b border-[#2B2B38] pb-4">
        <div>
          <h4 className="text-base font-bold font-display text-[#F5F5F5]">{title}</h4>
          <p className="text-xs text-[#A1A1AA]">{subtitle}</p>
        </div>
        <div className="flex items-center gap-3 font-mono text-xs">
          <span className="flex items-center gap-1.5 text-[#B8FF4D]">
            <span className="inline-block h-2 w-2 rounded-full bg-[#B8FF4D]" />
            Survival Curve
          </span>
          <span className="flex items-center gap-1.5 text-[#8B7CFF]">
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
                stroke="#2B2B38"
                strokeDasharray="3 3"
                strokeWidth="1"
              />
              <text
                x={padding.left - 8}
                y={getY(s) + 4}
                textAnchor="end"
                className="fill-[#71717A] text-[10px] font-mono"
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
                stroke="#2B2B38"
                strokeDasharray="2 2"
                strokeWidth="1"
              />
              <text
                x={getX(t)}
                y={height - padding.bottom + 18}
                textAnchor="middle"
                className="fill-[#A1A1AA] text-[11px] font-mono"
              >
                {t}s
              </text>
            </g>
          ))}

          {/* 95% Greenwood Confidence Interval Band */}
          {ciPath && (
            <path
              d={ciPath}
              fill="#8B7CFF"
              fillOpacity="0.12"
              stroke="none"
            />
          )}

          {/* Stepped Kaplan-Meier Survival Line */}
          <path
            d={stepPath}
            fill="none"
            stroke="#B8FF4D"
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
                  fill="#1B1B23"
                  stroke="#8B7CFF"
                  strokeWidth="2"
                  className="transition-transform group-hover:scale-150"
                />
                <text
                  y="-8"
                  textAnchor="middle"
                  className="fill-[#8B7CFF] text-[9px] font-mono font-bold"
                >
                  +
                </text>
              </g>
            );
          })}
        </svg>

        {/* Hover inspect card */}
        {hoveredPoint && (
          <div className="absolute top-2 right-4 rounded-[4px] border border-[#8B7CFF] bg-[#101014]/95 p-2 font-mono text-xs shadow-lg backdrop-blur-md">
            <div className="text-[#B8FF4D] font-bold">t = {hoveredPoint.t}s</div>
            <div className="text-[#F5F5F5]">
              Survival: {Math.round(hoveredPoint.survival * 100)}%
            </div>
            <div className="text-[#A1A1AA]">At Risk: {hoveredPoint.at_risk}</div>
            {hoveredPoint.ci_low !== null && (
              <div className="text-[#71717A] text-[10px]">
                95% CI: [{Math.round(hoveredPoint.ci_low * 100)}% -{" "}
                {Math.round(hoveredPoint.ci_high! * 100)}%]
              </div>
            )}
          </div>
        )}
      </div>

      {/* Chart Footer description */}
      <div className="mt-4 flex flex-col sm:flex-row items-start sm:items-center justify-between border-t border-[#2B2B38] pt-3 text-[11px] font-mono text-[#A1A1AA]">
        <div>
          Kaplan-Meier estimate · <span className="text-[#8B7CFF] font-bold">+</span> indicates right-censoring at observed call end
        </div>
        <div className="text-[#B8FF4D] font-bold mt-1 sm:mt-0">
          {endSurvivalPercent}% unaccused at 90s
        </div>
      </div>
    </div>
  );
}
