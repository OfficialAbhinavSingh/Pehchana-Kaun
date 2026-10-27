import type { Metadata, Viewport } from "next";
import { Space_Grotesk, Inter, JetBrains_Mono } from "next/font/google";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import "./globals.css";

const spaceGrotesk = Space_Grotesk({
  variable: "--font-space-grotesk",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
  display: "swap",
});

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
  display: "swap",
});

const jetbrainsMono = JetBrains_Mono({
  variable: "--font-jetbrains-mono",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
  display: "swap",
});

export const viewport: Viewport = {
  themeColor: "#101014",
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
      className={`${spaceGrotesk.variable} ${inter.variable} ${jetbrainsMono.variable} h-full dark`}
    >
      <body className="min-h-full flex flex-col bg-[#101014] text-[#F5F5F5] font-sans antialiased selection:bg-[#B8FF4D] selection:text-[#101014]">
        <Navbar />
        <div className="flex-1 flex flex-col">{children}</div>
        <Footer />
      </body>
    </html>
  );
}
