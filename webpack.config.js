const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const CompressionPlugin = require('compression-webpack-plugin');
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');

module.exports = {
    mode: 'production',
    context: __dirname,
    entry: './assets/index.js',
    output: {
        path: path.resolve('./habitstacker/static/'),
        filename: "[name]-[contenthash].js",
        publicPath: '/static/',
        clean: true,
    },
    module: {
        rules: [
            /**
             * Rule 1: use babel to transform all the js.files.
             * Exclude the node_modules folder.
             */
            {
                test: /\.m?js$/,
                exclude: /(node_modules|bower_components)/,
                use: {
                    loader: "babel-loader",
                    options: {
                        presets: ["@babel/preset-env"],
                    },
                },
            },
            /**
             * Rule 2: understand and parse the css files
             * A directory path will be created as for the source file.
             */
            {
                test: /\.css$/,
                use: [MiniCssExtractPlugin.loader, "css-loader", "postcss-loader"],
            },
            /**
             * Rule 3: understand and parse the image files
             * Using webpack assets to load image files
             */
            {
                test: /\.(png|svg|jpg|jpeg|gif|webp|ico)$/i,
                type: "asset/resource",
                generator: {
                    filename: "./images/[name][ext]",
                },
            },
        ]
    },
    plugins: [
        new BundleTracker({ path: __dirname, filename: "webpack-stats.json" }),
        new MiniCssExtractPlugin({ filename: '[name]-[contenthash].css', }),
        new CompressionPlugin({ test: /\.js(\?.*)?$/i }),
    ],
    optimization: {
        minimize: true,
        minimizer: [new CssMinimizerPlugin]
    }
};
