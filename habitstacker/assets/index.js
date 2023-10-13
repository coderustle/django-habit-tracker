/**
 * Style
 */
import "./css/main.css";

/**
 * Images
 */
import "./images/favicon.ico";
import "./images/apple-touch-icon.png";
import "./images/android-chrome-192x192.png";

/**
 * Alpine JS
 */
import Alpine from "alpinejs";

window.Alpine = Alpine;

Alpine.start();

/**
 * Htmx setup
 */
window.htmx = require("htmx.org");
