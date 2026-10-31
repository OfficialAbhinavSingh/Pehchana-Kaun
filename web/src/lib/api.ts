// Contract with the backend (backend/src/pehchana/api/leaderboard.py).
// Keep both sides in sync in the same PR. Owner: WS3.

export type SurvivalPoint = {
  t: number; // seconds since the arm answered
  survival: number; // P(not yet accused at t)
  at_risk: number;
  events: number;
  ci_low: number | null; // 95% band (Greenwood, log-log); null while survival is 1
  ci_high: number | null;
};

export type ArmStats = {
  arm_id: string; // slug of the public label (e.g. "voice-a") unless REVEAL_VENDORS=true
  display_name: string; // vendor name only when REVEAL_VENDORS=true
  kind: "human" | "ai";
  ranked: boolean; // false below min_calls_for_ranking: show the numbers, not a rank
  n_calls: number;
  n_accused: number;
  accusation_rate: number; // for the human arm this is the false-accusation rate
  median_turing_clock_s: number | null; // null = never fell to 50%: arm "passed"
  median_ci_low_s: number | null; // 95% CI for the median; null = bound not reached yet
  median_ci_high_s: number | null;
  fooled_at_60s: number | null; // null when no call lasted 60 s (survival unknown)
  max_observed_s: number | null; // longest call seen; with no median, the clock is longer than this
  curve: SurvivalPoint[];
  top_giveaways: { tag: string; count: number }[];
};

export type Leaderboard = {
  generated_at: string;
  includes_demo_data: boolean;
  first_call_only: boolean; // GET /leaderboard?first_call_only=true
  min_calls_for_ranking: number;
  total_calls: number;
  arms: ArmStats[]; // human baseline first, then ranked AI arms, then unranked
  by_language: Record<string, ArmStats[]>;
};

const rawApiUrl =
  process.env.NEXT_PUBLIC_API_URL || process.env.API_URL || "http://localhost:8000";

export const API_URL = rawApiUrl.replace(/\/+$/, "");

export const GAME_NUMBER =
  process.env.NEXT_PUBLIC_GAME_NUMBER || process.env.BOLNA_NUMBER_KALPA || "+918065356581";

export async function getLeaderboard(firstCallOnly = false): Promise<Leaderboard> {
  const res = await fetch(`${API_URL}/leaderboard${firstCallOnly ? "?first_call_only=true" : ""}`);
  if (!res.ok) throw new Error(`leaderboard ${res.status}`);
  return (await res.json()) as Leaderboard;
}
