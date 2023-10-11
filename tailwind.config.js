module.exports = {
  mode: "jit",
  content: ["./habitstacker/**/*.{html,js}"],
  theme: {
    extend: {
      container: { center: true },
      colors: {
        primary: "#FCBE5B",
        secondary: "#F5604A",
        third: "#7EB67E",
        dark: "#202020",
      },
      fontFamily: {
        worker: ["Work Sans", "sans-serif"],
      },
    },
  },
  plugins: [],
};
