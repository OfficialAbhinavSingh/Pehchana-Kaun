import React from "react";

interface GiveawayItem {
  tag: string;
  count: number;
}

interface GiveawayBarProps {
  items: GiveawayItem[];
  totalDetected?: number;
  title?: string;
  subtitle?: string;
}

export default function GiveawayBar({
  items,
  totalDetected,
  title = "What gave it away?",
  subtitle = "Coded post-call giveaway themes among detected calls.",
}: GiveawayBarProps) {
  const sumCount = items.reduce((acc, curr) => acc + curr.count, 0);
  const total = totalDetected && totalDetected > 0 ? totalDetected : sumCount > 0 ? sumCount : 1;

  return (
    <div className="rounded-[4px] border border-[#2B2B38] bg-[#1B1B23] p-5 sm:p-6 text-[#F5F5F5]">
      <div className="border-b border-[#2B2B38] pb-4">
        <h4 className="text-base font-bold font-display text-[#F5F5F5]">{title}</h4>
        <p className="text-xs text-[#A1A1AA]">{subtitle}</p>
      </div>

      <div className="mt-5 space-y-4">
        {items.map((item, index) => {
          const percent = Math.min(100, Math.round((item.count / total) * 100));
          return (
            <div key={item.tag} className="space-y-1.5">
              <div className="flex items-center justify-between text-xs font-mono">
                <span className="text-[#F5F5F5] font-medium flex items-center gap-2">
                  <span className="text-[#8B7CFF] font-bold">0{index + 1}</span>
                  {item.tag}
                </span>
                <span className="text-[#A1A1AA]">
                  <strong className="text-[#B8FF4D]">{percent}%</strong> · {item.count} calls
                </span>
              </div>
              <div className="h-2 w-full overflow-hidden rounded-[2px] bg-[#101014]">
                <div
                  className="h-full bg-gradient-to-r from-[#8B7CFF] to-[#B8FF4D] transition-all duration-500"
                  style={{ width: `${percent}%` }}
                />
              </div>
            </div>
          );
        })}
      </div>

      <div className="mt-5 border-t border-[#2B2B38] pt-3 text-[11px] font-mono text-[#71717A]">
        One primary theme coded per detected call. No accusation is not proof of belief.
      </div>
    </div>
  );
}
