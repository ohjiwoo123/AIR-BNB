module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      spacing: {
        "25vh" : "25vh",
        "50vh" : "50vh",
        "75vh" : "75vh"
      },
      borderRadius: {
        xl: "1.5rem"
      },
      colors:{
        teal: {
          50: "#f0fdfa",
          100: "#ccfbf1",
          200: "#99f6e4",
          300: "#5eead4",
          400: "#2dd4bf",
          500: "#14b8a6",
          600: "#0d9488",
          700: "##0f766e",
          800: "#115e59",
          900: "#134e4a"
        }
      }
    }
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
