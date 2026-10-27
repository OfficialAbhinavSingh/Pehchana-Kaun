import ModelProfileClient from "./ModelProfileClient";

// Voice ids come from the live leaderboard, not a known set at build time.
export const instant = false;

export default async function ModelProfilePage({
  params,
}: {
  params: Promise<{ modelId: string }>;
}) {
  const { modelId } = await params;
  return <ModelProfileClient modelId={modelId} />;
}
