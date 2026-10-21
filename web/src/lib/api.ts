// Contract with the backend (backend/src/pehchana/api/leaderboard.py).
// Keep both sides in sync in the same PR. Owner: WS3.

export type SurvivalPoint = {
  t: number; // seconds since the arm answered
  survival: number; // P(not yet accused at t)
  at_risk: number;
  events: number;
};

export type ArmStats = {
  arm_id: string;
  display_name: string; // vendor name only when REVEAL_VENDORS=true
  kind: "human" | "ai";
  n_calls: number;
  n_accused: number;
  accusation_rate: number; // for the human arm this is the false-accusation rate
  median_turing_clock_s: number | null; // null = never fell below 50%: arm "passed"
  fooled_at_60s: number;
  curve: SurvivalPoint[];
  top_giveaways: { tag: string; count: number }[];
};

export type Leaderboard = {
  generated_at: string;
  includes_demo_data: boolean;
  total_calls: number;
  arms: ArmStats[];
  by_language: Record<string, ArmStats[]>;
};

const API_URL = process.env.API_URL ?? process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export async function getLeaderboard(): Promise<Leaderboard> {
  const res = await fetch(`${API_URL}/leaderboard`);
  if (!res.ok) throw new Error(`leaderboard ${res.status}`);
  return (await res.json()) as Leaderboard;
}
