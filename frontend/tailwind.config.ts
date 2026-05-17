import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./src/**/*.{js,ts,jsx,tsx,mdx}"],
  theme: {
    extend: {
      colors: {
        brand: {
          50: "#f3f8ff",
          100: "#e6f0ff",
          600: "#1d5fd6",
          700: "#1649a6",
          900: "#102b5c",
        },
        accent: {
          500: "#f2b705",
          600: "#d99f00",
        },
      },
      boxShadow: {
        soft: "0 16px 50px rgba(16, 43, 92, 0.12)",
      },
    },
  },
  plugins: [],
};

export default config;

