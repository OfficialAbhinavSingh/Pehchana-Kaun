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
    <div className=" border-2 border-[#201e1d] bg-[#ffffff] p-5 sm:p-6 text-[#201e1d]">
      <div className="border-b-2 border-[#201e1d] pb-4">
        <h4 className="text-base font-bold font-display text-[#201e1d]">{title}</h4>
        <p className="text-xs text-[#605d5d]">{subtitle}</p>
      </div>

      <div className="mt-5 space-y-4">
        {items.map((item, index) => {
          const percent = Math.min(100, Math.round((item.count / total) * 100));
          return (
            <div key={item.tag} className="space-y-1.5">
              <div className="flex items-center justify-between text-xs font-mono">
                <span className="text-[#201e1d] font-medium flex items-center gap-2">
                  <span className="text-[#ae1800] font-bold">0{index + 1}</span>
                  {item.tag}
                </span>
                <span className="text-[#605d5d]">
                  <strong className="text-[#ec3013]">{percent}%</strong> · {item.count} calls
                </span>
              </div>
              <div className="h-2 w-full overflow-hidden bg-[#f3f2f2]">
                <div
                  className="h-full bg-gradient-to-r from-[#ae1800] to-[#ec3013] transition-all duration-500"
                  style={{ width: `${percent}%` }}
                />
              </div>
            </div>
          );
        })}
      </div>

      <div className="mt-5 border-t-2 border-[#201e1d] pt-3 text-[11px] font-mono text-[#7d7979]">
        One primary theme coded per detected call. No accusation is not proof of belief.
      </div>
    </div>
  );
}
