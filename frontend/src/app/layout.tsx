import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Duvi's Job.bo | Empleos en Bolivia",
  description:
    "Vacantes verificadas, postulaciones simples y oportunidades laborales para Bolivia.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es">
      <body>{children}</body>
    </html>
  );
}

