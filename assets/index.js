/**
 * Alpine JS
 */
import Alpine from "alpinejs";

/**
 * Htmx setup
 */
window.htmx = require("htmx.org");
/**
 * Style
 */
import "./css/main.css";
import "boxicons";

/**
 * Images
 */
import "./favicon.ico";
import "./images/apple-touch-icon.png";
import "./images/android-chrome-192x192.png";

window.Alpine = Alpine;

Alpine.start();
