var path = require('path');
var clientContext = path.join(__dirname, 'client');

var config = {
  context: path.join(clientContext, 'src'),
  entry: {
    main: ['./main.jsx', 'webpack/hot/only-dev-server'],
    devServerClient: 'webpack-dev-server/client?http://0.0.0.0:8080'
  },
  output: {
    path: path.join(clientContext, 'dist'),
    filename: '[name].entry.js'
  },
  module: {
    loaders: [
      {
        test: /\.js[x]$/,
        exclude: /node_modules|bower_components/,
        loader: 'babel',
        query: {
          presets: ['es2015', 'react']
        }
      },
      {
        test: /\.scss|\.sass$/,
        loader: 'style!css!postcss!sass?indentedSyntax=true'
        // loader: ['style', 'css', 'postcss-loader', 'sass?indentedSyntax=true']
      }
    ]
  },
  postcss: function() {
    return [require('autoprefixer')]
  },
  devServer: {
    contentBase: path.join(clientContext, 'dist'),
    inline: true,
    hot: true,
    progress: true
  }
};

module.exports = config;
