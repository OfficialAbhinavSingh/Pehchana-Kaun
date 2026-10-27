import { Leaderboard, ArmStats, SurvivalPoint } from "./api";

// 90-second Kaplan-Meier curve generator for sample data matching the design spec in Untitled.pdf
export function generateSampleCurve(endSurvival = 0.4): SurvivalPoint[] {
  const points: SurvivalPoint[] = [
    { t: 0, survival: 1.0, at_risk: 300, events: 0, ci_low: null, ci_high: null },
    { t: 10, survival: 0.95, at_risk: 285, events: 15, ci_low: 0.92, ci_high: 0.97 },
    { t: 20, survival: 0.86, at_risk: 258, events: 27, ci_low: 0.81, ci_high: 0.89 },
    { t: 26, survival: 0.78, at_risk: 234, events: 24, ci_low: 0.73, ci_high: 0.82 },
    { t: 32, survival: 0.68, at_risk: 204, events: 30, ci_low: 0.62, ci_high: 0.73 },
    { t: 38, survival: 0.58, at_risk: 174, events: 30, ci_low: 0.52, ci_high: 0.64 },
    { t: 45, survival: 0.52, at_risk: 156, events: 18, ci_low: 0.46, ci_high: 0.58 },
    { t: 60, survival: 0.46, at_risk: 138, events: 18, ci_low: 0.40, ci_high: 0.52 },
    { t: 75, survival: 0.42, at_risk: 126, events: 12, ci_low: 0.36, ci_high: 0.48 },
    { t: 90, survival: endSurvival, at_risk: 120, events: 6, ci_low: endSurvival - 0.05, ci_high: endSurvival + 0.05 },
  ];
  return points;
}

export const SAMPLE_ASTER_CURVE = generateSampleCurve(0.5);
export const SAMPLE_ECHO_CURVE = generateSampleCurve(0.4);
export const SAMPLE_MICA_CURVE = generateSampleCurve(0.3);
export const SAMPLE_OVERALL_CURVE = generateSampleCurve(0.4);

export const SAMPLE_ARMS: ArmStats[] = [
  {
    arm_id: "human-control",
    display_name: "Human Volunteers (Control)",
    kind: "human",
    ranked: true,
    n_calls: 300,
    n_accused: 45,
    accusation_rate: 0.15, // 15% false accusation rate
    median_turing_clock_s: null,
    median_ci_low_s: null,
    median_ci_high_s: null,
    fooled_at_60s: 0.85,
    max_observed_s: 118,
    curve: [
      { t: 0, survival: 1.0, at_risk: 300, events: 0, ci_low: null, ci_high: null },
      { t: 30, survival: 0.94, at_risk: 282, events: 18, ci_low: 0.91, ci_high: 0.96 },
      { t: 60, survival: 0.89, at_risk: 267, events: 15, ci_low: 0.85, ci_high: 0.92 },
      { t: 90, survival: 0.85, at_risk: 255, events: 12, ci_low: 0.80, ci_high: 0.89 },
    ],
    top_giveaways: [
      { tag: "Too polite or calm", count: 20 },
      { tag: "Delayed audio response", count: 14 },
      { tag: "Stuttered or coughed", count: 11 },
    ],
  },
  {
    arm_id: "aster-v1",
    display_name: "Aster / v1 (Orchid Labs)",
    kind: "ai",
    ranked: true,
    n_calls: 300,
    n_accused: 150,
    accusation_rate: 0.5,
    median_turing_clock_s: 38,
    median_ci_low_s: 34,
    median_ci_high_s: 43,
    fooled_at_60s: 0.52,
    max_observed_s: 112,
    curve: SAMPLE_ASTER_CURVE,
    top_giveaways: [
      { tag: "Unnatural pauses", count: 63 },
      { tag: "Overly polished replies", count: 51 },
      { tag: "Missed context", count: 36 },
    ],
  },
  {
    arm_id: "echo-v2",
    display_name: "Echo / v2 (Fable Audio)",
    kind: "ai",
    ranked: true,
    n_calls: 300,
    n_accused: 180,
    accusation_rate: 0.6,
    median_turing_clock_s: 32,
    median_ci_low_s: 28,
    median_ci_high_s: 36,
    fooled_at_60s: 0.42,
    max_observed_s: 98,
    curve: SAMPLE_ECHO_CURVE,
    top_giveaways: [
      { tag: "Robotic pitch / cadence", count: 72 },
      { tag: "Latency hesitation", count: 61 },
      { tag: "Ignored interruption", count: 47 },
    ],
  },
  {
    arm_id: "mica-v1",
    display_name: "Mica / v1 (Loom Voice)",
    kind: "ai",
    ranked: true,
    n_calls: 300,
    n_accused: 210,
    accusation_rate: 0.7,
    median_turing_clock_s: 26,
    median_ci_low_s: 22,
    median_ci_high_s: 30,
    fooled_at_60s: 0.31,
    max_observed_s: 91,
    curve: SAMPLE_MICA_CURVE,
    top_giveaways: [
      { tag: "Pronoun confusion", count: 88 },
      { tag: "Unnatural Hinglish switch", count: 68 },
      { tag: "Repetitive affirmations", count: 54 },
    ],
  },
];

export const SAMPLE_LEADERBOARD: Leaderboard = {
  generated_at: new Date().toISOString(),
  includes_demo_data: true,
  first_call_only: false,
  min_calls_for_ranking: 10,
  total_calls: 1200,
  arms: SAMPLE_ARMS,
  by_language: {
    hi: [
      {
        ...SAMPLE_ARMS[1],
        n_calls: 150,
        n_accused: 81,
        accusation_rate: 0.54,
        median_turing_clock_s: 36,
        median_ci_low_s: 31,
        median_ci_high_s: 41,
      },
      {
        ...SAMPLE_ARMS[2],
        n_calls: 150,
        n_accused: 93,
        accusation_rate: 0.62,
        median_turing_clock_s: 30,
      },
      {
        ...SAMPLE_ARMS[3],
        n_calls: 150,
        n_accused: 108,
        accusation_rate: 0.72,
        median_turing_clock_s: 24,
      },
    ],
    en: [
      {
        ...SAMPLE_ARMS[1],
        n_calls: 150,
        n_accused: 69,
        accusation_rate: 0.46,
        median_turing_clock_s: 40,
        median_ci_low_s: 35,
        median_ci_high_s: 47,
      },
      {
        ...SAMPLE_ARMS[2],
        n_calls: 150,
        n_accused: 87,
        accusation_rate: 0.58,
        median_turing_clock_s: 34,
      },
      {
        ...SAMPLE_ARMS[3],
        n_calls: 150,
        n_accused: 102,
        accusation_rate: 0.68,
        median_turing_clock_s: 28,
      },
    ],
  },
};
