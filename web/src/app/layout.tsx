import type { Metadata, Viewport } from "next";
import { Archivo } from "next/font/google";
import { Analytics } from "@vercel/analytics/next";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import "./globals.css";

// The whole site runs on one typeface — Archivo — matching the Modernist
// design system this UI is themed from. Turbopack's font loader only allows
// a single next/font/google call per family per build, so every weight the
// site uses is requested once here and reused for all three theme roles.
const archivo = Archivo({
  variable: "--font-archivo",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700", "800", "900"],
  display: "swap",
});

export const viewport: Viewport = {
  themeColor: "#f3f2f2",
  width: "device-width",
  initialScale: 1,
};

export const metadata: Metadata = {
  title: "Pehchana Kaun? — The Voice Identity Experiment",
  description:
    "India's first phone-line Turing test for voice AI. Call a number, chat for two minutes, and say 'tum bot ho!' when you think it's a bot.",
  keywords: [
    "Voice AI",
    "Turing Test",
    "Turing Clock",
    "Bolna",
    "Kalpa",
    "Cartesia",
    "Sarvam",
    "Pehchana Kaun",
  ],
  openGraph: {
    title: "Pehchana Kaun? — The Voice Identity Experiment",
    description: "One phone call. One mystery voice. Can you tell if it's human or AI?",
    type: "website",
    locale: "en_IN",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html
      lang="en"
      className={`${archivo.variable} h-full`}
    >
      <body className="min-h-full flex flex-col bg-[#f3f2f2] text-[#201e1d] font-sans antialiased selection:bg-[#ec3013] selection:text-[#f3f2f2]">
        <Navbar />
        <div className="flex-1 flex flex-col">{children}</div>
        <Footer />
        <Analytics />
      </body>
    </html>
  );
}
