import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  cacheComponents: true,
  partialPrefetching: true,
  env: {
    NEXT_PUBLIC_API_URL:
      process.env.NEXT_PUBLIC_API_URL || process.env.API_URL || "http://localhost:8000",
    NEXT_PUBLIC_GAME_NUMBER:
      process.env.NEXT_PUBLIC_GAME_NUMBER || process.env.BOLNA_NUMBER_KALPA || "+918065356581",
  },
  turbopack: {
    rules: {
      "*.css": {
        loaders: ["@tailwindcss/turbopack"],
        as: "*.css",
      },
    },
  },
};

export default nextConfig;
