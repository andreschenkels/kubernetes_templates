// This library allows us to combine paths easily
const path = require('path');
const webpack = require('webpack')
const HWP = require('html-webpack-plugin');

module.exports = {
 entry: path.resolve(__dirname, './src/index.jsx'),
 output: {
  path: path.resolve(__dirname, 'build'),
  filename: 'app.bundle.js'
 },
 resolve: {
  extensions: ['.js', '.jsx']
 },
 module: {
  rules: [
    {
      exclude: /node_modules/,
      test: /\.jsx/,
      use: {
        loader: 'babel-loader',
        options: { presets: ['react', 'es2015'] }
      }
    },
    {
      test: /\.scss/,
      use: ['style-loader', 'css-loader', 'sass-loader']
    }
  ]
 },
 plugins:[
    new HWP({
        template: path.join(__dirname, '/src/index.html')
      }
    ),
    new webpack.EnvironmentPlugin({
      API_URL: 'http://127.0.0.1:5000'
    })
  ]
};
